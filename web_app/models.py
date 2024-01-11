from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class OlxSite(db.Model):
    __tablename__ = 'olx_site'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, unique=True)
    category = db.Column(db.String)
    ads_name = db.Column(db.String)
    ads_content = db.Column(db.Text)
    phone_number = db.Column(db.String)
    seller_name = db.Column(db.String)
    date_registered = db.Column(db.DateTime)
    date_of_last_visit = db.Column(db.DateTime)
    date_posted = db.Column(db.DateTime)
    number_of_looks = db.Column(db.Integer)
    location = db.Column(db.String)
    picture = db.Column(db.String)

    def __repr__(self):
        return f'<Ads {self.name} {self.content}>'

