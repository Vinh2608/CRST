import os
import sys
from math import floor

name_dataset = 'Dataset2'
f = open('dataset/list/dataset2/dataset2_valid.txt', "w")
root = 'Dataset2'

def searchForMatchingMask(directory,img_name):
    for file in os.listdir(directory):
        if file.startswith(img_name.split('.')[0]):
            return file

train_or_valid = os.listdir(root + '/' + 'Image')

for subfolder in train_or_valid:
    if subfolder == 'valid':
        for file in os.listdir(root + '/' + 'Image' + '/' + subfolder):
            f.write(root + '/' + 'Image' + '/' + subfolder + '/' + file + ' ' + root + '/' + 'Masks' + '/' + subfolder + '/' + searchForMatchingMask(root + '/' + 'Masks' + '/' + subfolder,file) + '\n')
