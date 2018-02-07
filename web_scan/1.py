import requests
import threading
from threading import Thread
import Queue

web_paths = Queue.Queue()
lock=threading.Lock()
def open_dic():
	url = raw_input('please input the website:')
	with open('new_web.txt','r') as f:
	    for line in f:
		if url.startswith('http'):
			wb = url + line
			web = wb.strip()
			web_paths.put(web)
		else:
                	wb = 'http://' + url + line
                	web = wb.strip()
               		web_paths.put(web)

def start_scan():
	lock.acquire()
	while not web_paths.empty(): 
		path = web_paths.get()
		r = requests.get(path)
		rs = r.status_code
	  	if rs == 200:
			print rs,
			print path,'found'
		if rs == 302:
			print rs,
			print 'Object moved'
		else:
			continue
	lock.release()
def main():
	open_dic()
	for i in range(2):
		print "Spawning thread: %d" % i
		xx = Thread(target=start_scan)
		xx.start()
if __name__ == '__main__':
	main()
