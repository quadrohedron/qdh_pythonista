import ui,scene,time,threading

_timer=None

def fsets(sender):
	global _msh
	_msh.hidden=False

def sendhlep(sender):
	global _hsh
	_hsh.hidden=False

def fback(sender):
	sender.superview.hidden=True

def mb_action(sender):
	if 'test' in dir(sender):
		key,val=sender.test
		if sender.superview[key].value!=val:
			print('Nope.')
			return None
	print(sender.vars,sender.vals)

def msw_action(sender):
	sup=sender.superview
	for i in sender.fields:
		sup[i].enabled=not sup[i].enabled

def ccseg_action(sender):
	menu=sender.superview
	if sender.selected_index:
		labels=['R:','G:','B:']
	else:
		labels=['H:','S:','V:']
	for i in range(3):
		menu['ccl'+str(i+1)].text=labels[i]

def gzcenter(sender):
	print('gzcenter call')

def airkdec(sender):
	val=sender.superview['airsw'].value
	print('airkdec call,',val)

def airkinc(sender):
	val=sender.superview['airsw'].value
	print('airkinc call,',val)

def scenesizeout(obj):
	global _timer
	_timer=None
	print('Scene size:',obj.size)

def resizemenu():
	global _sc,_msh,_hsh
	w,h=_sc.size
	print(_hsh.width,_hsh.height)
	if h<700:
		_msh['menu'].content_size=(_msh.width-20,1500)
		_hsh['hlepitself'].content_size=(_hsh.width,2100)
	elif h<900:
		_msh['menu'].content_size=(540,847)
	else:
		_msh['menu'].content_size=(540,759)

def hsv2rgb(h,s,v):
	v/=100.0
	hi=floor(h/60.0)%6
	vmin=(100-s)*v/100.0
	a=(v-vmin)*(h%60)/60.0
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

class vectd:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	
	def __repr__(self):
		return '2D vector '+str((self.x,self.y))
	
	def __str__(self):
		return '2D vector '+str((self.x,self.y))
	
	def __mul__(self,arg):
		return vectd(self.x*arg,self.y*arg)
	
	def __add__(self,arg):
		return vectd(self.x+arg.x,self.y+arg.y)
	
	def __iadd__(self,arg):
		return vectd(self.x+arg.x,self.y+arg.y)
	
	def __sub__(self,arg):
		return vectd(self.x-arg.x,self.y-arg.y)
	
	def __isub__(self,arg):
		return vectd(self.x-arg.x,self.y-arg.y)
	
	def __abs__(self):
		return hypot(self.x,self.y)
	
	def dot(self,arg):
		return self.x*arg.x+self.y*arg.y
	
	def norm(self):
		a=abs(self)
		if a:
			return vectd(1.0*self.x/a,1.0*self.y/a)
		else:
			return vectd(0,0)

class particle:
	def __init__(self,r,p,v,c):
		self.r=r
		self.p=p
		self.v=v
		self.c=c
	
	def __repr__(self):
		return '''{} particle with
position: {}
velocity: {}
colour(RGB): {}'''.format(('Real' if self.r else 'Ghost'),self.p,self.v,self.c)

class xploder(scene.Scene):
	def setup(self):
		self.background_color=0
		self.show_fps=True
		self.mainview=None
		self.state='setup'
		self.background_color=0
		self.tlabel=None
		self.cdict={'npart': 50, 'Gx': 362, 'Gy': 352, 'g': 9.81, 'cor': 1, 'sigvmu': 0, 'sigthmu': 0, 'resk': 0.01, 'vmu': 1, 'thmu': -1}
		self.g=None
		self.ghostps=None
		self.realps=None
		self.timestamp=None
		self.deltat=0
		self.boundson=True
		self.reson=True
	
	def did_change_size(self):
		resizemenu()
		
	def touch_began(self,touch):
		'''global _timer
		_timer=threading.Timer(.5,scenesizeout,[self])
		_timer.start()'''
	
	def touch_ended(self,touch):
		'''global _timer
		if _timer:
			_timer.cancel()'''

v=ui.load_view('xplodrrr.pyui')
v.name='Xplodrrr Gamma'
_msh=v['menushell']
_hsh=v['hlepshell']
_sc=v['scene'].scene
_timelab=v['timelab']
if max(v.height,v.width)>600: #iPad INVERSED
	_msh.remove_subview(_msh['menu_iphone'])
	_msh['menu_ipad'].name='menu'
else: #iPhone
	_msh.remove_subview(_msh['menu_ipad'])
	_msh['menu_iphone'].name='menu'
	hlis=_hsh['hlepitself']
	hlis.x=0
	hlis.y=25
	hlis.width=v.width
	hlis.content_size=(v.width,2100)
	hlis.flex='wh'
v.present('full_screen')
print(_sc.size)
