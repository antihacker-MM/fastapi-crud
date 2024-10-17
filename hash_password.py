import bcrypt

def hash_passwd(plain_password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(plain_password.encode('utf-8'),salt)
    return hashed_password