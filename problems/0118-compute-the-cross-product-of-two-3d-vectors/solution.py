import numpy as np

def cross_product(a, b):
    c_x = a[1] * b[2] - a[2] * b[1]
    c_y = a[2] * b[0] - a[0] * b[2]
    c_z = a[0] * b[1] - a[1] * b[0]
    
    return [c_x, c_y, c_z]