#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import time
import pandas as pd
import math
import pickle


# load
with open('./lifestylegroup4-3.pickle', 'rb') as f:
    lifestylegroup = pickle.load(f)
f.close()

lifestylegroup.rename(columns = {'store' : 'store_id'}, inplace = True)
lifestylegroup["image"] = None

print(lifestylegroup.head())
# print(lifestylegroup.index)

<<<<<<< Updated upstream
# driver = webdriver.Chrome('./chromedriver')
# options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
# options.add_argument('headless') # headless 모드 설정
# options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
# options.add_argument("disable-gpu") 
# options.add_argument("disable-infobars")
# options.add_argument("--disable-extensions")
# options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('./chromedriver')
# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
# driver.implicitly_wait(3)
=======

options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_argument('headless') # headless 모드 설정
options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
options.add_argument("disable-gpu") 
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome('./chromedriver', options=options)
# 암묵적으로 웹 자원 로드를 위해 3초까지 기다려 준다.
driver.implicitly_wait(3)
>>>>>>> Stashed changes

# search_url = 'https://www.diningcode.com/isearch.php?query='
# search_word = ''

# data = []

# # image가 안들어간 데이터 id 모음
# non_image = []
# error_data = []

# print(lifestylegroup)
# print(type(lifestylegroup))

# # f.close()

csvfile = open('./img3.csv', "w", newline="")
csvwriter = csv.writer(csvfile)

for i in lifestylegroup.index:
    # if i+1 == 13698:
    #     break

    try:
        print(i)
        search_word = lifestylegroup['store_name'][i]
        put_url = search_url + search_word
        print(put_url)

        # search_word = lifestylegroup[i, 'store_name']
        # driver.get(search_url+search_word)

        driver.get(put_url)
        
        try:
            print("=========2======")
            driver.find_element_by_id("btn_rn_list").click()
        except:
            print("except2")
            lifestylegroup['image'][i] = 'https://s3-ap-northeast-1.amazonaws.com/dcicons/new/images/web/noimage/1.jpg'
            non_image.append(i)


            csvwriter.writerow([i, lifestylegroup['image'][i]])

            time.sleep(3)
            continue
        
        # time.sleep(3)
        # 총 list 개수
        print("=========3======")

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        full_list_num = soup.find(id="lbl_count").get_text()
        pointer = full_list_num.find('곳')
        full_list_num = full_list_num[:pointer]

        # 총 list가 출력되었는지 판정
        print("=========4======")

        group_now = soup.find_all("span", class_="btxt")
        last = group_now[-1].get_text()
        p = last.find('.')
        last = last[:p]
        
        # while int(last) < int(full_list_num):
        #     time.sleep(1)
        #     try:
        #         driver.find_element_by_id("div_list_more").click()
        #         soup = BeautifulSoup(html, 'html.parser')
        #         group_now = soup.find_all("span", class_="btxt")
        #         last = group_now[-1].get_text()
        #         p = last.find('.')
        #         last = last[:p]
        #     except:
        #         break
        print("=========5======")

        soup = BeautifulSoup(html, 'html.parser')
        # 주소 추출

        group_loca = soup.find_all("span", class_="ctxt")
        
        idx = -1
        str_len = len(lifestylegroup['address'][i]) * (-1)

        for j in range(1, len(group_loca), 2):

            address = group_loca[j].get_text()
            address = address[str_len:]
            print("adress", address)
            print("match", lifestylegroup['address'][i])
            if address == lifestylegroup['address'][i]:
                idx = j
                break
        

        if idx == -1:
            lifestylegroup['image'][i] = 'https://s3-ap-northeast-1.amazonaws.com/dcicons/new/images/web/noimage/1.jpg'
            print(lifestylegroup['image'][i])
            csvwriter.writerow([i, lifestylegroup['image'][i]])
            non_image.append(i)
            time.sleep(3)
            continue

        idx = idx//2 + 1
        new_soup = soup.find_all("li", onmouseenter="setIcon(" + str(idx) + ");")
        url = new_soup[0].span['style']
        p_f = url.find('(')
        p_l = url.find(')')
        url = url[p_f+2:p_l-1]
        print("=========8======")

        lifestylegroup['image'][i] = url
        # print("저장하고자 하는 데이터")
        print("저장되었는지 확인")
        print(lifestylegroup['image'][i])

        # print("저장하고자 하는 row")
        # print(lifestylegroup[i])
        csvwriter.writerow([i, lifestylegroup['image'][i]])
    
        time.sleep(3)


    except:
        print("except1")
        lifestylegroup['image'][i] = 'https://s3-ap-northeast-1.amazonaws.com/dcicons/new/images/web/noimage/1.jpg'
        error_data.append(i)

        csvwriter.writerow([i, lifestylegroup['image'][i]])

        time.sleep(3)
        continue

csvfile.close()

# 에러가 발생한 상점들의 id
# txtfile = open('./error_data.txt', "w")
# txtfile.write(non_image)
# txtfile.write(error_data)
# txtfile.close()

# # 결과 데이터 저장
# csvfile = open('./store_img1.csv', "w", newline="")

# # csvwriter = csv.writer(csvfile)
# # for row in data:

# #     csvwriter.writerow(row)

# # csvfile.close()

# pickle파일로 저장 # lifestylegroup4 는 중복 제거함
#%%
# print("크롤링끝")
# #%%
# print(lifestylegroup.head())
# #%%
# with open('./data/image5.pickle', 'wb') as f:
#     pickle.dump(lifestylegroup, f, pickle.HIGHEST_PROTOCOL)

# # load
# with open('./data/image5.pickle', 'rb') as f:
#     lifestylegroup = pickle.load(f)
