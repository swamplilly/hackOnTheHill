
import pygame, Buttons
import Tkinter
from pygame.locals import *
from pygame.color import Color

(width, height) = (650,480)
background_color = Color("pink")
text_color = Color("black")

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("HACK Sim")
screen.fill(background_color)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


# #Initialize pygame
# pygame.init()

# class Button_Example:
#     def __init__(self):
#         self.main()
    
#     #Create a display
#     def display(self):
#         self.screen = pygame.display.set_mode((650,370),0,32)
#         pygame.display.set_caption("Buttons.py - example")

#     #Update the display and show the button
#     def update_display(self):
#         background_color = Color("pink")
#         text_color = (255,255,255)
#         self.screen.fill(background_color)
#         #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
#         self.Button1.create_button(self.screen, (107,142,35), 225, 135, 200,    100,    0,        "Example", text_color)
#         pygame.display.flip()


#     #Run the loop
#     def main(self):
#         self.Button1 = Buttons.Button()
#         self.display()
#         while True:
#             self.update_display()
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                 elif event.type == MOUSEBUTTONDOWN:
#                     if self.Button1.pressed(pygame.mouse.get_pos()):
#                         print "Give me a command!"

# if __name__ == '__main__':
#     obj = Button_Example()
