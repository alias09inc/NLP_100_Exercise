import json
import re

# １行ずつ読み込んで、json形式で取り出してリストに入れる
articles = []
with open('jawiki-country.json', 'r', encoding="utf-8") as f:
    for article in f:
        articles.append(json.loads(article))
len(articles)

for i in range(len(articles)):
    if articles[i]['title']=='イギリス':
        uk_text = articles[i]['text']
        break

pattern = "Category"
result = re.findall(pattern, uk_text)
print(result)