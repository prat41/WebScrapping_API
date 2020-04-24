from googlesearch import *
from flask import  Flask,jsonify
from flask_restful import Resource,Api


app = Flask(__name__)
api = Api(app)

# class Search_api(Resource):
@app.route('/<string:keyword>')
def geto(keyword):
    json_file = []
    result = search(keyword, tld="co.in", stop=50)
    j = 1
    for i in result:
        json_file.append(
            {'Position': j,
                'link': i
            }
        )
        j += 1
    return jsonify(json_file)

#







#api.add_resource(Search_api,'/keyword/<string:keyword>',endpoint= 'keyword')
# api.add_resource(find_position,'/<string:keyword>/<string:url>')

app.run(debug=True,port=4323)





