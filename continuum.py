import numpy as np
import matplotlib.pyplot as plt
import astropy.units as u
from mpdaf.obj import Cube, WCS, WaveCoord
#WCS for spatial coordinates and WaveCoord for spectral coordinates

obj1 = Cube('DATA/ADP.2017-03-23T15_47_52.027.fits')
obj1.info()

from mpdaf.obj import iter_spe
from tqdm import tqdm

def continuum_extraction(cube,cont_cube):
    for sp, co in tqdm(zip(iter_spe(cube), iter_spe(cont_cube))):        
        co[:] = sp.poly_spec(5)

#duplicate obj1

small = obj1[:,0:10,0:10] #specify dimensions as needed
small.info()

cont_cube = small.clone(data_init=np.empty, var_init=np.zeros)
cont_cube.info()


continuum_extraction(small,cont_cube)

#subtracting continuum
line1 = small - cont1
plt.figure()
line.sum(axis=0).plot(scale='arcsinh',colobar='v')
line.sum(axis=(1,2)).plot()
