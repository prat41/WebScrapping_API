from serpwow.google_search_results import GoogleSearchResults
import json
from flask import Flask,jsonify
app = Flask(__name__)


# create the serpwow object, passing in our API key
@app.route('/<string:query>/<string:location>')
def locate_url(query,location):
    serpwow = GoogleSearchResults("6C6E8E58B43740A0BB943B8AD68D53C4")

# set up a dict for the search parameters
    params = {
              "q" : query,
              "location" : location
            }

# retrieve the search results as JSON
    result = serpwow.get_json(params)

# pretty-print the result
    return (json.dumps(result, indent=2, sort_keys=True))

if __name__ == '__main__':
  app.run(debug=True,port=4121)


