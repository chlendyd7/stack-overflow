from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm

def find_css_element_safe(driver, value):
    try:
        element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        return element
    except NoSuchElementException:
        return None


class Naver:

    def __init__(self, driver, urls, ids):
        self.driver = driver
        self.urls = urls
        self.ids = ids

    def start(self):
        for id, pw in tqdm(self.ids, desc="Processing"):
            if id == None:
                continue
            print(f'{id} processing')
            self.naver_login(self.driver, id, pw)
            for url in self.urls:
                if type(url) != str:
                    continue
                self.click_sympathy(self.driver, url)

    def naver_login(self, driver, id, pw):
        try:
            url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/'
            driver.get(url)
            driver.execute_script("document.getElementById('id').value = arguments[0];", id)
            driver.execute_script("document.getElementById('pw').value = arguments[0];", pw)

            check_button = find_css_element_safe(driver, '.switch_btn')
            check_button.click()
            login_button = find_css_element_safe(driver, '#log\.login')
            if login_button:
                login_button.click()
            time.sleep(2)
            # 로그인 성공 로직 넣기

        except Exception as e:
            print(f"로그인 실패: id:{id}, pw:{pw}")

    def click_sympathy(self, driver, url):
        try:
            print(f'{url} processing')
            driver.get(url)
            WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
                (By.CSS_SELECTOR, "iframe#mainFrame")))

            # 스크롤 스크립트
            # for _ in range(6):
            #     driver.execute_script("window.scrollBy(0, 500);")
            #     time.sleep(1)

            css_selector = 'div[id^="area_sympathy"] > div > a'

            sympathy_element = find_css_element_safe(driver, css_selector)
            is_like = sympathy_element.get_attribute('aria-pressed')
            if is_like == 'true':
                return print('이미 공감을 눌렀습니다')

            # 모바일 배너 내리기
            # xpath = '//*[@id="floating_bottom"]/div/div/div[1]/div/div/a/span'
            # sympathy_element = WebDriverWait(driver, 10).until(
            #     EC.presence_of_element_located((By.XPATH, xpath2))
            # )

            sympathy_element.click()
            error_check_blog_name = find_css_element_safe(driver, '#blogDomainTitle')
            time.sleep(2)
            if error_check_blog_name:
                return print('공감을 남기려면 블로그 아이디가 필요해요')
            else:
                return print(f'공감 버튼을 성공적으로 눌렀습니다 링크:{url}')
        except Exception as e:
            print(f"오류 발생: {e}")
