import re

import pandas as pd

def extract_by_title(title):
    df_wiki = pd.read_json('jawiki-country.json', lines=True)
    return df_wiki[(df_wiki['title'] == title)]['text'].values[0]

wiki_body = extract_by_title('イギリス')

results = re.findall(r'''
                    (?:File|ファイル)
                    :
                    (.+?)
                    \|
                    ''', wiki_body, re.VERBOSE)

for result in results:
    print(result)