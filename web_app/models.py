from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Olx_Site(db.Model):
    __tablename__ = 'olx_site'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    ads_name = db.Column(db.String)
    ads_content = db.Column(db.Text)
    phone_number = db.Column(db.Integer)
    seller_name = db.Column(db.String)
    registration_date = db.Column(db.DateTime, nullable=False)
    number_of_looks = db.Column(db.Integer)
    location = db.Column(db.String)
    picture = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return f'<Ads {self.name} {self.content}>'
