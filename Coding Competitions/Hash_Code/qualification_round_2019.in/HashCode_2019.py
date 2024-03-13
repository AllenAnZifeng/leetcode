#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@author: Allen(Zifeng) An
@course: 
@contact: anz8@mcmaster.ca
@file: HashCode_2019.py
@time: 2020/2/11 18:15
'''

#

from typing import List
from random import shuffle

class Picture():
    def __init__(self,orientation:str,number:str,tags:list, id:int):
        self.orientation = orientation
        self.number = number
        self.tags=tags
        self.id=id

class Slideshow():
    def __init__(self,pic_list:List[Picture]):
        self.picIDs = [ pic.id for pic in pic_list]
        if len(pic_list)==1:
            self.tags = set(pic_list[0].tags)
        elif len(pic_list)==2:
            self.tags= (set(pic_list[0].tags).union(set(pic_list[1].tags)))

def score(slideshow1:Slideshow,slideshow2:Slideshow)->int:
    return min(len(slideshow1.tags-slideshow1.tags.intersection(slideshow2.tags)),
               len(slideshow1.tags.intersection(slideshow2.tags)),
               len(slideshow2.tags-slideshow2.tags.intersection(slideshow1.tags))
               )



if __name__ == '__main__':
    with open('b_lovely_landscapes.txt', 'r') as f:
        file = f.read()
    file=file.split('\n')
    file.pop(-1) # remove white space in the end
    # print(file)
    picturesH=[]
    picturesV=[]
    slideshows=[]
    res=0
    for i in range(1,len(file)):
        if file[i][0]=='H':
            picturesH.append(Picture(file[i][0],file[i][2],file[i][4:].split(),i-1))
        else:
            picturesV.append(Picture(file[i][0], file[i][2], file[i][4:].split(), i - 1))
    # for pic in picturesH:
    #     print(pic.orientation,pic.number,pic.tags,pic.id)
    # for pic in picturesV:
    #     print(pic.orientation, pic.number, pic.tags, pic.id)

    for pic in picturesH:
        slideshows.append(Slideshow([pic]))

    slideshows.sort(key=lambda slides:len(slides.tags),reverse=True)
    print([s.tags for s in slideshows])
    # shuffle(slideshows)

    for i in range(len(slideshows)-1):
        res+=score(slideshows[i],slideshows[i+1])
    print(res)

