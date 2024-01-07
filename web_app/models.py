from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class OlxSite(db.Model):
    __tablename__ = 'olx_site'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String)
    category = db.Column(db.String)
    ads_name = db.Column(db.String)
    ads_content = db.Column(db.Text)
    phone_number = db.Column(db.Integer)
    raw_url_num_loc = db.Column(db.String)
    seller_name = db.Column(db.String)
    registration_date = db.Column(db.DateTime, nullable=False)
    number_of_looks = db.Column(db.Integer)
    location = db.Column(db.String)
    picture = db.Column(db.String(120))

    def __repr__(self):
        return f'<Ads {self.name} {self.content}>'

