from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Para testes locais, usar SQLite
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///agente_marketing.db')

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
