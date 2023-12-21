import numpy as np
from mpdaf.obj import Cube, Spectrum

datapath='/home/spectram/projects/cartwheel/muse/'
full_cube = Cube(datapath+'ADP.2017-03-23T15:47:52.027.fits')

full_cube.info()
full_cont = full_cube.loop_spe_multiprocessing(f=Spectrum.poly_spec, deg=5)
full_line=full_cube-full_cont

full_line.write(datapath+'cw-line.fits')
full_cont.write(datapath+'cw-cont.fits')