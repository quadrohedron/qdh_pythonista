import scene, scene_drawing
from math import sqrt, acos, atan2, sin, cos, pi
from motion import *

def magnorm():
	v=get_magnetic_field()
	if v[3]<0:
		return (0,0,0)
	else:
		v=v[:3]
		l=sum(map(lambda x: x**2,v))**.5
		return tuple(map(lambda x: x/l,v))

class quubcam(scene.Scene):
	def setup(self):
		self.background_color=1
		start_updates()
	
	def update(self):
		gx,gy,gz=get_gravity()
		m=magnorm()
		if sum(m):
			mx,my,mz=m
			wx,wy,wz=my*gz-mz*gy,mz*gx-mx*gz,mx*gy-my*gx
			absw=sqrt(sum(map(lambda t: t**2,(wx,wy,wz))))
			for i in wx,wy,wz:
				i/=absw
			sx,sy,sz=gy*wz-gz*wy,gz*wx-gx*wz,gx*wy-gy*wx
			alpha=atan2(sy*gx-sx*gy,wx*gy-wy*gx)
			if alpha<0:
				alpha+=2*pi
			eta=acos(-gz)
			rho=atan2(-gx,-gy)
			if rho<0:
				rho+=2*pi
		cvert=[[4,4,4],[-4,4,4],[4,-4,4],[4,4,-4]]
		lne=1/sqrt(1-gz**2)
		neta=[-gy*lne,gx*lne,0]
		try:
			eta
		except:
			eta=alpha=rho=0
#		quats=[[rho,[0,0,1]],[alpha,[-gx,-gy,-gz]],[eta,neta]]
		physvert=[None for i in range(8)]
		for j in range(4):
			i=cvert[j]
			cx=-i[0]*wx+i[1]*sx-i[2]*gx/2.8
			cy=-i[0]*wy+i[1]*sy-i[2]*gy/2.8
			cz=-i[0]*wz+i[1]*sz-i[2]*gz/2.8
			cvert[j]=[cx,cy,cz]
		inds=((0,1,3,4),(6,7,5,2))
		for i in range(4):
			physvert[inds[0][i]]=cvert[i]
			physvert[inds[1][i]]=list(map(lambda x: -x,cvert[i]))
		faces=((2,3,6,7,'#ff6060'),(0,1,4,5,'#a00000'),(0,3,4,7,'#60ff60'),(1,2,5,6,'#00a000'),(0,1,3,2,'#6060ff'),(4,5,7,6,'#0000a0'))
		faceord=sorted([0,1,2,3,4,5],key=lambda x: sum([physvert[n][2] for n in faces[x][:4]]))
		visvert=[]
		D=4*2048*.5/(.61*19.8)
		centx,centy=self.size/2
		for i in physvert:
			z=i[2]
			rad=D*4*sqrt(48-z**2)/(65-z)
			visvert.append((rad*i[0]+centx,rad*i[1]+centy))
		for i in faceord:
			scene_drawing.fill(faces[i][4])
			scene_drawing.triangle_strip([visvert[j] for j in faces[i][:4]])
	
	def stop(self):
		stop_updates()

if __name__=='__main__':
	scene.run(quubcam(),scene.PORTRAIT,show_fps=True)
