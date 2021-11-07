import tensorflow as tf
import tensorflow_datasets as tfds
# from drive.MyDrive.examples.tensorflow_examples.models.pix2pix import pix2pix_resnet  # Colab

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))
from Desktop.Capstone.fromGit.examples.tensorflow_examples.models.pix2pix import pix2pix_resnet  # 내 PC
from Desktop.Capstone.fromGit.image_super_resolution_master.ISR.models import RDN

import time
import matplotlib.pyplot as plt
from IPython.display import clear_output

import cv2 as cv
import numpy as np
from PIL import Image


def sw():

  # 1. 함수 선언

  def normalize(image):
    image = tf.cast(image, tf.float32)
    image = (image / 127.5) - 1
    return image

  def generate_images(model, test_input):
    prediction = model(test_input)
      
    plt.figure(figsize=(12, 12))

    display_list = [test_input[0], prediction[0]]
    title = ['Input Image', 'Predicted Image']

    # for i in range(2):
    #   plt.subplot(1, 2, i+1)
    #   plt.title(title[i])
    #   # getting the pixel values between [0, 1] to plot it.
    #   plt.imshow(display_list[i] * 0.5 + 0.5)
    #   plt.axis('off')
    # plt.show()
    
    return prediction


  # 2. Cyclegan 변환

  OUTPUT_CHANNELS = 3

  generator_g = pix2pix_resnet.resnet_generator(OUTPUT_CHANNELS, norm_type='instancenorm')
  generator_f = pix2pix_resnet.resnet_generator(OUTPUT_CHANNELS, norm_type='instancenorm')

  discriminator_x = pix2pix_resnet.discriminator(norm_type='instancenorm', target=False)
  discriminator_y = pix2pix_resnet.discriminator(norm_type='instancenorm', target=False)

  LAMBDA = 10
  loss_obj = tf.keras.losses.BinaryCrossentropy(from_logits=True)

  def discriminator_loss(real, generated):
    real_loss = loss_obj(tf.ones_like(real), real)

    generated_loss = loss_obj(tf.zeros_like(generated), generated)

    total_disc_loss = real_loss + generated_loss

    return total_disc_loss * 0.5

  def generator_loss(generated):
    return loss_obj(tf.ones_like(generated), generated)

  def calc_cycle_loss(real_image, cycled_image):
    loss1 = tf.reduce_mean(tf.abs(real_image - cycled_image))
    
    return LAMBDA * loss1

  def identity_loss(real_image, same_image):
    loss = tf.reduce_mean(tf.abs(real_image - same_image))
    return LAMBDA * 0.5 * loss

  generator_g_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)
  generator_f_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)

  discriminator_x_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)
  discriminator_y_optimizer = tf.keras.optimizers.Adam(2e-4, beta_1=0.5)


  # 3. Checkpoint 설정

  checkpoint = tf.train.Checkpoint(generator_g=generator_g,
                                  generator_f=generator_f,
                                  discriminator_x=discriminator_x,
                                  discriminator_y=discriminator_y,
                                  generator_g_optimizer=generator_g_optimizer,
                                  generator_f_optimizer=generator_f_optimizer,
                                  discriminator_x_optimizer=discriminator_x_optimizer,
                                  discriminator_y_optimizer=discriminator_y_optimizer)

  # checkpoint_path = '/content/drive/MyDrive/save_sw'  # Colab
  checkpoint_path = r'C:\Users\BTLsub\Desktop\checkpoints-002\save_sw'   # ''사이에 save_sw 압축 푼 경로 복붙
  # print('Version :', tf.train.latest_checkpoint(checkpoint_path))  # 확인용
  checkpoint.restore(r'C:\Users\BTLsub\Desktop\checkpoints-002\save_sw\ckpt-74').assert_existing_objects_matched()  # ''사이에 save_sw 압축 푼 경로 복붙하고 +\ckpt_74


  # 4. 수행

  #img_path = r'C:\Users\BTLsub\realsite\media\1'
  #filenames = glob.glob(img_path + '/*.jpg')
  #new_name = '\원본.jpg'
  #os.rename(filenames[0],img_path+new_name)

  input_img = tf.io.read_file(r'C:\Users\BTLsub\realsite\media\input\원본.jpg') # Tensor 형태로 이미지 저장 위치에서 불러오기

  # 형변환 및 normalization
  input_img = tf.image.decode_image(input_img)
  input_exp = tf.expand_dims(input_img, 0)
  input_exp = normalize(input_exp)

  output = generate_images(generator_g, input_exp)    # image 변환

  save_image = (output[0]+1)*127.5
  save_image = tf.cast(save_image, tf.uint8)
  save_image = save_image.numpy()

  result_image = Image.fromarray(save_image)
  result_image.save("result1.jpg")

  # 확인용
  img = Image.open('result1.jpg')
  img = np.array(img)
  Image.fromarray(img)


  # 5. 화질 개선

  rdn3 = RDN(weights='noise-cancel')

  img = Image.open('result1.jpg')
  lr_img = np.array(img)
  Image.fromarray(lr_img)
  nc = rdn3.predict(lr_img)  # 출력 type : ndarray

  sr_img = cv.resize(nc, dsize=(0, 0), fx=0.5, fy=0.5)

  # 저장
  final_result_1 = Image.fromarray(sr_img)
  final_result_1.save("C:\\Users\\BTLsub\\realsite\\media\\output\\result.jpg")
