#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#~ @require apt-get install python-imaging

from PIL import Image
from PIL import ImageCms
import os
import sys
import glob
import gc
import time

gc.enable()
gc.collect()

SRGB_PROFILE='sRGB.icm'
CMYK_PROFILE='ISOwebcoated.icc'

images = (glob.glob('*.jpg'))
for i in images:
    gc.collect()
    im = Image.open(i)
    
    #~ new_height = 1200
    #~ new_width  = new_height * width / height
    
    #~ new_width  = 1200
    #~ new_height = new_width * height / width 
    
    #~ height = im.size[0]
    #~ width = im.size[1]
    

    if im.mode is not 'RGB':
        print(i+' is '+im.mode)
        popa = ImageCms.getOpenProfile(SRGB_PROFILE)
        popa2 = ImageCms.getOpenProfile(CMYK_PROFILE)
        trans = ImageCms.buildTransform(popa2,popa,'CMYK','RGB')
        convo = ImageCms.applyTransform(im,trans)
        #~ convo = convo.resize([new_height, new_width] , Image.ANTIALIAS)
        #~ cdata = list(convo.getdata())
        #~ nimage = Image.new('RGB',im.size)
        #~ nimage.putdata(cdata)
        #~ nimage.save('ready/'+i, 'JPEG', quality=95, dpi=(72,72))
        convo.save('ready/'+i, 'JPEG', quality=100, dpi=(72,72))
        convo.close()
        #~ time.sleep(5)
    else:
        print(i+' is '+im.mode)
        #~ cdata = list(im.getdata())
        #~ nimage = Image.new('RGB',im.size)
        #~ nimage.putdata(cdata)
        #~ nimage.save('ready/'+i, 'JPEG', quality=95, dpi=(72,72))
        #~ im = im.resize([new_height, new_width] , Image.ANTIALIAS)
        im.save('ready/'+i, 'JPEG', quality=100, dpi=(72,72))
        #~ nimage.close()
        #~ time.sleep(5)
    im.close()
