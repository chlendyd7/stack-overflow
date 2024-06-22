from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def auto_create_blog():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 브라우저를 열지 않고 실행
    service = Service('C:\Program Files\Google\Chrome\Application\chrome.exe')  # ChromeDriver 경로 설정
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')  # 브라우저 최대화 옵션

    # 크롬 드라이버 생성
    driver = webdriver.Chrome(service=service, options=options)

    # 웹사이트 열기
    driver.get('https://www.google.com')

    # 검색 창에 키워드 입력하고 검색
    search_box = driver.find_element(By.NAME, 'q')
    search_box.send_keys('Selenium')
    search_box.send_keys(Keys.RETURN)

    # 검색 결과 출력
    print(driver.title)

    # 브라우저 닫기
    driver.quit()

auto_create_blog()