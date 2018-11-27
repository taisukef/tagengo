if __name__ == '__main__':
	import sys
	if len(sys.argv) < 4:
		print("[client_id] [clint_secret] [script.csv]")
		exit(0)
	
	client_id = sys.argv[1]
	client_secret = sys.argv[2]
	csvfn = sys.argv[3]
	
	from getAccessToken import getAccessToken
	access_token = getAccessToken(client_id, client_secret)
	
	from datetime import datetime
	startt = int(datetime.now().strftime('%s'))
	
	import csv
	with open(csvfn, newline = '') as csvfile:
		reader = csv.reader(csvfile, delimiter = ',')
		for row in reader:
			dt = int(row[0])
			src = row[1]
			dst = row[2]
			text = row[3]
			
			if src != dst:
				from translate import translate
				text2 = translate(access_token, src, dst, text)
				print("time " + str(dt) + "sec : " + text + " -> " + text2)
			else:
				print("time " + str(dt) + "sec : " + text)
				text2 = text
			
			from time import sleep
			while 1:
				sleep(0.1)
				now = int(datetime.now().strftime('%s'))
				if now > startt + dt:
					break
			
			from say import say
			say(dst, text2)
