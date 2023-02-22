# PicoSystem 2D-Plotter
import math
import time

class Plotter ():
	def __init__ (self):
		pass
	
	""" Clears the screen for plotting, takes optional colour to use """
	def clear (self, colour=[3, 3, 3]):
		pen (colour[0], colour[1], colour[2])
		clear ()
		flip ()
		
		pen (10, 10, 10)
		for i in range (0, 120, 10):
			hline (0, i, 120)
			vline (i, 0, 120)
		
		# Pixel 120 is outside the screen, so 119 is the last one
		# This is weird/clunky setup
		hline (0, 119, 120)
		vline (119, 0, 120)
		
		# Make the X- and Y-Axis
		pen (15, 15, 15)
		line (0, 60, 120, 60)
		line (60, 0, 60, 120)
		
		flip ()
	
	""" Plot a given function, doesn't work """
	def plot (self, f, rgb = [15, 0, 0], f_domain = [-10, 10], r_range = [-10, 10], speed = 0):
		origo_offset = 60
		
		x_list = range (120)
		for x in x_list:
			y_list.append (f(x))
		
		y_list = list (map (f, x_list[0:]))
		point = []
		
		pen (rgb[0], rgb[1], rgb[2])
		
		for i in range (0, 119):
			point.append ([x_list[i], y_list[i]])
		
			line (i, origo_offset - point[i], i+1, origo_offset - point[i+1])
			flip ()
	
	""" One that works """
	def function (self, f, rgb, f_domain = [-60, 60], f_range = [0, 120], Yscale = 1.0, speed = 0):
		origin = 60
		x_pos = [0, 0] # Declaring it for later use
		y_pos = [0, 0] # Declaring it for later use
		# We have 120 pixels to work with, so scale it by the domain
		delta_step = (f_domain[1] - f_domain[0]) / (2 * origin)
		
		# Change the colour on the pen
		pen (rgb[0], rgb[1], rgb[2])
		
		# Make the graph, line by line (point by point)
		# First all the points, then connect them
		for i in range (0, 2*origin, 1):
			x_pos[0] = i - origin
			x_pos[1] = x_pos[0] + 1
			y_pos[0] = f(x_pos[0] * delta_step) * Yscale + origin
			y_pos[1] = f(x_pos[1] * delta_step) * Yscale + origin
			
			line (int (x_pos[0] + origin), int (y_pos[0]), int (x_pos[1] + origin), int (y_pos[1]))
			
			# Do you want to watch it draw line by line?
			if speed != 0:
				time.sleep_ms (speed)
				flip ()
		flip ()


scrn = Plotter ()
scrn.clear ()

"""
	This is the Newest of plots functions, and it works.
"""
def new_plot (f, rgb=[15, 0, 0], f_domain=[-60, 60], f_range=[-60, 60]):
	SCRN_LENGTH = 120
	
	delta_step = (f_domain[1] - f_domain[0]) / SCRN_LENGTH
	Y_SCALE = SCRN_LENGTH / (f_range[1] - f_range[0])
	#x_values = [i * delta_step for i in range(SCRN_LENGTH)]
	#y_values = [f(x) for x in x_values]
	
	pen(rgb[0], rgb[1], rgb[2])
	for i in range (SCRN_LENGTH):
		x = [f_domain[0] + i * delta_step, f_domain[0] + (i + 1) * delta_step]
		y = [(SCRN_LENGTH / 2) - int(f(x[0]) * Y_SCALE), (SCRN_LENGTH / 2) - int(f(x[1]) * Y_SCALE)]
		
		line (i, y[0], i+1, y[1])
	flip ()

beats = lambda x: 2 * math.sin ((10 + 11) * x / 2) * math.cos ((10-11) * x / 2)
scrn.function (beats, [0, 15, 0], [-2*math.pi, 2*math.pi], Yscale = 20.0, speed = 1)

