import sys
from subprocess import PIPE,Popen
from threading import Thread
from queue import Queue,Empty

def _queueqd(ip,q):
	for line in iter(ip.readline,b''):
		q.put(line)
	ip.close()
	
def exit():
	qdp.terminate()
	sys.exit()
	
def send(*args):
	s=""
	for a in args:
		s+=str(a)
		if s[-1]!=" ":s+=" "
	op.write((s[:-1]+"\n").encode('utf-8'))

def receive():
	try:
		return qdq.get_nowait().decode('utf-8')[:-1]
	except Empty:
		return None

def running():
	return qdp.poll()==None

def circle(x,y,r):
	send("circle ",x,y,r)

def button(name,caption,x,y,w,h):
	send("button ",name,x,y,w,h,'"'+caption+'"')	

try:
	qdp = Popen("java -jar ../quickdraw.jar",shell=True,stdout=PIPE,stdin=PIPE)
	op=qdp.stdin
	qdq = Queue()
	qdt = Thread(target=_queueqd,args=(qdp.stdout,qdq))
	qdt.daemon=True
	qdt.start()
except:
	print("quickdraw.jar must be in the same directory as this python script.")
	quit()
	
