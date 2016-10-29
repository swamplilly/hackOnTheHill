import json
import urllib
import oauth2
import random

#location parameters go as "location=zip"
#change for the sake of change

#In line with yelp samples
Api_Host = 'api.yelp.com'
Default = 'dinner'
Location = '90210' #hard coding for now
Search_Limit = 10 #for now
Search_Path = '/v2/search'
Business_Path = 'v2/business' #idkkk

#Oauth garbage aka things that should NOT be hardcoded ^^;
#Assuming these are all passed as strings...
Consumer_Key = '93Qg25NU0Affw7QHpxbSog'
Consumer_Secret = 'exmJrdia8Xxm2cklwpj9bLLiXIQ' 
Token = '2wiqohihnsRi7B5rMwj9SS-rbZKrOoHK'
Token_Secret = 'jD4XYIvBKf_lvfDujURszXMU00o'

#example code parses argument then tries to query the api.
#taken verbatim, now modifying
#installing setup tools to get this to work...?
def request(host, path, url_params=None):
    """Prepares OAuth authentication and sends the request to the API.
    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        url_params (dict): An optional set of query parameters in the request.
    Returns:
        dict: The JSON response from the request.
    Raises:
        urllib2.HTTPError: An error occurs from the HTTP request.
    """
    url_params = url_params or {}
    url = 'https://{0}{1}?'.format(host, urllib.quote(path.encode('utf8')))

    consumer = oauth2.Consumer(Consumer_Key, Consumer_Secret)
    oauth_request = oauth2.Request(method="GET", url=url, parameters=url_params)

    oauth_request.update(
        {
            'oauth_nonce': oauth2.generate_nonce(),
            'oauth_timestamp': oauth2.generate_timestamp(),
            'oauth_token': Token,
            'oauth_consumer_key': Consumer_Key
        }
    )
    token = oauth2.Token(Token, Token_Secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()
    
    print u'Querying {0} ...'.format(url)

    conn = urllib.urlopen(signed_url, None)
    try:
        response = json.loads(conn.read())
    finally:
        conn.close()

    return response



def search(term, location):
    """Query the Search API by a search term and location.
    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.
    Returns:
        dict: The JSON response from the request.
    """
    
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': Search_Limit
    }
    return request(Api_Host, Search_Path, url_params=url_params)
response = search(Default, Location)
#print(response)
f = open('dump.txt','w')
#json.dump(response, f)

ran_num=random.randint(0,9)
print(ran_num)

biz = response['businesses'][ran_num]
biz_loc = biz['location']
biz_coord = biz_loc['coordinate']
print(biz_coord)
json.dump(biz, f)

#define string by
#dinner_base = "https://api.yelp.com/v2/search?term=dinner&location="

#zip = get_user_input() #whatever user input is
#zip_str = str(zip) #should probably escape / throw error if not a 5 digit integer...

#request_url=dinner_base + zip_str #I think this is fine

#Which would look like
#"https://api.yelp.com/v2/search?term=cream+puffs&location=90210"

#Want to limit to top ten results so we'll use limit=10
#"https://api.yelp.com/v2/search?term=cream+puffs&location=90210&limit=1"

