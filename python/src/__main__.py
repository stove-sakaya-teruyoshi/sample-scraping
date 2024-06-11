import my_reg
import my_reg2
import my_fetch
import csv

def main():
    url = 'https://coconala.com/categories/'
    categories = [
        ['9', 'イラスト・漫画'],
        ['18', 'デザイン'],
        ['22', 'Webサイト制作・Webデザイン'],
        ['10', '動画制作・アニメーション制作・撮影'],
        ['13', 'ビジネス代行・アシスタント'],
        ['23', '音楽・ナレーション'],
        ['1001', 'ハンドメイド・グッズ']
    ]
    categories2 = [
        ['16', 'マーケティング・Web集客'],
        ['11', 'IT・プログラミング・開発'],
        ['19', 'ライティング・翻訳'],
        ['27', 'コンサルティング・士業'],
        ['28', 'AI'],
        ['3', '占い'],
        ['2', '悩み相談・恋愛相談（恋愛カウンセリング）・話し相手'],
        ['12', '学習・就職・資格・コーチング'],
        ['5', '住まい・美容・生活・趣味'],
        ['26', 'オンラインレッスン・アドバイス']
    ]
    sort_bys = [
        ['recommend', 'おすすめ順'],
        ['ranking', 'ランキング順']
    ]
    datas = [['並び順', 'カテゴリ', 'タイトル', '値段', 'リンク']]

    for category in categories:
        for sort_by in sort_bys:
            content = my_fetch.my_fetch(url + category[0], sort_by[0])
            datas += my_reg.my_reg(content, sort_by[1], category[1])

    for category in categories2:
        for sort_by in sort_bys:
            content = my_fetch.my_fetch(url + category[0], sort_by[0])
            datas += my_reg2.my_reg2(content, sort_by[1], category[1])

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