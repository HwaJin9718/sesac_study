import smtplib
from email.mime.text import MIMEText # 메일의 컨텐츠 인코딩 포멧
import os
from dotenv import load_dotenv

load_dotenv()

# Gmail IMAP 설정 : 
# Gmail > Manage labels > Forwarding and POP/IMAP > IMAP access > When I mark a message in IMAP as deleted > Auto-Expunge on - Immediately update th server.(default) > check > Save Changes

# Gmail 2단계 인증 : 우측 상단 프로필 > Manage your Google Account > Security > 2-Step Verification > phone number or Google prompt 설정 > Turn on 2-Step Verification > App passwords (메뉴 안보이면 앱 비밀번호 검색) > App name 입력 후 Create

# Google IMAP 설정 참고 url : https://kincoding.com/entry/Google-Gmail-SMTP-%EC%82%AC%EC%9A%A9%EC%9D%84-%EC%9C%84%ED%95%9C-%EC%84%B8%ED%8C%85-2025%EB%85%84-%EB%B2%84%EC%A0%84

SMTP_SERVER = os.getenv('GOOGLE_SMTP_SERVER')
SMTP_PORT = os.getenv('GOOGLE_SMTP_PORT')

GOOGLE_EMAIL = os.getenv('GOOGLE_EMAIL')
GOOGLE_PASSWORD = os.getenv('GOOGLE_PASSWORD')

# 받는사람 메일 주소
RECIPIENT_MAIL = 'ajffhsk2248@naver.com'

# 메일 내용
subject = 'Gmail 발송 테스트 입니다.'
body = '이 메일은 파이썬을 통해서 생성되었습니다.'

message = MIMEText(body, _charset='utf-8')
message['subject'] = subject
message['from'] = GOOGLE_EMAIL
message['to'] = RECIPIENT_MAIL

try:
    smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    smtp.starttls() # TLS 보안 연결 시작
    smtp.login(GOOGLE_EMAIL, GOOGLE_PASSWORD) # 로그인
    smtp.sendmail(GOOGLE_EMAIL, RECIPIENT_MAIL, message.as_string()) # 전송
    print('메일이 성공적으로 발송되었습니다.')
except Exception as e:
    print(f'메일 전송 중 오류 발생 : {e}')
finally:
    smtp.quit() # 종료
