import sys
import os
import main

image_directory = os.path.join(os.getcwd(), "../tests/images")

image = main.process_picture(os.path.join(image_directory, "input/test_bird0.jpg"), os.path.join(image_directory, "output/test_bird0.jpg"))
image = main.process_picture(os.path.join(image_directory, "input/test_bird1.jpg"), os.path.join(image_directory, "output/test_bird1.jpg"))
