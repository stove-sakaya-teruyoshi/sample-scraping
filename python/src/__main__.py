import my_reg
import my_fetch
import csv

def main():
    categories = ['イラスト・漫画']
    urls = ['https://coconala.com/categories/9']
    sort_bys = [
        ['recommend', 'おすすめ順'],
        ['ranking', 'ランキング順']
    ]
    datas = [['並び順', 'カテゴリ', 'タイトル', '値段', 'リンク']]

    for category, url in zip(categories, urls):
        for sort_by in sort_bys:
            content = my_fetch.my_fetch(url, sort_by[0])
            datas += my_reg.my_reg(content, sort_by[1], category)

    # テスト用ファイルからデータを取得
    # content = get_content()
    # datas = my_reg.my_reg(content, sort_bys[0][1], categories[0], 10)

    with open('coconala-scraping.csv', 'w') as csvfile:
        csvWriter = csv.writer(csvfile)
        for data in datas:
            csvWriter.writerow(data)

def get_content():
    with open('coconala-scraping.txt', 'r', encoding='utf-8') as file:
        return file.read()
    if content != None:
        return ""

if __name__ == "__main__":
    main()