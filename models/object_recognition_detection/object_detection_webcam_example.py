

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import threading, time
import pytesseract
from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import urllib
import time


from utils import label_map_util

from utils import visualization_utils as vis_util
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

# # Model preparation 
# Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing `PATH_TO_CKPT` to point to a new .pb file.  
# By default we use an "SSD with Mobilenet" model here. See the [detection model zoo](https://github.com/tensorflow/models/blob/master/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.
def odw():
    # What model to download.
    MODEL_NAME = 'food_graph5_mobile_v2'
    MODEL_FILE = MODEL_NAME + '.tar.gz'
    DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

    # Path to frozen detection graph. This is the actual model that is used for the object detection.
    PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

    # List of the strings that is used to add correct label for each box.
    PATH_TO_LABELS = os.path.join('training5_mobile_v2', 'object-detection.pbtxt')

    NUM_CLASSES = 5


    # ## Download Model

    if not os.path.exists(MODEL_NAME + '/frozen_inference_graph.pb'):
        print ('Downloading the model')
        opener = urllib.request.URLopener()
        opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
        tar_file = tarfile.open(MODEL_FILE)
        for file in tar_file.getmembers():
          file_name = os.path.basename(file.name)
          if 'food_graph.pb' in file_name:
            tar_file.extract(file, os.getcwd())
        print ('Download complete')
    else:
        print ('Model already exists')

    ### Load a (frozen) Tensorflow model into memory.

    detection_graph = tf.Graph()
    with detection_graph.as_default():
      od_graph_def = tf.GraphDef()
      with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')




    # ## Loading label map
    # Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine

    label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
    categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
    category_index = label_map_util.create_category_index(categories)

    #intializing the web camera device

    import cv2
    #def VideoCapture(self):
    cap = cv2.VideoCapture(0)
    import scipy.misc

        # Running the tensorflow session
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
          ret = True
          counts = 0
          while (ret):
              ret,image_np = cap.read()

            # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
              image_np_expanded = np.expand_dims(image_np, axis=0)
              image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
              # Each box represents a part of the image where a particular object was detected.
              boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
              # Each score represent how level of confidence for each of the objects.
              # Score is shown on the result image, together with the class label.
              scores = detection_graph.get_tensor_by_name('detection_scores:0')
              classes = detection_graph.get_tensor_by_name('detection_classes:0')
              num_detections = detection_graph.get_tensor_by_name('num_detections:0')

              img2 = Image.fromarray(image_np, 'RGB')
              img2.save('my.png')
              text = pytesseract.image_to_string(Image.open('my.png'))

              text=text.split()
              text=''.join(text)
              print (text)

              # Actual detection.-
              boxes, scores, classes, num_detections = sess.run(
                  [boxes, scores, classes, num_detections],
                  feed_dict={image_tensor: image_np_expanded})
              # ---------------------
              # sava list of classes on the file
              # classes_list = classes.tolist()
              # def save_list():
              #     classes_save_list = []
              #     for i in classes_list:
              #       if not i in classes_save_list:
              #           classes_save_list.append(i)
              #       for j in classes_save_list:
              #           if j not in classes_save_list:
              #               classes_save_list.remove(j)
              #
              #     with  open( 'db_with_gui/food_list.txt','w') as insert_DB_txt_file:
              #         insert_DB_txt_file.seek(0)
              #         insert_DB_txt_file.write(str(classes_save_list))
              #         threading.Timer(3,save_list()).start()

              #save_list()

              # Visualization of the results of a detection.
              classls=vis_util.visualize_boxes_and_labels_on_image_array(
                  image_np,
                  np.squeeze(boxes),
                  np.squeeze(classes).astype(np.int32),
                  np.squeeze(scores),
                  category_index,
                  use_normalized_coordinates=True,
                  line_thickness=8)

        #      plt.figure(figsize=IMAGE_SIZE)
        #      plt.imshow(image_np)
              font = cv2.FONT_HERSHEY_SIMPLEX
              bottomLeftCornerOfText = (10, 500)
              fontScale = 1
              fontColor = (255, 255, 255)
              lineType = 2

              #img=cv2.resize(image_np,(1280,960))
              img = cv2.resize(image_np, (900, 750))

              font                   = cv2.FONT_HERSHEY_SIMPLEX
              bottomLeftCornerOfText = (10,500)
              fontScale              = 1
              fontColor              = (255,255,255)
              lineType               = 2
              #
              cv2.putText(img,text.encode('utf-8'),
              bottomLeftCornerOfText,
              font,
              fontScale,
              fontColor,
              lineType)
              #draw = ImageDraw.Draw(img)
              #draw.text((0, 0), "This is a test", (255, 255, 0))
              #draw = ImageDraw.Draw(img)
              #img.save("a_test.png")
              # 1. include mechine learning

              # 2. extract

              #cv2.putText(img, text,bottomLeftCornerOfText,font,fontScale,fontColor,lineType)
              cv2.imshow("image", img)

              if cv2.waitKey(25) & 0xFF == ord('q'):
                  cv2.destroyAllWindows()
                  cap.release()
                  break
              counts+=1
              if counts >=15 and len(classls) >= 1:
                     break
              print classls,counts,'j'
    return classls
odw()