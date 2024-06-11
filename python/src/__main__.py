import requests
import re

def main():
    url = "https://coconala.com/categories/9"
    content = my_fetch(url)

    # content = ""
    # with open('coconala-scraping.txt', 'r', encoding='utf-8') as file:
    #     content = file.read()
    # if content != None:
    #     return
    
    my_reg(content)

def my_reg(content):
    items = get_items(content)
    
    result_str = ""
    count = 0

    for item in items:
        title = get_title(item)
        price = get_price(item)
        item_status = title + " : " + price
        if count < 10:
            result_str += item_status + "\n"
        count += 1

    with open("coconala-scraping-div.txt", "w") as f:
        f.write(result_str)

def get_items(content):
    pattern_item = r"(<div class=\"c-searchPageItemBlock\".+?)<div class=\"c-searchPageItemBlock\""
    items = re.findall(pattern_item, content, re.MULTILINE | re.DOTALL)
    return items

def get_title(content):
    pattern_title = r"<h3 class=\"c-serviceBlockItemContent_name\"[^>]*>([^<]+)<"
    title = re.findall(pattern_title, content, re.MULTILINE | re.DOTALL)
    return title[0]

def get_price(content):
    pattern_price = r"<strong[^>]*>([\d|,]+)</strong>\s*(円)"
    price = re.findall(pattern_price, content, re.MULTILINE | re.DOTALL)
    return price[0][0] + price[0][1]

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

if __name__ == "__main__":
    main()