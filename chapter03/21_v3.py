import re
import pandas as pd

def extract_by_title(title):
    df_wiki = pd.read_json('jawiki-country.json', lines=True)
    return df_wiki[(df_wiki['title'] == title)]['text'].values[0]

wiki_body = extract_by_title('イギリス')

result = re.findall(r''' #rでraw文字にすることでエスケープシーケンスを回避、トリプルクウォートで改行
                    ^#文字列の先頭
                    (#グルーピングの開始
                        .*#0文字以上
                        \[\[Category:#\はエスケープ処理
                        .*
                        \]\]
                        .*
                        
                    )#グルーピングの終了
                    $
                    ''', wiki_body, re.MULTILINE+re.VERBOSE)

print(result)