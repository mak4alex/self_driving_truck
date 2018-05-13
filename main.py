# -*- coding: utf-8 -*-
import cv2
import time
import importlib
import win32api

import recognizer
import screen


for module in [recognizer, screen]:
  importlib.reload(module)


def convert_image(image):
  return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def crop_image(image):
  return image[25:470, 10:640]

def add_labels(image):
  labels = recognizer.recognize(image)
  recognized_image = recognizer.add_labels(image, labels)
  return recognized_image


def main():
  game_title = 'king of the road'
  last_time = time.time()

  for image in  screen.get_window_screen(game_title):
    converted_image = convert_image(crop_image(image))
    labeled_image   = add_labels(converted_image)

    fps = (1.0 / (time.time() - last_time))
    last_time = time.time()
    print('Loop took %.2f FPS' % fps)
    cv2.imshow('Game screen', labeled_image)
    cv2.waitKey(1)

    button = ''
    for i in range(1, 256):
      if win32api.GetAsyncKeyState(i):
        button = chr(i)

    if button == 'O':
      screen.save_screenshot(converted_image)
    elif button == 'Q':
      cv2.destroyAllWindows()
      break
    elif button == '':
      pass
    else:
      print('Unknown button %s' % button)

main()

