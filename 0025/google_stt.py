# -*- coding: utf-8 -*-
"""
Created on Tue Nov 01 12:56:58 2016

@author: MagicWang
"""

import base64  
import json
from googleapiclient import discovery  
import httplib2
from oauth2client.client import GoogleCredentials

speech_file = 'file.wav'  
encoding = 'Linear-16'  
sampleRate = 8000  
languageCode = 'en-US'

DISCOVERY_URL = ('https://{api}.googleapis.com/$discovery/rest?'  
                 'version={apiVersion}')

def get_speech_service():  
    credentials = GoogleCredentials.get_application_default().create_scoped(
        ['https://www.googleapis.com/auth/cloud-platform'])
    http = httplib2.Http(proxy_info=httplib2.ProxyInfo(httplib2.socks.PROXY_TYPE_HTTP, 'localhost', 1080))
    credentials.authorize(http)

    return discovery.build(
        'speech', 'v1beta1', http=http, discoveryServiceUrl=DISCOVERY_URL)


def main(speech_file):  
    with open(speech_file, 'rb') as speech:
        speech_content = base64.b64encode(speech.read())

    service = get_speech_service()
    service_request = service.speech().syncrecognize(
        body={
            'config': {
                'encoding': encoding,
                'sampleRate': sampleRate,  
                'languageCode': languageCode,  
            },
            'audio': {
                'content': speech_content.decode('UTF-8')
                }
            })
    response = service_request.execute()
    print(json.dumps(response))

if __name__ == '__main__':

    main(speech_file)