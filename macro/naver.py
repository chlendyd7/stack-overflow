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
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import openpyxl

def find_element_safe(driver, by, value):
    try:
        element = driver.find_element(by, value)
        return element
    except NoSuchElementException:
        return None 


class Naver:

    def __init__(self, urls):
        self.urls = urls

    def start(self, id, pw):
        try:
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            driver = webdriver.Chrome(service=service, options=options)

            url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
            driver.get(url)
            # TODO 엑셀이나 db와 연동
            id = id
            password = pw

            driver.execute_script("document.getElementById('id').value = arguments[0];", id)
            driver.execute_script("document.getElementById('pw').value = arguments[0];", password)

            check_butoon = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.switch_btn')))
            check_butoon.click()
            # 로그인 버튼 클릭
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#log\.login')))
            login_button.click()

            for url in self.urls:
                if type(url) != str:
                    continue
                self.click_sympathy(driver, url)

        except Exception as e:
            print(f"로그인 실패: id:{id}, pw:{pw}")

    def click_sympathy(self, driver, url):
        # Chrome WebDriver 설정

        try:
            driver.get(url)
            # 메인 프레임으로 전환
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe#mainFrame")))

            # 스크롤 스크립트
            # for _ in range(6):
            #     driver.execute_script("window.scrollBy(0, 500);")
            #     time.sleep(1)

            css_selector = 'div[id^="area_sympathy"] > div > a'

            sympathy_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
            )
            is_like = sympathy_element.get_attribute('aria-pressed')
            if is_like == 'true':
                return print('이미 공감을 눌렀습니다')

            # 모바일 배너 내리기
            # xpath = '//*[@id="floating_bottom"]/div/div/div[1]/div/div/a/span'
            # sympathy_element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, xpath2))
            # )

            sympathy_element.click()
            time.sleep(2)
            try:
                error_check_blog_name = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#blogDomainTitle'))
                )
                if error_check_blog_name:
                    return print('공감을 남기려면 블로그 아이디가 필요해요')

            except NoSuchElementException as e:
                pass

        except Exception as e:
            print(f"오류 발생: {e}")
