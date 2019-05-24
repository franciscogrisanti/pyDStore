#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:37:53 2019
@author: franciscogrisanti
"""

import os

### find location of the file

def isDS(path):
    """Returns a boolean that indicates if a '.DS_Store' is on the indicated path
    
    isDS(path) 
    """
    try:
        return '.DS_Store' in os.listdir(path)
    except KeyError:
        raise ValueError("Not any '.DS_Store' file on the folder")

def countDS(path):
    """Returns a count that indicates how many a '.DS_Store' 
    is on the indicated directory path
    
    isDS(path) 
    """
    try:
        return os.listdir(path).count(".DS_Store")
    
    except KeyError:
        raise ValueError("Not any '.DS_Store' file on the folder")
    
    
    
def delDS(path):
    """Delete 
    
    isDS(path) 
    """
    try:
        os.remove(path+'.DS_Store')
    except KeyError:
        raise ValueError("Not any '.DS_Store' file on the folder")
        

def delDSrecursively(path):
    """Returns a boolean that indicates if a '.DS_Store' is on the indicated path
    
    isDS(path) 
    """
    try:
        for root in os.walk(path):
            if isDS(path) == True:
                os.remove(root + '.DS_Store')
    except KeyError:
        raise ValueError("Not any '.DS_Store' file on the folder")

def countDSrecursively(path):
    """Returns a count that indicates how many a '.DS_Store' 
    is on the indicated directory and subdirectories path
    
    countDSrecursively(path) ask for the dir path
    """
    try:
        count=0
        for root, dirs, files in os.walk(path):
            print(root)
            if isDS(path) == True:
                count += os.listdir(path).count(".DS_Store")
        return count
    except KeyError:
        raise ValueError("Not any '.DS_Store' file on the folder")
        

