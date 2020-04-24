from flask import Flask,jsonify
from googleapiclient.discovery import build

app = Flask(__name__)
@app.route('/<string:url>')
def Find_Keyword(url):

    api = "Your API KEY"
    resource = build('customsearch', 'v1', developerKey = api).cse()
    sources = []

    for i in range(1,30,10):
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

    return {"keywords": final_result}

print((Find_Keyword('www.hackerrank.com')))
if __name__ == '__main__':
     app.run(debug=True,port=4998)
#




