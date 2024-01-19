import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from mpdaf.obj import Cube, WCS, WaveCoord
from mpdaf.obj import iter_spe
from tqdm import tqdm

full_cube = Cube('DATA/ADP.2017-03-23T15_47_52.027.fits')
full_cube.info()
#got full cube
def continuum_extraction(cube, cont_cube):
    i=0
    for sp, co in tqdm(zip(iter_spe(cube), iter_spe(cont_cube))):
        
        if not sp.data.any():
            #Nan detected
            i+=1
            co[:] = 1
            
            
        else:
            co[:] = sp.poly_spec(5)
    print(i)
    return cube, cont_cube
#starting loop
sub_cube, cont_cube= continuum_extraction(full_cube, \
   full_cube.clone(data_init=np.empty, var_init=np.zeros))
#writing sub cube
sub_cube.write("sub.fits")
#writing sub cube
cont_cube.write("cont.fits")