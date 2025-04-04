import requests
import json

url = 'https://api.artic.edu/api/v1/artworks/search'

def get_artwork(keyword):
    querystring = {'q': keyword}
    response = requests.request('GET', url, params=querystring)
    return response.text


if response.choices[0].finish_reason=='tool_calls':
    function_call = response.choices[0].message.tool_calls[0].function
    if function_call.name == 'get_artwork':
        artwork_keyword  = json.loads(function_call.arguments)['artowrk keyword']
        artwork = get_artwork(artwork_keyword)

        if artwork:
            print(f"Here are some recommendations:
            {[i['title'] for i in json.loads(artwork)['data']]}")
        else:
            print("Apologies, I couldn't find any recommendations based on the request")
    else:
        print("Apologies, I couldn't find any artwork.")
else:
    print("I am sorry, but I couldn't understand your request.")