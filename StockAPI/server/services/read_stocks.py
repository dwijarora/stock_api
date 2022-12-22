import xml.etree.ElementTree as et
import json
from server.constants.json_constants import *
from server.constants.request_consts import req_session
from server.constants.api_constants import server_url

def readStocks():
    try:
        
        xml = """<v:Envelope xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns:d="http://www.w3.org/2001/XMLSchema" xmlns:c="http://schemas.xmlsoap.org/soap/encoding/" xmlns:v="http://schemas.xmlsoap.org/soap/envelope/"><v:Header /><v:Body><GetALL xmlns="http://tempuri.org/" id="o0" c:root="1"><scrips i:type="d:string">S</scrips></GetALL></v:Body></v:Envelope>"""
        headers = {
            'User-Agent': 'kSOAP/2.0',
            'SOAPAction': 'http://tempuri.org/GetALL',
            'Content-Type': 'text/xml',
            'Connection': 'close',
            'Host': 'api.dgpluslive.com',
            'Accept-Encoding': 'gzip, deflate'
        }



        str_data = req_session.post(server_url,
                                    data=xml, headers=headers).text

        tree = et.fromstring(str_data)
        all_results = tree[0][0][0].text
    
        return kSuccessResponse(data=json.loads(all_results))

    except Exception as e:
        return kErrorResponse(message=e)

    # for envelope in tree.findall('Envelope'):
    #     print(envelope)
    #     body = envelope.find('Body').text
    #     print(body)
