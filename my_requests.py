import http.client
import json
from urllib.parse import urlparse

def get(url):
    parsed_url = urlparse(url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)
    conn.request("GET", parsed_url.path)
    response = conn.getresponse()
    data = response.read()
    return json.loads(data.decode('utf-8'))

def post(url, body):
    parsed_url = urlparse(url)
    conn = http.client.HTTPSConnection(parsed_url.netloc)
    headers = {'Content-type': 'application/json'}
    json_data = json.dumps(body)
    conn.request("POST", parsed_url.path, body=json_data, headers=headers)
    response = conn.getresponse()
    data = response.read()
    return json.loads(data.decode('utf-8'))
