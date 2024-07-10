from tqdm import tqdm
import time
import openpyxl


def open_excel():
    wb = openpyxl.load_workbook('macro/naver.xlsx')
    url_sheet = wb.active
    url_list = []
    urls = url_sheet[1]
    for cell in urls:
        url_list.append(cell.value)

    id_sheet = wb['id_pw']
    id_list = []
    for row in id_sheet.iter_rows(values_only=True):
        id_list.append(row)

    return url_list, id_list


def tqdm_work():
    total_iterations = 100

    # tqdm을 사용하여 진행 상황 표시
    for i in tqdm(range(total_iterations)):
        # 각 작업의 내용
        time.sleep(0.1)  # 예시로 작업 시간을 0.1초로 가정
    print("모든 작업이 완료되었습니다.")


# 작업 완료 메시지 출력
# print(tqdm_work())
# print(open_excel())
