from passlib.context import CryptContext


pwd_context:CryptContext = CryptContext(schemes=['bcrypt'])


def verify_hash(text, hashed_text) ->bool:
    return pwd_context.verify(text, hashed_text)


def create_hash(text) ->str:
    return pwd_context.hash(text)   