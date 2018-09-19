import keyboard
import time
import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import pyautogui as gui
import os
import time

# fashion_mnist = keras.datasets.fashion_mnist

# (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()


# f = open("v.txt", "r")

cats_dir="./cats_r/"
dogs_dir="./dogs_r/"
cats = os.listdir(cats_dir)
dogs = os.listdir(dogs_dir)


# cats= os.listdir(cats_dir)
print("ready")

keyboard.wait('esc')
button= gui.locateOnScreen('cap_but.png')
buttonx, buttony= gui.center(button)
gui.click(buttonx,buttony)
time.sleep(1.2)

c_banner= gui.locateOnScreen('cats_banner.png')
d_banner= gui.locateOnScreen('dogs_banner.png')
print(c_banner)
if c_banner:
	print("im in")
	for pic in cats:
		imgl = gui.locateOnScreen(cats_dir+pic)
		if imgl:
			xloc, yloc = gui.center(imgl)
			gui.click(xloc,yloc)

