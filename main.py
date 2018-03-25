# -*- coding: utf-8 -*-
import cv2
import time
import importlib

import screen_reader
import recognizer


importlib.reload(screen_reader)
importlib.reload(recognizer)


def process_image(image):
  converted_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  labels = recognizer.recognize(converted_image)
  recognized_image = recognizer.add_labels(converted_image, labels)

  return recognized_image


def main():
  game_title = 'king of the roQad'
  last_time = time.time()

  for image in  screen_reader.get_window_screen(game_title):
    image = process_image(image)


    print('Loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()
    cv2.imshow('Game screen', image)

    if cv2.waitKey(25) & 0xFF == ord('q'):
      cv2.destroyAllWindows()
      break

main()

