from tkinter import *
from PIL import ImageTk, Image
from playsound import playsound
import sys
import os

def raise_error(title1, text1):
    error = Tk()
    error.title(title1)
    errornote = Label(error, text=text1)
    def close_error():
        error.destroy()
    okbtn = Button(error, text = 'OK', command=close_error)
    errornote.pack()
    okbtn.pack()
    error.mainloop()

window = Tk()
window.title('核彈引爆器')
title = Label(window, text='核彈引爆器', font = ('Arial', 22))
info = Label(window, text = '在引爆核彈之前，請確認一下內容...')

img = ImageTk.PhotoImage(Image.open('icon.jpg'))
pic = Label(window, image = img)
chk_state = BooleanVar()
chk_state.set(False)
cb1 = Checkbutton(window, text='沒有人能夠檢視你的電腦屏幕', var=chk_state, onvalue = True, offvalue=False)
chk_state1 = BooleanVar()
chk_state1.set(False)
cb2 = Checkbutton(window, text='電腦的揚聲器音量已為最高', var=chk_state1, onvalue = True, offvalue=False)
chk_state2 = BooleanVar()
chk_state2.set(False)
cb3 = Checkbutton(window, text='附近的人（如果有）都能聽到', var=chk_state2, onvalue = True, offvalue=False)
def ready():
    
    if chk_state.get() == True and (chk_state1.get() == True and chk_state2.get() == True):
        stment = Tk()
        stment.title('聲明')
        std = Text(stment)
        std.insert(END, '版權聲明\n本產品[核彈發射器v1.14.514]由Viktor&CO提供，該應用程式所有資料之著作權、所有權與智慧財產權，包括文字、圖片、聲音、影像、軟體、編曲…等，均為麥書原創作品或依法向原作者或代理人機構取得合法重製授權。未經麥書文化許可，禁止任何形式的複製、重製，直接或間接做為商業用途使用。\n免責聲明\n本公司不會對任何錯誤或遺漏承擔責任。 本公司不會對使用或任何人士使用本網頁而引致任何損害（包括但不限於電腦病毒、系統固障、資料損失）承擔任何賠償。 本應用程式可能會連結至其他機構所提供的模塊，但這些模塊並不是由本公司所控制。 本公司不會對這些模塊所顯示的內容作出任何保證或承擔任何責任。')
        def getvarcb():
            if agree_state.get() == False:
                agree_state.set(True)
            else:
                agree_state.set(False)
        def get2():
            if email_state.get() == False:
                email_state.set(True)
            else:
                email_state.set(False)
        def get3():
            if lw_state.get() == False:
                lw_state.set(True)
            else:
                lw_state.set(False)

        global lw_state
        global agree_state
        global email_state
        agree_state = BooleanVar()
        agree_state.set(False)
        agree = Checkbutton(stment, text = '我同意上述條款也願意承擔啟動該應用程式的風險', var=agree_state, onvalue = True, offvalue=False, command = getvarcb)
        '''
        email_state = BooleanVar()
        email_state.set(False)
        email = Checkbutton(stment, text='我希望將上述條款傳送至我的郵箱', var=email_state, onvalue = True, offvalue=False, command = get2)
        '''
        lw_state = BooleanVar()
        lw_state.set(False)
        lastword = Checkbutton(stment, text='我希望使用該軟件將我的遺言保存到此計算機上',var = lw_state, onvalue = True, offvalue=False, command = get3)
        
        std.pack()
        agree.pack()
        '''
        email.pack()
        '''
        lastword.pack()
        
        
        def gofinal():
            if agree_state.get() == 1:
                '''
                if email_state.get() == True:
                    email = Tk()
                    email.title('請輸入你的電子郵箱|Quelqu\'un@example.com')
                    temp = StringVar()
                    email_entry = Entry(email, textvariable = temp)
                    note = Label(email, text = '輸入你的電子郵箱:')
                    def end_this():
                        email.destroy()
                    end_email = Button(email, text = 'OK', command = end_this)
                    note.pack()
                    email_entry.pack()
                    end_email.pack()
                    email.mainloop()
                    '''
                if lw_state.get() == True:
                    lw = Tk()
                    lw.title('遺言')
                    lwtex = Text(lw, height=10)
                    lwtex.insert('1.0','希望天堂沒有核彈發射器，雖然你和我相處的時間可能只有短短10分鐘，請容許我在此獻上最後的道別\n大衛·西斯林坦\nR.I.P')
                    lwtex.pack()
                    def gettext():
                        result = lwtex.get('1.0','end')
                        file = open('遺言.txt','a')
                        file.close()
                        file = open('遺言.txt','w')
                        file.write('')
                        file.close()
                        file = open('遺言.txt','a')
                        file.write(result)
                        file.close()
                        #raise_error('完成','你的遺言已保存至該應用程式的根目錄下...')
                        lw.destroy()
                        print('7')
                        stment.destroy()
                        window.destroy()
                    complete = Button(lw, text='完成',command = gettext)
                    complete.pack()
                    lw.mainloop()
                window.destroy()
                stment.destroy()
            else:
                print(agree_state.get())
                raise_error('無法繼續執行','請同意條款以繼續...')
                
        final = Button(stment, text = '繼續', command=gofinal)
        final.pack()
        stment.mainloop()
    else:
        raise_error('無法繼續執行','我們認為你還未就緒，當三個選項框都為True後才能繼續...')
Continue = Button(window, text='我已就緒', command=ready)

title.grid(column = 1, row = 0)
info.grid(column = 1, row = 1)
pic.grid(column = 1, row = 2)
cb1.grid(column=1,row=3)
cb2.grid(column=1,row=4)
cb3.grid(column=1,row=5)
Continue.grid(column=1,row=6)

window.mainloop()
main = Tk()
main.title('危險')
danger = Label(main, text='核彈已發射...',font=('Arial',50))
'''
img1 = ImageTk.PhotoImage(Image.open('hy.jpg'))
hpic = Label(main, image = img1)
'''
try:
    if agree_state.get() == True:
        pass
    else:
        sys.exit(1)
        quit()
except:
    sys.exit(1)
    quit()
img2 = ImageTk.PhotoImage(Image.open('sdl2.png'))
hpic1 = Label(main,image = img2)
danger.grid(column = 0, row = 0)
#hpic.grid(column = 0, row = 1)
hpic1.grid(column = 0, row = 1)
playsound('hm.wav', False)
main.mainloop()

    
