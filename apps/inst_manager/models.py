from extensions import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    code = db.Column(db.String(50), unique=True, nullable=False)


class InstrumentType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)


class Instrument(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(200))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    instrument_type_id = db.Column(db.Integer, db.ForeignKey("instrument_type.id"))


class JunctionBox(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(120), unique=True, nullable=False)
    location = db.Column(db.String(200))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
