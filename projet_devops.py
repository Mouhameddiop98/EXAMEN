# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:31:37 2023

@author: kalz
"""

import os

def renommer():
    i=0
    url="C:/Users/kalz/Documents/photo"
    for filename in os.listdir(url):
        my_dest= "image" + str(i) + "img"
        source = os.path.join(url, filename)
        os.rename(source,my_dest)
        i+=1

renommer()        
        