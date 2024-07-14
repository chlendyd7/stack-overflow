import openpyxl
import os

def open_excel():
    BASE_DIR = os.getcwd()
    try:
        file_path = os.path.join(BASE_DIR, 'naver.xlsx')
    except:
        raise Exception('현재 폴더에 naver.xlsx이 존재하지 않습니다')

    wb = openpyxl.load_workbook(file_path)
    assert 'id_pw' in wb.sheetnames, 'id_pw 시트가 존재하지 않습니다'
    assert 'urls' in wb.sheetnames, 'urls 시트가 존재하지 않습니다'
    url_sheet = wb['urls']
    url_list = []
    urls = url_sheet.iter_rows(min_row=1, max_row=url_sheet.max_row, min_col=1, max_col=1)
    for row in urls:
        for cell in row:
            url_list.append(cell.value)

    id_sheet = wb['id_pw']
    id_list = []
    for row in id_sheet.iter_rows(values_only=True):
        id_list.append(row)

    return url_list, id_list
