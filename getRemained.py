def getRemained(access_token):
	import urllib.parse
	import http.client
	import json
	
	import ssl # for "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed"
	ssl._create_default_https_context = ssl._create_unverified_context
	
	host = "apis.mimi.fd.ai"
	path = "/v1/applications/counter"
	params = None
	headers = {
		"Authorization": "Bearer " + access_token,
	}
	connect = http.client.HTTPSConnection(host)
	connect.request("GET", path, params, headers)
	s = connect.getresponse().read()
	res = json.loads(s)
	return res[0]["counts"]["ticket_remained"]

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		print("[client_id] [clint_secret]")
		exit(0)
	
	client_id = sys.argv[1];
	client_secret = sys.argv[2];
	
	import getAccessToken
	access_token = getAccessToken.getAccessToken(client_id, client_secret)
	
	remained = getRemained(access_token)
	print(remained)
