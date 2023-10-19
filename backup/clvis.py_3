import os
import sys
import time
from PIL import Image, ImageFilter   # installation : pip install pillow
import cv2                           # installation : pip install opencv2-python

def main():
    
    if check() == True:
        
        opt = options()
        
        try:
            if opt[0] == 'img':
                
                image(opt[1], int(opt[2]), int(opt[3]), int(opt[4]))

            elif opt[0] == 'vid':
                video(opt[1], int(opt[2]), int(opt[3]), int(opt[4]), int(opt[5]))
                
        except:
            ...

def usage():
    # Print usage
    print(textstyle.red + "\nUsage for image: clvis img 'filename' 'char.set(0 to 8)' 'size in pixel(X,Y)'")
    print(textstyle.green + "Ex.: clvis.py img image.jpg 2 40,40\n")

    print(textstyle.red + "Usage for video: clvis.py vid 'filename' 'char.set(0 to 8)' 'sizes in pixel(X,Y)' 'framerate'")
    print(textstyle.green + "Ex.: clvis.py vid video.mp4 2 40,70 30\n" + textstyle.default)
    
    sys.exit()

def check():
    #sys.tracebacklimit = 0   #disabling error traceback lines to print screen

    if len(sys.argv) == 1 or len(sys.argv) > 6 or 1 < len(sys.argv) < 5:
        usage()
    
    elif sys.argv[1] not in ["img", "vid"]:
        usage()
    
    elif sys.argv[1] == "vid" and len(sys.argv) < 6:
        usage()
    
    elif int(sys.argv[3]) < 0 or int(sys.argv[3]) > 8:
        raise TypeError(textstyle.red + "Usage: char.set(0 to 8)\n" + textstyle.default)
       
    elif "," not in sys.argv[4]:
        raise TypeError(textstyle.red + "Usage: sizes in pixel(X,Y)\n" + textstyle.default)

    else:
        return True
    
def options():
    # Image Options
    if len(sys.argv) == 5:
        file = sys.argv[2]                        #File name
        c_set = sys.argv[3]                       #Character set
        size_x, size_y = sys.argv[4].split(",")   #Print size
        
        return [sys.argv[1], file, c_set, size_x, size_y]

    #Video Options
    elif len(sys.argv) == 6:
        file = sys.argv[2]                        #File name
        c_set = int(sys.argv[3])                  #Character set
        size_x, size_y = sys.argv[4].split(",")   #Print size
        fps = sys.argv[5]                         #Frame Rate
        
        return [sys.argv[1], file, c_set, size_x, size_y, fps] 

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