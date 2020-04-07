from .app import db
from . import util


class Matrix(db.Model):
        __tablename__ = 'matrix'
        __table_args__ = {'extend_existing': True}

        id = db.Column(db.Integer,primary_key=True)
        device_id = db.Column(db.Integer)
        client_os_name = db.Column(db.String(255))
        Horizon_client_version = db.Column(db.String(255))
        agent_os_name = db.Column(db.String(255))
        Horizon_agent_version= db.Column(db.String(255))
        redirect_method = db.Column(db.String(255))

        def to_json(self):
            return util.to_json(self, self.__class__)

        def __repr__(self):
            return '<matrix:{}>'.format(self.device_id)


class Device(db.Model):
        __tablename__ = 'device'
        __table_args__ = {'extend_existing': True}
        device_id = db.Column(db.Integer, primary_key=True, unique=True)
        device_name = db.Column(db.String(255))
        device_version = db.Column(db.String(255))
        vendor_id = db.Column(db.String(255), db.ForeignKey('vendor.vendor_id'))
        description = db.Column(db.String(999))
        picture= db.Column(db.String(255))

        def to_json(self):
            return util.to_json(self, self.__class__)

        def __repr__(self):
            return '<device:{}>'.format(self.device_id)


class Vendor(db.Model):
        __tablename__ = 'vendor'
        __table_args__ = {'extend_existing': True}
        vendor_id = db.Column(db.Integer, primary_key= True, unique=True)
        vendor_name = db.Column(db.String(255))
        vendor_logo = db.Column(db.String(255))
        vendor_link = db.Column(db.String(255))

        def to_json(self):
                return util.to_json(self, self.__class__)

        def __repr__(self):
                return '<vendor:{}>'.format(self.vendor_id)


class Driver(db.Model):
        __tablename__ = 'driver'
        __table_args__ = {'extend_existing': True}
        id = db.Column(db.Integer,primary_key=True)
        device_id = db.Column(db.Integer)
        os_name = db.Column(db.String(255))
        client_driver = db.Column(db.String(255))
        agent_driver = db.Column(db.String(255))

        def to_json(self):
                return util.to_json(self, self.__class__)

        def __repr__(self):
                return '<vendor:{}>'.format(self.vendor_id)
