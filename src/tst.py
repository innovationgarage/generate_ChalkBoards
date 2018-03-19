
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as spim
import cv2
#%pylab inline
import os
from drawing import *
from board import *
#np.random.seed(42)


# In[2]:


data_path = '../data/'
data_type = 'Numpy bitmap files'


# In[3]:


circles = np.load(os.path.join(data_path, 'circle.npy'))
envelopes = np.load(os.path.join(data_path, 'envelope.npy'))
hexagons = np.load(os.path.join(data_path, 'hexagon.npy'))
lines = np.load(os.path.join(data_path, 'line.npy'))
octagons = np.load(os.path.join(data_path, 'octagon.npy'))
squares = np.load(os.path.join(data_path, 'square.npy'))
zigzags = np.load(os.path.join(data_path, 'zigzag.npy'))
triangles = np.load(os.path.join(data_path, 'triangle.npy'))


# In[4]:


data = [
    {'dataset': circles, 'label': 'circle'},
    {'dataset': envelopes, 'label': 'envelope'},
    {'dataset': hexagons, 'label': 'hexagon'},
    {'dataset': lines, 'label': 'line'},
    {'dataset': octagons, 'label': 'octagon'},
    {'dataset': squares, 'label': 'square'},
    {'dataset': zigzags, 'label': 'zigzag'},
    {'dataset': triangles, 'label': 'triangle'}
]


# In[5]:


size = 300
drawing_types = np.random.randint(0, len(data), size)
drawing_indices = [np.random.randint(0, len(data[x]['dataset']), 1)[0] for x in drawing_types]
#print(drawing_types)
#print(drawing_indices)
#initialize a board
width = 4640
height = 3480
bgcolor = 255
brd = board(width, height, bgcolor)


# In[6]:


for (t,i) in zip(drawing_types, drawing_indices):
    dataset = data[t]['dataset']
    label = data[t]['label']
    #print(label, i)
    array = data[t]['dataset'][i]
    dr = drawing(label, i, array)
    dr.rotate(0.8)
    dr.scale(1.0, 10, 3)
    brd.add_drawing(dr, np.random.randint(0, high=width), np.random.randint(0, high=height))
brd.save('board.jpg')
brd.label('label.csv')


# In[8]:

# plt.figure(figsize=(25,25))
# brd.show()
# plt.show()

brd.change_bgcolor(200.)

plt.figure(figsize=(25,25))
brd.save('board_gray.jpg')
brd.show()
plt.show()


