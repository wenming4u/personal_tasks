#-*- coding: utf-8 -*-
from selenium import webdriver
import time
from datetime import date, datetime, timedelta
from pymouse import PyMouse 
import win32api
import win32con
import win32gui
import ctypes
from Tkinter import *
import Tkinter
import tkMessageBox

url = "http://moni.51hupai.org/" 
numdict = {"0":"96","1":"97","2":"98","3":"99","4":"100","5":"101","6":"102","7":"103","8":"104","9":"105"}

class RECT(ctypes.Structure):
    _fields_ = [('left', ctypes.c_int),  
                ('top', ctypes.c_int),  
                ('right', ctypes.c_int),  
                ('bottom', ctypes.c_int)]

def get_cords():
	rect = RECT()
	HWND = win32gui.GetForegroundWindow()#获取当前窗口句柄
	ctypes.windll.user32.GetWindowRect(HWND, ctypes.byref(rect))#获取当前窗口坐标
	return rect 

def automation(x,y,amt):
	numdict = {"0":"96","1":"97","2":"98","3":"99","4":"100","5":"101","6":"102","7":"103","8":"104","9":"105"}
	m = PyMouse()
	x1 = x+60
	y1 = y
	m.click(x1,y1)#鼠标移动到xy位置
	n = str(amt)
	for i in range(len(n)):
		x = numdict[n[i]]
		win32api.keybd_event(int(x),0,0,0)  #v键位码是86
		win32api.keybd_event(int(x),0,win32con.KEYEVENTF_KEYUP,0) #释放按键
	time.sleep(0.2)
	x2 = x1+117
	m.click(x2,y1)#移动并且在xy位置点击
	y2 = y1+105
	time.sleep(0.2)
	m.click(x2,y2)#移动并且在xy位置点击,左右键点击
	x3 = x2-245
	y3 = y2+84
	m.move(x3,y3)

def confirm(x,y):
	m = PyMouse()
	p = m.position()
	print p
	m.click(p[0],p[1])


def test(bidtime=48,confirmtime=57,refreshtime=58,amt=700): #默认参数后必须都是默认参数
	mydriver=webdriver.Ie()
	mydriver.set_page_load_timeout(10)
	mydriver.get(url)
	now = datetime.now()
	strnow = now.strftime('%Y-%m-%d %H:%M:%S')
	print "now time:",str(strnow)
	# strnext_time = now.strftime('2017-01-12 11:29:45')
	# strconfirm_time = now.strftime('2017-01-12 11:30:55')
	# refresh_time = now.strftime('2017-02-06 14:49:'+str(refreshtime)) #'2017-01-19 13:28:58'
	refresh_time2 = ((datetime.now() + timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:')+str(refreshtime)) 
	# strnext_time = now.strftime('2017-02-06 14:50:'+str(bidtime)) #'2017-01-19 13:29:48'
	strnext_time2 = ((datetime.now() + timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:')+str(bidtime)) 
	# strconfirm_time = now.strftime('2017-02-06 14:50:'+str(confirmtime)) #'2017-01-19 13:29:57'
	strconfirm_time2 = ((datetime.now() + timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:')+str(confirmtime)) 
	while True:
		strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print strnow,refresh_time2
		time.sleep(0.1)
		if str(strnow) == str(refresh_time2):
			print strnow
			mydriver.refresh()
			print "refresh."
			break
	print "call time:",str(strnext_time2)
	print "confirm time:",str(strconfirm_time2)
	print 'get cords'
	while True:
		strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print strnow,strnext_time2
		time.sleep(0.1)
		if str(strnow) == str(strnext_time2):
			print strnow
			rect=get_cords()
			x1 = (rect.left+rect.right)/2+175
			y1 = rect.top+382
			automation(x1,y1,amt)
			print "called."
			break
	while True:
		strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		if str(strnow) == str(strconfirm_time2):
			rect=get_cords()
			x2 = (rect.left+rect.right)/2+175
			y2 = rect.top+382
			confirm(x2,y2)
			print "confirmed."
			break

def real(bidtime=48,confirmtime=56,amt=700,xcord=0,ycord=385): #默认参数后必须都是默认参数
	# mydriver=webdriver.Ie()
	# mydriver.set_page_load_timeout(10)
	# mydriver.get(url)
	now = datetime.now()
	strnow = now.strftime('%Y-%m-%d %H:%M:%S')
	print "now time:",str(strnow)
	strnext_time2 = datetime.now().strftime('%Y-%m-%d ')+'11:29:'+str(bidtime)
	strconfirm_time2 = datetime.now().strftime('%Y-%m-%d ')+'11:29:'+str(confirmtime)
	print "call time:",str(strnext_time2)
	print "confirm time:",str(strconfirm_time2)
	print 'get cords'
	while True:
		strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print strnow,strnext_time2
		time.sleep(0.1)
		if str(strnow) == str(strnext_time2):
			print strnow
			rect=get_cords()
			if xcord == 0:
				x1 = (rect.left+rect.right)/2+175
			else:
				x1 = xcord + rect.left
			y1 = rect.top+ycord
			automation(x1,y1,amt)
			print "called."
			break
	while True:
		strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		if str(strnow) == str(strconfirm_time2):
			rect=get_cords()
			if xcord == 0:
				x2 = (rect.left+rect.right)/2+175
			else:
				x2 = xcord + rect.left
			y2 = rect.top+ycord
			confirm(x2,y2)
			print "confirmed."
			break

def psudo_real(bidtime=48,confirmtime=56,amt=700,xcord=0,ycord=385): #默认参数后必须都是默认参数
	# mydriver=webdriver.Ie()
	# mydriver.set_page_load_timeout(10)
	# mydriver.get(url)
	now = datetime.now()
	strnow = now.strftime('%Y-%m-%d %H:%M:%S')
	print "now time:",str(strnow)
	strnext_time2 = ((datetime.now() + timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:')+str(bidtime)) 
	strconfirm_time2 = ((datetime.now() + timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:')+str(confirmtime)) 
	print "call time:",str(strnext_time2)
	print "confirm time:",str(strconfirm_time2)
	print 'get cords'
	while True:
		strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print strnow,strnext_time2
		time.sleep(0.1)
		if str(strnow) == str(strnext_time2):
			print strnow
			rect=get_cords()
			print rect.left,rect.top
			if xcord == 0:
				x1 = (rect.left+rect.right)/2+175
			else:
				x1 = xcord + rect.left
			y1 = rect.top+ycord
			print '---'
			print x1, y1
			automation(x1,y1,amt)
			print "called."
			break
	while True:
		strnow = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		if str(strnow) == str(strconfirm_time2):
			rect=get_cords()
			if xcord == 0:
				x2 = (rect.left+rect.right)/2+175
			else:
				x2 = xcord + rect.left
			y2 = rect.top+ycord
			confirm(x2,y2)
			print "confirmed."
			break


# def tick():
#     global time1
#     # 从运行程序的计算机上面获取当前的系统时间
#     time2 = time.strftime('%H:%M:%S')
#     # 如果时间发生变化，代码自动更新显示的系统b时间
#     if time2 != time1:
#         time1 = time2
#         clock.config(text=time2)
#         # calls itself every 200 milliseconds
#         # to update the time display as needed
#         # could use >200 ms, but display gets jerky
#     clock.after(200, tick)

# time1 = ''

root = Tk()
root.title('撒网拍牌')
root.geometry('280x460') 
# canvas = Tkinter.Canvas(root,  
#         width = 300,      # 指定Canvas组件的宽度  
#         height = 420,      # 指定Canvas组件的高度  
#         bg = 'white')      # 指定Canvas组件的背景色  
# canvas.pack()
l = Label(root, fg='red', bg='white',text='William的大杀器')
l.pack(ipadx='600p',ipady='15p')
# status = Label(root, text="v1.0", bd=1, relief=SUNKEN, anchor=W)
# status.pack(ipadx='600p',ipady='10p')
# clock = Label(root, font=('times', 20, 'bold'), bg='green')
# clock.grid(row=0, column=1) 
# tick()
l1 = Label(root, text = '出价时间(秒）')
l1.pack()
e1 = Entry(root, text = '秒')
e1.pack()
l2 = Label(root, text = '确认时间(秒)')
l2.pack()
e2 = Entry(root, text = '确认时间')
e2.pack()
# l3 = Label(root, text = '刷新时间(模拟才填)')
# l3.pack()
# e3 = Entry(root, text = '刷新时间')
# e3.pack()
l4 = Label(root, text = '加价金额(元)')
l4.pack()
e4 = Entry(root, text = '加价金额')
e4.pack()

l5 = Label(root, text = 'x偏移量')
l5.pack()
e5 = Entry(root, text = 'x偏移量')
e5.pack()

l6 = Label(root, text = 'y偏移量')
l6.pack()
e6 = Entry(root, text = 'y偏移量')
e6.pack()
 
def btn_test():
	bidtime = int(e1.get())
	confirmtime = int(e2.get())
	refreshtime = int(e3.get())
	amt = int(e4.get())
	if bidtime<60 and confirmtime<60 and refreshtime<60:
		tkMessageBox.showinfo('确认', '已确认, %s秒加价%s元，并在%s秒自动确定' % (bidtime,amt,confirmtime))
		test(bidtime,confirmtime,refreshtime,amt)
	else:	
		tkMessageBox.showinfo('出错','所填时间为秒数，当前输入大于60，请重新填写')

def btn_real():
	bidtime = int(e1.get())
	confirmtime = int(e2.get())
	amt = int(e4.get())
	if e5.get():
		xcord = int(e5.get())
		ycord = int(e6.get())
	else:
		xcord = 0
		ycord = 385
	if bidtime<60 and confirmtime<60:
		tkMessageBox.showinfo('确认', '已确认, %s秒加价%s元，并在%s秒自动确定' % (bidtime,amt,confirmtime))
		real(bidtime,confirmtime,amt,xcord,ycord)
	else:	
		tkMessageBox.showinfo('出错','所填时间为秒数，当前输入大于60，请重新填写')

def btn_psudo_real():
	bidtime = int(e1.get())
	confirmtime = int(e2.get())
	amt = int(e4.get())
	if e5.get():
		xcord = int(e5.get())
		ycord = int(e6.get())
	else:
		xcord = 0
		ycord = 385
	if bidtime<60 and confirmtime<60:
		tkMessageBox.showinfo('确认', '已确认, %s秒加价%s元，并在%s秒自动确定' % (bidtime,amt,confirmtime))
		psudo_real(bidtime,confirmtime,amt,xcord,ycord)
	else:	
		tkMessageBox.showinfo('出错','所填时间为秒数，当前输入大于60，请重新填写')


l4a = Label(root, text = '')
l4a.pack()
l5 = Label(root, text = '点击确认')
l5.pack()
# b = Button(root, text='模拟', command=btn_test)
# b['width'] = 10
# b['height'] = 1
# b.pack()
b2 = Button(root, text='实战', command=btn_real)
b2['width'] = 14
b2['height'] = 2
b2.pack()
lt2 = Label(root,height=1)
lt2.pack()
b3 = Button(root, text='测试', command=btn_psudo_real)
b3['width'] = 14
b3['height'] = 2
b3.pack()
# b.grid(row = 5, column = 1)
l4b = Label(root, text = '')
l4b.pack()
mail = Label(root, fg='red', bg='white',text='wenming4u@163.com')
mail.pack(ipadx='600p',ipady='15p')

root.mainloop()