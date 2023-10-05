from tkinter import *


tk = Tk()
# 함수 정의 (버튼을 누르면 텍스트 내용이 바뀜)
def event():
    button['text'] = '버튼 누름!'

button = Button(tk,text='버튼입니다. 누르면 함수가 실행됩니다.',command=event)
button2 = Button(tk,text='버튼2 입니다.')
button.pack(side=LEFT,padx=10,pady=10) #side로 배치설정, padx로 좌우 여백설정, pady로 상하 여백설정 
button2.pack(side=LEFT, padx=10, pady= 10)
tk.mainloop()
