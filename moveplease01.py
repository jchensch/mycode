#!/usr/bin/env python3

# Import shutil Module

import shutil

# Import OS Module

import os

# Change to working directory
os.chdir('/home/student/mycode/')

# THe following line will rename a file
shutil.move('raynor.obj', 'ceph_storage/')

# Request a new file name
xname = input('What is the new name for kerrigan.obj? ')

#The following line will rename a file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



