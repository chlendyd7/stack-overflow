import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Chrome WebDriver 설정
service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    after_login_url = "https://blog.naver.com/meso88/223438959888"
    driver.get(after_login_url)

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe#mainFrame")))
    # 공감 버튼 요소를 찾기
    # element = driver.find_element(By.CSS_SELECTOR, "div.u_likeit_list_module")
    # driver.execute_script("arguments[0].scrollIntoView();", element)
    # element.click()


    # # 공감 버튼 찾아서 클릭
    # sympathy_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span.u_likeit_text._count.num")))

    # 스크롤 다운
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # confirmlike = driver.find_element(By.XPATH, "//*[@id='body']/div[10]/div/div[1]/div/div/a").get_attribute("class").split(" ")
    driver.execute_script("window.scrollBy(0, 500);")
    driver.execute_script("window.scrollBy(0, 500);")
    driver.execute_script("window.scrollBy(0, 500);")
    driver.execute_script("window.scrollBy(0, 500);")
    driver.execute_script("window.scrollBy(0, 500);")
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(10)
    like_list = driver.find_elements(By.CLASS_NAME, 'u_likeit_list_btn._button.off')
    import re
    for like in like_list:
        like_cnt = re.findall("\d+",like.text)
        if like_cnt and int(like_cnt[0]) < 2:
            continue
        else:
            like.click()
            break
    # like_btn = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, '//*[@id="your_element_id"]'))
    # )
    # print(like_btn)

    # driver.execute_script("arguments[0].scrollIntoView({block : 'center'});", like_btn)
    # like_btn.click()
    print('공감 버튼 클릭 완료')
    input()


except Exception as e:
    print(f"로그인 실패: {e}")

finally:
    # 브라우저 닫기
    driver.quit()
