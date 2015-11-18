#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cercles` module

:author: Sauvage Célestine ,Danneels Sophie , Soltysiak Samuel

:date: November-December, 2015

Module for cercle.


"""
import math

def create(x,y,r):
    """
    create a circle with center x which is  x-axis  and y-axis and r radius

    :param x: x-axis for the center of circle
    :type x: int or float
    :param y: y-axis for the center of circle
    :type y: int or float
    :param r: radius of  circle
    :type r: int or float
    :return: {'center':(x,y),'radius':r}
    :rtype: a dict
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> get_center(cercle)
    (250,250)
    >>> imag_part (z)
    2
    """
    return {'center':(x,y),'radius':r}

def get_center(cercle):
    """
    return the center (x-axis,y-axis)

    :param cercle: a circle
    :type cercle: a circle ( dict)
    :return: the center  of circle
    :rtype:tuple
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> get_center(cercle)
    (250,250)
    
    """
    return cercle['center']

def get_x_axis(cercle):
    """
    return x-axis
    
    :param cercle: a circle
    :type cercle: a circle ( dict)
    :return: x-axis of center of circle
    :rtype:float or int
    :UC: none
    :Example:
    >>> cercle = create(250,250,100)
    >>> get_x_axis(cercle)
    250
    """
    return get_center(cercle)[0]

def get_y_axis(cercle):
    """
    return y-axis
    
    :param cercle: a circle
    :type cercle: a circle ( dict)
    :return: y-axis of center of circle
    :rtype: float or int
    :UC: none
    :Example:
    >>> cercle = create(250,250,100)
    >>> get_y_axis(cercle)
    250
    """
    return get_center(cercle)[1]

def get_radius(cercle):
    """
    return the radius of center

    :param cercle: a circle
    :type cercle: a circle ( dict)
    :return: the raidus  of circle
    :rtype: int or float
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> get_radius(cercle)
    100
    
    """
    return cercle['radius']

from tkinter import *
fenetre=Tk()
can = Canvas(fenetre,bg='white',height=500,width=500)
can.pack()

def draw_circle(cercle):
    """
    draw a circle

    :param cercle: a circle
    :type cercle: a circle ( dict)
    :return: none
    :rtype: none
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> draw_circle(cercle)
    
    """
    x=get_x_axis(cercle)
    y=get_y_axis(cercle)
    r=get_radius(cercle)
    can.create_oval(x-r, y-r, x+r, y+r) 

def r(cercle,n):
    """
    the radius of the middle circle

    :param cercle: a circle
    :type cercle: a circle ( dict)
    :return: none
    :rtype: none
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> draw_circle(cercle)
    
    """
    return ((get_radius(cercle))*((1-math.sin(math.pi/n))/(1+(math.sin((math.pi/n))))))

def r1(cercle,n):
    """
    the radius of tangent circles

    :param cercle: a circle
    :type cercle: a circle ( dict)
    :return: int
    :rtype: int
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> r1(cercle)
    >>> 46.410161513775456
    
    """
    
    return ((get_radius(cercle)*math.sin(math.pi/n))/(1+(math.sin((math.pi/n)))))

def alpha(i,n):
    """
    get the angle for center of the i th cercle

    :param i: a number
    :type z: a circle ( dict)
    :return: none
    :rtype: none
    :UC: none
    :Example:

    >>> alpha(3)
    >>> 6.283185307179586
    
    """
    return (2*i*math.pi)/n

def cerclenimporte(r,r1,alpha,x,y):
    """
    the position of the i th cercle

    :param cercle: a circle
    :type z: a circle ( dict)
    :return: (a,b)
    :rtype: tuple
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> cerclenimporte(r1(cercle),r(cercle),alpha(3),get_x_axis(cercle),get_y_axis(cercle))
    >>> (303.58983848622455, 250.0)
    
    """
    return (x+(r+r1)*math.cos(alpha),(r+r1)*math.sin(alpha)+y)

def draw_ncercles(cercle,n):
    
    """
    draw n th cercle of circle tangent crown 

    :param cercle: a circle
    :type cercle: a circle ( dict)
    :param n: number of circle 
    :type n: int
    :return: non
    :rtype: non
    :UC: none
    :Example:

    >>> cercle = create(250,250,100)
    >>> quifaittout(cercle,4)
    
    """
    draw_circle(cercle)
    r_petit = r(cercle,n)
    r1_ncercle = r1(cercle,n)
    x_cercle=get_x_axis(cercle)
    y_cercle=get_y_axis(cercle)
    for i in range (1, n+1):
        alph= alpha(i,n)
        new_center=cerclenimporte(r_petit,r1_ncercle,alph,x_cercle,y_cercle)
        new_cercle=create(new_center[0],new_center[1],r1_ncercle)
        draw_circle(new_cercle)
    petit_cercle=create(x_cercle,y_cercle,r_petit)
    draw_circle(petit_cercle)
