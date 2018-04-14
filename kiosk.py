from tkinter import *
from tkinter import font
from itertools import cycle
import time

preview1 = ['preview/1-1.png','preview/1-2.png','preview/1-3.png','preview/1-4.png','preview/1-5.png']
preview2 = ['preview/2-1.png','preview/2-2.png','preview/2-3.png']
preview3 = ['preview/3-1.png','preview/3-2.png','preview/3-3.png']
preview4 = ['preview/5-1.png','preview/5-2.png','preview/5-3.png']
preview5 = ['preview/4-1.png','preview/4-2.png','preview/4-3.png','preview/4-4.png']
preview6 = ['preview/6-1.png','preview/6-2.png','preview/6-3.png']

class Application(Canvas):
    def __init__(self, master = None):
        self.master = master
        Canvas.__init__(self, width=800,height=480)

        self.init_ui()

    def init_ui(self):

        #Background 설정
        
        self.config(bg='#403A35')
        self.grid(column=0, row=0)

        self.photoBg = PhotoImage(file = "bg.png")
        bg = self.create_image(0,0,anchor='nw',image = self.photoBg)

        #Button1
        self.photo1 = PhotoImage(file="icon/school_icon.png")
        self.button1 = Button(width=360, height=230, image=self.photo1, bg='#403A35', activebackground='#403A35', 
                            borderwidth=0, relief=FLAT,command = self.click1)


        self.button1.configure(width=360, height=230, activebackground='#403A35',  highlightthickness=0)
        but1 = self.create_window(60, 75, anchor='nw', window=self.button1, tags = 'button')


        #Button2
        self.photo2 = PhotoImage(file="icon/sub_button1.png")
        self.button2 = Button(width=150, height= 160, image=self.photo2, bg='#403A35', activebackground='#403A35',
                            borderwidth=0, relief=FLAT, command = self.click2)
        self.button2.configure(width=150, height=160, activebackground='#403A35', highlightthickness=0)
        but2 = self.create_window(430, 75, anchor='nw', window=self.button2,tags = 'button')


        #Button3
        self.photo3 = PhotoImage(file="icon/sub_button2.png")
        self.button3 = Button(width=150, height= 160, image=self.photo3, bg='#403A34', activebackground='#403A34',
                            borderwidth=0, relief=FLAT, command =self.click3)
        self.button3.configure(width=150, height=160, activebackground='#403A34', highlightthickness=0)
        but3 = self.create_window(590, 75, anchor='nw', window=self.button3, tags = 'button')


        #Button4
        self.photo4 = PhotoImage(file="icon/sub_button3.png")
        self.button4 = Button(width=150, height= 160, image=self.photo4, bg='#403A34', activebackground='#403A34',
                            borderwidth=0, relief=FLAT, command = self.click4)
        self.button4.configure(width=150, height=160, activebackground='#403A34', highlightthickness=0)
        but4 = self.create_window(430, 245, anchor='nw', window=self.button4, tags = 'button')


        #Button5
        self.photo5 = PhotoImage(file="icon/sub_button4.png")
        self.button5 = Button(width=150, height= 160, image=self.photo5, bg='#403A34', activebackground='#403A34',
                            borderwidth=0, relief=FLAT, command = self.click5)
        self.button5.configure(width=150, height=160, activebackground='#403A34', highlightthickness=0)
        but5 = self.create_window(590, 245, anchor='nw', window=self.button5, tags = 'button')



        #Button6
        self.photo6 = PhotoImage(file="icon/narshya-icon.png")
        self.button6 = Button(width=360, height= 90, image=self.photo6, bg='#403A35', activebackground='#403A35',
                            borderwidth=0, relief=FLAT,command  =self.click6)
        self.button6.configure(width=360, height=90, activebackground='#403A35', highlightthickness=0)
        but5 = self.create_window(60, 315, anchor='nw', window=self.button6, tags = 'button')


    #Button 1 클릭 이벤트
    #대구소프트웨어고등학교 소개
    def click1(self):
        print('click 1')
        self.previewA = cycle((PhotoImage(file = image)) for image in preview1)
        self.previewA_display = Label(self)

        self.photoClose = PhotoImage(file = "preview/close.png")
        self.close = Button(width = 48, height = 38, image = self.photoClose, borderwidth  =0, command=self.close1, relief=FLAT,highlightthickness=0)
        clo = self.create_window(678,71, anchor = 'nw', window = self.close,tags = 'sub_button')

        self.photoNext = PhotoImage(file = "preview/next.png")
        self.next = Button(width = 40, height = 38, image = self.photoNext, borderwidth = 0,command = self.show1,relief = FLAT,highlightthickness=0)
        ne = self.create_window(628, 71, anchor = 'nw', window = self.next,tags = 'sub_button')

        self.photoPrev = PhotoImage(file = "preview/prev.png")
        self.prev = Button(width = 40, height = 38, image = self.photoPrev, borderwidth = 0,command = self.prev1, relief = FLAT,highlightthickness=0)
        ne = self.create_window(583, 71, anchor = 'nw', window = self.prev,tags = 'sub_button')

        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        
        self.show1()
        
    def show1(self):
        self.img_object = next(self.previewA)
        self.previewA_display.config(image=self.img_object)
        self.previewA_display.place(x=60,y=60,anchor='nw')

    def prev1(self):
        for i in range(len(preview1)-2) :
            self.img_oobject = next(self.previewA)
        self.show1()
                                                        
    def close1(self):                   # 슬라이더 삭제
        self.previewA_display.destroy()
        self.delete('sub_button')
        self.init_ui()



    #sub_Button1 클릭 이벤트
    #Iot 소개
    def click2(self):
        print('click2')
        self.previewB = cycle((PhotoImage(file = image)) for image in preview2)
        self.previewB_display = Label(self)

        self.photoClose = PhotoImage(file = "preview/close.png")
        self.close = Button(width = 48, height = 38, image = self.photoClose, borderwidth  =0, command=self.close2, relief=FLAT,highlightthickness=0)
        clo = self.create_window(678,71, anchor = 'nw', window = self.close,tags = 'sub_button')

        self.photoNext = PhotoImage(file = "preview/next.png")
        self.next = Button(width = 40, height = 38, image = self.photoNext, borderwidth = 0,command = self.show2,relief = FLAT,highlightthickness=0)
        ne = self.create_window(628, 71, anchor = 'nw', window = self.next,tags = 'sub_button')

        self.photoPrev = PhotoImage(file = "preview/prev.png")
        self.prev = Button(width = 40, height = 38, image = self.photoPrev, borderwidth = 0,command = self.prev2, relief = FLAT,highlightthickness=0)
        ne = self.create_window(583, 71, anchor = 'nw', window = self.prev,tags = 'sub_button')

        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        
        self.show2()

        
    def show2(self):
        self.img_object = next(self.previewB)
        self.previewB_display.config(image=self.img_object)
        self.previewB_display.place(x=60,y=60,anchor='nw')

    def prev2(self):
        for i in range(len(preview2)-2) :
            self.img_oobject = next(self.previewB)
        self.show2()
                                                        
    def close2(self):                   # 슬라이더 삭제
        self.previewB_display.destroy()
        self.delete('sub_button')
        self.init_ui()


    #sub_Button2 클릭 이벤트
    #스마트홈 소개
    def click3(self):
        print('click3')
        self.previewC = cycle((PhotoImage(file = image)) for image in preview3)
        self.previewC_display = Label(self)

        self.photoClose = PhotoImage(file = "preview/close.png")
        self.close = Button(width = 48, height = 38, image = self.photoClose, borderwidth  =0, command=self.close3, relief=FLAT,highlightthickness=0)
        clo = self.create_window(678,71, anchor = 'nw', window = self.close,tags = 'sub_button')

        self.photoNext = PhotoImage(file = "preview/next.png")
        self.next = Button(width = 40, height = 38, image = self.photoNext, borderwidth = 0,command = self.show3,relief = FLAT,highlightthickness=0)
        ne = self.create_window(628, 71, anchor = 'nw', window = self.next,tags = 'sub_button')

        self.photoPrev = PhotoImage(file = "preview/prev.png")
        self.prev = Button(width = 40, height = 38, image = self.photoPrev, borderwidth = 0,command = self.prev3, relief = FLAT,highlightthickness=0)
        ne = self.create_window(583, 71, anchor = 'nw', window = self.prev,tags = 'sub_button')

        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        
        self.show3()

        
    def show3(self):
        self.img_object = next(self.previewC)
        self.previewC_display.config(image=self.img_object)
        self.previewC_display.place(x=60,y=60,anchor='nw')

    def prev3(self):
        for i in range(len(preview3)-2) :
            self.img_oobject = next(self.previewC)
        self.show3()
                                                        
    def close3(self):                   # 슬라이더 삭제
        self.previewC_display.destroy()
        self.delete('sub_button')
        self.init_ui()



    #sub_Button3 이벤트
    #소프트웨어 개발과 소개
    def click4(self):
        print('click4')
        self.previewD = cycle((PhotoImage(file = image)) for image in preview4)
        self.previewD_display = Label(self)

        self.photoClose = PhotoImage(file = "preview/close.png")
        self.close = Button(width = 48, height = 38, image = self.photoClose, borderwidth  =0, command=self.close4, relief=FLAT,highlightthickness=0)
        clo = self.create_window(678,71, anchor = 'nw', window = self.close,tags = 'sub_button')

        self.photoNext = PhotoImage(file = "preview/next.png")
        self.next = Button(width = 40, height = 38, image = self.photoNext, borderwidth = 0,command = self.show4,relief = FLAT,highlightthickness=0)
        ne = self.create_window(628, 71, anchor = 'nw', window = self.next,tags = 'sub_button')

        self.photoPrev = PhotoImage(file = "preview/prev.png")
        self.prev = Button(width = 40, height = 38, image = self.photoPrev, borderwidth = 0,command = self.prev4, relief = FLAT,highlightthickness=0)
        ne = self.create_window(583, 71, anchor = 'nw', window = self.prev,tags = 'sub_button')

        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        
        self.show4()

        
    def show4(self):
        self.img_object = next(self.previewD)
        self.previewD_display.config(image=self.img_object)
        self.previewD_display.place(x=60,y=60,anchor='nw')

    def prev4(self):
        for i in range(len(preview4)-2) :
            self.img_oobject = next(self.previewD)
        self.show4()
                                                        
    def close4(self):                   # 슬라이더 삭제
        self.previewD_display.destroy()
        self.delete('sub_button')
        self.init_ui()


    #sub_Button4 이벤트
    #임베디드 프로그래밍과과 소개
    def click5(self):
        print('click5')
        self.previewE = cycle((PhotoImage(file = image)) for image in preview5)
        self.previewE_display = Label(self)

        self.photoClose = PhotoImage(file = "preview/close.png")
        self.close = Button(width = 48, height = 38, image = self.photoClose, borderwidth  =0, command=self.close5, relief=FLAT,highlightthickness=0)
        clo = self.create_window(678,71, anchor = 'nw', window = self.close,tags = 'sub_button')

        self.photoNext = PhotoImage(file = "preview/next.png")
        self.next = Button(width = 40, height = 38, image = self.photoNext, borderwidth = 0,command = self.show5,relief = FLAT,highlightthickness=0)
        ne = self.create_window(628, 71, anchor = 'nw', window = self.next,tags = 'sub_button')

        self.photoPrev = PhotoImage(file = "preview/prev.png")
        self.prev = Button(width = 40, height = 38, image = self.photoPrev, borderwidth = 0,command = self.prev5, relief = FLAT,highlightthickness=0)
        ne = self.create_window(583, 71, anchor = 'nw', window = self.prev,tags = 'sub_button')

        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        
        self.show5()

        
    def show5(self):
        self.img_object = next(self.previewE)
        self.previewE_display.config(image=self.img_object)
        self.previewE_display.place(x=60,y=60,anchor='nw')

    def prev5(self):
        for i in range(len(preview5)-2) :
            self.img_oobject = next(self.previewE)
        self.show5()
                                                        
    def close5(self):                   # 슬라이더 삭제
        self.previewE_display.destroy()
        self.delete('sub_button')
        self.init_ui()


    #Button2 이벤트
    #나르샤 소개
    def click6(self):
        print('click6')
        self.previewF= cycle((PhotoImage(file = image)) for image in preview6)
        self.previewF_display = Label(self)

        self.photoClose = PhotoImage(file = "preview/close.png")
        self.close = Button(width = 48, height = 38, image = self.photoClose, borderwidth  =0, command=self.close6, relief=FLAT,highlightthickness=0)
        clo = self.create_window(678,71, anchor = 'nw', window = self.close,tags = 'sub_button')

        self.photoNext = PhotoImage(file = "preview/next.png")
        self.next = Button(width = 40, height = 38, image = self.photoNext, borderwidth = 0,command = self.show6,relief = FLAT,highlightthickness=0)
        ne = self.create_window(628, 71, anchor = 'nw', window = self.next,tags = 'sub_button')

        self.photoPrev = PhotoImage(file = "preview/prev.png")
        self.prev = Button(width = 40, height = 38, image = self.photoPrev, borderwidth = 0,command = self.prev6, relief = FLAT,highlightthickness=0)
        ne = self.create_window(583, 71, anchor = 'nw', window = self.prev,tags = 'sub_button')

        self.button1.destroy()
        self.button2.destroy()
        self.button3.destroy()
        self.button4.destroy()
        self.button5.destroy()
        self.button6.destroy()
        
        self.show6()

        
    def show6(self):
        self.img_object = next(self.previewF)
        self.previewF_display.config(image=self.img_object)
        self.previewF_display.place(x=60,y=60,anchor='nw')

    def prev6(self):
        for i in range(len(preview6)-2) :
            self.img_oobject = next(self.previewF)
        self.show6()
                                                        
    def close6(self):                   # 슬라이더 삭제
        self.previewF_display.destroy()
        self.delete('sub_button')
        self.init_ui()
        

root = Tk()
root.geometry("800x480")
app = Application(master = root)
root.mainloop()
