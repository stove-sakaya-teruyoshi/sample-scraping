import requests
import time

def my_fetch(url, sort_by="recommend"):
    user_agent = "SampleScraping/0.1.0"
    headers = {
        "User-Agent": user_agent
    }
    params = {
        "sort_by": sort_by
    }

    response = requests.get(url, headers=headers, params=params, timeout=(3.0, 7.5))
    print(url + 'を' + sort_by + '順で取得中')
    time.sleep(1)
    if response.status_code == 200:
        print(url + 'を' + sort_by + '順で取得しました。')
        textRes = response.text
        with open("coconala-scraping.txt", "w") as f:
            f.write(textRes)
        return textRes
    else:
        print('失敗しました。')
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None