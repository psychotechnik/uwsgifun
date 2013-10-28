from flreports import db


class Emperor(db.Document):
    name = db.StringField(required=True)


class Vassal(db.Document):
    name = db.StringField(required=True)
