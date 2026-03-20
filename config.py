<<<<<<< HEAD
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-this')
    
    #Supabase PostgreSQL URL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }
    
    DEBUG = True
=======
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-change-this')
    
    #Supabase PostgreSQL URL
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_pre_ping': True,
        'pool_recycle': 300,
    }
    
    DEBUG = True
>>>>>>> d4e61db924589eff607351afb22ce15104705d0b
    TEMPLATES_AUTO_RELOAD = True