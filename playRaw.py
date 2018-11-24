def playRaw(fn):
	# hello-ja.raw
	
	cmd = "play -t raw -r 16k -e signed -b 16 -c 1 " + fn
	
	import subprocess
	popen = subprocess.Popen(cmd, shell=True)
	popen.wait()

if __name__ == '__main__':
	import sys
	if len(sys.argv) < 1:
		print("[fn]")
		exit(0)
	
	fn = sys.argv[1]
	
	playRaw(fn)
