from app import db
import util

class Matrix(db.Model):
        __tablename__ = 'matrix'
        device_name = db.Column(db.String(255), primary_key=  True)
        device_version = db.Column(db.String(255))
        client_os = db.Column(db.String(255))
        client_version = db.Column(db.String(255))
        agent_os = db.Column(db.String(255))
        agent_version = db.Column(db.String(255))
        suggestions = db.Column(db.String(999))

        def to_json(self):
            return util.to_json(self, self.__class__)

        def __repr__(self):
            return '<matrix:{}>'.format(self.device_name)


