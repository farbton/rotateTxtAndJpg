# RotateTxtAndJpg

Tool for Rotation for images in.jpg-format and 
the Bounding Box in .txt-format for training in darknet

## Getting Started

Clone this repo on your local machine using: 
	
	git clone https://github.com/farbton/rotateTxtAndJpg


### Requirements

	numpy==1.18.1
	py-opencv==3.4.2


### Usage

txt and jpg must hast the same name

file1.txt and file1.jpg

Open cmd and call "rotateTxtAndJpg"__directory

```
python rotateTxtandJpg.py -txt txt -out out -ang angle
```


#### Example


without output dir (default=out):

	python rotateTxtAndJpg -txt txt -a 90

with output dir:
			
	python rotateTxtAndJpg -txt txt -out out -a 90

txt - source directory of .txt and .jpg files; default: txt ; required=True <br/>
out - target directory of roteted .txt and .jpg files; default out <br/>
angle - angle for rotation the bbox (90,180,270)


## Authors

* **Kirko Groﬂe M. Sc.** BTU Cottbus-Senftenberg 2020 

