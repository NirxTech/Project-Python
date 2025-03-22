import re

def cek_keamanan_pw(password):

    panjang = len(password) >= 8
    huruf_besar = bool(re.search(r'[A-Z]', password))
    huruf_kecil = bool(re.search(r'[a-z]', password))
    angka = bool(re.search(r'[0-9]', password))
    simbol = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    if panjang and huruf_besar and huruf_kecil and angka and simbol:
        return "Password Mu Kuat, se Kuat baja"
    elif panjang and (huruf_besar or huruf_kecil) and angka:
        return "Password Mu Kurang Kuat, coba tambahkan simbol"
    else:
        return "Password Mu Kaya Kerupuk"
    
def cek_keamanan_email(email):

    pola_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pola_email, email):
        return "Email Anda valid"
    else:
        return "Ga Valid"
    
print()
email_user = input("Masukkan Email Mu: ")
password_user = input("Masukkan Password Mu: ")
tingkat_keamanan_email = cek_keamanan_email(email_user)
tingkat_keamanan_pw = cek_keamanan_pw(password_user)
print()
print(f"Email: {email_user} - Tingkat Keamanan: {tingkat_keamanan_email}")
print(f"Password: {password_user} - Tingkat Keamanan: {tingkat_keamanan_pw}")