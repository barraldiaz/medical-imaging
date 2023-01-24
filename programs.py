import numpy as np
import os
from PIL import Image

def readDat(dat,chanels):
    file=np.fromfile(dat,dtype='int16')
    columns,rows=chanels,int(os.stat(dat).st_size/2/chanels)
    file=np.reshape(file,(rows,columns))
    return file


    

