from Flask_SQLAlchemy import SQLAlchemy

db = SQLAlchemy()

class Fact(db.mModel):
    __tablename__ = 'facts'

    id = db.Column(db.Integer, primary_key=True)
    submitter = db.Column(db.String(250))
    fact = db.Column(db.Text)