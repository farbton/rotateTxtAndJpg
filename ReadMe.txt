RotateTxtAndJpg
=========

Tool for Rotation for images in.jpg-format and 
the Bounding Box in .txt-format for training in darknet

.jpg and .txt must have exact the same filename

Requirements
------------
	numpy==1.18.1
	py-opencv==3.4.2	

Usage
-----

git clone

Open cmd and call "rotateImg"__directory

	python rotateImg.py -txt txt -out out -ang angle

		txt - source directory of .txt files; default: txt
		out - target directory of roteted .txt files; default out
      angle - angle for rotation the bbox (90,180,270)
