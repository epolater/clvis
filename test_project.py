from project import options, image, video
import unittest

def test_options():
    with unittest.mock.patch("sys.argv",["clvis.py", "-t", "img", "-f", "image.jpeg", "-c", "4", "-s", "50,50"]):
        options()

def test_image():
    file = "image.jpeg"
    image(file, 4, 50, 50)

def test_video():
    file = "video.mp4"
    video(file, 4, 50, 50)
    



