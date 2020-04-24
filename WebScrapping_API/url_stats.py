# from pytrends.request import TrendReq
# from pytrends.test_trendReq import *
# from pytrends import dailydata
# pytrends = TrendReq(hl='en-US', tz=360)
# kw_list = ['apples', 'oranges', 'bananas']
# interest_over_time_df = pytrends.interest_over_time()
# print(dailydata)
from flask import Flask,jsonify
app = Flask(__name__)

@app.route('/<string:url>')
def statistics(url):
    import requests
    from bs4 import BeautifulSoup
    url1 = requests.get("https://rt.nextnetmedia.com/thehoth-ser/domain/88879cea2f08cff12c74772aadf01d60/{}/?db=us".format(url),verify=False)
    url2 = requests.get("https://rt.nextnetmedia.com/thehoth-ser/viewmore/domain/bc0c3e9a8949f694aa763ef75e07d9b4/{}/2/?db=us".format(url),verify=False)
    soup1 = BeautifulSoup(url1.content,"html.parser")
    soup2 = BeautifulSoup(url2.content,"html.parser")
    li1 = [i.text for i in soup1.find_all('td') if i.text !='\xa0Add\xa0Links' and len(i.text) != 0]
    li2 = [i.text for i in soup2.find_all('td') if i.text !='\xa0Add\xa0Links' and len(i.text) != 0]

# res = [i for i in li if (li.index(i)+1) % 6 !=0]

    index1 = li1[0:len(li1)-1:6]
    keywords1 = li1[1:len(li1)-1:6]
    rank1 = li1[2:len(li1)-1:6]
    volume1 = li1[3:len(li1)-1:6]
    traffic1 = li1[4:len(li1)-1:6]

    index2 = li2[0:len(li2)-1:6]
    keywords2 = li2[1:len(li2)-1:6]
    rank2 = li2[2:len(li2)-1:6]
    volume2 = li2[3:len(li2)-1:6]
    traffic2 = li2[4:len(li2)-1:6]
    API1 = []
    API2 = []
    for i,j,k,l,m in zip(index1,keywords1,rank1,volume1,traffic1):
        API1.append({
            "Index":i,
            "Keyword":j,
            "Rank":k,
            "Volume":l,
            "Traffic":m
        })

    for n,o,p,q,r in zip(index2,keywords2,rank2,volume2,traffic2):
        API2.append({
            "Index":n,
            "Keyword":o,
            "Rank":p,
            "Volume":q,
            "Traffic":r
        })
    return jsonify(API1 + API2)

if __name__ == '__main__':
    app.run(debug=True,port=4222)

