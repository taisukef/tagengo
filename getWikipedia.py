def getRawWikipedia(keyword):
	import urllib.parse
	import http.client
	
	import ssl # for "[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed"
	ssl._create_default_https_context = ssl._create_unverified_context
	
	host = "en.wikipedia.org";
	path = "/wiki/" + keyword
	connect = http.client.HTTPSConnection(host)
	connect.request("GET", path, {}, {})
	s = connect.getresponse().read().decode('utf-8')
	return s

def getWikipedia(keyword, bodylen):
	s = getRawWikipedia(keyword)
	
	#with open(keyword + ".txt", "w") as f:
	#	f.write(s) #.encode('utf-8'))
	
	#with open(keyword + ".txt", "r") as f:
	#	s = f.read()
	
	n = s.find("<div class=\"mw-parser-output\">")
	s = s[n: n + bodylen]
	
	m = s.rfind("<")
	if m >= 0:
		s = s[:m]
	
	#print(s)
	
	s = s.replace("</caption>", ". ")
	s = s.replace("</tr>", ". ")
	s = s.replace("</td>", " ")
	s = s.replace("</th>", " ")
	s = s.replace("&#160;", " ")
	
	import re
	p = re.compile(r"<[^>]*?>")
	s = p.sub("", s)
	
#	p = re.compile(r"&#91;?&#93;")
#	s = p.sub("", s)
	s = s.replace("&#91;1&#93;", "")
	s = s.replace("&#91;2&#93;", "")
	s = s.replace("&#91;3&#93;", "")
	s = s.replace("&#91;4&#93;", "")
	s = s.replace("&#91;5&#93;", "")
	
	s = s.replace("\n", " ")
	s = s.replace("\r", "")
	
	m = s.rfind(".")
	if m >= 0:
		s = s[:m + 1]
	
	return s

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 2:
		print("[keyword]")
		exit(0)
	
	keyword = sys.argv[1];
	s = getWikipedia(keyword)
	
	print(s)
