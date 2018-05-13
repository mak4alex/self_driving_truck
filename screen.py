# -*- coding: utf-8 -*-
from PIL import ImageGrab
import win32gui, win32com.client
import numpy as np
import cv2
import os
import time


def get_window_screen(title):
  shell = win32com.client.Dispatch("WScript.Shell")
  shell.SendKeys('%')

  toplist = []
  windows_list = []

  def enum_cb(hwnd, results):
    windows_list.append((hwnd, win32gui.GetWindowText(hwnd)))

  win32gui.EnumWindows(enum_cb, toplist)

  processes = [(hwnd, win_title) for hwnd, win_title in windows_list if title in win_title.lower()]

  if not processes:
    raise Exception("Process '{}' not found".format(title))

  print('Founded processes:')
  for process in processes:
    print('hwnd: {} -> {}'.format(process[0], process[1]))

  game_hwnd = processes[0][0]

  win32gui.SetForegroundWindow(game_hwnd)
  win32gui.MoveWindow(game_hwnd, 0, 0, 640, 480, False)
  bounded_box = win32gui.GetWindowRect(game_hwnd)

  while True:
    screen_image = np.array(ImageGrab.grab(bounded_box))
    yield screen_image


def save_screenshot(image, directory='screenshots'):
  if not os.path.exists(directory):
    os.makedirs(directory)
  file_name = 'screenshot_%0.f.png' % time.time()
  file_path = os.path.join(directory, file_name)
  cv2.imwrite(file_path, image)
  print('Screenshot screenshot %s have been created' % file_path)

