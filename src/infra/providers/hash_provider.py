from passlib.context import CryptContext
from src.infra.config.config import settings

pwd_context = CryptContext(schemes=[settings.hash.scheme])


def create_hash(texto):
    return pwd_context.hash(texto)


def verify_hash(texto, hash):
    return pwd_context.verify(texto, hash)
