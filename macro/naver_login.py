from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

# Chrome WebDriver 설정


def login_naver():
    try:
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)

        url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
        driver.get(url)

        # TODO 엑셀이나 db와 연동
        id = 'chlendyd7'
        password = 'd4632077zZ@'

        driver.execute_script("document.getElementById('id').value = arguments[0];", id)
        driver.execute_script("document.getElementById('pw').value = arguments[0];", password)

        check_butoon =  WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.switch_btn')))
        check_butoon.click()
        # 로그인 버튼 클릭
        login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#log\.login')))
        login_button.click()

        after_login_url = "https://blog.naver.com/meso88/223438959888"

        login_and_click_sympathy(driver, after_login_url)

    except Exception as e:
        print(f"로그인 실패: {e}")

    finally:
        # 브라우저 닫기
        driver.quit()

def login_and_click_sympathy(driver, after_login_url):
    # Chrome WebDriver 설정

    try:
        driver.get(after_login_url)
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#mainFrame")))

        for _ in range(6):  # 여기서는 6번 스크롤 다운 예시를 사용했습니다.
            driver.execute_script("window.scrollBy(0, 500);")

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
        driver.quit()


login_naver()
