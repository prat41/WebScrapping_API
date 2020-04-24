from re import search

from flask import Flask
from googlesearch import *
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)

@app.route('/<string:keyword>/<string:url>')
def position(url,keyword):
     json_file = []
     result = search(keyword, tld="co.in", stop=30)
     j = 1
     for i in result:
         json_file.append(
              {
                  'link': i.split('/')[2],
                  'Position': j
              }
             )
         j += 1

     print(json_file)

     if (url.startswith('www') or url.startswith('en')) and (url.endswith('.in') or url.endswith('.net') or url.endswith('.org') or url.endswith('.com')):
         res = [i['Position'] for i in json_file if i['link'] == url ]
         return {'Positions': res}

     elif url:
         res = [i['Position'] for i in json_file if i['link'] == url]
         if len(res) == 0:
             return {"Error Message":"No Url Found"}
         else:
             return {'Positions': res}

     else:
         return {"Error Message" : "Invalid URL try www.xyz.com"}


# api.add_resource(find_position,'/<string:keyword>/<string:url>')
if __name__ == '__main__':
    app.run(debug=True,port=4333)
