from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ChromeDriver 경로 설정
chromedriver_path = 'C:\Program Files\Google\Chrome\Application\chrome_proxy.exe'
chromedriver_path = "C:\Program Files\Google\Chrome\Application\chrome_proxy.exe"
# --profile-directory=Default --app-id=aoeeckacjnficgikkpbofpdcjoohpkld"
service = Service(chromedriver_path)
print('work1')
service = Service(chromedriver_path, log_path='chromedriver.log')
# ChromeDriver 옵션 설정
options = webdriver.ChromeOptions()
print('work2')
options.add_argument('--start-maximized')  # 브라우저 최대화 옵션

# ChromeDriver 생성
driver = webdriver.Chrome(service=service, options=options)
print('work3')
try:
    print('work1')
    driver.implicitly_wait(10)
    print('work2')
    # 웹사이트 열기
    driver.get('https://www.google.com')
    print('work3')
    # 검색 창이 로드될 때까지 대기
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, 'q'))
    )
    print('work4')
    # 검색 창에 키워드 입력하고 검색
    search_box.send_keys('Selenium')
    search_box.send_keys(Keys.RETURN)

    # 검색 결과가 로드될 때까지 대기
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'search'))
    )

    # 검색 결과 출력
    print(driver.title)
finally:
    # 브라우저 닫기
    driver.quit()
