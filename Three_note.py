import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Three notepad")
root.geometry("400x580")
root.resizable(False, False) # 크기 수정 금지

# 노트패드 정보 알림
def info():
    msgbox.showinfo("메모장 정보", "Three notepad\n2020.09.22\nHarry")
# 첫번째 함수
def firstcopy():
    pass
def firstsave():
    pass
# 두번째 함수
def secondcopy():
    pass
def secondsave():
    pass
# 세번째 함수
def thirdcopy():
    pass
def thirdsave():
    pass
# 모두 저장
def allsave():
    pass

# 메뉴
menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="모두 저장", command=allsave)
menu_file.add_separator()
menu_file.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일", menu=menu_file)
# 도움말 메뉴
menu_question = Menu(menu, tearoff=0)
menu_question.add_command(label="메모장 정보", command=info)
menu.add_cascade(label="도움말", menu=menu_question)

# 제목 프레임
frame_title = Frame(root, padx=5, pady=0)
frame_title.pack(padx=0, pady=0)

# 제목 엔트리 창
title_txt = Entry(frame_title, width=90)
title_txt.pack(side="top", fill="both", expand=True, padx=5, pady=5, ipady=3)
title_txt.insert(0, " 제목을 입력하세요.")

# 첫번째 레이블 프레임
first_frame = LabelFrame(root, padx=5, pady=5, text="01")
first_frame.pack(fill="x", padx=10)

# 첫번째 기능 프레임
first_button_frame = Frame(first_frame)
first_button_frame.pack(fill="y", side="right")
first_copy = Button(first_button_frame, text="복사", width=5, command=firstcopy())
first_copy.pack(padx=2, pady=1)
first_save = Button(first_button_frame, text="저장", width=5, command=firstsave())
first_save.pack(padx=2)

# 첫번째 텍스트 프레임
first_txt_frame = Frame(first_frame) # 첫번째 레이블 프레임에 삽입
first_txt_frame.pack(side="left")

scrollbar1 = Scrollbar(first_txt_frame)
scrollbar1.pack(side="right", fill="y")

first_txt = Text(first_txt_frame, width=42,height=10, yscrollcommand=scrollbar1.set)
first_txt.pack(side="left")
scrollbar1.config(command=first_txt.yview)

# 두번째 레이블 프레임
second_frame = LabelFrame(root, padx=5, pady=5, text="02")
second_frame.pack(fill="x", padx=10, pady=10)

# 두번째 기능 프레임
second_button_frame = Frame(second_frame)
second_button_frame.pack(fill="y", side="right")
second_copy = Button(second_button_frame, text="복사", width=5, command=secondcopy())
second_copy.pack(padx=2, pady=1)
second_save = Button(second_button_frame, text="저장", width=5, command=secondsave())
second_save.pack(padx=2)

# 두번째 텍스트 프레임
second_txt_frame = Frame(second_frame) # 두번째 레이블 프레임에 삽입
second_txt_frame.pack(side="left")

scrollbar2 = Scrollbar(second_txt_frame)
scrollbar2.pack(side="right", fill="y")

second_txt = Text(second_txt_frame, width=42,height=10, yscrollcommand=scrollbar2.set)
second_txt.pack(side="left")
scrollbar2.config(command=second_txt.yview)

# 세번째 레이블 프레임
third_frame = LabelFrame(root, padx=5, pady=5, text="03")
third_frame.pack(fill="x", padx=10)

# 세번째 기능 프레임
third_button_frame = Frame(third_frame)
third_button_frame.pack(fill="y", side="right")
third_copy = Button(third_button_frame, text="복사", width=5, command=thirdcopy())
third_copy.pack(padx=2, pady=1)
third_save = Button(third_button_frame, text="저장", width=5, command=thirdsave())
third_save.pack(padx=2)

# 세번째 텍스트 프레임
third_txt_frame = Frame(third_frame) # 세번째 레이블 프레임에 삽입
third_txt_frame.pack(side="left")

scrollbar3 = Scrollbar(third_txt_frame)
scrollbar3.pack(side="right", fill="y")

third_txt = Text(third_txt_frame, width=42,height=10, yscrollcommand=scrollbar3.set)
third_txt.pack(side="left")
scrollbar3.config(command=third_txt.yview)

root.config(menu=menu) # 메뉴 적용
root.mainloop()