#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 23:31:48 2017

@author: josebarretto
"""

import math # enables the use of the tan function and the pi definition

def polysum(n, s):
    """
    this function calculates the sum of the area and the square of the perimeter
    of a regular polygon with n sides of lenght s
    """
    
    area = (0.25*n*(s**2))/(math.tan(math.pi/n)) # calculates the area of the polygon
    per = n*s # calculates the perimeter of the polygon
    
    return round(per**2 + area, 4) #returns the desired sum rounded up to four digits