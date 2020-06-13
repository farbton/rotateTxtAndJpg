import os
#import cv2 

class Reader(object):
    def __init__(self, source_dir):
        self.source_dir = source_dir

    #def get_list_of_filenames(self, txt_file_names_list):
    #    images_files_names = []
    #    #TODO:Liste aus listen:[[img,txt],[img,txt]]



    def get_list_of_filenames(self):
        list_of_filenames = []
        txt_filename = ""
        jpg_filename = ""

        for i, filename in enumerate(os.listdir(self.source_dir)):
            #print(i, filename)
            if filename.endswith('.txt'):
                txt_filename = os.path.join(self.source_dir, filename)
                jpg_filename = os.path.splitext(txt_filename)[0]
                list_of_filenames.append((txt_filename, (jpg_filename+".jpg")))
        #print(*list_of_filenames, sep = "\n")
        return list_of_filenames


    def get_bbox_list(self,txt_filename):
       #print(txt_filename)
       bbox_list = []
       txt_file = open(txt_filename)
       bbox_list = txt_file.readlines()
       return bbox_list

       