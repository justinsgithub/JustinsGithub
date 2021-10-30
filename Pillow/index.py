#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import ImageColor
from PIL import Image
import os
from PIL import Image, ImageDraw

#redRbga = ImageColor.getcolor('red', 'RGBA')
#chocolateRbga = ImageColor.getcolor('chocolate', 'RGBA')

#print(redRbga)
#print(chocolateRbga)

#boxTupleExample = (3, 1, 9, 6)
#print(boxTupleExample)


#os.chdir('/home/jewell/Downloads/lovelittlelemon-main/public/images/')
#profilePicture = Image.open('profile.jpg')
#print(profilePicture)
#sizeOfProfilePicture = profilePicture.size
#print(sizeOfProfilePicture)
#profilePictureWidth, profilePictureHeight = sizeOfProfilePicture
#print(profilePictureWidth)
#print(profilePictureHeight)

#profilePictureFilename = profilePicture.filename
#print(profilePictureFilename)

#profilePictureFormat = profilePicture.format
#print(profilePictureFormat)

#profilePictureFormatDescription = profilePicture.format_description
#print(profilePictureFormatDescription)

# WORKED profilePicture.save('profile.png')

#os.chdir('/home/jewell/bin/Python3/Pillow/')
#newPurpleImage = Image.new('RGBA', (100, 200), 'purple')
#newPurpleImage.save('purpleImage.png')


#newTransparentImage = Image.new('RGBA', (20, 20))
#newTransparentImage.save('transparentImage.png')


profilePicture = Image.open('profile.jpg')

pP = profilePicture

#pPtopLeftCorner = 0
#pPtopRightCorner = 1536
#pPbottomLeftCorner = 2048
#pPbottomRightCorner = 1536

#newPpLeftSide = 0 # cuts 200 px off left side of profile picture
#newPpTopSide = 200 # cuts 200 px off top of profile picture
#newPpRightSide = 1536 # cuts 335 px off right side of profile picture 
#newPpBottomSide = 2048 # cuts 247 px off bottom of profile picture

#newPpLeftSide = 200 # cuts 200 px off left side of profile picture
#newPpTopSide = 200 # cuts 200 px off top of profile picture
#newPpRightSide = 1201 # cuts 335 px off right side of profile picture 
#newPpBottomSide = 1801 # cuts 247 px off bottom of profile picture

#croppedProfilePicture = profilePicture.crop((200, 200, 1501, 1501))
#croppedProfilePicture.save('croppedProfilePicture.png')
#sizeOfProfilePicture = profilePicture.size
#print(sizeOfProfilePicture)
#profilePictureWidth, profilePictureHeight = sizeOfProfilePicture
#print(profilePictureWidth)
#print(profilePictureHeight)

#newPpLeftSide = 0 # cuts 200 px off left side of profile picture
#newPpTopSide = 200 # cuts 200 px off top of profile picture
#newPpRightSide = 1536 # cuts 335 px off right side of profile picture 
#newPpBottomSide = 2048 # cuts 247 px off bottom of profile picture

croppedProfilePicture = Image.open('croppedProfilePicture.png')
cPPcopy = croppedProfilePicture.copy()
jCrop = cPPcopy.crop((0, 200, 1536, 2048))
zophie = Image.open('zophie.png')
sizeOfZophie = zophie.size
#print(sizeOfZophie)
zophieCopy = zophie.copy()
zophieCrop = zophieCopy.crop((0, 40, 510, 648))

