# Created by: Jacob Liberty 
# Created on: September 25 2017
# Created for: ICS3U
# This program calculates the circumference of a circle 

def calculate_touch_up_inside(sender):
    # calculate circumference
    
    # constants
    PI = 3.14
    
    # input
    radius = int(view['radius_textbox'].text)
    
    # process
    circumference = 2 * PI * radius
    
    # output
    view['circumference_label'].text = 'The circumference is: ' + str(circumference) + ' cm'

import ui

view = ui.load_view()
view.present('sheet')
