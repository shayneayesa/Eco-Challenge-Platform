from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    points = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def get_id(self):
        return str(self.id)
    
class Admin(db.Model):
    __tablename__ = "admins"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Feedback(db.Model):
    __tablename__ = "feedbacks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=True)
    message = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class HomeContent(db.Model):
    __tablename__ = "home_content"
    id = db.Column(db.Integer, primary_key=True)
    general_objective = db.Column(db.Text, nullable=False)
    background_info = db.Column(db.Text, nullable=False)

class ReforestationData(db.Model):
    __tablename__ = 'reforestation_data'
    
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    reforestation_percentage = db.Column(db.Float, nullable=False)
    forest_restored_hectares = db.Column(db.Integer)
    notes = db.Column(db.Text)
    
    __table_args__ = (
        db.UniqueConstraint('country', 'year', name='unique_country_year'),
    )

class CountryMetadata(db.Model):
    __tablename__ = 'country_metadata'
    
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(100), unique=True, nullable=False)
    total_forest_restored_2015_2025 = db.Column(db.Integer)
    avg_annual_reforestation_rate = db.Column(db.Float)
    description = db.Column(db.Text)