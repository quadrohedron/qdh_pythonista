from scene import *
from motion import *
from math import atan2, sin, cos, pi, floor, acos, sqrt, hypot
import time

PU=PN=PE=VU=VN=VE=0
TIMESTAMP=time.time()
AU=[]
VBARS=None
UA=[]

def mau():
	return sum(AU)/len(AU)

def mua(*args):
	if args:
		U=args[0]
		l=len(U)
		x=sum([i[0] for i in U])/l
		y=sum([i[1] for i in U])/l
		z=sum([i[2] for i in U])/l
	else:
		l=len(UA)
		x=sum([i[0] for i in UA])/l
		y=sum([i[1] for i in UA])/l
		z=sum([i[2] for i in UA])/l
	return x,y,z

def magnorm():
	v=get_magnetic_field()
	if v[3]<0:
		return (0,0,0)
	else:
		v=v[:3]
		l=sum(map(lambda x: x**2,v))**.5
		return tuple(map(lambda x: x/l,v))

def rezero(sender):
	global VBARS
	if not VBARS:
		if sender:
			VBARS=sender.items['xbar']
	global PU,PN,PE,VU,VN,VE
	PU=PN=PE=VU=VN=VE=0
	print('zero')
	return 0

# g=eta/(2*pi),alpha/(2*pi),rho/(2*pi)

class vbars(Scene):
	def setup(self):
		self.background_color='black'
		self.items={
			'xbar':ShapeNode(ui.Path.rect(0,0,36,200),'red'),
			'ybar':ShapeNode(ui.Path.rect(0,0,36,200),'red'),
			'zbar':ShapeNode(ui.Path.rect(0,0,36,200),'red'),
			'0mark':LabelNode("0",font=('Kailasa',25),color=1),
			'+mark':LabelNode("+2m/s",font=('Kailasa',15),color=1),
			'-mark':LabelNode("-2m/s",font=('Kailasa',15),color=1),
			'xmark':LabelNode("au",font=('Kailasa',30),color=1),
			'ymark':LabelNode("an",font=('Kailasa',30),color=1),
			'zmark':LabelNode("ae",font=('Kailasa',30),color=1),
			'lines':[ShapeNode(ui.Path.rect(0,0,120,2),'white') for i in range(9)]
		}
		rezero(self)
		for i in self.items:
			if i=='lines':
				for j in self.items[i]:
					j.anchor_point=(.5,.5)
					self.add_child(j)
			else:
				if not 'bar' in i:
					self.items[i].anchor_point=(.5,.5)
				self.add_child(self.items[i])
		for i in range(9):
			self.items['lines'][i].position=(95,45+50*i)
		for i in range(3):
			key=chr(120+i)
			self.items[key+'bar'].anchor_point=(.5,0)
			self.items[key+'bar'].position=(56+39*i,245)
			self.items[key+'mark'].position=(56+39*i,25)
		k=['-','0','+']
		for i in range(3):
			self.items[k[i]+'mark'].position=(18,54+190*i)
	
	def update(self):
		global VU,VN,VE
		g=VU,VN,VE
		for i in range(3):
			self.items[chr(120+i)+'bar'].y_scale=g[i]

class abars(Scene):
	def setup(self):
		start_updates()
		global AU,UA
		AU=[]
		UA=[]
		rezero(None)
		self.background_color='black'
		self.items={
			'xbar':ShapeNode(ui.Path.rect(0,0,36,200),'red'),
			'ybar':ShapeNode(ui.Path.rect(0,0,36,200),'red'),
			'zbar':ShapeNode(ui.Path.rect(0,0,36,200),'red'),
			'0mark':LabelNode("0",font=('Kailasa',25),color=1),
			'+mark':LabelNode("+g",font=('Kailasa',22),color=1),
			'-mark':LabelNode("-g",font=('Kailasa',22),color=1),
			'xmark':LabelNode("au",font=('Kailasa',30),color=1),
			'ymark':LabelNode("an",font=('Kailasa',30),color=1),
			'zmark':LabelNode("ae",font=('Kailasa',30),color=1),
			'lines':[ShapeNode(ui.Path.rect(0,0,120,2),'white') for i in range(9)]
		}
		for i in self.items:
			if i=='lines':
				for j in self.items[i]:
					j.anchor_point=(.5,.5)
					self.add_child(j)
			else:
				if not 'bar' in i:
					self.items[i].anchor_point=(.5,.5)
				self.add_child(self.items[i])
		for i in range(9):
			self.items['lines'][i].position=(95,45+50*i)
		for i in range(3):
			key=chr(120+i)
			self.items[key+'bar'].anchor_point=(.5,0)
			self.items[key+'bar'].position=(56+39*i,245)
			self.items[key+'mark'].position=(56+39*i,25)
		k=['-','0','+']
		for i in range(3):
			self.items[k[i]+'mark'].position=(18,54+190*i)
	
	def update(self):
		global TIMESTAMP,VU,VN,VE,PU,PN,PE
		T=time.time()
		DT=T-TIMESTAMP
		TIMESTAMP=T
		x,y,z=get_gravity()
		m=magnorm()
		if sum(m):
			c,d,e=m
			wx,wy,wz=d*z-e*y,e*x-c*z,c*y-d*x
			absw=sqrt(sum(map(lambda t: t**2,(wx,wy,wz))))
			for i in wx,wy,wz:
				i/=absw
			sx,sy=y*wz-z*wy,z*wx-x*wz
			alpha=atan2(sy*x-sx*y,wx*y-wy*x)
			if alpha<0:
				alpha+=2*pi
			eta=acos(-z)
			rho=atan2(-x,-y)
			if rho<0:
				rho+=2*pi
			ax,ay,az=get_user_acceleration()
			au=ax*x+ay*y+az*z
			an=0
			ae=0
			PU+=DT*VU
			PN+=DT*VN
			PE+=DT*VE
			VU+=DT*au
			VN+=DT*an
			VE+=DT*ae
			g=au,an,ae
			global AU,UA
			if len(UA)<8191:
				UA.append((ax,ay,az))
			elif len(UA)==8191:
				UA.append((ax,ay,az))
				print('                D O N E')
			AU.append(au)
			for i in range(3):
				self.items[chr(120+i)+'bar'].y_scale=g[i]
	
	def stop(self):
		stop_updates()

v=ui.load_view('igyro.pyui')
v.present('sheet')
