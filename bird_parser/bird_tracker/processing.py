import sys
import os
import main

image_directory = os.path.join(os.getcwd(), "bird_parser/tests/images")

image = main.process_picture(os.path.join(image_directory, "input/test_bird0.jpg"), os.path.join(os.getcwd(), "output/test_bird0.jpg"))
image = main.process_picture(os.path.join(image_directory, "input/test_bird1.jpg"), os.path.join(os.getcwd(), "output/test_bird1.jpg"))
