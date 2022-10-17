class Config(object):
    DEBUG = TESTING = True
    DATABASE_URI = "mysql+mysqlconnector://aluno:aluno123@localhost/RICK_MORTY"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI