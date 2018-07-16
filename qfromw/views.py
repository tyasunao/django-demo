from django.shortcuts import render
import requests   # Web からデータを取ってくる時に使う
import bs4        # スクレイピング
import re         # 正規表現によるマッチングを使う

def appmain(request):
    while True:
        # wikipedia の「おまかせ表示」にアクセスして結果を res に入れる
        res = requests.get('https://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:%E3%81%8A%E3%81%BE%E3%81%8B%E3%81%9B%E8%A1%A8%E7%A4%BA')
        
        # 「おまかせ表示」に現われたページをスクレイピング
        soup = bs4.BeautifulSoup(res.text, "html5lib")

        # この Wiki エントリのタイトルの文字列を変数 title に代入
        title = soup.select("#firstHeading")[0].getText()

        # この Wiki エントリのトップにある説明文だけ取り出して変数 description に代入
        description = soup.select('div.mw-parser-output p')[0].getText()

        # ( ) 内に答えにつながる言葉があるエントリが多いので，( ) は取り除いてしまう．最短マッチが重要
        description2 = re.sub(r"（.*?）", ' ', description)

        # 答えに当たる部分を ◯ で置き換える．文字数が同じなのはヒントのため
        description3 = description2.replace(title, '◯' * len(title))

        # 答えが置き換わったときだけクイズにする
        if description2 != description3:
            break

    # demo/main.hml に値を渡す
    return render(request, 'demo/main.html', {
p        'answer' : title,
        'descr' : description3,
    })


