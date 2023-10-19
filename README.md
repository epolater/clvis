# CLVIS : Command-line Visualizer
#### Video Demo:  <https://youtu.be/mPuDry_eO4Q>

#### **Description**:

CLVIS is a command-line program to visualize image or video files on terminal window. With CLVIS it is possible to see basic represantation of the image/video file on terminal window with special characters pre-defined in program.  Purpose of the program is to see some fancy images on the primitive terminal windows while boredom is at maximum level. 

#### **Programs used to develop the CLVIS**:

Some python libraries used in project as below;
- Pillow : It is used to process image files
- OpenCV for python : it is used to read and process video files.

#### **How To Use**:

To see usage of the program, it is possible to run program with -h option or simply run the program. The print-out of -help option is below.

usage: project.py [-h] [-t {vid,img}] [-f F] [-c {0,1,2,3,4,5,6,7,8}] [-s S] [-fps FPS]

CLVIS : Commandline Image Visualizer

options:
  * -h, --help            : show this help message and exit
  * -t {vid,img}          : File type; 'img' for images 'vid for videos'
  * -f F                  : File name with extension; ex. 'video.mp4'
  * -c {0,1,2,3,4,5,6,7,8}: Character set to be used for printing; 'from 0 to 8'
  * -s S                  : Sizes to print in pixels; ex. '40,40'
  * -fps FPS              : Frame per second to print on screen for video files

Works best on full screen terminal window

- Changing terminal windows text-size to smallest and setting sizes to bigger values can result in better resolution.
- Image/Video file should be on the same root with app. file
- Video frames are created in /frames file and deleted immediately after printing on screen. To end video printing press ctrl+c 