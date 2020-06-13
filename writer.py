import os
import cv2

class Writer(object):
    def __init__(self, out_dir, angle):
        self.out_dir = out_dir
        self.angle = angle

    def give_angle_ext(self):
        def set_90():
            return ("_rot90")
        def set_180():
            return ("_rot180")
        def set_270():
            return ("_rot270")

        switch = {
            90:  set_90(),
            180: set_180(),
            270: set_270(),                      
        }
        return switch.get(int(self.angle), "error in give_angle_ext()")

    def write_rotate_bbox_list(self, txt_filename, bbox_list_rotated):
        head, tail = os.path.split(txt_filename)
        file_name, file_ext = os.path.splitext(tail)
        angle_ext = self.give_angle_ext()
        new_file_name = file_name + angle_ext + file_ext
        new_file_path = self.out_dir + "\\" + new_file_name
        new_file = open(new_file_path, "w")
        new_file.writelines(str(bbox) for bbox in bbox_list_rotated)
        new_file.close()

    def write_img_rotated(self, jpg_filename, img_rotated):
        head, tail = os.path.split(jpg_filename)
        file_name, file_ext = os.path.splitext(tail)
        angle_ext = self.give_angle_ext()
        new_file_name = file_name + angle_ext + file_ext
        new_file_path = self.out_dir + "\\" + new_file_name
        name = os.path.splitext(jpg_filename)[0]
        cv2.imwrite(new_file_path, img_rotated)
        
