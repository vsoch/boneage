#!/usr/bin/python

import argparse
from glob import glob
import pickle
import os
import sys

def get_parser():

    parser = argparse.ArgumentParser(description="Predict bone age of an image.")

    parser.add_argument("--image", 
                        dest='image', 
                        help="Path to single bone image.", 
                        type=str,
                        default=None)

    parser.add_argument("--demo",
                        dest='demo',
                        help="Specific demo image to run",
                        type=int,
                        default=None)


    parser.add_argument("--output", 
                        dest='output', 
                        help="Path to output file to write results.", 
                        type=str,
                        default=None)

    parser.add_argument("--gender", 
                        dest='gender', 
                        help="the gender of the individual (M or F), default is M (male)", 
                        type=str,
                        choices=["M","F"],
                        default="M")

    parser.add_argument("--width", 
                        dest='width', 
                        help="warped width to resize the image in pixels (default 256)", 
                        type=int,
                        default=256)

    parser.add_argument("--height", 
                        dest='height', 
                        help="warped height to resize the image in pixels (default 256)", 
                        type=int,
                        default=256)

    # Does the user want to have verbose logging?
    parser.add_argument('--debug', dest="debug", 
                        help="use verbose logging to debug.", 
                        default=False, action='store_true')

    return parser



def main():
    parser = get_parser()
    
    try:
        args = parser.parse_args()
    except:
        sys.exit(0)

    # if environment logging variable not set, make silent
    if args.debug == False:
        os.environ['MESSAGELEVEL'] = "CRITICAL"

    # Tell the user what is going to be used, in case is incorrect
    from logman import bot
    from predict_image import Model
    from utils import get_image, write_json
    bot.logger.debug("\n*** Starting Bone Age Prediction ****")

    # Get the gender
    is_male = True
    if args.gender == "F":
        is_male = False

    image = args.image
    if image == None:
        bot.logger.debug("No image selected, will use provided example...")
        if args.demo is None:
            from utils import select_example_image
            image = select_example_image(start=0,end=9)
        else:
            if args.demo in range(0,10):
                image = '/code/example_images/%s.png' %(args.demo)
            else:
                print({'error':'Please select a demo image between [0,9]'})
                sys.exit(32)
        is_male = True # all examples male

    # Print parameters for user
    bot.logger.debug("is_male: %s", is_male)
    bot.logger.debug("image: %s", image)
    bot.logger.debug("height: %s", args.height)
    bot.logger.debug("width: %s", args.width)

    # Get the array of data (uint8) - H/W should be set to 256
    image_path = image
    image = get_image(image_path=image,
                      warped_height=args.height,
                      warped_width=args.width)

    bot.logger.debug("Building model, please wait.")
    model = Model()
    result = model.get_result(image=image,
                              image_path=image_path,
                              is_male=is_male)

    result['scores'] = list(model.get_scores(image,is_male=is_male))

    # Print the json to stdout
    print(result)

    bot.logger.debug('Predicted Age : %d Months' %result['predicted_age'])
    bot.logger.debug('Weighted Prediction : %f Months' %result['predicted_weight'])


    if args.output != None:
        output = write_json(json_object=result,
                            filename=args.output)        
        bot.logger.debug('Result written to %s',args.output)

if __name__ == '__main__':
    main()
