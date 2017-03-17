''' utils.py

Utility functions for bone age prediction demo

'''

import os
import re
from logman import bot

from numpy import (
    array,
    uint8
)

from PIL import Image
import simplejson
import tempfile
import sys

try:
    from urllib import urlretrieve
except:
    from urllib.request import urlretrieve


def get_image(image_path,warped_height=256,warped_width=256):
    '''get_image will return an image array (using import image)
    after checking that the image exists.
    :param image_path: the path to the image file
    :param warped_width: the width of the image, in pixels
    :param warped_height: the height of the image, in pixels
    '''
    # If it's a url, download first.
    delete_image = False
    if re.search('http://|https',image_path):
        image_path = download_image(image_path)
        delete_image = True

    image = os.path.abspath(image_path)

    # Make sure it exists
    if os.path.exists(image) == False:
        bot.logger.error("Error, cannot find %s, exiting!",image)
        sys.exit(1)

    data = import_image(img_path=image, 
                        warped_height=warped_height, 
                        warped_width=warped_width)

    if delete_image is True:
        os.remove(image_path)
    return data


def download_image(image_path):
    '''download image will download image to a temporary location
    '''
    tmpfile = tempfile.mkstemp(prefix='tmp', dir='/tmp')[-1]
    os.remove(tmpfile)
    ext = os.path.splitext(image_path)[-1]
    download_file = "%s%s" %(tmpfile,ext)
    download_file,response = urlretrieve(image_path,download_file)
    return download_file


def import_image(img_path, warped_height=256, warped_width=256):
    '''import image will return the ind-th image specified by 
    list img_names - uint8 array
    :param image_path: the path to the image file
    :param warped_width: the width of the image, in pixels
    :param warped_height: the height of the image, in pixels
    '''    
    # Must have ints for sizes
    warped_width = check_type(warped_width,int)
    warped_height = check_type(warped_height,int)

    # image resize is specified with width then height in PIL Image
    img_data = Image.open(img_path).resize((warped_width,warped_height))
    img_array = array(img_data.convert('L'))

    # In rare cases the image has three channels instead of 1
    if len(img_array.shape) > 2:
        bot.logger.info('Converting img %s to Grayscale...',imgnames[i])
        bot.logger.debug(img_array.shape)

    # Must be uint8 to continue
    if img_array.dtype != uint8:
        bot.logger.error("Image array data type is not uint8. Exiting.")
        sys.exit(1)

    return img_array


def select_example_image(basepath=None,start=0,end=9,extension=None):
    '''select_example_image will select an image from start to finish
    in some basepath folder. If none provided, defaults are used.
    :param basepath: the base path to select image from (default /code/example_images/
    :param start: the first image (default 0)
    :param end: the last image (default 9)
    :param extension: the extension of the image (without dot). default is png
    '''
    from random import sample
    image = None
    if basepath == None:
        basepath = '/code/example_images'

    if extension == None:
        extension = "png"
    contenders = list(range(start,end))

    # Keep going until we get an image, then return it
    while image == None:
        selection = "%s/%s.%s" %(basepath,
                                 sample(contenders,1)[0],
                                 extension)
        if os.path.exists(selection):
            image = selection

    return image


def check_type(variable,desired_type):
    '''check_type will check if a variable is a desired type. If not,
    if will convert and return the fixed variable.
    :param variable: the input to check
    :param desired_type: the desired type
    '''
    if not isinstance(variable,desired_type):
        variable = desired_type(variable)
    return variable


def check_install(software,command=None):
    '''check_install will attempt to run the command specified with some argument, 
    and return an error if not installed.
    :param software: the executable to check for
    :param command: the command argument to give to the software (default is --version)
    '''    
    if command == None:
        command = '--version'
    cmd = [software,version]
    version = run_command(cmd,error_message="Cannot find %s. Is it installed?" %software)
    if version != None:
        bot.logger.info("Found %s version %s",software.upper(),version)
        return True
    else:
        return False

def write_json(json_object,filename,mode="w",print_pretty=True):
    '''write_json will (optionally,pretty print) a json object to file
    :param json_object: the dict to print to json
    :param filename: the output file to write to
    :param pretty_print: if True, will use nicer formatting   
    '''
    with open(filename,mode) as filey:
        if print_pretty == True:
            filey.writelines(simplejson.dumps(json_object, indent=4, separators=(',', ': ')))
        else:
            filey.writelines(simplejson.dumps(json_object))
    filey.close()
    return filename
