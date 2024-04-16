from passlib.context import CryptContext
# passlib no longer maintained, consider using bcrypt directly https://github.com/pyca/bcrypt/issues/684

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)