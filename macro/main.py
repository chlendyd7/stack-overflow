from excel import open_excel
from naver import Naver
from tqdm import tqdm

def main():
    try:
        url_list, id_list = open_excel()
        for id, pw in tqdm(id_list, desc="Processing"):
            print()
            print(f'{id} working')
            if id == None:
                continue
            Naver(url_list).start(id, pw)
            input("종료 하시려면 엔터를 누르세요")
    except Exception as e:
        print(f"오류 발생: {e}")
        input("종료 하시려면 엔터를 누르세요")  # 사용자가 엔터 키를 누를 때까지 대기

if __name__ == '__main__':
    main()
