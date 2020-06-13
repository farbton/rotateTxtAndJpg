import os
import numpy as np
import cv2

from reader import Reader
from writer import Writer

class Manipulate(object):
    def __init__(self, source_dir, out_dir, angle):
        self.source_dir = source_dir
        self.out_dir = out_dir
        self.angle = angle

    def rotate_img(self, jpg_filename):
        def rotation_90(jpg_filename):
            img = cv2.imread(jpg_filename)
            rotate_img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            return rotate_img

        def rotation_180(jpg_filename):
            img = cv2.imread(jpg_filename)
            rotate_img = cv2.rotate(img, cv2.ROTATE_180)
            return rotate_img

        def rotation_270(jpg_filename):
            img = cv2.imread(jpg_filename)
            rotate_img = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)
            return rotate_img
        
        switch = {
            90:  rotation_90(jpg_filename),
            180: rotation_180(jpg_filename),
            270: rotation_270(jpg_filename),                      
        }
        return switch.get(int(self.angle), "error in rotate_img()")


    def manipulate_files(self, list_of_filenames):
        print("manipulate files...")
        for i, (txt_filename, jpg_filename) in enumerate(list_of_filenames):
            bbox_list = self.reader.get_bbox_list(txt_filename)
            bbox_list_rotated = self.rotate_bbox_list(bbox_list)
            img_rotated = self.rotate_img(jpg_filename)
            self.writer.write_rotate_bbox_list(txt_filename, bbox_list_rotated)
            self.writer.write_img_rotated(jpg_filename, img_rotated)
        print("Edited files:",2 * (i + 1), "| txt_files:",i + 1, "| jpg_files:",i + 1)

    def start(self):
        self.writer = Writer(out_dir=self.out_dir, angle=self.angle)
        self.reader = Reader(source_dir=self.source_dir)
        list_of_filenames = self.reader.get_list_of_filenames()
        self.manipulate_files(list_of_filenames)
        
            
    def rotate_bbox_list(self,bbox_list):
        bbox_rotate_list = []
        for bbox in bbox_list:
            bbox_rotate = self.calculate_points(bbox)
            bbox_rotate_list.append(bbox_rotate)
            bbox_rotate_list.append('\n')
        return bbox_rotate_list
          

    def calculate_points(self, bbox):
        classname, x_center, y_center, width, height = bbox.split()
        v = np.array([float(x_center),float(y_center)])
        m = self.rotation_matrix()
        coordinate = m @ v.T
        x_pixel, y_pixel, width_new, height_new = self.set_corr_img_pixel(coordinate, width, height)
        bbox_rotate = "{}, {:f}, {:f}, {:f}, {:f}".format(int(classname), float(x_pixel), float(y_pixel), float(width_new), float(height_new))       
        bbox_rotate = bbox_rotate.replace(',', '')
        return bbox_rotate
   
    def set_corr_img_pixel(self, coordinates, width, height):
        x, y = coordinates
        def set_pix_90():
            return x + 1, y, height, width
        def set_pix_180():
            return x + 1, y + 1, width, height
        def set_pix_270():
            return x, y + 1, height, width

        switch = {
            90:  set_pix_90(),
            180: set_pix_180(),
            270: set_pix_270(),                      
        }
        return switch.get(int(self.angle), "error in set_coor_img_pixel()")

    def rotation_matrix(self):
        def rotationmatrix_90():
            return np.array(((0,-1),(1,0)))

        def rotationmatrix_180():
            return np.array(((-1,0),(0,-1)))

        def rotationmatrix_270():
            return np.array(((0,1),(-1,0)))
        
        switch = {
            90:  rotationmatrix_90(),
            180: rotationmatrix_180(),
            270: rotationmatrix_270(),                      
        }
        return switch.get(int(self.angle), "error in rotation_matrix()")
        