import secrets
import string

length = int(input("Password length: "))

if length < 4:
    print("Use at least 4 characters.")
    raise SystemExit

characters = string.ascii_letters + string.digits + "!@#$%^&*"
password = "".join(secrets.choice(characters) for _ in range(length))

print("Generated password:", password)
