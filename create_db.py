from web_app import create_app
from web_app.models import db

app = create_app()
app.app_context().push()
db.create_all()