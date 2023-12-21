import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from mpdaf.obj import Cube, WCS, WaveCoord
from mpdaf.obj import iter_spe
from tqdm import tqdm

def continuum_extraction(cube,cont_cube):
    for sp, co in tqdm(zip(iter_spe(cube), iter_spe(cont_cube))):        
        co[:] = sp.poly_spec(5)
    return cube, cont_cube

datapath='/home/spectram/projects/cartwheel/muse/'
full_cube = Cube(datapath+'ADP.2017-03-23T15:47:52.027.fits')

# small_cube = full_cube[:,60:70,60:70] #specify dimensions as needed

_, full_cont= continuum_extraction(full_cube, \
    full_cube.clone(data_init=np.empty, var_init=np.zeros))

full_line=full_cube-full_cont
full_line.write(datapath+'cw-line.fits')
full_cont.write(datapath+'cw-cont.fits')
