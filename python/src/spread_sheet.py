import google.auth
from googleapiclient.discovery import build

def get_sheet_service():
    json = "sample-scraping.json"
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    credentials, _ = google.auth.load_credentials_from_file(json, scopes=scopes)
    service = build('sheets', 'v4', credentials=credentials)

    return service

def write_csv(values):
    value_input_option = "USER_ENTERED"
    key = "1XtW0PVmnCY0v-TQh6jkmrqI8qdycQsHTBShbqEwdwvk"
    print('スプレッドシートに記載中')
    range_name = "A1:E" + str(len(values))
    try :
        service = get_sheet_service()
        data = [
            {"range": range_name, "values": values}
        ]
        body = {"valueInputOption": value_input_option, "data": data}
        result = (
            service.spreadsheets()
            .values()
            .batchUpdate(spreadsheetId=key, body=body)
            .execute()
        )
        print('記載処理が完了しました。')
        return result
    except HttpError as error:
        print(f"An error occurred: {error}")
        return error