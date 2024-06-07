import requests
import re

def main():
    my_reg()

def my_reg():
    with open('coconala-scraping.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        items = get_item(content)
        
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

def get_item(content):
    pattern_item = "(<div class=\"c-searchPageItemBlock\".+?)<div class=\"c-searchPageItemBlock\""
    item = re.findall(pattern_item, content, re.MULTILINE | re.DOTALL)
    return item

def get_title(content):
    pattern_title = "<h3 class=\"c-serviceBlockItemContent_name\"[^>]*>([^<]+)<"
    title = re.findall(pattern_title, content, re.MULTILINE | re.DOTALL)
    return title[0]

def get_price(content):
    pattern_price = "<strong[^>]*>([\d|,]+)</strong>\s*(円)"
    price = re.findall(pattern_price, content, re.MULTILINE | re.DOTALL)
    return price[0][0] + price[0][1]

def my_fetch():
    url = "https://coconala.com/categories/9"
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
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

if __name__ == "__main__":
    main()