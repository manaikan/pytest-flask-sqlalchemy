from .database import DATABASE

class Table(DATABASE.Model):
    __tablename__ = 'table'
    id = DATABASE.Column(DATABASE.Integer, primary_key=True)
    name = DATABASE.Column(DATABASE.String(80))

    # def __init__(self, name):
    #     self.name = name

    def set_name(self, new_name):
        self.name = new_name
        DATABASE.session.add(self)
        DATABASE.session.commit()