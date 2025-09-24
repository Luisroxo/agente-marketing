from src.models.user import User
from src.database.session import SessionLocal
from sqlalchemy.orm import Session
from passlib.hash import bcrypt

class AuthService:
    def __init__(self, db: Session = None):
        self.db = db or SessionLocal()

    def create_user(self, name, email, password, profile='user'):
        password_hash = bcrypt.hash(password)
        user = User(name=name, email=email, password_hash=password_hash, profile=profile)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def authenticate(self, email, password):
        user = self.db.query(User).filter(User.email == email).first()
        if user and bcrypt.verify(password, user.password_hash):
            return user
        return None
