# -*- coding: utf-8 -*-
"""Colab Camera Capture

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SU1YE8iKCmW3hcpGLkiPa66pAn_fRIuL

## Using a webcam to Capture images, Save images and Display images.

## Camera Capture and Helper Functions
"""

from IPython.display import display, Javascript, Image
from google.colab.patches import cv2_imshow
from google.colab.output import eval_js
from base64 import b64decode
import numpy as np
import cv2

def js_cam():
  js = Javascript('''
    async function takePhoto(quality){ // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function

      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true}); // https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia
      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();  //  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/await

      // Resize the output to fit the video element.
      //google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);  //  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      // https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/getContext
      // https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage
      canvas.getContext('2d').drawImage(video, 0, 0); // video is name of frame
      // https://developer.mozilla.org/en-US/docs/Web/API/MediaStream/getVideoTracks
      // https://developer.mozilla.org/en-US/docs/Web/API/MediaStreamTrack/stop
      stream.getVideoTracks()[0].stop();
      div.remove();  //  https://developer.mozilla.org/en-US/docs/Web/API/Element/remove
      return canvas.toDataURL('image/jpeg', quality);  //  https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL
    }
    ''')
  display(js)  # to display javascript in colab output console

def photo_save(filename, quality=1):   # quality 0 to 1
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename

def photo_display(quality=1):    # quality 0 to 1
  data = eval_js('takePhoto({})'.format(quality))
  imgdata = b64decode(data.split(',')[1])
  image = np.frombuffer(imgdata,np.uint8)  # https://numpy.org/doc/stable/reference/generated/numpy.frombuffer
  # https://docs.opencv.org/3.4/d4/da8/group__imgcodecs.html#ga288b8b3da0892bd651fce07b3bbd3a56  ==>  https://docs.opencv.org/3.4/d8/d6a/group__imgcodecs__flags.html#ga61d9b0126a3e57d9277ac48327799c80
  img = cv2.imdecode(image, flags=1)  # cv::IMREAD_COLOR = 1  ==>  flags=1 for colored image
  cv2_imshow(img)

"""## Main Program for Save Photo

"""

js_cam()  #  initializing javascript in this main program
filename = 'photo1.jpg' # define filename to save
photo_save(filename)
print('{} Saved'.format(filename))
display(Image(filename)) # display the photo that is saved

"""## Main Program for Display Photo

"""

js_cam()  #  initializing javascript in this main program
photo_display()

"""## Showing CV2 Images

The ``cv2.imshow()`` and ``cv.imshow()`` functions from the [opencv-python](https://github.com/skvark/opencv-python) package are incompatible with Jupyter notebook

see https://github.com/jupyter/notebook/issues/3935

cv2.imshow() is crashing the server

If we avoid cv2.waitForKey() and cv2.closeAllWindows(), and keep the windows open, the notebook will continue running

As a replacement, you can use the following function :
"""

import cv2
help(cv2.imshow)
print("##################################################################################################################################################################################")
from google.colab.patches import cv2_imshow
help(cv2_imshow)

"""For example, here we download and display a PNG image of the Colab logo :"""

!curl -o logo.png https://colab.research.google.com/img/colab_favicon_256px.png
import cv2
from google.colab.patches import cv2_imshow
img = cv2.imread('logo.png', cv2.IMREAD_UNCHANGED)
cv2_imshow(img)
img = cv2.imread('photo1.jpg', cv2.IMREAD_UNCHANGED)
cv2_imshow(img)