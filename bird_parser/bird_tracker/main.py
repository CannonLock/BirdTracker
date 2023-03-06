import cv2
from imageai.Detection import ObjectDetection
import os
import glob
import time
import tempfile
import subprocess
from datetime import datetime, timezone

def transfer_file(file, server_path):
  subprocess.run(["scp", file, server_path])


def save_image_to_mac(image_path, output_path=None):
  if output_path is None:
    random_name = image_path.split("/")[-1]
    output_path = f"cannonlock@192.168.1.6:/Users/cannonlock/Birds/{random_name}"

  transfer_file(image_path, output_path)


def log_birds(bird_count):
  with open("~/logs/birds.csv", "a") as bird_log:
    bird_log.write(f"{datetime.now(timezone.utc)},{bird_count}")


def setup_detector():
  execution_path = os.getcwd()
  detector = ObjectDetection()
  detector.setModelTypeAsRetinaNet()
  detector.setModelPath(os.path.join(execution_path, "../../retinanet_resnet50_fpn_coco-eeacb38b.pth"))
  detector.loadModel()

  return detector


def process_picture(image_path, output_path):
  detector = setup_detector()
  custom_object = detector.CustomObjects(bird=True)
  detections = detector.detectObjectsFromImage(custom_objects=custom_object,
                                               input_image=image_path,
                                               output_image_path=output_path,
                                               minimum_percentage_probability=1,
                                               display_object_name=False)

  if detections:
    return detections


def take_image():
  camera = cv2.VideoCapture(0)

  res, image = camera.read()
  if res:
    return image

  raise Exception("Image did not work as expected")


def save_image_to_file(fp, image):
  file_name = fp.name

  cv2.imwrite(file_name, image)

  return file_name


def main():
  while True:
    fp = tempfile.NamedTemporaryFile("w", suffix=".jpg")
    image = take_image()

    image_path = save_image_to_file(fp, image)

    output_path = process_picture(image_path)

    time.sleep(10)


