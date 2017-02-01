#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    sides = [a,b,c]
    second_side = [b,c,a]
    third_side = [c,a,b]
    for x in range(0,3):
        if sides[x] <= 0:
            raise TriangleError("Side must be non-zero or positive")
        
        if sides[x] + second_side[x] <= third_side[x]:
            raise TriangleError("Sides "+str(a)+","+str(b)+","+str(c)+" cannot construct a triangle")
    
    distinct_sides = len(set(sides))
    
    if distinct_sides == 1:
        return "equilateral"
    elif distinct_sides == 2:
        return "isosceles"
    else:
        return "scalene"
        
# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
