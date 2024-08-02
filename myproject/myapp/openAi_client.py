from __future__ import print_function
from pprint import pprint
import time
import swagger_client

configuration = swagger_client.Configuration()
configuration.host = 'http://127.0.0.1:8080'
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))

pprint(dir(api_instance))
