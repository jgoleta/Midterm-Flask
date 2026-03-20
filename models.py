<<<<<<< HEAD
from datetime import datetime
from app import db

class ProductStock(db.Model):
    __tablename__ = 'product_stock'
    __table__ = db.Table('product_stock', db.metadata, autoload_with=db.engine)
    
    def __repr__(self):
        return f"<ProductStock {self.name}>"

class ProductTransaction(db.Model):
    __tablename__ = 'product_transactions'
    __table__ = db.Table('product_transactions', db.metadata, autoload_with=db.engine)
    
    def __repr__(self):
        return f"<ProductTransaction {self.name}>"

=======
from datetime import datetime
from app import db

class ProductStock(db.Model):
    __tablename__ = 'product_stock'
    __table__ = db.Table('product_stock', db.metadata, autoload_with=db.engine)
    
    def __repr__(self):
        return f"<ProductStock {self.name}>"

class ProductTransaction(db.Model):
    __tablename__ = 'product_transactions'
    __table__ = db.Table('product_transactions', db.metadata, autoload_with=db.engine)
    
    def __repr__(self):
        return f"<ProductTransaction {self.name}>"

>>>>>>> d4e61db924589eff607351afb22ce15104705d0b
