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

Clone this repo to your local machine using :> git clone https://github.com/farbton/rotateTxtAndJpg

Open cmd and call "rotateTxtAndJpg"__directory

	python rotateTxtandJpg.py -txt txt -out out -ang angle

		txt - source directory of .txt files; default: txt ; required=True
		out - target directory of roteted .txt files; default out
      angle - angle for rotation the bbox (90,180,270)

Example:
--------
		
	without output dir:

		python rotateTxtAndJpg -txt txt -a 90

	with output dir:
			
		python rotateTxtAndJpg -txt txt -out out -a 90
