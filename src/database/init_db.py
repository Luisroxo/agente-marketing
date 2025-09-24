from models.user import Base
from database.session import engine

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")
