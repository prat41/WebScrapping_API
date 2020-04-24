from googleapiclient.discovery import build   #Import the library

api_key = "my-secret-api-key"
cse_id = "my-secret-custom-search-id "
def google_query(query, api_key, cse_id, **kwargs):
    query_service = build("customsearch",
                          "v1",
                          developerKey=api_key
                          )
    query_results = query_service.cse().list(q=query,    # Query
                                             cx=cse_id,  # CSE ID
                                             **kwargs
                                             ).execute()
    return query_results['items']
my_results_list = []
my_results = google_query("apple iphone news 2019",
                          api_key,
                          cse_id,
                          num = 10
                          )
for result in my_results:
    my_results_list.append(result['link'])
    print(result['link'])