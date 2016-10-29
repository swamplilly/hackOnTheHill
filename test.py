################################################################################
#
#  IMPORT
#
################################################################################

import os, sys
from os.path import dirname as d
sys.path.insert(1, d(d(os.path.abspath(sys.argv[0]))))

import pygame
pygame.init()
from pygame.color import Color
from pygame.locals import *

from math import pi
from albow.widget import Widget
from albow.controls import Label, Button, Image, AttrRef, \
  RadioButton, ValueDisplay
from albow.layout import Row, Column, Grid
from albow.fields import TextField, FloatField
from albow.shell import Shell
from albow.screen import Screen
from albow.text_screen import TextScreen
from albow.resource import get_font, get_image
from albow.grid_view import GridView
from albow.palette_view import PaletteView
from albow.image_array import get_image_array
from albow.dialogs import alert, ask
from albow.file_dialogs import \
  request_old_filename, request_new_filename, look_for_file_or_directory
from albow.tab_panel import TabPanel
from albow.table_view import TableView, TableColumn

screen_size = (640,480)
flags = 0
frame_time = 50

class Start(Screen):
  def __init__(self,shell):
    Screen.__init__(self,shell)
    self.shell = shell
    f1 = get_font(24,"VeraBd.ttf")
    title = Label("Test Demo", font = f1)
    def screen_button(text,screen):
      return Button(text,action=lambda:shell.show_screen(screen))
    start_button = screen_button("Start",shell.button1)
    start_button.enabled_bg_color = Color("green")
    quit_button = Button("Quit",shell.quit)
    quit_button.enabled_bg_color = Color("red")
    menu = Column([
      start_button,
      quit_button
    ], align='l')
    contents = Column([
      title,
      menu,
    ], align='l', spacing=20)
    self.add_centered(contents)

  def show_buttons(self):
    self.shell.show_screen(self.button1)

  def quit(self):
    sys.exit(0)


class TestShell(Shell):
  def __init__(self,display):
    Shell.__init__(self,display)
    self.create_screens()
    self.menu_screen = Start(self)
    self.set_timer(frame_time)
    self.show_menu()
    self.create_screens()

  def create_screens(self):
    self.button1 = TextScreen(self, "demo_text.txt")
    self.test_screen = Start(self)

  def show_menu(self):
    self.show_screen(self.menu_screen)






def main():
  display = pygame.display.set_mode(screen_size,flags)
  shell = TestShell(display)
  shell.run()

main()

# class MenuScreen(Screen):
#   def __init__(self,shell):
#     Screen.__init__(self,shell)
#       title = Label("Welcome")
#       def screen_button(text,screen):
#         return Button(text,action = lambda: shell.show_screen(screen))
#       menu = Column([
#         screen_button("Start",shell.start)
#       ], align = 'l')
#       contents = Column([
#         title,
#         menu
#       ], align = 'l',spacing = 20)
#       self.add_centered(contents)

#   def show_start_screen(self):
#     self.shell.show_screen(self.start)

#   def quit(self):
#     sys.exit(0)

# class Start(Screen):

#   def __init__(self,shell):
#     Screen.__init__(self,shell)
#     lbl = Label("hi")
#     lbl.rect.width = 400
#     lbl.rect.topleft = (200,350)
#     self.lbl = lbl
#     self.add(lbl)

# class TestShell(Shell):

#   def __init__(self,display):
#     Shell.__init__(self,display)
#     self.create_screens()
#     self.menu_screen = MenuScreen(self)
#     self.show_menu()

#     def create_screens(self):
#       self.start = 

# def main():
#   display = pygame.display.set_mode(screen_size,flags)
#   shell = TestShell(display)
#   shell.run()

# main()