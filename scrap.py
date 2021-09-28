from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
import time
import os
import re
import csv

def d_dir():
    "사용자에게 저장 할 경로를 입력받는 함수"
    try:
        d = input('저장 할 경로를 선택하세요. (특수문자 제외, 종료 = "q")\n예 : C:\\Users\\wnlk\\ \n>>> ')
        # 폴더 명으로 사용할 수 없는 문자 제거
        if d == 'q' or d == 'Q':
            print('프로그램을 종료합니다.')
            browser.close()
            return
        else:
            d = re.sub("[*?\"<>| ]", "", d)
            if not os.path.isdir(d):
                os.mkdir(d)
            return d          
    except FileNotFoundError:
        # 경로에 대한 예외처리
        print('경로가 올바르지 않습니다. 다시 입력 해 주세요.')
        return d_dir()

def search_input():
    "사용자에게 검색어를 입력받고 카테고리를 출력, 저장하는 함수"
    q = input('검색어를 입력 해 주세요. (특수문자 제외, 종료 = "q")\n>>> ')
    # 검색어 > 파일명으로 사용할 수 없는 문자 제거
    if q == 'q' or q == 'Q':
        print('프로그램을 종료합니다.')
        browser.close()
        return   
    else:
        q = re.sub("[\/:*?\"<>| ]", "", q)
    # 검색어가 없을 경우 예외처리
    if q:
        # 검색어에 대한 안내
        print(f'"{q}"을(를) 검색합니다.')
    else:
        print('검색어를 입력하지 않았습니다.')
        return search_input()
        
    # 검색창에 검색어 입력, 엔터
    bar = browser.find_element_by_id('twotabsearchtextbox')
    bar.send_keys(q)
    bar.send_keys(Keys.ENTER)
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # 결과 페이지의 소스 중 카테고리에 해당하는 부분 리스트화
    category_list = soup.find('div', {'id':'departments'})
    categorys = category_list.find_all('li')
    cnt = 1
    cate_choice = [0]
    print(divison)
    for category in categorys:
        cate = category.find('span').text.strip()
        # 하위요소가 포함된 마지막 리스트의 예외처리
        if '\n' in cate:
            continue
        # 인덱스와 카테고리명 출력
        print(cnt, ':', cate)
        cate_choice.append((cnt, cate))
        cnt += 1
    print(divison)
    # 튜플(검색어, 리스트) 형태로 반환
    return (q, cate_choice)

def search_output(ctg):
    "사용자에게 검색 할 카테고리와 수량을 입력받아 해당 데이터를 출력하는 함수"
    ctg_inp = input('검색 할 카테고리에 해당하는 번호를 입력 해 주세요. (종료 = "q") \n>>> ')
    if ctg_inp == 'q' or ctg_inp == 'Q':   
        print('프로그램을 종료합니다.')
        browser.close()
        return
    else:
        try:
            # 사용자가 입력한 번호에 대한 예외처리
            ctg_index = int(ctg_inp.strip())
            if ctg_index < 0 or ctg_index >= len(ctg):
                ('없는 카테고리 번호입니다. 다시 입력 해 주세요.')
                return search_output(ctg)
        except AttributeError or ValueError:
            print('숫자가 아닙니다. 숫자를 입력 해 주세요.')
            return search_output(ctg)
        
    print(f'입력하신 번호의 카테고리는 "{ctg[ctg_index][1]}"입니다.')
    while True:
        search_num = input('저장 할 검색 결과의 갯수를 입력 해 주세요. \n>>> ')
        # 숫자가 아닐 경우에 대한 예외처리
        try:
            num = int(search_num)
            print(f'{num}개의 검색 결과 저장을 시도합니다.')
            break
        except AttributeError:
            print('숫자가 아닙니다. 숫자를 입력 해 주세요.')
            continue
    # 카테고리를 확장하고 해당하는 카테고리를 클릭
    browser.find_element_by_class_name('a-expander-prompt').click()
    time.sleep(1)
    browser.find_element_by_link_text(f'{ctg[ctg_index][1]}').click()
    time.sleep(3)
    results = browser.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]').text
    result = re.sub(r"[^0-9]", "", results[7:])
    while int(result) < num:
        gostop = input(f'검색 결과가 {result}개 입니다. 계속 진행 하시겠습니까? (Y/N) \n>>> ')
        if gostop not in yn:
            print('"Y" 또는 "N"만 입력이 가능합니다.')
            continue
        else:
            if gostop == 'y' or gostop == 'Y':
                num = result
                break
            else:
                print('검색어 입력으로 돌아갑니다.')
                browser.get(url)
                return search_input()
    data_index = 0
    data = []
    # 사용자가 입력한 결과 갯수를 넘을 때 까지
    while data_index < num:
        # 끝까지 내리기
        prev_height = browser.execute_script("return document.body.scrollHeight")
        while True:
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(2)
            curr_height = browser.execute_script("return document.body.scrollHeight")
            # 더이상 내려가지 않을 때 까지 반복
            if curr_height == prev_height:
                break
            prev_height = curr_height
        # html 가져오기
        html = browser.page_source
        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.find_all('div', {'class':'s-result-item'})
        # 요소 추출, 리스트에 저장
        for card in cards:
            if card.find('img', {'class':'s-image'}):
                image_url = card.find('img', {'class':'s-image'})['src']
            else:
                image_url = 'n/a'
            if card.find('h2'):
                title = card.find('h2').text
            else:
                title = 'n/a'
            if card.find('span', {'class':'a-offscreen'}):
                price = card.find('span', {'class':'a-offscreen'}).text
            else:
                price = 'n/a'
            if card.find('span', {'class':'a-icon-alt'}):
                grade = card.find('span', {'class':'a-icon-alt'}).text
            else:
                grade = 'n/a'
            if (data_index, image_url, title, price, grade).count('n/a') > 2:
                continue
            else:
                data.append((data_index, data_index+1, image_url, title, price, grade))
            data_index += 1
            print(divison)
            print("번호 :", data_index, "\n이미지 :", image_url, "\n제목 :", title.strip(), "\n가격 :", price, "\n평점 :", grade)
        # 다음 페이지로 갈 수 없다면 종료
        if browser.find_element_by_class_name('a-last'):
            browser.find_element_by_class_name('a-last').click()
        else:
            print(divison)
            print(f'더이상 검색 결과가 없습니다. 총 {data_index-1}개가 검색 되었습니다.')
            break
        time.sleep(2)
    # 검색 갯수만큼 반환
    return data[:num]

def save_data(l):
    "저장된 데이터를 사용자가 원하는 파일 형식으로 저장하는 함수"
    print('다음 중 저장 할 파일 타입의 번호를 콤마(,)로 구분하여 모두 입력하세요. (입력 순서대로 실행)')
    saves = list(map(str, input('1 : txt / 2 : csv / 3 : image파일 / 4 : 저장하지 않음 >>> ').split(',')))
    # 사용자가 입력한 번호의 타입에 맞게 저장
    for i in saves:
        try:
            if int(i) in (1, 2, 3):
                if int(i) == 1:
                    with open(download_dir+f"/amazon_{query}.txt", 'w', encoding='utf-8') as file:
                        for j in l:
                            file.write(f'인덱스 : {j[0]}\n')
                            file.write(f'번호 : {j[1]}\n')
                            file.write(f'제목 : {j[3]}\n')
                            file.write(f'가격 : {j[4]}\n')
                            file.write(f'평점 : {j[5]}\n')
                            file.write(f'{divison}\n')
                    continue
                if int(i) == 2:
                    with open(download_dir+f"/amazon_{query}.csv", 'w', encoding='utf-8') as file:
                        wr = csv.writer(file)
                        wr.writerow(['인덱스', '번호', '제목', '가격', '평점'])
                        for j in l:
                            wr.writerow(j[:2] + j[3:])
                    continue
                if int(i) == 3:
                    for j in l:
                        k = j[1]
                        src = j[2]
                        if src == 'n/a':
                            continue
                        urllib.request.urlretrieve(src, f"{download_dir}/amazon_{query}{k}.jpg")
                    continue
            else:
                break
        # 숫자가 아닌 경우 예외처리
        except AttributeError or ValueError:
            print('해당하는 번호를 입력하세요.')
            return save_data(l)
    
    print('작업을 완료했습니다.')
    print(divison)
    browser.get(url)
    return search_input()

# 아마존 상품 검색(카테고리별), 저장용 스크래퍼
version = 'ver1.1'
divison = '=' * 60
yn = ('y', 'Y', 'n', 'N')
print(divison)
print(f'Amazon Downloader by woodnlowkey({version})')
print(divison)
# 웹드라이버 경로
path = 'C:/python_temp/chromedriver_win32/chromedriver.exe'
browser = webdriver.Chrome(path)
# 최대화
browser.maximize_window()
# url 이동
url = "https://www.amazon.com/"
browser.get(url)

download_dir = d_dir()
if download_dir:
    query, ctg_list = search_input()
if query:
    data_list = search_output(ctg_list)
if data_list:
    save_data(data_list)
