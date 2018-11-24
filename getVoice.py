def getVoice(access_token, lang, gender, text, fn):
	import urllib.parse
	import http.client
	import json
	
	host = "tts.mimi.fd.ai"
	path = "/speech_synthesis"
	params = urllib.parse.urlencode({
		"text": text,
		"engine": "nict",
		"lang": lang, # ja, en, zh, ko, id, vi, my, th
		"gender": gender,
		"audio_format": "RAW", # "WAV"
	})
	headers = {
		"Content-Type": "application/x-www-form-urlencoded",
		"Authorization": "Bearer " + access_token,
	}
	connect = http.client.HTTPSConnection(host)
	connect.request("POST", path, params, headers)
	s = connect.getresponse().read()
	
	with open(fn, "wb") as f:
		f.write(s) #.encode('utf-8'))

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		print("[client_id] [clint_secret] [text]")
		exit(0)
	
	client_id = sys.argv[1];
	client_secret = sys.argv[2];
	text = sys.argv[3]
	
	import getAccessToken
	access_token = getAccessToken.getAccessToken(client_id, client_secret)
	print(access_token)
	
	fn = "female.raw"
	getVoice(access_token, "ja", "female", text, fn)

	import playRaw
	playRaw.playRaw(fn)
	
	fn = "male.raw"
	getVoice(access_token, "ja", "male", text, fn)

	import playRaw
	playRaw.playRaw(fn)
