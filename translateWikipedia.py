if __name__ == '__main__':
	import sys
	if len(sys.argv) < 4:
		print("[client_id] [clint_secret] [keyword]")
		exit(0)
	
	client_id = sys.argv[1]
	client_secret = sys.argv[2]
	keyword = sys.argv[3]
	
	import getAccessToken
	access_token = getAccessToken.getAccessToken(client_id, client_secret)
	
	import getWikipedia
	s = getWikipedia.getWikipedia(keyword, 6000)
	
	while 1:
		n = s.find(".")
		en = ""
		if n >= 0:
			en = s[:n + 1]
		if len(en) < 2:
			break;
		
		import translate
		ja = translate.translate(access_token, "en", "ja", en)
		
		import say
		print("en: " + en)
		say.say("en", en)
		
		print("ja: " + ja)
		say.say("ja", ja)
		
		s = s[n + 2:]
	
	#import speech
	#fn = speech.speech(access_token, "ja", ja)
	
	#import play
	#play.play(fn)
