import imaplib # 메일 받아오는 라이브러리
import email # 파싱
from email.header import decode_header # 헤더정보 가져오기
from dotenv import load_dotenv
import os

load_dotenv()

IMAP_SERVER = 'imap.naver.com'
IMAP_PORT = 993

NAVER_EMAIL = os.getenv('NAVER_EMAIL')
NAVER_PASSWORD = os.getenv('NAVER_PASSWORD')

mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
mail.login(NAVER_EMAIL, NAVER_PASSWORD)

# 메일함 선택 (기본 메일함 INBOX)
mail.select('INBOX')
status, messages = mail.search(None, 'ALL')

# print(status, messages)

mail_ids = messages[0].split()
latest_mail_id = mail_ids[-1] # 가장 끝, (즉 최시 이메일 ID 가져오기)

# 최신 메일 가져오기
status, msg_data = mail.fetch(latest_mail_id, '(RFC822)')
print(status, msg_data)

# 이제 본문 데이터 파싱하기
for response_part in msg_data:
    if isinstance(response_part, tuple):
        msg = email.message_from_bytes(response_part[1])

        # 메일 제목 디코딩
        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding if encoding else 'utf-8')
        print(f'제목: {subject}')

        # 발신자 정보
        from_ = msg.get('From')
        print(f'발신자 : {from_}')

        # 메일 본문 추출
        if msg.is_multipart():
            for part in msg.walk(): # 메일 본문, 멀티파트로 인코딩 된걸 하나하나 읽어가기
                content_type = part.get_content_type()
                # body = part.get_payload(decode=True).decode('utf-8')
                
                # 본문이 없는 경우 decode 시 오류 발생 if else 문으로 예외처리
                body = part.get_payload(decode=True)
                if body:
                    body = body.decode('utf-8')
                else:
                    body = '본문에 텍스트가 없습니다.'

                # 본문이 없는 경우 decode 시 오류 발생 try ... catch 문으로 예외처리
                # try:
                #     body = part.get_payload(decode=True)
                #     if body:
                #         body = body.decode('utf-8')
                #     else:
                #         body = '본문에 텍스트가 없습니다.'
                # except Exception as e:
                #     print(f'메일 전송 중 오류 발생 : {e}')
                print(f'본문: {body}')
                
        else: # 단일 파트 메일
            body = msg.get_payload(decode=True).decode('utf-8')
            print(f'본문: {body}')
            break
    
    mail.logout()
