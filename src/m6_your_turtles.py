"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Shane Saylor.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

jeff=rg.SimpleTurtle('turtle')
jeff.pen=rg.Pen('purple',7)
jeff.speed=7

size=150

for k in range(12):
    jeff.draw_regular_polygon(5,size)
    jeff.pen_up()
    jeff.right(30)
    jeff.forward(10)
    jeff.pen_down()

nathan=rg.SimpleTurtle('turtle')
nathan.pen=rg.Pen('light green',4)
nathan.speed=10

for k in range(57):
    nathan.left(105)
    nathan.forward(100)

window.close_on_mouse_click()