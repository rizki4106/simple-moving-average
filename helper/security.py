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

def verify_password(entered_password, stored_hashed_password):
    """
    Memverifikasi apakah password user sama dengan yang dia masukan
    pada saat pendaftaran

    Args:
        entered_password: str -> password yang diinput user pada waktu login
        store_hased_password: str -> password yang tersimpan di database
    
    Returns:
        boolean -> true jika sama dan false jika tidak sama
    """
    return bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password.encode('utf-8'))