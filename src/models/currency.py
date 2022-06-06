from src import db, ma

class Currency(db.Model):
    __tablename__ = 'currencies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    endpoint = db.Column(db.String(120))
    created_at = db.Column(db.DateTime, default=db.func.now(), nullable=False)
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now(), nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=True)
        
    def __init__(self, name, endpoint):
        self.name = name
        self.endpoint = endpoint
        
    def __repr__(self):
        return '<Currency %r>' % self.name