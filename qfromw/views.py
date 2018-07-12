from django.shortcuts import render
import requests
import bs4
import re

# Create your views here.

def appmain(request):
    while True:
        res = requests.get('https://ja.wikipedia.org/wiki/%E7%89%B9%E5%88%A5:%E3%81%8A%E3%81%BE%E3%81%8B%E3%81%9B%E8%A1%A8%E7%A4%BA')
        soup = bs4.BeautifulSoup(res.text, "html5lib")
        title = soup.select("#firstHeading")[0].getText()
        description = soup.select('div.mw-parser-output p')[0].getText()
        description2 = re.sub(r"（.*?）", ' ', description)
        description3 = description2.replace(title, '◯' * len(title))
        if description2 != description3:
            break

    return render(request, 'demo/main.html', {
        'answer' : title,
        'descr' : description3,
    })

#    return render(request, 'blog/post_list2.html', {'posts':posts})


