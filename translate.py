def translate(token, source_lang, target_lang, text):
	import urllib.parse
	import http.client
	import json
	
	host = "tra.mimi.fd.ai";
	path = "/machine_translation";
	params = urllib.parse.urlencode({
		"text": text,
		"source_lang": source_lang,
		"target_lang": target_lang,
	})
	headers = {
		"Content-Type": "application/x-www-form-urlencoded",
		"Authorization": "Bearer " + token,
	}
	connect = http.client.HTTPSConnection(host)
	connect.request("POST", path, params, headers)
	s = connect.getresponse().read()
	if s.decode("utf-8") == "Unauthorized":
		return null;
	res = json.loads(s)
	return res[0]

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		print("[client_id] [clint_secret]")
		exit(0)
	
	client_id = sys.argv[1];
	client_secret = sys.argv[2];
	
	import getAccessToken
	access_token = getAccessToken.getAccessToken(client_id, client_secret)
	print(access_token)
	
	print(translate(access_token, "en", "ja", "Hello!"))
