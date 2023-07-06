import re

import pandas as pd

def extract_by_title(title):
    df_wiki = pd.read_json('jawiki-country.json', lines=True)
    return df_wiki[(df_wiki['title'] == title)]['text'].values[0]

wiki_body = extract_by_title('イギリス')

# rを先頭にするとraw string でエスケープシーケンス無視
# 3重クォートで途中改行無視
# re.VERBOSEオプションを使うことによって、空白とコメント無視
# re.MULTILINEで複数行に対して検索
# 非貪欲マッチにすることで、短い文字列を検索
sections = re.findall(r'''
                      ^         # 文字列の先頭
                      (={2,})   # キャプチャ対象、2回以上の'='
                      \s*       # 非キャプチャ、余分な0個以上の空白('哲学'や'婚姻'の前後に余分な空白があるので除去)
                      (.+?)     # キャプチャ対象、任意の文字が1文字以上、非貪欲(以降の条件の巻き込み防止)
                      \s*       # 非キャプチャ、余分な0個以上の空白
                      \1        # 後方参照、1番目のキャプチャ対象(={2,})と同じ内容
                      $         # 行末
                      ''', wiki_body, re.MULTILINE+re.VERBOSE)

for section in sections:
    level = len(section[0]) - 1    # '='の数-1
    print('{indent}{sect}({level})'.format(
        indent='\t'*(level-1), sect=section[1], level=level))