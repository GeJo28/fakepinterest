from fakepinterest import app, database
from fakepinterest.models import Usuario, Foto

with app.app_context():
    database.create_all()