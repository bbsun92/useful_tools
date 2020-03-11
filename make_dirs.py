#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:55:24 2020

@author: Benjamin Sun (bbsun92@outlook.com)
"""

## Creates folder structure for projects
import os
import argparse
import subprocess


## initiate parser
parser = argparse.ArgumentParser()

## add options
parser.add_argument('rtpath')
parser.add_argument('-t','--tree', action='store_true')

## parse arguments
args = parser.parse_args()

# specify where you want to out folder from option arguments
dir_path = args.rtpath

if os.path.exists(dir_path):
    print('Directory {} already exists'.format(dir_path))
else:
    os.makedirs(dir_path)
    
    # create sub-directories
    subdirs = {'admin':['drafts', 'internal', 'external', 'formal'], 
               'analysis':['input', 'interim', 'scripts', 'output'],
               'dissemination':['presentations','reports']}
    
    for lv1 in subdirs:
        for lv2 in subdirs[lv1]: 
            os.makedirs(os.path.join(dir_path, lv1, lv2), exist_ok=True)

# display tree structure if -t is true
if args.tree:
    subprocess.run(["tree",args.rtpath])



