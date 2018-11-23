def getAccessToken(client_id, client_secret):
	import urllib.parse
	import http.client
	import json
	
	import ssl # for "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed"
	ssl._create_default_https_context = ssl._create_unverified_context
	
	host = "auth.mimi.fd.ai";
	path = "/v2/token";
	params = urllib.parse.urlencode({
		"grant_type": "https://auth.mimi.fd.ai/grant_type/application_credentials",
		"client_id": client_id,
		"client_secret": client_secret,
		"scope": "https://apis.mimi.fd.ai/auth/nict-tts/http-api-service;https://apis.mimi.fd.ai/auth/nict-tra/http-api-service;https://apis.mimi.fd.ai/auth/nict-asr/http-api-service;https://apis.mimi.fd.ai/auth/nict-asr/websocket-api-service;https://apis.mimi.fd.ai/auth/applications.r",
	})
	headers = {
		"Content-Type": "application/x-www-form-urlencoded",
	}
	connect = http.client.HTTPSConnection(host)
	connect.request("POST", path, params, headers)
	res = json.loads(connect.getresponse().read())
	
	return res["accessToken"]

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		print("[client_id] [clint_secret]")
		exit(0)
	
	client_id = sys.argv[1];
	client_secret = sys.argv[2];
	
	access_token = getAccessToken(client_id, client_secret)
	print(access_token)
