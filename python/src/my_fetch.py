import requests

def my_fetch(url):
    user_agent = "SampleScraping/0.1.0"
    headers = {
        "User-Agent": user_agent
    }
    params = {
        "sort_by": "recommend"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        textRes = response.text
        with open("coconala-scraping.txt", "w") as f:
            f.write(textRes)
        return textRes
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None