from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def create_hash(texto):
    return pwd_context.hash(texto)


def verify_hash(texto, hash):
    return pwd_context.verify(texto, hash)
