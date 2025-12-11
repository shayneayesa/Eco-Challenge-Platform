import os
from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, Admin, Feedback, HomeContent, ReforestationData, CountryMetadata
from forms import SignupForm, LoginForm, AdminSignupForm, AdminLoginForm, FeedbackForm, HomeContentForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from functools import wraps

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sevensecret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'eco.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(BASE_DIR, 'static', 'uploads')

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class UserLogin(UserMixin):
    def __init__(self, user):
        self._user = user
    def get_id(self):
        return str(self._user.id)
    @property
    def username(self):
        return self._user.username
    @property
    def points(self):
        return self._user.points
    def add_points(self, n):
        self._user.points += n
        db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    u = User.query.get(int(user_id))
    if u:
        return UserLogin(u)
    return None

with app.app_context():
    db.create_all()

def admin_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get('admin_id'):
            flash("Admin login required.", "error")
            return redirect(url_for('admin_login'))
        return f(*args, *kwargs)
    return wrapped

# HOMEPAGE
@app.route('/')
def home():
    content = HomeContent.query.first()
    return render_template('home.html', content=content)

# INFOGRAPHICS
@app.route('/infographics')
def infographics():
    if current_user.is_authenticated:
        if not session.get('viewed_infographics'):
            u = User.query.get(int(current_user.get_id()))
            if u:
                u.points = (u.points or 0) + 2
                db.session.commit()
            session['viewed_infographics'] = True
    return render_template('infographics.html')

# GALLERY
@app.route('/gallery')
def gallery():
    files = []
    try:
        files = os.listdir(app.config['UPLOAD_FOLDER'])
    except FileNotFoundError:
        files = []
    return render_template('gallery.html', files=files)

# FEEDBACK
@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    form = FeedbackForm()
    if form.validate_on_submit():
        message = form.message.data.strip()
        name = form.name.data.strip() if form.name.data else None
        user_id = None
        if current_user.is_authenticated:
            user_id = int(current_user.get_id())
            u = User.query.get(user_id)
            if u:
                u.points = (u.points or 0) + 5
                db.session.commit()
            flash("Thank you! You earned +5 points for your feedback!", "success")
        else:
            flash("Thank you for your feedback!", "success")
        fb = Feedback(user_id=user_id, name=name, message=message)
        db.session.add(fb)
        db.session.commit()
        return redirect(url_for('feedback'))
    
    feedbacks = Feedback.query.order_by(Feedback.created_at.desc()).limit(20).all()
    return render_template('feedback.html', form=form, feedbacks=feedbacks)

# ECO PROFILE
@app.route('/eco_profile')
@login_required
def eco_profile():
    u = User.query.get(int(current_user.get_id()))
    return render_template('eco_profiles.html', profile=u)

@app.route('/collect_tree', methods=['POST'])
def collect_tree():
    if current_user.is_authenticated:
        u = User.query.get(int(current_user.get_id()))
        if u:
            u.points = (u.points or 0) + 1
            db.session.commit()
            return jsonify({"status":"ok","points":u.points})
        return jsonify({"status":"error","message":"user not found"}), 404
    return jsonify({"status":"guest","message":"guest"}), 200

@app.route('/uploads/<filename>')
def upload_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# GRAPH
@app.route('/graph')
def graph():
    return render_template("graph.html")

@app.route('/api/graph/<country>')
def get_graph_data(country):
    try:
        data = ReforestationData.query.filter_by(country=country).order_by(ReforestationData.year).all()
        
        metadata = CountryMetadata.query.filter_by(country=country).first()
        
        if not data:
            return jsonify({'error': 'Country not found'}), 404
        
        response = {
            'country': country,
            'years': [d.year for d in data],
            'percentages': [d.reforestation_percentage for d in data],
            'hectares': [d.forest_restored_hectares for d in data],
            'metadata': {
                'total_loss': metadata.total_forest_restored_2015_2025 if metadata else 0,
                'avg_rate': metadata.avg_annual_reforestation_rate if metadata else 0,
                'description': metadata.description if metadata else ''
            }
        }
        
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/graph/countries')
def get_countries():
    try:
        countries = db.session.query(ReforestationData.country).distinct().all()
        return jsonify({'countries': [c[0] for c in countries]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# SIGN-IN-OUT USERS
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data.strip()
        if User.query.filter_by(username=username).first():
            flash("Username already exists.", "error")
            return redirect(url_for('signup'))
        hashed = generate_password_hash(password)
        user = User(username=username, password=hashed, points=0)
        db.session.add(user)
        db.session.commit()

        login_user(UserLogin(user))
        flash("Account created. Welcome!", "success")
        return redirect(url_for('home'))
    return render_template('signup.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data.strip()
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            flash("Invalid username or password.", "error")
            return redirect(url_for('login'))
        login_user(UserLogin(user))
        flash("Logged in successfully.", "success")
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    if current_user.is_authenticated:
        logout_user()
    flash("Logged out.", "success")
    return redirect(url_for('home'))

# ADMIN
@app.route('/admin/signup', methods=['GET', 'POST'])
def admin_signup():
    form = AdminSignupForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data.strip()
        if Admin.query.filter_by(username=username).first():
            flash("Admin username already taken.", "error")
            return redirect(url_for('admin_signup'))
        hashed = generate_password_hash(password)
        a = Admin(username=username, password_hash=hashed)
        db.session.add(a)
        db.session.commit()
        flash("Admin account created. Please login.", "success")
        return redirect(url_for('admin_login'))
    return render_template('admin/admin_signup.html', form=form)

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    form = AdminLoginForm()
    if form.validate_on_submit():
        username = form.username.data.strip()
        password = form.password.data.strip()
        a = Admin.query.filter_by(username=username).first()
        if not a or not check_password_hash(a.password_hash, password):
            flash("Invalid admin credentials.", "error")
            return redirect(url_for('admin_login'))
        session['admin_id'] = a.id
        session['admin_username'] = a.username
        flash("Admin logged in.", "success")
        return redirect(url_for('admin_dashboard'))
    return render_template('admin/admin_login.html', form=form)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    session.pop('admin_username', None)
    flash("Admin logged out.", "success")
    return redirect(url_for('home'))

@app.route('/admin/dashboard')
@admin_required
def admin_dashboard():
    feedbacks = Feedback.query.order_by(Feedback.created_at.desc()).all()
    users = User.query.order_by(User.points.desc()).all()
    total_countries = db.session.query(ReforestationData.country).distinct().count()
    total_records = ReforestationData.query.count()
    return render_template('admin/admin_dashboard.html', feedbacks=feedbacks, users=users, reforestation_countries=total_countries, reforestation_records=total_records)


@app.route('/admin/graph')
def admin_graph():
    if 'admin_id' not in session:
        flash("Please log in to access this page.", "error")
        return redirect(url_for('admin_login'))
    
    countries = db.session.query(CountryMetadata).all()
    return render_template('admin_reforestation.html', countries=countries)

@app.route('/admin/edit_dashboard', methods=['GET', 'POST'])
@admin_required
def admin_edit_dashboard():
    content = HomeContent.query.first()
    form = HomeContentForm(obj=content)

    if form.validate_on_submit():
        if not content:
            content=HomeContent()
            db.session.add(content)

        content.general_objective = form.general_objective.data
        content.background_info = form.background_info.data
        db.session.commit()

        flash("Home page content updated successfully!", "success")
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin/admin_edit_dashboard.html', form=form)

@app.route('/test-data')
def test_data():
    countries = db.session.query(ReforestationData.country).distinct().all()
    count = ReforestationData.query.count()
    metadata_count = CountryMetadata.query.count()
    
    return f"""
    <h2>Database Test</h2>
    <p>Total reforestation records: {count}</p>
    <p>Total country metadata: {metadata_count}</p>
    <p>Countries: {[c[0] for c in countries]}</p>
    """


if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)