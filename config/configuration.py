from distutils.debug import DEBUG

class Config:
    DEBUG=True
    TESTING=True
    
    USER_DB = 'root'
    PASS_DB = 'Lepo#1867'
    HOST_DB = 'localhost'
    PORT_DB = 3306
    NAME_DB = 'pyments_db'
    #Confiuracion Base de Datos
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://{}:{}@{}:{}/{}'.format(USER_DB, PASS_DB, HOST_DB, PORT_DB, NAME_DB)
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    
class ProductionConfig(Config):
    DEBUG=False
    
class DevelopmentConfig(Config):
    DEBUG=True
    SECRET_KEY='dev'
    TESTING=True