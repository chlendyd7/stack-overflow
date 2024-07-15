from excel import open_excel
from naver import Naver
import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


def get_driver():
    service = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(service=service, options=options)

    return driver

def main():
    test_date_end = datetime.datetime(2024, 7, 20)
    now = datetime.datetime.now()
    if test_date_end > now:
        try:
            driver = get_driver()
            url_list, id_list = open_excel()
            naver = Naver(driver, url_list, id_list)
            naver.start()
            input("모두 완료했습니다 종료 하시려면 엔터를 누르세요")
        except Exception as e:
            print(f"오류 발생: {e}")
            input("종료 하시려면 엔터를 누르세요")  # 사용자가 엔터 키를 누를 때까지 대기
    else:
        print('테스트 기간이 경과 되었습니다. 개발자에게 문의 해주세요')

if __name__ == '__main__':
    main()
