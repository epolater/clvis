import os
import sys
import time
import argparse
from PIL import Image, ImageFilter   # installation : pip install pillow
import cv2                           # installation : pip install opencv-python

def main():

    if check() == True:
        
        opt = options()
        
        try:
            if set_args.args.t == 'img':
                image(opt[0], int(opt[1]), int(opt[2]), int(opt[3]))
               

            elif set_args.args.t == 'vid':
                video(opt[0], int(opt[1]), int(opt[2]), int(opt[3]), int(opt[4]))
                
        except:
            pass


class set_args():

    parser = argparse.ArgumentParser(
        description = "CLVIS : Commandline Image Visualizer", epilog="Works best on full screen terminal window")

    parser.add_argument("-t", help="File type; 'img' for images 'vid for videos' ", choices=["vid", "img"])
    parser.add_argument("-f", help="File name with extension; ex. 'video.mp4' ")
    parser.add_argument("-c", help="Character set to be used for printing; 'from 0 to 8' ",\
         default=3, choices=["0", "1", "2", "3", "4", "5", "6", "7", "8"])
    parser.add_argument("-s", help="Sizes to print in pixels; ex. '40,40' ", default="40,40")
    parser.add_argument("-fps", help="Frame per second to print on screen for video files", default=30)

    args = parser.parse_args()

def check():

    # Print help and options if no argument
    if len(sys.argv) == 1:
        print(textstyle.green + "")
        set_args.parser.print_help()
        print("" + textstyle.default)
    
    else:
        return True
    
def options():

    file = set_args.args.f                        #File name
    c_set = set_args.args.c                       #Character set
    size_x, size_y = set_args.args.s.split(",")   #Print size
    fps = set_args.args.fps                       #Frame Rate
        
    return [file, c_set, size_x, size_y, fps]

def image(file, c_set, size_x, size_y):

    # Opening Original Image file
    img = Image.open(file)

    # Resizing, filtering  and Saving as new Image nad Opening
    img = img.resize((size_y, size_x))
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    img.save('img_new.jpeg')

    # Openning edited image
    img_new = Image.open('img_new.jpeg')

    # Assigning height and weight of resized image
    img_new_height, img_new_width = img_new.size

    # Character Set
    chars = [
                ["  ", ". ", ": ", ":.", "::"],
                [". ", ". ", ": ", ":.", "::"],
                ["::", ":.", ": ", ". ", "  "],

                ["  ", ": ", "+ ", "% ", "# "],
                ["` ", ": ", "+ ", "% ", "# "],
                ["# ", "% ", "+ ", ": ", "  "],

                ["  ", "1 ", "+ ", "% ", "0 "],
                [". ", "1 ", "+ ", "% ", "0 "],
                ["0 ", "% ", "+ ", "1 ", "  "],
            ]       


    # Mapping RGB values to Character Set in char_map list
    char_map = []
    for i in range(len(chars)):
        char_map.append(round(255 / len(chars) * (i+1)))


    # Cleaning screen before printing
    os.system('clear')

    # Printing image values to screen
    for y in range(img_new_width):
        for x in range(img_new_height):
            R, G, B = img_new.getpixel((x, y))

            # Creating black and white image (avarage of RGB values)
            avg_RGB = ( round((R + G + B) / 3) )

            # Matching RGB color with Char Set and Printing to screen
            if avg_RGB <= char_map[0]:
                print(chars[c_set][0], end="")

            elif char_map[0] < avg_RGB <= char_map[1]:
                print(chars[c_set][1], end="")

            elif char_map[1] < avg_RGB <= char_map[2]:
                print(chars[c_set][2], end="")

            elif char_map[2] < avg_RGB <= char_map[3]:
                print(chars[c_set][3], end="")
            else:
                print(chars[c_set][4], end="")
        print("")
    print("")

def video(file, c_set=2, size_x=40, size_y=70, fps=30):
    try:
        # Opening Video file
        video = cv2.VideoCapture(file)

        # Looping through all frames
        frame_no = 1
        success = True

        while success:
            success, frame = video.read()

            if success:
                # Save the frame as a JPEG image
                cv2.imwrite(f'frames/f{frame_no}.jpg', frame)
                
                # Edit frame and print to screen
                image(f'frames/f{frame_no}.jpg', c_set, size_x, size_y)

                #Remove frame image created
                os.remove(f'frames/f{frame_no}.jpg')
                
                # Time interval for image to print screen
                time.sleep(1/fps)

            #Set frame value for next frame
            frame_no = frame_no + 1
    
    
    except KeyboardInterrupt:
        pass
        os.system('clear') # Clean Screen
        os.remove('img_new.jpeg')
    
    os.system('clear') # Clean Screen
    os.remove('img_new.jpeg')

class textstyle:
    purple = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    default = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'

if __name__ == "__main__":
    main()