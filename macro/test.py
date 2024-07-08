import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 크롬 드라이버 생성
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Google 웹사이트에 접속
driver.get("https://www.tistory.com/auth/login")
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn_login')))
login_button = driver.find_element(By.CLASS_NAME, 'btn_login')
login_button.click()
# driver.find_element(By.CLASS_NAME, 'btn_login').click()
# 검색 입력창 찾기 (검색창의 이름이 'q')
username = 'chlendyd8@daum.net'
password = 'd4632077zZ@'
login_id_element  = driver.find_element(By.ID, 'loginId--1')
login_id_element .send_keys(username)
print(login_id_element)
driver.find_element(By.ID, 'password--2').send_keys(password)
driver.find_element(By.CLASS_NAME, 'submit').click()


# link_profile = driver.find_element(By.CSS_SELECTOR, 'a.link_profile')
# link_profile.click()
wait = WebDriverWait(driver, 10)
WebDriverWait(driver, 1000)

    # '쓰기' 링크 클릭
profile_info = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'thumb_profile')))
print(profile_info)
# 이 요소 내부에서 '쓰기' 링크 찾기
thumb_profile = driver.find_element(By.CLASS_NAME, 'thumb_profile')
thumb_profile.click()
WebDriverWait(driver, 10)
link = driver.find_element(By.CSS_SELECTOR, 'a.img_common_tistory.link_edit')
link.click()
# '쓰기' 링크 클릭
print("쓰기 링크를 클릭했습니다.")


WebDriverWait(driver, 100)

# search_box = driver.find_element(By.ID, 'loginId--1').send_keys(username)

# # 검색어 입력
# search_box.send_keys('Jennie')

# # 검색 실행
# search_box.submit()
# time.sleep(5)

# # 결과 페이지 스크린샷 저장
# driver.save_screenshot('search_results.png')

# # 브라우저 종료
# driver.quit()