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
from selenium.webdriver.chrome.service import Service
import openpyxl


class Naver:

    def __init__(self, url):
        self.url = url

    def start(self, id_list):
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

            check_butoon = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.switch_btn')))
            check_butoon.click()
            # 로그인 버튼 클릭
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#log\.login')))
            login_button.click()

            after_login_url = "https://blog.naver.com/eojining/223433776731"

            self.click_sympathy(driver, after_login_url)

        except Exception as e:
            print(f"로그인 실패: {e}")

    def click_sympathy(self, driver, url):
        # Chrome WebDriver 설정

        try:
            driver.get(url)
            # 메인 프레임으로 전환
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe#mainFrame")))

            for _ in range(6):
                driver.execute_script("window.scrollBy(0, 500);")
                time.sleep(1)

            xpath = '//*[@id="floating_bottom"]/div/div/div[1]/div/div/a/span'
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            element.click()
            time.sleep(2)

        except Exception as e:
            print(f"오류 발생: {e}")

        finally:
            # 브라우저 종료
            driver.quit()
