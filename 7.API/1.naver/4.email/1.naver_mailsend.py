import smtplib
from email.mime.text import MIMEText # 메일의 컨텐츠 인코딩 포멧
import os
from dotenv import load_dotenv

load_dotenv()

# 전통적으로 메일 발송하는 프로토콜 : 메일 보내기 -> SMTP , 메일 받기 -> POP
# 위 두가지를 통합해 놓은 IMAP (요즘 최신)

SMTP_SERVER = 'smtp.naver.com' # 이것도 환경변수로 빼는게 가장 좋음
SMTP_PORT = 587 # SMTP 는 465, IAMP 는 587 (단, 서버 주소(SMTP_SERVER)는 동일)

NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

# 받는사람 메일 주소
RECIPIENT_MAIL = 'ajffhsk2248@naver.com'

# 메일 내용
subject = '네이버 이메일 테스트 입니다.'
body = '이 메일은 파이썬을 통해서 생성되었습니다.'

message = MIMEText(body, _charset='utf-8')
message['subject'] = subject
message['from'] = NAVER_EMAIL
message['to'] = RECIPIENT_MAIL

try:
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls() # TLS 보안 연결 시작
    smtp.login(NAVER_EMAIL, NAVER_PASSWORD) # 로그인
    smtp.sendmail(NAVER_EMAIL, RECIPIENT_MAIL, message.as_string()) # 전송
    print('메일이 성공적으로 발송되었습니다.')
except Exception as e:
    print(f'메일 전송 중 오류 발생 : {e}')
finally:
    smtp.quit() # 종료
