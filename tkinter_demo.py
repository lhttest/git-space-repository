# 导入tkinter库 一个gui图形界面库
import tkinter as tk


def tkinter():
    # 创建主窗口
    root_window = tk.Tk()
    # 给主窗口设置标题
    root_window.title('python_tkinter')
    # 设置主窗口的大小
    root_window.geometry("450x500")
    # 设置主窗口ico图标
    root_window.iconbitmap('D:/python/Lib/site-packages/robotide/widgets/robot.ico')
    # 设置主窗口的背景色
    root_window["background"] = '#C9C9C9'
    # 添加文本框，在主窗口中，在文本框中添加文字，设置前景色，背景色，font设置文本字体，大小，样式
    text = tk.Label(root_window, text='欢迎使用tkinter框架', bg='yellow', fg='red', font=('Courier New', 16, 'underline'))
    # 将文本添加到主窗口中
    text.pack()
    # 为主窗口添加按钮
    button = tk.Button(root_window, text="关闭", bg="#C9C9C9", command=root_window.quit)
    # 将按钮放入主窗口
    button.pack(side="bottom")
    # 循环主窗口
    root_window.mainloop()
# tkinter()


def two():
    # 实例化主窗口
    window = tk.Tk()
    # 设置主窗口标题
    window.title('我在学tkinter库')
    # 设置主窗口的ico图标
    window.iconbitmap('D:/python/Lib/site-packages/robotide/widgets/robot.ico')
    # 设置主窗口的背景色
    window.config(background='red')
    # 设置主窗口的大小
    window.geometry("500x500")
    # 获取电脑屏幕分辨率
    print("屏幕分辨率为%d%d" % (window.winfo_screenwidth(), window.winfo_screenheight()))
    # 获取主窗口的分辨率，不过首先要刷新
    window.update()
    print("主窗口的分辨率为%d%d" % (window.winfo_width(), window.winfo_height()))
    # 如果使用该函数，resizable()函数不能使用
    # window.resizable(0,0)
    # 设置窗口的处于顶层
    window.attributes('-topmost', True)
    # 设置窗口的透明度
    window.attributes('-alpha', 1)
    # 设置窗口被允许调整的最大范围,与resizable()冲突
    window.maxsize(600, 600)
    # 设置窗口被允许调整的最小范围,与resizable()冲突
    window.minsize(60, 50)
    # 设置文本框label,并使用pack窗口布局管理器进行管理
    text = tk.Label(window,text='你好',bg='yellow',fg='red',font=('Times', 15, 'bold italic underline'))
    text.pack()
    # 设置按钮
    button = tk.Button(window,text='关闭',bg='#C9C9C9',fg='red',font=(200), command=window.quit)
    button.pack(side="bottom")
    # 进入主循环
    window.mainloop()




# 导入对话框控件
from tkinter import messagebox
def 回调函数and协议处理机制的应用():
    # 回调函数，通过封装函数的形式来执行相应的gui控件功能
    # 创建主窗口
    root = tk.Tk()
    root.title('窗口一')
    root.iconbitmap('D:/python/Lib/site-packages/robotide/widgets/robot.ico')
    root.geometry('500x500')
    root.config(background='#C9C9C9')
    def CallBack():
        # 这是一个待会要被执行的回调函数
        root2 = tk.Tk()
        root2.title('窗口二')
        root2.iconbitmap('D:/python/Lib/site-packages/robotide/widgets/robot.ico')
        root2.geometry('700x600')
        root2.config(background='red')
        # 事件绑定机制，使用destory()函数可以实现只关闭该窗口
        button1 = tk.Button(root2,text="关闭",command=root2.destroy)
        button1.pack(side="bottom")
    # 创建一个按钮，并绑定回调函数
    button = tk.Button(root,text="窗口二",bg='#C9C9C9',font=("Arial", 16, "bold"),command=CallBack)
    button.pack(side="left")
    button2 = tk.Button(root,text="关闭",font=("Arial", 16, "bold"),command=root.quit)
    button2.pack(side="right")

    # 协议处理机制WM_DELETE_WINDOW
    # 定义一个回调函数，当用户点击主窗口x退出时，执行用户自定义的函数
    def QueryWindow():
        # 显示一个警告信息，点击确定后，销毁窗口
        if messagebox.showwarning('警告','出现了一个错误'):
            # 这里必须使用destory()关闭窗口，表示只关闭该提示窗口
            root.destroy()
    # 使用协议机制与窗口交互，并回调用户自定义的函数
    root.protocol('WM_DELETE_WINDOW',QueryWindow)
  # 循环主窗口
    root.mainloop()

def 处理主窗口打开位置():
    # 将主窗口打开在屏幕中央
    # 方法一：使用geometry(’450x400+300+200‘)  但是很局限
    # 方法二：计算获取屏幕大小，然后再运算
    window = tk.Tk()
    window.title('中央')
    window.iconbitmap('D:/python/Lib/site-packages/robotide/widgets/robot.ico')
    window.config(background='#C9C9C9')
    # 设置主窗口变量
    width = 500
    height = 500
    # 获取屏幕大小
    screenwidth = window.winfo_screenwidth()
    screenheight = window.winfo_screenheight()
    SizeCenter = '%dx%d+%d+%d' % (width, height, (screenwidth-width)/2, (screenheight-height)/2)
    window.geometry(SizeCenter)
    window.mainloop()


# label边框、填充、宽高设置
def borderwidth():
    window = tk.Tk()
    window.title("学习")
    # window.geometry("2000x600")
    # 设置运行被拉伸的最大范围，设置的值必须大于主窗口的大小
    window.maxsize(800,600)
    window.iconbitmap('D:/python/Lib/site-packages/robotide/widgets/robot.ico')
    window.config(background='#C9C9C9')
    # # label标签文本框
    # text = tk.Label(window,text='我要学习',font=("黑体",20,'bold italic underline'),bg='yellow',
    #                 # 设置标签内容区大小
    #                 width=10,height=10,
    #                 # 设置填充区的大小，边框的大小以及边框样式
    #                 # padx代表填充区的宽，pady代表填充区的高，borderwidth代表边框，relief代表边框的样式
    #                 padx=100,pady=5,borderwidth=10,relief='raised')
    # text.pack()
    # 首先获取gif背景图片的文件地址，默认支持的是gif图片
    photo = tk.PhotoImage(file='C:/Users/lenovo/Desktop/R-C.gif')
    # 将图片放入label文本框中
    tk_photo = tk.Label(window,image=photo,font=(20)).pack(side='right')
    text = "好可爱，\n" \
           "卡哇伊，\n" \
           "太爱了"
    # justify多行文本对齐方式
    lab_text = tk.Label(window,text=text,bg='#C9C9C9',font=("Arial", 16, "bold"),justify='left',
                        width=300,height=10,
                        borderwidth=20)
    lab_text.pack(side='left')
    window.mainloop()
# borderwidth()


