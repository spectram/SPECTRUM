import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from mpdaf.obj import Cube, WCS, WaveCoord
from mpdaf.obj import iter_spe

print("Finish importing packages")

sub_cube = Cube("sub.fits")
print("Finish importing subcube")

cont_cube = Cube("cont.fits")
print("Finish importing cont cube")

line = sub_cube - cont_cube
print("Finish line")

line.write("line_cube.fits")