# pip install bcrypt
import bcrypt

# bcrypt 내부 함수를 알아야 비밀번호 검증을 할 수 있음

def generate_hash(password):
    # hashlib.sha256(password.encode()).hexdigest() 방법으로 hash 값으로 변경한 경우 hash 값으로 변경한 암호도 털릴 수 있어 hash 암호에 salt(랜덤값)을 넣는 bcrypt 방식을 사용
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode(), salt)
    return hashed

def verify_password(password, hashed_password):
    return bcrypt.checkpw(password.encode(), hashed_password)

hashed1 = generate_hash('hello123')
hashed2 = generate_hash('hello123')

print('Hash1 :', hashed1)
print('Hash2 :', hashed2)

print("Hash1 암호검증: ", verify_password("hello222", hashed1))
print("Hash1 암호검증: ", verify_password("hello123", hashed1))
