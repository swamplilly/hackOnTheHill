#!/usr/bin/python

import pygame, Tkinter, tkMessageBox
from pygame.locals import *
from pygame.color import Color
from Tkinter import *

class App:
	def __init__(self,top):
		top.minsize(width=450, height=650)
		top.configure(background="pink")
		frame = Frame(top)

		button_frame = Frame(top)
		self.start = Button(button_frame,text="Start",command=self.start).pack(side=BOTTOM)

		button_frame.pack(side=BOTTOM)
		frame.pack(side=LEFT)


	def start(self):
		print "Hello"

top = Tk()

app = App(top)

top.mainloop()
top.destroy()