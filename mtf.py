import numpy as np
from scipy import ndimage, misc 
import scipy.interpolate
import matplotlib.pyplot as plt
from PIL import Image



def region(image,angle,xmi,xma,ymi,yma): #seleccionamos la imagen, el angulo de rotacion y la region que queremos

    image_rotate=ndimage.rotate(image,angle,reshape=True)
    plt.imshow(image_rotate,cmap='gray')
    image_cut=image_rotate[xmi:xma,ymi:yma]
    image_cut=-np.log10((image_cut)/max(image_cut.flatten()))
    print('numero de lineas:', image_cut.shape[0], 'longitud de las lineas', image_cut.shape[1])
    return image_cut



def edgeFunction(image,nInt): #obtenemos los bordes, promediamos e interpolamos
    edgeFnc=np.zeros(image.shape[1])
    for i in range(image.shape[1]):
        edgeFnc[i]=np.average(image[:,i].flatten())
    x_new=np.linspace(0,len(edgeFnc)-1,nInt)
    x=np.linspace(0,len(edgeFnc)-1,len(edgeFnc))
    interp=scipy.interpolate.interp1d(x,edgeFnc,kind='cubic')
    edgeFnc_int=interp(x_new)
    return edgeFnc_int,x_new
    
    
def LSF(edgeFnc): #derivamos
    lsf=np.abs(np.diff(edgeFnc))    
    axis=np.linspace(0,len(lsf)-1,len(lsf))
    return   lsf,axis



def MTF(lsf): #obtenemos la transformada de fourier
    mtf_aux=np.abs(np.fft.fft(lsf))    
    return mtf_aux

        


