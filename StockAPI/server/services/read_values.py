import xml.etree.ElementTree as et
import json
from server.constants.json_constants import kErrorResponse, kSuccessResponse
from server.constants.request_consts import req_session
from server.models.values_model import ValuesModel
from server.constants.api_constants import server_url
# 18237,18234,18235,16661,16662,16897,17644,18448,16893,18165,18203,18204,18205,18238,18228,17157,16663,16656


def readValues(model: ValuesModel):
    try:

        xml = f"""<v:Envelope xmlns:i="http://www.w3.org/2001/XMLSchema-instance" xmlns:d="http://www.w3.org/2001/XMLSchema" xmlns:c="http://schemas.xmlsoap.org/soap/encoding/" xmlns:v="http://schemas.xmlsoap.org/soap/envelope/"><v:Header /><v:Body><GetUpdatesWithColumns xmlns="http://tempuri.org/" id="o0" c:root="1"><scrips i:type="d:string">{model.scriptIds}</scrips><columns i:type="d:string">a6,a7,a9,a13,a14,a11</columns></GetUpdatesWithColumns></v:Body></v:Envelope>"""
        headers = {
            'User-Agent': 'kSOAP/2.0',
            'SOAPAction': 'http://tempuri.org/GetUpdatesWithColumns',
            'Content-Type': 'text/xml',
            'Connection': 'close',
            'Host': 'api.dgpluslive.com',
            'Accept-Encoding': 'gzip, deflate'
        }

        str_data = req_session.post(server_url,
                                    data=xml, headers=headers).text

        tree = et.fromstring(str_data)
        all_results = tree[0][0][0].text
        
        data = json.loads(all_results)
        changed_stock_name = []
        for stock in data:
            changed_stock_name.append({
                "scripid": stock['scripid'],
                "Bid": stock['6'],
                "Ask": stock['7'],
                "Ltp": stock['9'],
                "High": stock['13'],
                "Low": stock['14']
            })
 
        return kSuccessResponse(data=changed_stock_name)

    except Exception as e:
        print(f"Error readValues {e}")
        return kErrorResponse(message="Something went wrong")

    # for envelope in tree.findall('Envelope'):
    #     print(envelope)
    #     body = envelope.find('Body').text
    #     print(body)
