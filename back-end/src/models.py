from app import db
import util
from sqlalchemy import and_, or_


class Matrix(db.Model):
    __tablename__ = 'matrix'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(255), )
    vendor_id = db.Column(db.String(255), db.ForeignKey('vendor.vendor_id'))
    model = db.Column(db.String(255))
    Horizon_client_version = db.Column(db.String(255))
    Horizon_agent_version = db.Column(db.String(255))
    redirect_method = db.Column(db.String(255))

    def to_json(self):
        return util.to_json(self, self.__class__)

    def __repr__(self):
        return '<matrix:{}>'.format(self.id)


class Device(db.Model):
    __tablename__ = 'device'
    __table_args__ = {'extend_existing': True}
    product_id = db.Column(db.String(255), primary_key=True)
    device_name = db.Column(db.String(255))
    vendor_id = db.Column(db.String(255), db.ForeignKey('vendor.vendor_id'), primary_key=True)
    description = db.Column(db.String(999))
    picture = db.Column(db.String(255))
    model = db.Column(db.String(255), primary_key=True)

    def to_json(self):
        return util.to_json(self, self.__class__)

    def __repr__(self):
        return '<device:{}>'.format(self.product_id + self.vendor_id)


class Vendor(db.Model):
    __tablename__ = 'vendor'
    __table_args__ = {'extend_existing': True}
    vendor_id = db.Column(db.Integer, primary_key=True, unique=True)
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
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(255), primary_key=True)
    vendor_id = db.Column(db.String(255), db.ForeignKey('vendor.vendor_id'), primary_key=True)
    model = db.Column(db.String(255))
    os_name = db.Column(db.String(255))
    driver = db.Column(db.String(255))

    def to_json(self):
        return util.to_json(self, self.__class__)

    def __repr__(self):
        return '<driver:{}>'.format(self.driver)


# todo: unit test
if __name__ == '__main__':
    print('Unit Test')
    # item = Vendor.query.filter(Vendor.vendor_id == '04F9').with_entities(Vendor.vendor_name,
    #                                                                         Vendor.vendor_link,
    #
    #                                                                         Vendor.vendor_logo).all()
    item = Matrix.query.all()

    matrix = Matrix.query.join(Device,
                               and_(and_(Device.product_id == Matrix.product_id, Device.vendor_id == Matrix.vendor_id),
                                    or_(Matrix.model == None, Matrix.model == Device.model)
                                   )
                               ).with_entities(Device.device_name,
                                               Matrix.product_id, Matrix.vendor_id, Matrix.model,
                                               Matrix.Horizon_client_version,Matrix.Horizon_agent_version,
                                               Matrix.redirect_method).all()
    print(matrix)
