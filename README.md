# Bone-Age Model

This repository builds a Docker image and a [Singularity](http://singularity.lbl.gov) image, each that will run the bone age demo to predict bone age from a radiograph. The demo runs the prediction on the command line, either with a local image input, or using a demo image.

If you are working on your local machine, you can use either Docker or Singularity. If you are running in a shared cluster (HPC) environment where you do not have root permissions, Singularity is your best option. Instructions are included for both.

Packages that need to be installed are included in [requirements.txt](requirements.txt) and installed into the container via the [Dockerfile](Dockerfile) or [Singularity](Singularity).

# Docker

## Getting Started
You should first [install Docker](https://docs.docker.com/engine/installation/). The container is provided on [Docker Hub](https://hub.docker.com/r/vanessa/boneage/) and can be downloaded from there when you run it, and this is recommended because building it takes a while to compile OpenCV.

### I want to build it!
If you want to look at or make changes to the code, it's recommended to clone the repo and build the container locally:

    git clone http://www.github.com/vsoch/boneage
    cd boneage
    docker build -t vanessa/boneage .


The docker daemon will first look for an image called `vanessa/boneage` locally, and if not found, will then try Dockerhub, and download it from there. If for any reason you want to remove your image, just do the following:

    docker rmi vanessa/boneage


## Usage
The entry to the container is done simply by using it as an executable:


	docker run vanessa/boneage --help
	usage: cli.py [-h] [--image IMAGE] [--output OUTPUT] [--gender {M,F}]
		      [--width WIDTH] [--height HEIGHT] [--debug]

	Predict bone age of an image.

	optional arguments:
	  -h, --help       show this help message and exit
	  --image IMAGE    Path to single bone image.
	  --output OUTPUT  Path to output file to write results.
	  --gender {M,F}   the gender of the individual (M or F), default is M (male)
	  --width WIDTH    warped width to resize the image in pixels (default 256)
	  --height HEIGHT  warped height to resize the image in pixels (default 256)
	  --debug          use verbose logging to debug.



### Run Prediction Demo
To run the bone-age demo non interactively to get a prediction, you can run it without any arguments. Note that since this application is optimized to return a web response (json) you will only see a json object returned without the `--debug` argument:

      docker run vanessa/boneage

	{'gender': 'M', 'image': '/code/example_images/1.png', 'scores': [4.3481795e-32, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.95402247, 4.6613271e-30, 0.0, 0.0, 0.0, 3.5964787e-28, 0.045977563, 0.0, 0.0, 7.72608e-32, 3.5294469e-28, 3.2218784e-31, 8.7065415e-31, 0.0, 0.0, 1.4140952e-27, 2.0360324e-31, 1.3973739e-18, 0.0, 0.0, 9.1047968e-32, 0.0, 0.0, 0.0, 0.0, 5.5391993e-31, 0.0, 0.0, 0.0, 1.3619909e-16, 0.0, 0.0, 3.7027614e-31, 1.6943371e-30, 8.6800407e-32, 0.0, 0.0, 1.6423222e-28, 0.0, 5.1337822e-30, 2.6105505e-31, 4.9806177e-30, 4.3782129e-15, 4.614967e-32, 3.4625493e-27, 3.3474241e-32, 3.2968069e-27, 1.2063197e-29, 3.3373545e-30, 1.4215187e-27, 3.7455669e-28, 3.4475776e-11, 3.9599255e-23, 7.9019825e-23, 9.7098277e-27, 7.4687077e-28, 3.3236082e-30, 2.9441527e-25, 1.0912699e-25, 1.0655707e-22, 8.3881067e-27, 9.9488148e-28, 7.2947065e-31, 1.0451508e-28, 3.4619964e-30, 2.3976481e-26, 1.8529252e-26, 4.1468809e-13, 1.124584e-31, 3.3920541e-32, 1.0070911e-30, 2.3539665e-19, 1.2927373e-28, 0.0, 0.0, 6.4560408e-24, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0023609e-22, 0.0, 0.0, 0.0, 0.0, 0.0, 2.2730129e-32, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.8752429e-23, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.6301819e-32, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.1331077e-26, 0.0, 8.9587665e-29, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.98046e-27, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.7935414e-31, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.170995e-22, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9.1674999e-31, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0261926e-24, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.2983278e-12, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0756849e-12, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'predicted_age': 8, 'predicted_weight': 8.2758656171904867}

You can also run with `--debug` to get full "pretty print" output.


      docker run vanessa/boneage --debug

	Environment message level found to be DEBUG

	DEBUG:bone-age:
	*** Starting Bone Age Prediction ****
	DEBUG:bone-age:No image selected, will use provided example...
	DEBUG:bone-age:is_male: True
	DEBUG:bone-age:image: /code/example_images/0.png
	DEBUG:bone-age:height: 256
	DEBUG:bone-age:width: 256
	DEBUG:PIL.PngImagePlugin:STREAM IHDR 16 13
	DEBUG:PIL.PngImagePlugin:STREAM IDAT 41 65536
	DEBUG:bone-age:Building model, please wait.

        ...
 

	DEBUG:bone-age:Predicted Age : 8 Months
	DEBUG:bone-age:Weighted Prediction : 8.164139 Months


### Run Prediction With Your Own Image
If you want to provide your own image, you need to bind it to the /data directory in the folder, and map a path to it. Don't forget to specify the gender - the default is male, and you may want to change that:

       
       docker run -v $PWD/example_images:/data vanessa/boneage --image /data/4.png

	*** Starting Bone Age Prediction ****
	Building model, please wait.
	Predicted Age : 8 Months
	Weighted Prediction : 8.641131 Months


We can of course add debug to verify that the default is male, and we are using our mapped image:


        docker run -v $PWD/example_images:/data vanessa/boneage --image /data/4.png --debug
	Environment message level found to be DEBUG

	*** Starting Bone Age Prediction ****
	DEBUG:bone-age:is_male: True
	DEBUG:bone-age:image: /data/4.png
	DEBUG:bone-age:height: 256
	DEBUG:bone-age:width: 256
	DEBUG:PIL.PngImagePlugin:STREAM IHDR 16 13
	DEBUG:PIL.PngImagePlugin:STREAM IDAT 41 65536
	Building model, please wait.
	Predicted Age : 8 Months
	Weighted Prediction : 8.641131 Months


We can specify a different gender, and the prediction changes:

        docker run -v $PWD/example_images:/data vanessa/boneage --image /data/4.png --gender F --debug
	Environment message level found to be DEBUG

	Environment message level found to be DEBUG

	*** Starting Bone Age Prediction ****
	DEBUG:bone-age:is_male: False
	DEBUG:bone-age:image: /data/4.png
	DEBUG:bone-age:height: 256
	DEBUG:bone-age:width: 256
	DEBUG:PIL.PngImagePlugin:STREAM IHDR 16 13
	DEBUG:PIL.PngImagePlugin:STREAM IDAT 41 65536
	Building model, please wait.
	Predicted Age : 16 Months
	Weighted Prediction : 16.000000 Months


### Save output to file
If you specify the `--output` argument, you can save the result as a json to file. Again, we will need to specify a file in a folder mapped to our local machine:

      docker run -v $PWD/example_images:/data vanessa/boneage --output /data/demo.json --debug

	Environment message level found to be DEBUG

	*** Starting Bone Age Prediction ****
	No image selected, will use provided example...
	DEBUG:bone-age:is_male: True
	DEBUG:bone-age:image: /code/example_images/4.png
	DEBUG:bone-age:height: 256
	DEBUG:bone-age:width: 256
	DEBUG:PIL.PngImagePlugin:STREAM IHDR 16 13
	DEBUG:PIL.PngImagePlugin:STREAM IDAT 41 65536
	Building model, please wait.
	Predicted Age : 8 Months
	Weighted Prediction : 8.641131 Months
	DEBUG:bone-age:Result written to /data/demo.json


Now we can look at the data - remember the folder that was mapped on our local machine is `$PWD/example_images`

        cat $PWD/example_images/demo.json
        {
           "gender": "M",
           "image": "/code/example_images/4.png",
           "predicted_age": 8,
           "predicted_weight": 8.64113067092668
        }


## How do I shell into the container?
By default, running the container uses the `ENTRYPOINT`, meaning it is used as an executable and you do not enter the container. In the case that you want a container-based environment that is installed with the dependencies of boneage, or if you want to interactively work with the code, you may want to shell into the container.

      docker run -it --entrypoint /bin/bash vanessa/boneage

Keep in mind that once you exit from this run, the container image is not saved, including your changes.



# Singularity

## 1. Install Singularity

Instructions can be found on the [singularity site](https://singularityware.github.io).

## 2. Bootstrap the image
Bootstrapping means using something to build from, or not starting from nothing. In this case, we are going to use a build file that bootstraps a Docker image of boneage (yes, the same one discussed above). This build file is called [Singularity](Singularity), and for more details about this you can [read here](http://singularity.lbl.gov/docs-docker).

    sudo singularity create --size 6000 boneage.img
    sudo singularity bootstrap boneage.img Singularity


## 3. Run commands
The commands are equivalent as above, except we can use the container as an executable:

      ./boneage.img --help

and to make a drive, we use `--bind` instead

      singularity run --bind $PWD/example_images:/data boneage.img --debug


## How do I shell into the container?
Singularity has an easy, intuitive way to shell inside!

      singularity shell boneage.img



# Interactive Web Interface

**todo**

Ultimately, we will build this demo and serve on [singularity hub](http://www.singularity-hub.org) and then have an application that takes inputs / outputs for the container, and runs on demand.
