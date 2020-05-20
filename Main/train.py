from math import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def cilinder():
	R = 0.5

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, -0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

	glBegin(GL_QUAD_STRIP)

	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, 0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), 0.5)

	glEnd()

def conus():
	R = 0.5

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, -0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

	glBegin(GL_TRIANGLE_FAN)

	glVertex3d( 0,  0, 0.5)
	for i in range(21):
		glVertex3d(R * cos(2*pi*i/20), \
			R * sin(2*pi*i/20), -0.5)

	glEnd()

def sphere():
	R = 0.5

	for j in range(-9,9):
		glBegin(GL_QUAD_STRIP)

		for i in range(21):
			glVertex3d(R * cos(pi*j/18) * cos(2*pi*i/20), \
				R * cos(pi*j/18) * sin(2*pi*i/20), \
				R * sin(pi*j/18))
			glVertex3d(R * cos(pi*(j+1)/18) * cos(2*pi*i/20), \
				R * cos(pi*(j+1)/18) * sin(2*pi*i/20), \
				R * sin(pi*(j+1)/18))

		glEnd()

def thor():
	R = 0.5
	R2 = R * 0.3

	for i in range(20):
		glBegin(GL_QUAD_STRIP)

		for j in range(21):
			glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*i/20), \
				(R + R2 * cos(2*pi*j/20)) * sin(2*pi*i/20), \
				R2 * sin(2*pi*j/20))
			glVertex3d((R + R2 * cos(2*pi*j/20)) * cos(2*pi*(i+1)/20), \
				(R + R2 * cos(2*pi*j/20)) * sin(2*pi*(i+1)/20), \
				R2 * sin(2*pi*j/20))

		glEnd()

def cube():
	glBegin(GL_QUADS)

	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d(-0.5,  0.5, 0.5)
	glVertex3d(-0.5, -0.5, 0.5)
	glVertex3d( 0.5, -0.5, 0.5)
	
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	
	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	glVertex3d( 0.5, -0.5, 0.5)

	glVertex3d(-0.5,  0.5, 0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5, 0.5)

	glVertex3d( 0.5,  0.5, 0.5)
	glVertex3d( 0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5,-0.5)
	glVertex3d(-0.5,  0.5, 0.5)

	glVertex3d( 0.5, -0.5, 0.5)
	glVertex3d( 0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5,-0.5)
	glVertex3d(-0.5, -0.5, 0.5)

	glEnd()

# Процедура рисования
def train():
        #Osnova
	glPushMatrix()
	glColor3f(1, 0,0)
	glTranslated(0, 0, -0.3)
	glRotated(90,0,1,0)
	glScaled(0.5,0.5,1)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(1, 0.5,0)
	glTranslated(-0.55,0,-0.3)
	glRotated(-90,0,1,0)
	glScaled(0.5,0.5,0.1)
	conus()
	glPopMatrix()

	glPushMatrix()
	glColor3f(1, 1,0)
	glTranslated(0.5, 0, 0)
	glScaled(0.5,0.7,0.7)
	cube()
	glPopMatrix()

        #Balki
	glPushMatrix()
	glColor3f(0, 0,0)
	glTranslated(0.25, 0, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.07,0.07,0.5)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0, 0,0)
	glTranslated(-0.35, 0, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.07,0.07,0.5)
	cilinder()
	glPopMatrix()
	
	#Kolesa
	glPushMatrix()
	glColor3f(0, 0,0.4)
	glTranslated(-0.35, 0.25, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.3,0.3,0.05)
	cilinder()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0, 0,0.4)
	glTranslated(0.25, 0.25, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.3,0.3,0.05)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0, 0,0.4)
	glTranslated(-0.35, -0.25, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.3,0.3,0.05)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0, 0,0.4)
	glTranslated(0.25, -0.25, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.3,0.3,0.05)
	cilinder()
	glPopMatrix()

	#Pimpochki
	glPushMatrix()
	glColor3f(0, 0,1)
	glTranslated(-0.35, 0.3, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.07,0.07,0.02)
	cilinder()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0, 0,1)
	glTranslated(0.25, 0.3, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.07,0.07,0.02)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0, 0,1)
	glTranslated(-0.35, -0.3, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.07,0.07,0.02)
	cilinder()
	glPopMatrix()
	
	glPushMatrix()
	glColor3f(0, 0,1)
	glTranslated(0.25, -0.3, -0.5)
	glRotated(90,1,0,0)
	glScaled(0.07,0.07,0.02)
	cilinder()
	glPopMatrix()

	#Fonar'
	glPushMatrix()
	glColor3f(0, 0.4,0)
	glTranslated(-0.37, 0, 0.05)
	glScaled(0.15,0.15,0.15)
	cube()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.9,0.9,0.9)
	glTranslated(-0.47, 0, 0.05)
	glRotated(90,0,1,0)
	glScaled(0.25,0.25,0.25)
	conus()
	glPopMatrix()

	#Truba
	glPushMatrix()
	glColor3f(0,0,1)
	glTranslated(-0.1, 0, 0.1)
	glScaled(0.2,0.2,0.3)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(1,0.2,0.2)
	glTranslated(-0.1, 0, 0.29)
	glScaled(0.27,0.27,0.07)
	cilinder()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0,0,0)
	glTranslated(-0.1, 0, 0.35)
	glScaled(0.1,0.1,0.15)
	thor()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.2,0.2,0.2)
	glTranslated(-0.1, 0, 0.4)
	glScaled(0.15,0.15,0.15)
	thor()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.3,0.3,0.3)
	glTranslated(-0.1, 0, 0.45)
	glScaled(0.2,0.2,0.15)
	thor()
	glPopMatrix()

	glPushMatrix()
	glColor3f(0.4,0.4,0.4)
	glTranslated(-0.1, 0, 0.5)
	glScaled(0.25,0.25,0.15)
	thor()
	glPopMatrix()
