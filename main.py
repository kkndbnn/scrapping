import requests
import bs4
HEADERS = {
    'Cookie': '_ym_uid=1661628002717828153; _ym_d=1661628002; hl=ru; fl=ru; _ga=GA1.2.1825526209.1661628002; _ym_isad=2; habr_web_home_feed=/all/; _gid=GA1.2.1742897579.1662059796; visited_articles=537174',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

KEYWORDS = ['дизайн', 'фото', 'web', 'python *']
KEYWORDS_title = []
base_url = 'https://habr.com'
for key in KEYWORDS:
    res = key.title()
    KEYWORDS_title.append(res)
response = requests.get(base_url, headers=HEADERS)
text = response.text
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    hubs = article.find_all(class_='tm-article-snippet__hubs-item')
    hubs = set(hub.text.strip() for hub in hubs)
    for key in KEYWORDS_title:
        if key in hubs:
            date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
            href = article.find(class_='tm-article-snippet__title-link').attrs['href']
            link = base_url + href
            title = article.find('h2').find('span').text
            result = f'{date} {title} - {link}'
            print(result)