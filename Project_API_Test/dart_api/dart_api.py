# 기업 정보 데이터
# 공시서류원본파일 : https://opendart.fss.or.kr/guide/detail.do?apiGrpCd=DS001&apiId=2019003

from dotenv import load_dotenv
from flask import Flask, request, redirect, url_for, session, jsonify
import requests
import os
import zipfile
import io
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
import re

load_dotenv()

app=Flask(__name__)
app.secret_key = os.getenv("SESSION_SECRET")

DART_CLIENT_ID=os.getenv("DART_API_KEY")


# 1단계: 기업 고유번호 조회
# def get_company_unique_code(code):

#     corp_code_url = "https://opendart.fss.or.kr/api/corpCode.xml"
#     response = requests.get(corp_code_url, params={'crtfc_key': DART_CLIENT_ID})

#     # ZIP 파일에서 XML 추출
#     zip_file = zipfile.ZipFile(io.BytesIO(response.content))
#     xml_data = zip_file.read('CORPCODE.xml').decode('utf-8')
#     root = ET.fromstring(xml_data)

#     # 종목코드로 기업 고유번호 찾기
#     corp_code = None
#     for item in root.findall('.//list'):
#         if item.find('stock_code') is not None and item.find('stock_code').text == code:
#             corp_code = item.find('corp_code').text
#             break
    
#     if not corp_code:
#         return f"종목코드 {code}를 찾을 수 없습니다."
    
#     print(f"기업 고유번호: {corp_code}")

#     return corp_code


# 2단계: 공시목록 조회 (사업보고서 찾기)
# def get_report_receipt_number(code):

#     list_url = "https://opendart.fss.or.kr/api/list.json"
#     params = {
#         'crtfc_key': DART_CLIENT_ID,
#         'corp_code': code,
#         'bgn_de': '20230101',  # 2023년부터
#         'pblntf_ty': 'A',      # 정기공시
#         'page_count': 10
#     }

#     response = requests.get(list_url, params=params)
#     data = response.json()

#     if data['status'] != '000' or 'list' not in data:
#         return "사업보고서를 찾을 수 없습니다."
    
#     # 사업보고서 접수번호 찾기
#     rcept_no = None
#     for report in data['list']:
#         if '사업보고서' in report.get('report_nm', ''):
#             rcept_no = report['rcept_no']
#             break
    
#     if not rcept_no:
#         return "사업보고서를 찾을 수 없습니다."
    
#     print(f"사업보고서 접수번호: {rcept_no}")
    
#     return rcept_no


# 3단계: 공시서류 하위문서 구조 조회 -> 회사 개요 찾기
# def search_company_overview(url, receipt_number):

#     params = {
#         'crtfc_key': DART_CLIENT_ID,
#         'rcept_no': receipt_number
#     }
    
#     response = requests.get(url, params=params)
    
#     # XML에서 회사의 개요 섹션 찾기
#     soup = BeautifulSoup(response.text, 'xml')
    
#     overview_section = None
#     for elem in soup.find_all():
#         if elem.string and ('회사의 개요' in elem.string or '회사개요' in elem.string):
#             # 상위 요소에서 dcm_no, ele_id 찾기
#             parent = elem.parent
#             while parent:
#                 if parent.name and parent.get('dcm_no') and parent.get('ele_id'):
#                     overview_section = {
#                         'dcm_no': parent.get('dcm_no'),
#                         'ele_id': parent.get('ele_id'),
#                         'title': elem.string
#                     }
#                     break
#                 parent = parent.parent
#             if overview_section:
#                 break
    
#     if not overview_section:
#         # 대안: 첫 번째 문서에서 찾기
#         first_doc = soup.find(attrs={'dcm_no': True, 'ele_id': True})
#         if first_doc:
#             overview_section = {
#                 'dcm_no': first_doc.get('dcm_no'),
#                 'ele_id': first_doc.get('ele_id'),
#                 'title': '회사 정보'
#             }
    
#     if not overview_section:
#         return "회사의 개요 섹션을 찾을 수 없습니다."
    
#     print(f"개요 섹션 발견: {overview_section['title']}")

#     return overview_section


# 4단계: 특정 섹션 내용 조회 -> 회사 개요 내용
# def search_overview_section(url, receipt_number, section):

#     params = {
#         'crtfc_key': DART_CLIENT_ID,
#         'rcept_no': receipt_number,
#         'dcm_no': section['dcm_no'],
#         'ele_id': section['ele_id']
#     }
    
#     response = requests.get(url, params=params)
    
#     # HTML/XML에서 텍스트 추출
#     soup = BeautifulSoup(response.text, 'html.parser')
    
#     # 불필요한 태그 제거
#     for script in soup(["script", "style"]):
#         script.decompose()
    
#     # 텍스트 추출 및 정리
#     text = soup.get_text()
#     lines = (line.strip() for line in text.splitlines())
#     text = '\n'.join(line for line in lines if line)
    
#     # 너무 길면 처음 2000자만
#     # if len(text) > 2000:
#     #     text = text[:2000] + "..."

#     return text


# @app.route('/api/dart/<stock_code>')
# def dart(stock_code):

#     doc_url = "https://opendart.fss.or.kr/api/document.xml"

#     # 1단계: 기업 고유번호 조회
#     corp_code = get_company_unique_code(stock_code)

#     # 2단계: 공시목록 조회 (사업보고서 찾기)
#     rcept_no = get_report_receipt_number(corp_code)

#     # 3단계: 공시서류 하위문서 구조 조회
#     company_overview = search_company_overview(doc_url, rcept_no)

#     # 4단계: 특정 섹션 내용 조회
#     text = search_overview_section(doc_url, rcept_no, company_overview)

#     return {
#         'stock_code': stock_code,
#         'corp_code': corp_code,
#         'rcept_no': rcept_no,
#         'section_title': company_overview['title'],
#         'overview': text
#     }


@app.route('/api/dart/<stock_code>')
def dart(stock_code):

    """반기보고서에서 사업의 개요 추출"""

    # 1단계: 기업 고유번호 조회
    print("1단계: 기업 고유번호 조회...")
    corp_code_url = "https://opendart.fss.or.kr/api/corpCode.xml"
    response = requests.get(corp_code_url, params={'crtfc_key': DART_CLIENT_ID})
    
    zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    xml_data = zip_file.read('CORPCODE.xml').decode('utf-8')
    root = ET.fromstring(xml_data)
    
    corp_code = None
    corp_name = None
    for item in root.findall('.//list'):
        if item.find('stock_code') is not None and item.find('stock_code').text == stock_code:
            corp_code = item.find('corp_code').text
            corp_name = item.find('corp_name').text
            break
    
    if not corp_code:
        return {"error": f"종목코드 {stock_code}를 찾을 수 없습니다."}
    
    print(f"기업: {corp_name} ({corp_code})")
    
    # 2단계: 반기보고서 접수번호 조회
    print("2단계: 반기보고서 접수번호 조회...")
    list_url = "https://opendart.fss.or.kr/api/list.json"
    params = {
        'crtfc_key': DART_CLIENT_ID,
        'corp_code': corp_code,
        'bgn_de': '20230101',  # 2023년부터
        'pblntf_ty': 'A',      # 정기공시
        'page_count': 10
    }
    
    response = requests.get(list_url, params=params)
    data = response.json()
    
    if data['status'] != '000' or 'list' not in data:
        return {"error": "반기보고서를 찾을 수 없습니다."}
    
    # 반기보고서 접수번호 찾기 (가장 최근)
    rcept_no = None
    report_nm = None
    for report in data['list']:
        if '반기보고서' in report.get('report_nm', ''):
            rcept_no = report['rcept_no']
            report_nm = report['report_nm']
            break
    
    if not rcept_no:
        return {"error": "반기보고서를 찾을 수 없습니다."}
    
    print(f"반기보고서 발견: {report_nm} (접수번호: {rcept_no})")
    
    # 3단계: 반기보고서 ZIP 파일 다운로드 및 압축해제
    print("3단계: 반기보고서 다운로드...")
    doc_url = "https://opendart.fss.or.kr/api/document.xml"
    params = {
        'crtfc_key': DART_CLIENT_ID,
        'rcept_no': rcept_no
    }
    
    response = requests.get(doc_url, params=params)
    print(f"응답 상태: {response.status_code}")
    
    # ZIP 파일 처리
    if response.content[:2] == b'PK':
        try:
            zip_file = zipfile.ZipFile(io.BytesIO(response.content))
            file_list = zip_file.namelist()
            print(f"ZIP 파일 내용: {file_list}")
            
            # 첫 번째 XML 파일 읽기
            xml_filename = file_list[0]
            xml_content = zip_file.read(xml_filename).decode('utf-8')
            print(f"XML 파일 크기: {len(xml_content)} 문자")
            
        except Exception as e:
            print(f"ZIP 파일 처리 오류: {e}")
            return {"error": f"ZIP 파일 처리 오류: {e}"}
    else:
        xml_content = response.text
    
    # 4단계: "사업의 개요" 섹션 추출
    print("4단계: 사업의 개요 추출...")
    
    try:
        # XML parser 사용
        from bs4 import XMLParsedAsHTMLWarning
        import warnings
        warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
        
        soup = BeautifulSoup(xml_content, 'xml')
        full_text = soup.get_text()
        
        print(f"전체 텍스트 길이: {len(full_text)} 문자")
        
        # 사업의 개요 추출을 위한 패턴들
        business_overview = ""
        
        # 방법 1: 정규식 패턴 매칭
        patterns = [
            r'사업의\s*개요[\s\S]*?(?=(?:사업의\s*내용|주요\s*제품|영업\s*현황|II\.|2\.)[\s\S]{0,100})',
            r'I\.\s*사업의\s*개요[\s\S]*?(?=(?:II\.|2\.|사업의\s*내용)[\s\S]{0,100})',
            r'1\.\s*사업의\s*개요[\s\S]*?(?=(?:2\.|사업의\s*내용|주요\s*제품)[\s\S]{0,100})',
            r'가\.\s*사업의\s*개요[\s\S]*?(?=(?:나\.|사업의\s*내용)[\s\S]{0,100})',
        ]
        
        for i, pattern in enumerate(patterns):
            matches = re.finditer(pattern, full_text, re.IGNORECASE | re.DOTALL)
            for match in matches:
                text = match.group(0)
                if len(text) > 300:  # 충분한 길이의 텍스트만
                    business_overview = text
                    print(f"패턴 {i+1} 매칭 성공, 길이: {len(text)}")
                    break
            if business_overview:
                break
        
        # 방법 2: 키워드 주변 대량 텍스트 추출
        if not business_overview or len(business_overview) < 300:
            print("키워드 주변 대량 텍스트 추출...")
            
            # 사업의 개요 시작 위치 찾기
            start_keywords = ['사업의 개요', '사업개요', 'I. 사업', '1. 사업']
            start_pos = -1
            
            for keyword in start_keywords:
                pos = full_text.find(keyword)
                if pos != -1:
                    start_pos = pos
                    print(f"시작 키워드 '{keyword}' 발견: 위치 {pos}")
                    break
            
            if start_pos != -1:
                # 시작 위치에서 4000자 추출
                business_overview = full_text[start_pos:start_pos + 4000]
                
                # 적절한 끝 위치에서 자르기
                end_keywords = ['사업의 내용', '주요 제품', '영업 현황', 'II.', '2.', '나.']
                for keyword in end_keywords:
                    pos = business_overview.find(keyword, 300)  # 최소 300자 이후에서 찾기
                    if pos != -1:
                        business_overview = business_overview[:pos]
                        break
                
                print(f"키워드 주변 추출 성공, 길이: {len(business_overview)}")
        
        # 방법 3: 전체 텍스트에서 사업 관련 부분 추출 (최후의 수단)
        if not business_overview or len(business_overview) < 100:
            print("전체 텍스트에서 사업 관련 부분 추출...")
            
            # 사업 관련 키워드가 포함된 문단들 찾기
            sentences = full_text.split('\n')
            business_sentences = []
            
            business_keywords = ['사업', '제품', '서비스', '영업', '매출', '고객', '시장']
            
            for sentence in sentences:
                sentence = sentence.strip()
                if len(sentence) > 20 and any(keyword in sentence for keyword in business_keywords):
                    business_sentences.append(sentence)
                if len('\n'.join(business_sentences)) > 2000:
                    break
            
            if business_sentences:
                business_overview = '\n'.join(business_sentences[:20])  # 최대 20문장
                print(f"키워드 기반 추출 성공, 길이: {len(business_overview)}")
        
        # 텍스트 정리
        if business_overview:
            # 줄바꿈과 공백 정리
            lines = []
            for line in business_overview.splitlines():
                line = line.strip()
                if line and len(line) > 5:  # 의미있는 줄만
                    lines.append(line)
            
            business_overview = '\n'.join(lines)
            
            # 길이 제한
            if len(business_overview) > 2500:
                business_overview = business_overview[:2500] + "..."
        
        print(f"최종 추출된 텍스트 길이: {len(business_overview)}")
        print(f"추출된 텍스트 미리보기: {business_overview[:200]}...")
        
        # 결과 반환
        result = {
            'stock_code': stock_code,
            'corp_code': corp_code,
            'company_name': corp_name,
            'rcept_no': rcept_no,
            'report_name': report_nm,
            'business_overview': business_overview if business_overview else "사업의 개요를 추출할 수 없습니다.",
            'text_length': len(business_overview) if business_overview else 0
        }
        
        return result
        
    except Exception as e:
        print(f"XML 처리 오류: {e}")
        
        # 최후의 수단: 기업개황 API
        print("기업개황 API로 대체...")
        company_url = "https://opendart.fss.or.kr/api/company.json"
        params = {
            'crtfc_key': DART_CLIENT_ID,
            'corp_code': corp_code
        }
        
        response = requests.get(company_url, params=params)
        company_data = response.json()
        
        if company_data['status'] == '000':
            overview = f"{corp_name}의 사업 개요:\n"
            overview += f"대표자: {company_data.get('ceo_nm', '')}\n"
            overview += f"소재지: {company_data.get('adres', '')}\n"
            overview += f"홈페이지: {company_data.get('hm_url', '')}"
            
            return {
                'stock_code': stock_code,
                'corp_code': corp_code,
                'company_name': corp_name,
                'business_overview': overview,
                'fallback': True
            }
        else:
            return {"error": f"모든 방법 실패: {e}"}

#     {
#     "business_overview": "사업의 개요\n당사는 경기도 이천시에 위치한 본사를 거점으로 4개의 생산기지와 3개의 연구개발법인 및 미국, 중국, 싱가포르, 대만, 홍콩 등 판매법인과 사무소를 운영하고 있는 글로벌 반도체 기업입니다.\n당사 및 당사의 종속기업의 주력 제품은 DRAM 및 NAND를 중심으로 하는 메모리 반도체이며, Foundry 사업도 병행하고 있습니다. 반도체는 메모리 반도체와 시스템 반도체로 구분되고, 메모리 반도체는 정보를 저장하고 기억하는 기능을 하며, 일반적으로 '휘발성(Volatile)'과 '비휘발성(Non-volatile)'으로 분류됩니다. 휘발성 메모리 제품은 전원이 끊어지면 정보가 지워지는 반면, 비휘발성 제품은 전원이 끊겨도 저장된 정보가 계속 남아 있습니다. 당사는 휘발성 메모리인 DRAM과 비휘발성 메모리인 NAND Flash를 주력 생산하고 있습니다.\n당사의 연결 기준 매출액은 2025년 반기(누계) 39조 8,711억원을 기록하였습니다.",
#     "company_name": "SK하이닉스",
#     "corp_code": "00164779",
#     "rcept_no": "20250814003049",
#     "report_name": "반기보고서 (2025.06)",
#     "stock_code": "000660",
#     "text_length": 478
# }

    # 1단계: 기업 고유번호 조회
    # print("1단계: 기업 고유번호 조회...")
    # corp_code_url = "https://opendart.fss.or.kr/api/corpCode.xml"
    # response = requests.get(corp_code_url, params={'crtfc_key': DART_CLIENT_ID})
    
    # # ZIP 파일에서 XML 추출
    # zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    # xml_data = zip_file.read('CORPCODE.xml').decode('utf-8')
    # root = ET.fromstring(xml_data)
    
    # # 종목코드로 기업 고유번호 찾기
    # corp_code = None
    # for item in root.findall('.//list'):
    #     if item.find('stock_code') is not None and item.find('stock_code').text == stock_code:
    #         corp_code = item.find('corp_code').text
    #         break
    
    # if not corp_code:
    #     return {"error": f"종목코드 {stock_code}를 찾을 수 없습니다."}
    
    # print(f"기업 고유번호: {corp_code}")
    
    # # 2단계: 공시목록 조회 (사업보고서 찾기)
    # print("2단계: 사업보고서 접수번호 조회...")
    # list_url = "https://opendart.fss.or.kr/api/list.json"
    # params = {
    #     'crtfc_key': DART_CLIENT_ID,
    #     'corp_code': corp_code,
    #     'bgn_de': '20230101',  # 2023년부터
    #     'pblntf_ty': 'A',      # 정기공시
    #     'page_count': 10
    # }
    
    # response = requests.get(list_url, params=params)
    # data = response.json()
    
    # if data['status'] != '000' or 'list' not in data:
    #     return {"error": "사업보고서를 찾을 수 없습니다."}
    
    # # 사업보고서 접수번호 찾기
    # rcept_no = None
    # for report in data['list']:
    #     if '사업보고서' in report.get('report_nm', ''):
    #         rcept_no = report['rcept_no']
    #         break
    
    # if not rcept_no:
    #     return {"error": "사업보고서를 찾을 수 없습니다."}
    
    # print(f"사업보고서 접수번호: {rcept_no}")
    
    # # 3단계: 공시서류 원본 다운로드 (ZIP 파일)
    # print("3단계: ZIP 압축된 사업보고서 다운로드...")
    # doc_url = "https://opendart.fss.or.kr/api/document.xml"
    # params = {
    #     'crtfc_key': DART_CLIENT_ID,
    #     'rcept_no': rcept_no
    # }
    
    # response = requests.get(doc_url, params=params)
    # print(f"3단계 응답 상태: {response.status_code}")
    
    # # ZIP 파일 처리
    # if response.content[:2] == b'PK':
    #     try:
    #         zip_file = zipfile.ZipFile(io.BytesIO(response.content))
    #         file_list = zip_file.namelist()
    #         print(f"ZIP 파일 내용: {file_list}")
            
    #         # 첫 번째 XML 파일 읽기
    #         xml_filename = file_list[0]
    #         xml_content = zip_file.read(xml_filename).decode('utf-8')
    #         print(f"XML 파일 크기: {len(xml_content)} 문자")
            
    #     except Exception as e:
    #         print(f"ZIP 파일 처리 오류: {e}")
    #         return {"error": f"ZIP 파일 처리 오류: {e}"}
    # else:
    #     xml_content = response.text
    
    # # 4단계: XML 구조 분석 및 회사 개요 추출
    # print("4단계: XML 구조 분석...")
    
    # try:
    #     # XML parser 사용 (경고 해결)
    #     from bs4 import XMLParsedAsHTMLWarning
    #     import warnings
    #     warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)
        
    #     # XML로 파싱
    #     soup = BeautifulSoup(xml_content, 'xml')
        
    #     # DART XML 구조 분석
    #     print("DART XML 구조 분석 중...")
        
    #     # 방법 1: SECTION 태그에서 회사개요 찾기
    #     overview_text = ""
    #     sections = soup.find_all('SECTION')
        
    #     if sections:
    #         print(f"발견된 SECTION 태그 수: {len(sections)}")
            
    #         for i, section in enumerate(sections[:10]):  # 처음 10개만 확인
    #             section_title = ""
                
    #             # 섹션 제목 찾기
    #             title_tag = section.find('TITLE') or section.find('SECTION-1') or section.find('UNIT')
    #             if title_tag and title_tag.get_text():
    #                 section_title = title_tag.get_text().strip()
                    
    #             print(f"섹션 {i+1}: {section_title}")
                
    #             # 회사 개요 관련 섹션 찾기
    #             if any(keyword in section_title for keyword in ['회사의 개요', '회사개요', 'I. 회사', '1. 회사']):
    #                 print(f"회사 개요 섹션 발견: {section_title}")
                    
    #                 # 섹션 내용 추출
    #                 section_text = section.get_text(strip=True)
    #                 if len(section_text) > 200:  # 충분한 내용이 있는 경우
    #                     overview_text = section_text
    #                     break
        
    #     # 방법 2: P 태그나 TEXT 태그에서 내용 찾기
    #     if not overview_text or len(overview_text) < 200:
    #         print("P/TEXT 태그에서 내용 추출 시도...")
            
    #         # 전체 텍스트에서 회사 개요 부분 찾기
    #         full_text = soup.get_text()
            
    #         import re
            
    #         # 더 넓은 패턴으로 추출
    #         patterns = [
    #             r'회사의\s*개요[\s\S]*?(?=(?:회사의\s*연혁|자본금\s*변동|II\.|2\.)[\s\S]{0,100})',
    #             r'I\.\s*회사의\s*개요[\s\S]*?(?=(?:II\.|회사의\s*연혁)[\s\S]{0,100})',
    #             r'1\.\s*회사의\s*개요[\s\S]*?(?=(?:2\.|회사의\s*연혁)[\s\S]{0,100})',
    #         ]
            
    #         for i, pattern in enumerate(patterns):
    #             matches = re.finditer(pattern, full_text, re.IGNORECASE | re.DOTALL)
    #             for match in matches:
    #                 text = match.group(0)
    #                 if len(text) > 500:  # 충분한 길이의 텍스트만
    #                     overview_text = text
    #                     print(f"패턴 {i+1} 매칭 성공, 길이: {len(text)}")
    #                     break
    #             if overview_text:
    #                 break
        
    #     # 방법 3: 키워드 주변 텍스트 대량 추출
    #     if not overview_text or len(overview_text) < 200:
    #         print("키워드 주변 대량 텍스트 추출...")
            
    #         full_text = soup.get_text()
            
    #         # 회사 개요 시작 위치 찾기
    #         start_keywords = ['회사의 개요', '회사개요', 'I. 회사', '1. 회사']
    #         start_pos = -1
            
    #         for keyword in start_keywords:
    #             pos = full_text.find(keyword)
    #             if pos != -1:
    #                 start_pos = pos
    #                 print(f"시작 키워드 '{keyword}' 발견: 위치 {pos}")
    #                 break
            
    #         if start_pos != -1:
    #             # 시작 위치에서 5000자 추출
    #             overview_text = full_text[start_pos:start_pos + 5000]
                
    #             # 적절한 끝 위치에서 자르기
    #             end_keywords = ['회사의 연혁', '자본금 변동', 'II.', '2.', '나.']
    #             for keyword in end_keywords:
    #                 pos = overview_text.find(keyword, 500)  # 최소 500자 이후에서 찾기
    #                 if pos != -1:
    #                     overview_text = overview_text[:pos]
    #                     break
                
    #             print(f"키워드 주변 대량 추출 성공, 길이: {len(overview_text)}")
        
    #     # 텍스트 정리
    #     if overview_text:
    #         # 줄바꿈과 공백 정리
    #         lines = []
    #         for line in overview_text.splitlines():
    #             line = line.strip()
    #             if line and len(line) > 5:  # 의미있는 줄만
    #                 lines.append(line)
            
    #         overview_text = '\n'.join(lines)
            
    #         # 길이 제한
    #         if len(overview_text) > 3000:
    #             overview_text = overview_text[:3000] + "..."
        
    #     print(f"최종 추출된 텍스트 길이: {len(overview_text)}")
    #     print(f"추출된 텍스트 미리보기: {overview_text[:200]}...")
        
    #     # 결과 반환
    #     result = {
    #         'stock_code': stock_code,
    #         'corp_code': corp_code,
    #         'rcept_no': rcept_no,
    #         'overview': overview_text if overview_text else "회사 개요를 추출할 수 없습니다.",
    #         'text_length': len(overview_text) if overview_text else 0
    #     }
        
    #     return result
        
    # except Exception as e:
    #     print(f"XML 처리 오류: {e}")
        
    #     # 최후의 수단: 기업개황 API
    #     print("기업개황 API로 대체...")
    #     company_url = "https://opendart.fss.or.kr/api/company.json"
    #     params = {
    #         'crtfc_key': DART_CLIENT_ID,
    #         'corp_code': corp_code
    #     }
        
    #     response = requests.get(company_url, params=params)
    #     company_data = response.json()
        
    #     if company_data['status'] == '000':
    #         overview = f"{company_data.get('corp_name', '')}는 "
    #         overview += f"대표자 {company_data.get('ceo_nm', '')}이 운영하는 기업으로, "
    #         overview += f"{company_data.get('adres', '')}에 위치하고 있습니다."
            
    #         return {
    #             'stock_code': stock_code,
    #             'corp_code': corp_code,
    #             'company_name': company_data.get('corp_name', ''),
    #             'ceo_name': company_data.get('ceo_nm', ''),
    #             'overview': overview,
    #             'fallback': True
    #         }
    #     else:
    #         return {"error": f"모든 방법 실패: {e}"}


# {
#     "corp_code": "00164779",
#     "overview": "회사의 개요\n1. 회사의 개요\n가.  연결대상 종속회사 개황 [연결대상 종속회사 현황(요약)]\n(기준일: 2024년 12월 31일)\n(단위 : 사)\n연결대상회사수\n주요종속회사수\n※상세 현황은 '상세표-1. 연결대상 종속회사 현황(상세)' 참조\n※ 주요 종속회사 판단 기준: 직전 사업연도말 자산총액 750억원 이상 또는 지배회사 자산총액의 10% 이상\n[연결대상회사의 변동내용]\nSK hynix Semiconductor West Lafayette LLC\nSK hynix system ic Wuxi solutions Inc.\nSK hynix memory solutions Poland sp. z o.o.\nSK hynix memory solutions Eastern Europe, LLC.\nKEY FOUNDRY LTD.\nSK hynix America Investment Corporation\nSK hynix Italy S.r.l.\nSK hynix system ic (Wuxi) Co., Ltd\nSK hynix system ic Wuxi solutions Inc.\nSK hynix Semiconductor (Shanghai) Co.,Ltd.\n※ 한국채택국제회계기준에 따른 연결 기준으로 작성되었습니다.\n※ MMT 특정금전신탁은 연결에 포함된 회사수에서 제외하였습니다.\n나. 회사의 법적ㆍ상업적 명칭\n당사의 명칭은 에스케이하이닉스 주식회사이며, 영문으로는 SK hynix Inc.라고 표기합니다. 단, 약식으로 표기할 경우에는 SK하이닉스 또는 SK hynix라고 표기합니다.\n다. 설립일자당사는 1949년 10월 국도건설 주식회사로 설립되어 1983년 2월 현대전자산업주식회사로 상호를 변경하였으며, 이후 2001년 3월 주식회사 하이닉스반도체로, 2012년 3월 에스케이하이닉스 주식회사로 상호를 변경하였습니다. 회사가 발행한 주식은 한국거래소에 상장되어 유가증권시장에서 거래되고 있으며, 종목코드는 '000660'입니다.\n라. 본사의 주소, 전화번호, 홈페이지 주소주소: 경기도 이천시 경충대로 2091전화번호: 031-5185-4114홈페이지: https://www.skhynix.com\n마. 중소기업 등 해당 여부\n중소기업 해당 여부\n벤처기업 해당 여부\n중견기업 해당 여부\n바. 주요 사업의 내용\n현재 당사의 주력 생산제품은 DRAM, NAND Flash 및 MCP(Multi-chip Package)와 같은 메모리 반도체 제품입니다.\n당사 정관에 근거하여 회사가 영위하는 목적사업은 다음과 같습니다.\n-. 반도체소자 제조 및 판매\n-. 반도체소자 기타 이와 유사한 부품을 사용하여 전자운동의 특성을 응용하는 기계, 기구 및 이에 사용되는 부품과 재료 등의 제작, 조립 및 판매\n-. 컴퓨터 활용을 위한 소프트웨어 개발 및 임대업\n-. 전자 전기, 통신기계, 기구 및 그 부품의 제작, 판매, 임대 및 관련 서비스업\n-. 기계부분품 제조업 및 금형제조업\n-. 기술연구 및 용역수탁업\n-. 전자 전기기계, 기구의 임대업\n-. 특수통신(위성통신 등) 방송관련 기기 제작, 판매, 임대업 및 서비스업\n-. 정보서비스업\n-. 출판업\n-. 무역업\n-. 부동산 매매 및 임대업\n-. 발전업\n-. 건설업\n-. 전자관 제조업\n-. 창고업\n-. 주차장업\n-. 위성통신사업\n-. 전기통신회선설비 임대사업\n-. 전자상거래 및 인터넷 관련사업-. 전기 각호와 관련되는 사업 및 투자\n-. 평생교육 및 평생교육시설 운영업사업부문별 보다 자세한 사항은 Ⅱ. 사업의 내용을 참고하시기 바랍니다.\n사. 신용평가에 관한 사항\n본 보고서 제출일 현재 당사의 신용등급은 아래와 같습니다.\n한국기업평가\n2025.01.07\n한국신용평가\n2025.01.07\nNICE신용평가\n2025.01.07\nMoody's\n2024.08.14\n2024.11.19\n2024.08.30\n1. 최근 3년간 신용등급\n평가대상 유가증권 등\n평가대상 유가증권의 신용등급\n신용평가 등급범위",
#     "rcept_no": "20250319000665",
#     "stock_code": "000660",
#     "text_length": 1916
# }


if __name__ == '__main__':
    app.run(debug=True)
