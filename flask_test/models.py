from .database import db

class Table(db.Model):
    __tablename__ = 'table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    def set_name(self, new_name):
        self.name = new_name
        db.session.add(self)
        db.session.commit()