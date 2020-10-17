import numpy as np
import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse


def next_x(equation1,x,dt):
  x += eval(equation1) * dt
  return x

def create_graph(x_list,t_list):
  plt.plot(t_list, x_list, label="x")
  plt.xlabel('t')
  plt.ylabel('x')
  plt.savefig('figure01.jpg')
  print(1)