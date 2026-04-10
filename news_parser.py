import requests
from bs4 import BeautifulSoup

# 1. Загружаем страницу
url = "https://python.org"
response = requests.get(url)
response.raise_for_status()  # проверим, что нет ошибки

# 2. Парсим HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Находим заголовки новостей
# На python.org новости находятся в блоке <ul class="menu"> внутри <div class="blog-widget">
news_items = soup.select('.blog-widget li a')

# 4. Выводим нумерованный список
print("Последние новости с python.org:\n")
for i, item in enumerate(news_items, 1):
    title = item.get_text(strip=True)
    print(f"{i}. {title}")