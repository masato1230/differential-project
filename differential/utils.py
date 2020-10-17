import numpy as np
import matplotlib.pyplot as plt

def next_x(equation1,x,dt):
  x += eval(equation1) * dt
  return x