import time
from datetime import datetime as dt


#hosts_path = "hosts"
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
website_lists = ["www.facebook.com","facebook.com"]

while True:
	if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
		print("working hours....")
		with open(hosts_path, 'r+') as file:
			content = file.read()
			for website in website_lists:
				if website in content:
					pass
				else:
					 file.write(redirect+ " "+ website+"\n")	
	else:
		with open(hosts_path,'r+') as file:
			content = file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in website_lists):
					file.write(line)
			file.truncate()		
		print("fun hours....")
	time.sleep(5)
		