# RotateTxtAndJpg

Tool for Rotation for images in.jpg-format and 
the Bounding Box in .txt-format for training in darknet

## Getting Started

Clone this repo on your local machine using: 
	
	git clone https://github.com/farbton/rotateTxtAndJpg


### Requirements

	numpy==1.18.1
	py-opencv==3.4.2
```

### Usage

Open cmd and call "rotateTxtAndJpg"__directory

	python rotateTxtandJpg.py -txt txt -out out -ang angle

		txt - source directory of .txt files; default: txt ; required=True
		out - target directory of roteted .txt files; default out
      angle - angle for rotation the bbox (90,180,270)

```
Give the example
without output dir:

		python rotateTxtAndJpg -txt txt -a 90

	with output dir:
			
		python rotateTxtAndJpg -txt txt -out out -a 90
```


## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Kirko Groﬂe M.Sc.** - 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

<!--
## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
-->