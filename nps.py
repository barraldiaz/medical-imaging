import numpy as np
from scipy import ndimage, misc 
import scipy.interpolate
import matplotlib.pyplot as plt
from PIL import Image



def region(image,xmi,xma,ymi,yma):
    image_cut=image[xmi:xma,ymi:yma]
    #ny,nx=image_cut.shape
    #av=np.average(image_cut)
    #image_cut=image_cut-av
    print('numero de lineas:', image_cut.shape[0], 'longitud de las lineas', image_cut.shape[1])
    return image_cut




def divisor(image,nDiv): #Dividimos la imagen
    ny,nx=image.shape
    yl,xl=ny//nDiv,nx//nDiv
    div=[]
    for i in range(nDiv):
        for j in range(nDiv):
            div.append(image[j*yl:(j+1)*yl,i*xl:(i+1)*xl])
            
    return div
    


def fft2(divisiones): #filtramos la imagen y obtenemos su desviación respecto de la media:
    fft2=[]
    for i in range(len(divisiones)):
        divisiones[i]=-np.log10(divisiones[i]/max(divisiones[i].flatten()))
        divisiones[i]=divisiones[i]-np.average(divisiones[i])
        
    for i in range(len(divisiones)):
        fft2.append((np.abs(np.fft.fft2(divisiones[i]))))#transformada 3d de fourier
    return fft2








