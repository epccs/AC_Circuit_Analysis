# This is a partial program to run interactively from the command line, e.g.
# linux: python3 -i polar.py
# win: python -i polar.py

import numpy

# Euler's Formula for Polar (magnitude, degrees) to Rectangular (x, yj) on complex plane.
def Pd2R(A, deg):
    return A*( numpy.cos(numpy.deg2rad(deg)) + 1.0j*numpy.sin(numpy.deg2rad(deg)) )

# Display Polar format 
def R2Pd(x):
    string2return = ('{:0.3g}'.format(numpy.abs(x)) + "<" + '{:0.3g}'.format(numpy.rad2deg(numpy.angle(x))) + "deg")
    return string2return

# Display Polar format with unit
def R2PdU(x, unit):
    string2return = ('{:0.3g}'.format(numpy.abs(x)) + unit + "<" + '{:0.3g}'.format(numpy.rad2deg(numpy.angle(x))) + "deg")
    return string2return