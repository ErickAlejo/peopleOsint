from googleapiclient.discovery import build
import pprint
import json

data = input("Name: ")
people_object=[]

my_api_key = "AIzaSyDh_gEXc9kGF3hfmPjrvWIsp3ojCHf_X-I"
my_cse_id = "e74198dea603e4d4b"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

results = google_search(data, my_api_key, my_cse_id, num=10)

#for z in results:
#    pprint.pprint(z)

for a in range(len(results)):
    people_object.append(
    {
       'gathering-id':a,
       'gathering-title':results[a]['title'],
       'gathering-description':results[a]['snippet'],
       'gathering-url':results[a]['formattedUrl'],
       'gathering-link': results[a]['link']
    })
    if results[a]['pagemap']['metatags']:
       for b in results[a]['pagemap']['metatags'][0]:
           if b == 'citation_keywords':
              people_object[a]['gathering-keywords'] = [].append(results[a]['pagemap']['metatags'][0]['citation_keywords'])
           else:
              people_object[a]['gathering-keywords'] = "Not Found"

pprint.pprint(people_object)
print("Se ha creado el archivo gathering-output.txt")

