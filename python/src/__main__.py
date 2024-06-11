import my_reg
import my_fetch

def main():
    url = "https://coconala.com/categories/9"

    # content = my_fetch.my_fetch(url)
    content = get_content()

    my_reg.my_reg(content)


def get_content():
    with open('coconala-scraping.txt', 'r', encoding='utf-8') as file:
        return file.read()
    if content != None:
        return ""

if __name__ == "__main__":
    main()