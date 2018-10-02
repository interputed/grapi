import requests
from urllib.parse import urlparse
from .endpoints import Endpoints


class Grapi:
    # Class currently only supports the GET methods that don't insert values into the url and return a JSON object.
    # TODO: Extend to support POST, PUT, & DELETE methods.
    def __init__(self, url, access_token):

        self.url = url
        self._endpoint = urlparse(self.url).path
        self._access_token = (access_token, "token")
        self.methods = {
            "get": self._get,
            "post": self._post,
            "put": self._put,
            "delete": self._delete
        }

    def _get(self, **kwargs):
        response = requests.get(self.url, auth=self._access_token, params=kwargs)
        return response

    def _post(self, **kwargs):
        # TODO: Implement
        raise NotImplementedError("POST: Not Yet Implemented")

    def _put(self, **kwargs):
        # TODO: Implement
        raise NotImplementedError("PUT: Not Yet Implemented")

    def _delete(self, **kwargs):
        # TODO: Implement
        raise NotImplementedError("DELETE: Not Yet Implemented")

    def _methods(self, method):
        # Gets a pointer to the right function depending on API access method
        if method not in self.methods.keys():
            raise ValueError("\"{0}\" is not a supported method. " +
                             "Please use one of the following: {1}".format(method, self.methods.keys()))
        return self.methods[method]

    def send(self, method, **kwargs):
        endpoints = Endpoints()
        keys = kwargs.keys()
        print(self._endpoint)
        endpoints.check(keys, self._endpoint)
        return self._methods(method.lower())(**kwargs)





