# grapi
(Pronounced: gray-P-I)

Python3 bindings for Graylog's REST API

## Install
First, make sure you have at least Python 3.7 installed.
### Development
```
git clone git@github.com:interputed/grapi.git
cd grapi
pipenv install
```
### Library Usage
```
pip3 install grapi
```

## Example Usage
To use, you must first create an *access token* following the instructions at:
[Graylog REST API Documentation](http://docs.graylog.org/en/2.4/pages/configuration/rest_api.html#creating-and-using-access-token)
API does not support username/password logins as it makes it easier to accidentally expose user credentials.

Import after installation with pip:
```from grapi.grapi import Grapi```

Import access token string:
```token = "<your_access_token_string>"```

Set URL to desired API path:
```url = "https://<your Graylog URL>/api/search/universal/absolute"```

All currently implemented URL endpoints can be found in: ```grapi/endpoints.py```

The list of all possible endpoints that may be implemented in the future is found by adding ```/api/api-browser``` to the URL of your Graylog server.

Setup the Grapi object with url and token:
```my_api = Grapi(url, token)```

Build a dictionary of parameters mapped to string values for every parameter of your request:
```
my_params = {
  "query": "<your query string (lucene syntax)>", # Required
  "fields": "<fields you wish returned>", # Required
  "from": "<YYYY-MM-DD HH-MM-SS>", # Required
  "to": "<YYYY-MM-DD HH-MM-SS>", # Required
  "limit": 10 # Optional: Default limit is 150 in Graylog
}
```

Now, simply call the send method of my_api with the type of request method (get, post, put, delete):
```response = my_api.send("get", **my_params)```

That's it for a simple search in Python 3 using Graylog's REST API! Now you can manipulate the data however you wish directly in Python. To see the output of your search you can just print it as with anything else in Python:
```
print(response.json())
OR
print(response.text)
```

#### This is a work in progress, so if the method or endpoint you need isn't yet implemented, add it yourself and send a pull request, post to issues, or simply check back later and it should be added.
