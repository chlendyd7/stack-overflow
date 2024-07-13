from excel import open_excel
from naver import Naver
from tqdm import tqdm

def main():
    try:
        url_list, id_list = open_excel()
        for id, pw in tqdm(id_list, desc="Processing ID List"):
            Naver(url_list).start(id,pw)
    except Exception as e:
        return print(e)

main()
