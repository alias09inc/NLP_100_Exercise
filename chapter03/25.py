import re
from collections import OrderedDict
from pprint import pprint
import pandas as pd

def extract_by_title(title):
    df_wiki = pd.read_json('jawiki-country.json', lines=True)
    return df_wiki[(df_wiki['title'] == title)]['text'].values[0]

wiki_body = extract_by_title('イギリス')

basic = re.search(r'''
                    ^\{\{基礎情報.*?\n  #検索語句(\はエスケープ処理)、非キャプチャ、非貪欲
                    (.*?)              #任意の文字列
                    \}\}               #検索語句(\はエスケープ処理)
                    $                  #文字列の末尾
                    ''', wiki_body, re.MULTILINE+re.VERBOSE+re.DOTALL)
# print(basic.group(1))

results = re.findall(r'''
                        ^\|
                        (.*?)
                        \s*
                        =
                        \s*
                        (.*?)
                        (?:
                            (?=\n\|)
                        |   (?=\n$)
                        )
                        ''', basic.group(1), re.MULTILINE+re.VERBOSE+re.DOTALL)

result_dict = OrderedDict(results)

pprint(result_dict)