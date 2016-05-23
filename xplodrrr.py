import scene
import scene_drawing as scdr
import ui,random,time
from math import sin,cos,pi,floor

tnames=['Gx','Gy','vmu','sigvmu','thmu','sigthmu',
'g','cor','resk','npart']
snames=['boundsw','airsw','lolsw']
vnames=tnames+snames

def hsv2rgb(h,s,v):
	v/=100
	hi=floor(h/60)%6
	vmin=(100-s)*v/100
	a=(v-vmin)*(h%60)/60
	if hi==0:
		return(v,vmin+a,vmin)
	elif hi==1:
		return(v-a,v,vmin)
	elif hi==2:
		return(vmin,v,vmin+a)
	elif hi==3:
		return(vmin,v-a,v)
	elif hi==4:
		return(vmin+a,vmin,v)
	else:
		return(v,vmin,v-a)

def cswitch(sender):
	n=sender.name
	if n=='boundsw':
		val='cor'
	elif n=='airsw':
		val='resk'
	sender.superview[val].enabled=sender.value

def setng(sender):
	sender.superview['g'].text='9.81'

def startsim(sender):
	for i in vnames:
		sender.superview[i].enabled=False
	xscene=sender.superview['mainscene'].scene
	g=xscene.cdict['g']/10
	if sender.superview['lolsw'].value:
		xscene.g=vectd(.6*g,-.8*g)
	else:
		xscene.g=vectd(0,-g)
	xscene.timestamp=time.time()
	xscene.state='running'

def pausesim(sender):
	sender.superview['mainscene'].scene.state='paused'

def resetsim(sender):
	for i in vnames:
		if i=='cor':
			val=sender.superview['boundsw'].value
		elif i=='resk':
			val=sender.superview['airsw'].value
		else:
			val=True
		sender.superview[i].enabled=val
	xscene=sender.superview['mainscene'].scene
	xscene.deltat=0
	xscene.state='setup'
	xscene.PS=None

def tfee(sender):
	text=''
	for i in sender.text:
		if i in '+-.eE0123456789':
			text+=i
	if not text:
		if sender.name=='thmu':
			text='-1'
		else:
			text='0'
	xscene=sender.superview['mainscene'].scene
	xscene.cdict[sender.name]=eval(text)
	if sender.name=='npart':
		xscene.PS=None
	sender.text=text
	resetsim(sender)

class vectd:
	def __init__(self,x,y):
		self.XC=x
		self.YC=y
	
	def __mul__(self,arg):
		return self.x*arg,self.y*arg
	
	def __iadd__(self,arg):
		self.x+arg[0]
		self.y+arg[1]
		return self

class particle:
	def __init__(self,p,v,c):
		self.POS=p
		self.VEL=v
		self.COL=c

class xploder(scene.Scene):	
	def setup(self):
		self.mainview=None
		self.state='setup'
		self.background_color='white'
		self.tlabel=None
		self.cdict={'npart': 250, 'Gx': 362, 'Gy': 352, 'g': 9.81, 'cor': 0, 'sigvmu': 0, 'sigthmu': 0, 'resk': 0, 'vmu': 1, 'thmu': -1}
		self.g=None
		self.PS=None
		self.timestamp=None
		self.deltat=0
	
	def update(self):
		if self.state=='setup':
			if not self.PS:
				cd=self.cdict
				Gx,Gy,npart,vmu,sigvmu,thmu,sigthmu= cd['Gx'],cd['Gy'],cd['npart'],cd['vmu'],cd['sigvmu'], cd['thmu']*pi/180,cd['sigthmu']*pi/180
				self.PS=[]
				for i in range(npart):
					V=random.gauss(vmu,sigvmu)
					if thmu<0:
						th=2*pi*random.random()
					else:
						th=random.gauss(thmu,sigthmu)
					v=vectd(V*cos(th),V*sin(th))
					c=hsv2rgb(360*random.random(), min(100,random.gauss(100,15)),min(100, random.gauss(100,25)))
					self.PS.append(particle(vectd(Gx,Gy),v,c))
		elif self.state=='running':
			TS=time.time()
			DT=TS-self.timestamp
			self.deltat+=DT
			self.timestamp=TS
			for i in range(len(self.PS)):
				self.PS[i].POS.XC+=self.PS[i].VEL.XC*100*DT
				self.PS[i].POS.YC+=self.PS[i].VEL.YC*100*DT
				self.PS[i].VEL.XC+=self.g.XC*DT
				self.PS[i].VEL.YC+=self.g.YC*DT
		for j in range(len(self.PS)):
			scdr.fill(self.PS[j].COL)
			scdr.rect(self.PS[j].POS.XC-2, self.PS[j].POS.YC-2,4,4)
		if self.mainview:
			self.mainview['timelabel'].text='T = '+str(self.deltat)

if __name__=='__main__':
	v=ui.load_view('xplodrrr.pyui')
	v.present('full_screen')
	xscene=v['mainscene'].scene
	xscene.tlabel=v['timelabel']
	for i in tnames:
		xscene.i=eval(v[i].text)
	xscene.mainview=v
