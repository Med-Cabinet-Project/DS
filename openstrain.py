"""Simple openstrain to only depend on json, math, and requests (no dfs/plots)."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import requests
import math
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

class ApiError(Exception):
    pass

class API(object):
    """Generic API wrapper object.
    """
    def __init__(self, **kwargs):
        self._key       = kwargs.pop('key', '')
        self._pswd      = kwargs.pop('pswd', '')
        self._version   = kwargs.pop('version', None)
        self._baseurl   = kwargs.pop('baseurl', None)
        self._headers   = {'content-type': 'application/json'}

    def _make_url(self, endpoint, **kwargs):
        """Internal method to create a url from an endpoint.
        :param endpoint: Endpoint for an API call
        :type endpoint: string
        :returns: url
        """
        endpoint = "{}/{}/{}".format(self._baseurl, self._version, endpoint)

        extra = []
        for key, value in kwargs.items():
            if isinstance(value, list) or isinstance(value, tuple):
                #value = ','.join(value)
                for v in value:
                    extra.append("{}={}".format(key, v))
            else:
                extra.append("{}={}".format(key, value))

        if len(extra) > 0:
            endpoint = '/'.join([endpoint, '/'.join(lower(extra)), '/'.join(upper(extra))])

        return endpoint

    def _send(self, endpoint, method='GET', **kwargs):
        """Make an API call of any method

        :param endpoint: API endpoint
        :param method: API call type. Options are PUT, POST, GET, DELETE

        :type endpoint: string
        :type method: string

        :returns: (status_code, json_response)

        :raises ApiError: raises an exception
        """
        auth = (self._key, self._pswd)
        url  = self._make_url(endpoint, **kwargs)

        if method == 'GET':
            resp = requests.get(url, auth=auth, headers=self._headers)
        else:
            raise ApiError("Invalid Method")

        if resp.status_code != 200:
            raise ApiError("A bad request was made: {}".format(resp.status_code))

        res = resp.json()

        # Add a 'pages' attribute to the meta data
        try:
            res['meta']['pages'] = math.ceil(res['meta']['found'] / res['meta']['limit'])
        except:
            pass

        return resp.status_code, res

    def _get(self, url, **kwargs):
        return self._send(url, 'GET', **kwargs)

class OpenStrain(API):
    """Create an instance of the OpenAQ API

    """
    def __init__(self, version='v1', **kwargs):
        """Initialize the OpenStrain instance.

        :param version: API version.
        :param kwargs: API options.

        :type version: string
        :type kwargs: dictionary

        """
        self._baseurl = "http://strainapi.evanbusse.com/" + {API_KEY}

        super(OpenAQ, self).__init__(version=version, baseurl=self._baseurl)

    def name(self, **kwargs):
        """Returns a listing of all strains within the platform.

        :Example:

        >>> import openstrain
        >>> api = openstrain.OpenStrain()
        >>> status, resp = api/name/NAME()
        >>> resp['results']
        [
            {
                "city": "Amsterdam",
                "country": "NL",
                "count": 21301,
                "locations": 14
            },
            {
                "city": "Badhoevedorp",
                "country": "NL",
                "count": 2326,
                "locations": 1
            },
            ...
        ]
        """
        return self._get('name', **kwargs)



    def __repr__(self):
        return "OpenAQ API"