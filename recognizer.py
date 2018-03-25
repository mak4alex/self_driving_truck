# -*- coding: utf-8 -*-
import cv2
from darkflow.net.build import TFNet
import tensorflow as tf
import matplotlib.pyplot as plt


def test_tf_install():
  hello = tf.constant('Hello, TensorFlow!')
  session = tf.Session()
  print(session.run(hello))

def add_labels(img, labels, threhold = 0.1):
  labeled_img = img.copy()

  for label in labels:
    confidence = label['confidence'].round(4)
    if confidence > threhold:
      top_left = (label['topleft']['x'], label['topleft']['y'])
      bottom_right = (label['bottomright']['x'], label['bottomright']['y'])
      name = label['label'] + ' ' + str(confidence) + '%'
      labeled_img = cv2.rectangle(labeled_img, top_left, bottom_right, (0,0,255), 10)
      labeled_img = cv2.putText(labeled_img, name,
                                (top_left[0], top_left[1] - 10),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)

  return labeled_img


test_tf_install()

options = {
  'model': 'cfg/tiny-yolo-voc.cfg',
  'load': 'bin/tiny-yolo-voc.weights',
  'threshold': 0.3,
  'gpu': 1.0
}
tfnet = TFNet(options)


def recognize(image):
   predicted_labels = tfnet.return_predict(image)
   return predicted_labels

