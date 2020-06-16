# RotateTxtAndJpg

Tool for rotation of images in .jpg-format and 
the bounding box in .txt-format for training in darknet

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
python rotateTxtandJpg.py -s source -o out -a angle
```


#### Example


with default directory (-s=source, -o=out):

	python rotateTxtAndJpg -a 90

without default directory:
			
	python rotateTxtAndJpg -s source -o out -a 90

source - source directory of .txt and .jpg files; default: source  <br/>
out    - target directory of roteted .txt and .jpg files; default: out <br/>
angle  - angle to turn the bbox (90,180,270)


## Authors

* **Kirko Groﬂe M. Sc.** BTU Cottbus-Senftenberg  June 2020 

