import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
import pytest
from src.services.auth_service import AuthService
from src.database.session import SessionLocal
from src.models.user import User

@pytest.fixture
def db():
    session = SessionLocal()
    yield session
    session.close()

@pytest.fixture
def auth_service(db):
    return AuthService(db)

def test_create_user(auth_service):
    user = auth_service.create_user('Teste', 'teste@exemplo.com', 'senha123')
    assert user.email == 'teste@exemplo.com'
    assert user.name == 'Teste'
    assert user.password_hash != 'senha123'

def test_authenticate(auth_service):
    auth_service.create_user('Teste2', 'teste2@exemplo.com', 'senha456')
    user = auth_service.authenticate('teste2@exemplo.com', 'senha456')
    assert user is not None
    assert user.email == 'teste2@exemplo.com'
    assert auth_service.authenticate('teste2@exemplo.com', 'errada') is None
