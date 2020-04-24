from flask import Flask,jsonify
from googlesearch import *
from googleapiclient.discovery import build
from flask import Flask
app = Flask(__name__)
'''Google Custom Search Keywords 
for the particular website'''
def Find_Keywords(url):

    #api = "AIzaSyDcn5WPaRmpPo7HVCN8nS9DLm-hliBNaxM"
    api = "AIzaSyClGWdqO3wXqYK7ox1jDN9D-mwrh7Bm7jE"
    resource = build('customsearch', 'v1', developerKey = api).cse()
    sources = []

    for i in range(1,20,10):
        result = resource.list(q = url, cx = '004124293475798993048:uu7vpk6keyt',start=i).execute()
        sources += result['items']
    keywords = [i['title'] for i in sources]
    links = [i['link'] for i in sources]
    final_result = []
    for i in keywords:
        for j in i:
            if j == '|' or j == '-':
                result = i.split(j)[0]
                final_result.append(result)

    return final_result


def position(url, keyword):
    json_file = []
    result = search(keyword, tld="co.in", stop=10)
    j = 1

    for i in result:
        json_file.append(
            {
                'link': i.split('/')[2],
                'Position': j
            }
        )
        j += 1


    # if (url.startswith('www') or url.startswith('en')) and (url.endswith('.in') or url.endswith('.net') or url.endswith('.org') or url.endswith('.com')):
    #     res = [i['Position'] for i in json_file if i['link'] == url]
    #     return  res
    # return json_file
    if url:
        res = [i['Position'] for i in json_file if i['link'] == url]
        return  res
    #
    # else:
    #     return {"Error Message": "Invalid URL try www.xyz.com"}

@app.route('/<string:url>')
def keyword_wise_ranking(url):
    # ranks = [position(url,i) for i in Find_Keywords(url)]
    # for i in ranks:
    te = [{'Keyword':k, 'Ranks':position(url,k)[0:3]} for k in Find_Keywords(url) if len(position(url,k))!=0]
    # for k in Find_Keywords(url):
    #     if len(position(url,k)) == 0:
    #         continue
    #     else:
    #          print({'Keyword':k, 'Ranks':position(url,k)})
    for i in te:
        print(i)
# if __name__ == '__main__':
#      app.run(debug=True,port=4566)
print(keyword_wise_ranking("www.hackerrank.com"))