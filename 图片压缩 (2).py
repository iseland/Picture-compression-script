from  PIL  import Image
from glob import glob
import os
import math
import tkinter as tk
from tkinter import filedialog

print("图片压缩脚本                      版本  1.0                   无更新计划                      2019/10/31                    冰洋孤岛")
root = tk.Tk()
root.withdraw()
threshold =  int(input("请输入图片压缩后大小 以下M:"))*1024*1024
source_dir = filedialog.askdirectory(title=u"选择压缩文件夹路径:")
target_dir=filedialog.askdirectory(title=u"选择文件保存文件夹")


def resize_images(source_dir ,target_dir,threshold):
	filenames = glob('{}/*'.format(source_dir))
	for filename in filenames:
		filesize = os.path.getsize(filename)
		if filesize>=threshold :
			print( filename)
			with Image.open(filename) as im:
				width , height = im.size
				new_width =width
				while True:
					new_width =new_width-50
					new_height = int(new_width * height * 1.0 / width)
					if  new_width*new_height<=threshold:
						break


				resized_im = im.resize((new_width,new_height))
				output_filename = filename.replace(source_dir, target_dir)
				resized_im.save(output_filename)
resize_images(source_dir ,target_dir,threshold)

