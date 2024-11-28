# import http.client

# conn = http.client.HTTPSConnection("b043.lvn.broadcom.net:7554")

# headers = {
#     'Authorization': 'Basic ' + 'cHJvZDAwMTpQeXRob24yMQ==',
#     'X-CSRF-ZOSMF-HEADER': ""
#     }

# conn.request("POST", "/ibmzosmf/api/v1/zosmf/services/authenticate", headers=headers)

# res = conn.getresponse()
# data = res.read()

# print(data.decode("utf-8"))

import http.client

conn = http.client.HTTPSConnection("b043.lvn.broadcom.net:7554")

payload = "{\"scopes\":[\"string\"],\"validity\":0}"

headers = {
    'Authorization': "Basic cHJvZDAwMTpQeXRob24yMQ==",
    'content-type': "application/json"
    }

conn.request("POST", "/gateway/api/v1//auth/access-token/generate", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))