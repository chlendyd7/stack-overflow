from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import re

# Chrome WebDriver 설정
def start_naver():
    try:
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        # 네이버 로그인 페이지로 이동
        url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
        driver.get(url)

        # 아이디 입력
        id = 'chlendyd7'
        password = 'd4632077zZ@'

        # id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#id')))
        # id_input.send_keys(id)  # 여기에 네이버 아이디 입력

        # # 비밀번호 입력
        # pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#pw')))
        # pw_input.send_keys(password)  # 여기에 네이버 비밀번호 입력

        id_value = "your_naver_id"  # 여기에 네이버 아이디 입력
        driver.execute_script("document.getElementById('id').value = arguments[0];", id)

        # 비밀번호 입력
        pw_value = "your_password"  # 여기에 네이버 비밀번호 입력
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