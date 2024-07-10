from excel import open_excel
from naver import Naver
from tqdm import tqdm

url_list, id_list = open_excel()
print(id_list)
for id, pw in id_list:
    print(id, pw)
# for url in tqdm(url_list):
#     Naver(url).start(id_list)
# print('모든 작업이 끝났습니다')
# input()
