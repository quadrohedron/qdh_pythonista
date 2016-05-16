import scene, scene_drawing
from math import sqrt, acos, atan2, sin, cos, pi, hypot
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
			wx,wy,wz=list(map(lambda t: t/absw,(wx,wy,wz)))
			sx,sy,sz=gy*wz-gz*wy,gz*wx-gx*wz,gx*wy-gy*wx
		cvert=[[4,4,4],[-4,4,4],[-4,-4,4],[4,-4,4],[4,4,-4],[-4,4,-4],[-4,-4,-4],[4,-4,-4]]
		try:
			wx
		except:
			wx=wy=wz=sx=sy=sz=.5
		ue=(-wx,-wy,-wz)
		un=(sx,sy,sz)
		uu=(-gx,-gy,-gz)
		physvert=[None for i in range(8)]
		for j in range(8):
			i=cvert[j]
			cx=i[0]*ue[0]+i[1]*un[0]+i[2]*uu[0]
			cy=i[0]*ue[1]+i[1]*un[1]+i[2]*uu[1]
			cz=i[0]*ue[2]+i[1]*un[2]+i[2]*uu[2]
			physvert[j]=[cx,cy,cz]
		faces=((2,3,6,7,'#ff6060'),(0,1,4,5,'#a00000'),(0,3,4,7,'#60ff60'),(1,2,5,6,'#00a000'),(0,1,3,2,'#6060ff'),(4,5,7,6,'#0000a0'))
		faceord=sorted([0,1,2,3,4,5],key=lambda t: sum([physvert[n][2] for n in faces[t][:4]]))
		visvert=[]
		D=4*2048*.5/(.61*19.8)
		centx,centy=self.size/2
		for i in physvert:
			x,y,z=i
			rad=D*7/(65-z)
			visvert.append((rad*x+centx,rad*y+centy))
		for i in faceord:
			scene_drawing.fill(faces[i][4])
			scene_drawing.triangle_strip([visvert[j] for j in faces[i][:4]])

	def stop(self):
		stop_updates()

if __name__=='__main__':
	scene.run(quubcam(),scene.PORTRAIT,show_fps=True)
