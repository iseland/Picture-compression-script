from  PIL  import Image
from glob import glob
import os
import tkinter as tk
from tkinter import filedialog



def resize_images_1(source_dir ,target_dir,threshold):
    #遍历指定路径文件
	filenames = glob('{}/*'.format(source_dir))
	for filename in filenames:
        #得到图片文件大小
		filesize = os.path.getsize(filename)
		if filesize>=threshold:
			print(filename)
			with Image.open(filename) as im:
				width , height = im.size
				new_width =width
				while True:
					new_width =new_width-5
					new_height = int(new_width * height * 1.0 / width)
					if  new_width*new_height<=threshold:
						break

				resized_im = im.resize((new_width,new_height))
				output_filename = filename.replace(source_dir, target_dir)
                #将压缩后图片另存为新的文件夹中
				resized_im.save(output_filename)

def mode2():
    def mode2_confirm():
        #读取要压缩图片
        filenames = glob('{}/*'.format(source_dir))
        for filename in filenames:
            print(filename)
            #读取输入值并赋给变量
            width = int(new_width.get())
            height = int(new_height.get())

            resized_im = Image.open(filename).resize((width, height))
            output_filename = filename.replace(source_dir, target_dir)
            resized_im.save(output_filename)
        # 然后销毁窗口。
        mode2_window.destroy()

    source_dir = filedialog.askdirectory(title=u"选择压缩文件夹路径:")
    target_dir = filedialog.askdirectory(title=u"选择文件保存文件夹")
    #建立主窗口的子窗口
    mode2_window = tk.Toplevel()
    mode2_window.title('小文图片压缩')
    mode2_window.geometry('400x200')
    #设定压缩长度数值
    new_width = tk.StringVar()
    tk.Label(mode2_window, text='请输入图片长度值 ').place(x=10, y=50)
    entry_usr_nmr = tk.Entry(mode2_window, textvariable=new_width)
    entry_usr_nmr.place(x=140, y=50)

    # 设定压缩长度数值
    new_height = tk.StringVar()
    tk.Label(mode2_window, text='请输入图片宽度值 ').place(x=10, y=100)
    entry_usr_nmr = tk.Entry(mode2_window, textvariable=new_height)
    entry_usr_nmr.place(x=140, y=100)
#设定确认按钮
    tk.Button(mode2_window, text='开始压缩',command=mode2_confirm).pack()

def mode1():
    def mode1_confirm():
        threshold = float(int(new_nmr.get())* 1024 * 1024)
        resize_images_1(source_dir, target_dir, threshold)
        # 然后销毁窗口。
        mode1_window.destroy()
    #读取要压缩文件夹路径、另存为路径
    source_dir = filedialog.askdirectory(title=u"选择压缩文件夹路径:")
    target_dir = filedialog.askdirectory(title=u"选择文件保存文件夹")
    #建立主窗口的子窗口
    mode1_window = tk.Toplevel()
    mode1_window.title('小文图片压缩')
    mode1_window.geometry('400x200')
    #设定压缩数值
    new_nmr = tk.StringVar()
    tk.Label(mode1_window, text='请输入压缩值（单位M） ').place(x=10, y=50)
    entry_usr_nmr = tk.Entry(mode1_window, textvariable=new_nmr)
    entry_usr_nmr.place(x=140, y=50)

#设定确认按钮
    tk.Button(mode1_window, text='开始压缩',command=mode1_confirm).pack()




