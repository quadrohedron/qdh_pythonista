import scene
import scene_drawing as scdr
import ui,random,time
from math import sin,cos,pi,floor,hypot

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
	if sender.name=='airsw':
		val='resk'
		sender.superview['mainscene'].scene.reson=sender.value
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
	xscene=sender.superview['mainscene'].scene
	xscene.state='paused'
	print([i.p for i in xscene.ghostps],'\n\n',[i.p for i in xscene.realps])

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
	xscene.ghostps=None
	xscene.realps=None

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
		xscene.ghostps=None
		xscene.realps=None
	sender.text=text
	resetsim(sender)

class vectd:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def __repr__(self):
		return str((self.x,self.y))
	
	def __mul__(self,arg):
		return vectd(self.x*arg,self.y*arg)
	
	def __add__(self,arg):
		return vectd(self.x+arg.x,self.y+arg.y)
	
	def __iadd__(self,arg):
		return self+arg
	
	def __sub__(self,arg):
		return vectd(self.x-arg.x,self.y-arg.y)
	
	def __isub__(self,arg):
		return vectd(self.x-arg.x,self.y-arg.y)
	
	def dot(self,arg):
		return self.x*arg.x+self.y*arg.y
	
	def __abs__(self):
		return hypot(self.x,self.y)
	
	def norm(self):
		a=abs(self)
		if a:
			return vectd(self.x/a,self.y/a)
		else:
			return vectd(0,0)

class particle:
	def __init__(self,p,v,c):
		self.p=p
		self.v=v
		self.c=c

class xploder(scene.Scene):	
	def setup(self):
		self.mainview=None
		self.state='setup'
		self.background_color=1
		self.tlabel=None
		self.cdict={'npart': 50, 'Gx': 362, 'Gy': 352, 'g': 9.81, 'cor': 1, 'sigvmu': 0, 'sigthmu': 0, 'resk': 0.01, 'vmu': 1, 'thmu': -1}
		self.g=None
		self.ghostps=None
		self.realps=None
		self.timestamp=None
		self.deltat=0
		self.boundson=True
		self.reson=True
	
	def update(self):
		if self.state=='setup':
			if not self.ghostps or self.realps:
				cd=self.cdict
				Gx,Gy,npart,vmu,sigvmu,thmu,sigthmu= cd['Gx'],cd['Gy'],cd['npart'],cd['vmu'],cd['sigvmu'], cd['thmu']*pi/180,cd['sigthmu']*pi/180
				self.ghostps=[]
				for i in range(npart):
					V=random.gauss(vmu,sigvmu)
					if thmu<0:
						th=2*pi*random.random()
					else:
						th=random.gauss(thmu,sigthmu)
					v=vectd(V*cos(th),V*sin(th))
					c=hsv2rgb(360*random.random(), min(100,random.gauss(100,15)),min(100, random.gauss(100,25)))
					self.ghostps.append(particle(vectd(Gx,Gy),v,c))
					self.realps=[]
		elif self.state=='running':
#			TS=time.time()
#			DT=TS-self.timestamp
			DT=1/60
			self.deltat+=DT
#			self.timestamp=TS
			rlen=len(self.realps)
			resk=self.cdict['resk']
			if self.ghostps:
				reloc=[]
			COR=self.cdict['cor']
			for j in range(rlen+len(self.ghostps)):
				if j>=rlen:
					i=self.ghostps[j-rlen]
				else:
					i=self.realps[j]
					for q in self.realps[:j]+self.realps[j+1:]:
						if abs(q.p-i.p)<4:
							c=(q.p-i.p).norm()
							nc=vectd(-c.y,c.x)
							vic,vqc=c.dot(i.v),c.dot(q.v)
							vin,vqn=nc.dot(i.v),nc.dot(q.v)
							vcmu=(vic+vqc)/2
							i.p-=c*2
							q.p+=c*2
							i.v=c*(vcmu-vic*COR)+nc*vin
							q.v=c*(vcmu-vqc*COR)+nc*vqn
				if self.boundson:
					nx=i.p.x+i.v.x*100*DT
					if nx<0:
						i.p.x=0
						i.v.x*=-COR
					elif nx>723:
						i.p.x=723
						i.v.x*=-COR
					else:
						i.p.x=nx
					ny=i.p.y+i.v.y*100*DT
					if ny<0:
						i.p.y=0
						i.v.y*=-COR
					elif ny>703:
						i.p.y=703
						i.v.y*=-COR
					else:
						i.p.y=ny
					nx=i.p.x+i.v.x*100*DT
					if nx<0:
						i.p.x=0
						i.v.x*=-COR
					elif nx>723:
						i.p.x=723
						i.v.x*=-COR
				else:
					i.p+=i.v*(100*DT)
				if j>=rlen:
					
					if not sum(map(lambda x:abs(x.p-i.p)<4, self.ghostps[:j-rlen]+self.ghostps[j+1-rlen:] +self.realps)):
						reloc.append(j-rlen)
				if self.reson:
					i.v-=i.v.norm()*(i.v.dot(i.v)*resk)
				i.v+=self.g*DT
			if self.ghostps and reloc:
				for i in reloc:
					self.realps.append(self.ghostps[i])
				for i in sorted(reloc,key=int.__neg__):
					del self.ghostps[i]
		for i in self.ghostps+self.realps:
			scdr.fill(i.c)
			scdr.rect(i.p.x-2,i.p.y-2,4,4)
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
