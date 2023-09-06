#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import module
import arcade
  
# set parameters 
Width= 700
Height=700
Title="SUN"
  
# open window
arcade.open_window(Width, Height, Title)
  
# Set the background color
arcade.set_background_color(arcade.csscolor.BLUE);
  
# Get ready to draw
arcade.start_render();
  


# In[ ]:


# Draw a sun
arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)
  
# Rays to the left, right, up, and down
arcade.draw_line(500, 550, 400, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 600, 550, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 450, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 500, 650, arcade.color.YELLOW, 3)
  
# Diagonal ray
arcade.draw_line(500, 550, 550, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 550, 500, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 600, arcade.color.YELLOW, 3)
arcade.draw_line(500, 550, 450, 500, arcade.color.YELLOW, 3)
  
# Finish drawing
arcade.finish_render()
  
# Keep the window up until someone closes it.
arcade.run()

