import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_sheet():
    json = "sample-scraping.json"
    key = "1XtW0PVmnCY0v-TQh6jkmrqI8qdycQsHTBShbqEwdwvk"
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(json, scope)
    gc = gspread.authorize(credentials)
    SPREADSHEET_KEY = key
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    return worksheet

def write_csv(datas):
    print('スプレッドシートに記載中')
    range_name = "A1:E" + str(len(datas))
    sheet = get_sheet()
    rg = sheet.range(range_name)
    for i in range(len(datas)):
        for j in range(len(datas[i])):
            rg[i * len(datas[i]) + j].value = datas[i][j]
    
    sheet.update_cells(rg)
    print('記載処理が完了しました。')