from PIL import Image, ImageFilter
import cv2
import time
import os

# Options
ts = 1/30   # time.sleep
ch = 2      # Character set
size = 70   # Pixel size

video = cv2.VideoCapture('video.mp4')

frame_no = 1
success = True

while success:
#for i in range(3):
    # Read the next frame from the video
    success, frame = video.read()

    if success:
        # Save the frame as a JPEG image
        cv2.imwrite(f'frames/f{frame_no}.jpg', frame)
        
        # ____________________IMAGE PROCESS _____________________

        # Opening Original Image file with PIL
        img = Image.open(f'frames/f{frame_no}.jpg')

        img_size = img.size
        img_width, img_height = img.size


        # Resizing, filtering  and Saving as new Image
        img = img.resize((size, size))
        img = img.filter(ImageFilter.EDGE_ENHANCE)
        img.save('img_new.jpeg')

        # Openning edited image
        img_new = Image.open('img_new.jpeg')

        # Assigning height and weight of resized image
        img_new_width, img_new_height = img_new.size
        #print("widt :", img_new_width, "height :", img_new_height)


        # Character Set
        chars = [
                    ["  ", ". ", ": ", ":.", "::"],
                    [". ", ". ", ": ", ":.", "::"],

                    ["  ", ": ", "+ ", "% ", "# "],
                    ["` ", ": ", "+ ", "% ", "# "],

                    ["  ", "1 ", "+ ", "% ", "0 "],
                    [". ", "1 ", "+ ", "% ", "0 "],
                ]       


        # Mapping RGB values to Character Set in char_map list
        char_map = []
        for i in range(len(chars)):
            char_map.append(round(255 / len(chars) * (i+1)))
        #print(char_map) 

        med_RGB = []

        # Cleaning screen before printing
        os.system('clear')

        # Reading image values
        for y in range(img_new_width):
            for x in range(img_new_height):
                R, G, B = img_new.getpixel((x, y))
                #print(f"R: {R}, G: {G}, B: {B}")

                # Creating list of RGB color median values
                #med_RGB.append( round((R + G + B) / 3) )
                avg_RGB = ( round((R + G + B) / 3) )
                #print(avg_RGB, end="")

                # Matching RGB color with Char Set and Printing to screen
                if avg_RGB <= char_map[0]:
                    print(chars[ch][0], end="")

                elif char_map[0] < avg_RGB <= char_map[1]:
                    print(chars[ch][1], end="")

                elif char_map[1] < avg_RGB <= char_map[2]:
                    print(chars[ch][2], end="")

                elif char_map[2] < avg_RGB <= char_map[3]:
                    print(chars[ch][3], end="")
                else:
                    print(chars[ch][4], end="")
            print("")
        time.sleep(ts)

        # ___________________END OF IMAGE PROCESS _____________________


    os.remove(f'frames/f{frame_no}.jpg')
    
    frame_no = frame_no + 1



        
