from app import app
from models import db, ReforestationData, CountryMetadata

def seed_reforestation_data():
    
    # Reforestation percentage data (2016-2025)
    reforestation_data = [
        # Brazil
        {'country': 'Brazil', 'year': 2016, 'percentage': 0.22, 'hectares': 150000},
        {'country': 'Brazil', 'year': 2017, 'percentage': 0.24, 'hectares': 165000},
        {'country': 'Brazil', 'year': 2018, 'percentage': 0.25, 'hectares': 170000},
        {'country': 'Brazil', 'year': 2019, 'percentage': 0.26, 'hectares': 180000},
        {'country': 'Brazil', 'year': 2020, 'percentage': 0.27, 'hectares': 185000},
        {'country': 'Brazil', 'year': 2021, 'percentage': 0.28, 'hectares': 190000},
        {'country': 'Brazil', 'year': 2022, 'percentage': 0.30, 'hectares': 200000},
        {'country': 'Brazil', 'year': 2023, 'percentage': 0.31, 'hectares': 210000},
        {'country': 'Brazil', 'year': 2024, 'percentage': 0.33, 'hectares': 230000},
        {'country': 'Brazil', 'year': 2025, 'percentage': 0.35, 'hectares': 260000},
        
        # Angola
         {'country': 'Angola', 'year': 2016, 'percentage': 0.03, 'hectares': 10000},
        {'country': 'Angola', 'year': 2017, 'percentage': 0.04, 'hectares': 12000},
        {'country': 'Angola', 'year': 2018, 'percentage': 0.04, 'hectares': 13000},
        {'country': 'Angola', 'year': 2019, 'percentage': 0.05, 'hectares': 14000},
        {'country': 'Angola', 'year': 2020, 'percentage': 0.05, 'hectares': 15000},
        {'country': 'Angola', 'year': 2021, 'percentage': 0.05, 'hectares': 15500},
        {'country': 'Angola', 'year': 2022, 'percentage': 0.06, 'hectares': 16000},
        {'country': 'Angola', 'year': 2023, 'percentage': 0.06, 'hectares': 17000},
        {'country': 'Angola', 'year': 2024, 'percentage': 0.06, 'hectares': 18000},
        {'country': 'Angola', 'year': 2025, 'percentage': 0.06, 'hectares': 20000},
        
        # Tanzania
        {'country': 'Tanzania', 'year': 2016, 'percentage': 0.10, 'hectares': 50000},
        {'country': 'Tanzania', 'year': 2017, 'percentage': 0.11, 'hectares': 53000},
        {'country': 'Tanzania', 'year': 2018, 'percentage': 0.12, 'hectares': 56000},
        {'country': 'Tanzania', 'year': 2019, 'percentage': 0.12, 'hectares': 58000},
        {'country': 'Tanzania', 'year': 2020, 'percentage': 0.13, 'hectares': 60000},
        {'country': 'Tanzania', 'year': 2021, 'percentage': 0.13, 'hectares': 62000},
        {'country': 'Tanzania', 'year': 2022, 'percentage': 0.14, 'hectares': 65000},
        {'country': 'Tanzania', 'year': 2023, 'percentage': 0.14, 'hectares': 67000},
        {'country': 'Tanzania', 'year': 2024, 'percentage': 0.15, 'hectares': 69000},
        {'country': 'Tanzania', 'year': 2025, 'percentage': 0.15, 'hectares': 70000},
        
        # Myanmar
        {'country': 'Myanmar', 'year': 2016, 'percentage': 0.06, 'hectares': 20000},
        {'country': 'Myanmar', 'year': 2017, 'percentage': 0.07, 'hectares': 23000},
        {'country': 'Myanmar', 'year': 2018, 'percentage': 0.07, 'hectares': 25000},
        {'country': 'Myanmar', 'year': 2019, 'percentage': 0.08, 'hectares': 28000},
        {'country': 'Myanmar', 'year': 2020, 'percentage': 0.08, 'hectares': 30000},
        {'country': 'Myanmar', 'year': 2021, 'percentage': 0.09, 'hectares': 32000},
        {'country': 'Myanmar', 'year': 2022, 'percentage': 0.09, 'hectares': 33000},
        {'country': 'Myanmar', 'year': 2023, 'percentage': 0.09, 'hectares': 34000},
        {'country': 'Myanmar', 'year': 2024, 'percentage': 0.10, 'hectares': 36000},
        {'country': 'Myanmar', 'year': 2025, 'percentage': 0.10, 'hectares': 38000},
        
        # Democratic Republic of Congo
        {'country': 'DR Congo', 'year': 2016, 'percentage': 0.05, 'hectares': 40000},
        {'country': 'DR Congo', 'year': 2017, 'percentage': 0.06, 'hectares': 45000},
        {'country': 'DR Congo', 'year': 2018, 'percentage': 0.06, 'hectares': 48000},
        {'country': 'DR Congo', 'year': 2019, 'percentage': 0.06, 'hectares': 50000},
        {'country': 'DR Congo', 'year': 2020, 'percentage': 0.07, 'hectares': 52000},
        {'country': 'DR Congo', 'year': 2021, 'percentage': 0.07, 'hectares': 54000},
        {'country': 'DR Congo', 'year': 2022, 'percentage': 0.07, 'hectares': 56000},
        {'country': 'DR Congo', 'year': 2023, 'percentage': 0.07, 'hectares': 58000},
        {'country': 'DR Congo', 'year': 2024, 'percentage': 0.08, 'hectares': 60000},
        {'country': 'DR Congo', 'year': 2025, 'percentage': 0.08, 'hectares': 62000},
        
        # Mozambique
        {'country': 'Mozambique', 'year': 2016, 'percentage': 0.04, 'hectares': 15000},
        {'country': 'Mozambique', 'year': 2017, 'percentage': 0.05, 'hectares': 16000},
        {'country': 'Mozambique', 'year': 2018, 'percentage': 0.05, 'hectares': 17000},
        {'country': 'Mozambique', 'year': 2019, 'percentage': 0.05, 'hectares': 18000},
        {'country': 'Mozambique', 'year': 2020, 'percentage': 0.05, 'hectares': 19000},
        {'country': 'Mozambique', 'year': 2021, 'percentage': 0.05, 'hectares': 20000},
        {'country': 'Mozambique', 'year': 2022, 'percentage': 0.06, 'hectares': 21000},
        {'country': 'Mozambique', 'year': 2023, 'percentage': 0.06, 'hectares': 22000},
        {'country': 'Mozambique', 'year': 2024, 'percentage': 0.06, 'hectares': 24000},
        {'country': 'Mozambique', 'year': 2025, 'percentage': 0.06, 'hectares': 25000},
        
        # Cambodia 
        {'country': 'Cambodia', 'year': 2016, 'percentage': 0.05, 'hectares': 10000},
        {'country': 'Cambodia', 'year': 2017, 'percentage': 0.06, 'hectares': 11000},
        {'country': 'Cambodia', 'year': 2018, 'percentage': 0.06, 'hectares': 12000},
        {'country': 'Cambodia', 'year': 2019, 'percentage': 0.07, 'hectares': 13000},
        {'country': 'Cambodia', 'year': 2020, 'percentage': 0.07, 'hectares': 14000},
        {'country': 'Cambodia', 'year': 2021, 'percentage': 0.07, 'hectares': 15000},
        {'country': 'Cambodia', 'year': 2022, 'percentage': 0.08, 'hectares': 16000},
        {'country': 'Cambodia', 'year': 2023, 'percentage': 0.08, 'hectares': 17000},
        {'country': 'Cambodia', 'year': 2024, 'percentage': 0.09, 'hectares': 18000},
        {'country': 'Cambodia', 'year': 2025, 'percentage': 0.09, 'hectares': 18500},

        # Peru
        {'country': 'Peru', 'year': 2016, 'percentage': 0.05, 'hectares': 30000},
        {'country': 'Peru', 'year': 2017, 'percentage': 0.05, 'hectares': 32000},
        {'country': 'Peru', 'year': 2018, 'percentage': 0.06, 'hectares': 34000},
        {'country': 'Peru', 'year': 2019, 'percentage': 0.06, 'hectares': 36000},
        {'country': 'Peru', 'year': 2020, 'percentage': 0.06, 'hectares': 38000},
        {'country': 'Peru', 'year': 2021, 'percentage': 0.06, 'hectares': 40000},
        {'country': 'Peru', 'year': 2022, 'percentage': 0.07, 'hectares': 42000},
        {'country': 'Peru', 'year': 2023, 'percentage': 0.07, 'hectares': 43000},
        {'country': 'Peru', 'year': 2024, 'percentage': 0.07, 'hectares': 44000},
        {'country': 'Peru', 'year': 2025, 'percentage': 0.07, 'hectares': 45000},
        
        # Bolivia
        {'country': 'Bolivia', 'year': 2016, 'percentage': 0.05, 'hectares': 20000},
        {'country': 'Bolivia', 'year': 2017, 'percentage': 0.05, 'hectares': 22000},
        {'country': 'Bolivia', 'year': 2018, 'percentage': 0.05, 'hectares': 24000},
        {'country': 'Bolivia', 'year': 2019, 'percentage': 0.06, 'hectares': 26000},
        {'country': 'Bolivia', 'year': 2020, 'percentage': 0.06, 'hectares': 28000},
        {'country': 'Bolivia', 'year': 2021, 'percentage': 0.06, 'hectares': 30000},
        {'country': 'Bolivia', 'year': 2022, 'percentage': 0.06, 'hectares': 31000},
        {'country': 'Bolivia', 'year': 2023, 'percentage': 0.06, 'hectares': 32000},
        {'country': 'Bolivia', 'year': 2024, 'percentage': 0.07, 'hectares': 34000},
        {'country': 'Bolivia', 'year': 2025, 'percentage': 0.07, 'hectares': 35000},
        
        # Paraguay
        {'country': 'Paraguay', 'year': 2016, 'percentage': 0.04, 'hectares': 10000},
        {'country': 'Paraguay', 'year': 2017, 'percentage': 0.04, 'hectares': 11000},
        {'country': 'Paraguay', 'year': 2018, 'percentage': 0.05, 'hectares': 12000},
        {'country': 'Paraguay', 'year': 2019, 'percentage': 0.05, 'hectares': 13000},
        {'country': 'Paraguay', 'year': 2020, 'percentage': 0.05, 'hectares': 14000},
        {'country': 'Paraguay', 'year': 2021, 'percentage': 0.06, 'hectares': 15000},
        {'country': 'Paraguay', 'year': 2022, 'percentage': 0.06, 'hectares': 16000},
        {'country': 'Paraguay', 'year': 2023, 'percentage': 0.06, 'hectares': 17000},
        {'country': 'Paraguay', 'year': 2024, 'percentage': 0.07, 'hectares': 18000},
        {'country': 'Paraguay', 'year': 2025, 'percentage': 0.07, 'hectares': 20000},

        # Philippines
        {'country': 'Philippines', 'year': 2016, 'percentage': 0.12, 'hectares': 70000},
        {'country': 'Philippines', 'year': 2017, 'percentage': 0.13, 'hectares': 80000},
        {'country': 'Philippines', 'year': 2018, 'percentage': 0.14, 'hectares': 85000},
        {'country': 'Philippines', 'year': 2019, 'percentage': 0.15, 'hectares': 90000},
        {'country': 'Philippines', 'year': 2020, 'percentage': 0.15, 'hectares': 95000},
        {'country': 'Philippines', 'year': 2021, 'percentage': 0.16, 'hectares': 100000},
        {'country': 'Philippines', 'year': 2022, 'percentage': 0.16, 'hectares': 105000},
        {'country': 'Philippines', 'year': 2023, 'percentage': 0.17, 'hectares': 110000},
        {'country': 'Philippines', 'year': 2024, 'percentage': 0.17, 'hectares': 115000},
        {'country': 'Philippines', 'year': 2025, 'percentage': 0.18, 'hectares': 120000},

    ]
    
    # Country metadata
    country_metadata = [
        {'country': 'Philippines', 'total_restore': 1050000, 'avg_rate': 0.65, 'description': 'The Philippines implemented the National Greening Program (NGP), planting over 1 million hectares from 2011–2025. Major efforts focus on watershed rehabilitation and agroforestry.'},
        {'country': 'Brazil', 'total_restore': 1200000, 'avg_rate': 0.52, 'description': 'Brazil committed to restoring 12 million hectares by 2030. From 2015-2025, over 1.2 million hectares were reforested, focusing on degraded Amazon and Atlantic forest regions.'},
        {'country': 'Angola', 'total_restore': 210000, 'avg_rate': 0.28, 'description': 'Angola planted over 200,000 hectares from 2016-2025, restoring areas degraded by charcoal production and shifting agriculture.'},
        {'country': 'Tanzania', 'total_restore': 380000, 'avg_rate': 0.41, 'description': 'Tanzania’s national campaigns and community forestry programs planted roughly 380,000 hectares over the decade.'},
        {'country': 'Myanmar', 'total_restore': 320000, 'avg_rate': 0.38, 'description': 'Myanmar implemented national reforestation programs and mangrove rehabilitation, planting over 300,000 hectares between 2015–2025.'},
        {'country': 'DR Congo', 'total_restore': 250000, 'avg_rate': 0.21, 'description': 'DR Congo reforested approximately 250,000 hectares as part of community-led forest restoration and REDD+ initiatives.'},
        {'country': 'Mozambique', 'total_restore': 300000, 'avg_rate': 0.36, 'description': 'Mozambique planted around 300,000 hectares under post-cyclone restoration and community forestry initiatives.'},
        {'country': 'Cambodia', 'total_restore': 410000, 'avg_rate': 0.55, 'description': 'Cambodia restored around 400,000 hectares through community forestry, watershed rehabilitation, and protected-area restoration.'},
        {'country': 'Peru', 'total_restore': 420000, 'avg_rate': 0.33, 'description': 'Peru replanted over 400,000 hectares in the Andes and Amazon regions as part of national reforestation and native species recovery programs.'},
        {'country': 'Bolivia', 'total_restore': 350000, 'avg_rate': 0.29, 'description': 'Bolivia planted around 350,000 hectares through forest restoration and Chaco region rehabilitation programs.'},
        {'country': 'Paraguay', 'total_restore': 300000, 'avg_rate': 0.26, 'description': 'Paraguay restored around 300,000 hectares, focusing on the Atlantic Forest and sustainable ranching buffer zones.'},
    ]
    
    with app.app_context():
        try:
            ReforestationData.query.delete()
            CountryMetadata.query.delete()
            
            for data in reforestation_data:
                entry = ReforestationData(
                    country=data['country'],
                    year=data['year'],
                    reforestation_percentage=data['percentage'],
                    forest_restored_hectares=data['hectares']
                )
                db.session.add(entry)
            
            for meta in country_metadata:
                entry = CountryMetadata(
                    country=meta['country'],
                    total_forest_restored_2015_2025=meta['total_restore'],
                    avg_annual_reforestation_rate=meta['avg_rate'],
                    description=meta['description']
                )
                db.session.add(entry)
            
            db.session.commit()
            print("✓ Database seeded successfully!")
            print(f"✓ Inserted {len(reforestation_data)} deforestation records")
            print(f"✓ Inserted {len(country_metadata)} country metadata records")
            
        except Exception as e:
            print(f"✗ Error seeding database: {e}")
            db.session.rollback()

if __name__ == '__main__':
    seed_reforestation_data()