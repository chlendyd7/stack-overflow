from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import re

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
def start_naver():
# WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_blog_login')))
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    url = 'https://blog.naver.com/meso88/223438959888?isInf=true&infParams=eyJzY2lkIjoxMzU5Njg3NjAxNTU5NjgsInNraWQiOjE4NDA1NDE1ODkyNjA0OCwiY2lkIjo2OTEyNDQ0MDMwMjYzNjgsInF1ZXJ5IjoiJUVBJUIwJTg0JUVDJTlFJUE1JUVBJUIyJThDJUVDJTlFJUE1In0=&trackingCode=nx'
    driver.get(url)
    try:
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#mainFrame")))

        # 로그인 버튼 클릭
        login_button_selector = "#gnb-area > ul > li.i1.login > a"
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_button_selector))).click()

        # login_button_selector = "#gnb-area > ul > a"
        # xpath = "/html/body/div[7]/div[1]/div[1]/div/ul/a"
        # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath))).click()
        # print("요소 클릭 성공")
        id = 'chlendyd7'
        password = 'd4632077zZ@'
        # id_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "id")))
        id_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#id')))
        print(id_field)
        # pw_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#pw")))
        id_field.send_keys(id)
        # pw_field.send_keys(password)
        #input_item_id
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#log\\.login")))
        login_button.click()
        print("로그인 버튼 클릭 성공")

        login_and_click_sympathy(driver, after_login_url='https://blog.naver.com/meso88/223438959888')
    except Exception as e:
        print(f"버튼 클릭 실패: {e}")


def login_and_click_sympathy(driver, after_login_url):
    # Chrome WebDriver 설정

    try:
        # 블로그 페이지로 이동
        driver.get(after_login_url)

        # 메인 프레임으로 전환
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#mainFrame")))

        # 페이지 스크롤 다운
        for _ in range(6):  # 여기서는 6번 스크롤 다운 예시를 사용했습니다.
            driver.execute_script("window.scrollBy(0, 500);")

        # 공감 버튼 찾기
        like_list = driver.find_elements(By.CSS_SELECTOR, 'a.u_likeit_list_btn._button.off')

        # 공감 버튼 중 조건에 맞는 것 클릭
        for like in like_list:
            like_cnt = re.findall("\d+", like.text)
            if like_cnt and int(like_cnt[0]) < 2:
                continue
            else:
                like.click()
                print('공감 버튼 클릭 완료')
                break

    except Exception as e:
        print(f"오류 발생: {e}")

    finally:
        # 브라우저 종료
        driver.quit()

start_naver()