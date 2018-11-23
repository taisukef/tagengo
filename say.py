def say(lang, text):
	v = "Kyoko"
	if lang == "en":
		v = "Samantha"
	
	cmd = "say -v " + v + " \"" + text + "\""
	
	import subprocess
	popen = subprocess.Popen(cmd, shell=True)
	popen.wait()

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 3:
		print("[lang] [text]")
		exit(0)
	
	lang = sys.argv[1]
	text = sys.argv[2]
	
	say(lang, text)
