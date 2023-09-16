import bcrypt

def encrypt_password(password):
    """
    Enkripsi password:

    Args:
        password : str -> input password dari user
    
    Returns
        password : str -> password yang telah di enkripsi
    """
    
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    # Convert the bytes to a string for storage
    return hashed_password.decode('utf-8')