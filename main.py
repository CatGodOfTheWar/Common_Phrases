from tkinter import *
from tkinter import filedialog as fd


file1 = ""
file2 = ""
list_files = []


def write_gui_result(list_com):
    row = 0
    for phrase in list_com:
        label_phrase = Label(frame_phrases, text=phrase,
                             font=("Times New Roman", 20),
                             bg="#EF626C",
                             fg="#312F2F")
        label_phrase.grid(row=row, column=0)
        row += 1


def write_result(result_list):
    string_file = ""
    for phrase in result_list:
        string_file = string_file + phrase + "\n"
    with open("result.txt", "w+") as file_output:
        file_output.write(string_file)


def make_phrases_list(file):
    list_phrases = []
    phrase = ""
    for letter in file:
        phrase = phrase + letter
        if letter == "." or letter == "?" or letter == "!":
            list_phrases.append(phrase)
            phrase = ""
    return list_phrases


def compare_files(file_1, file_2):
    same_phrases = []
    list_phrases1 = make_phrases_list(file_1)
    list_phrases2 = make_phrases_list(file_2)
    for phrase1 in list_phrases1:
        for phrase2 in list_phrases2:
            if phrase1.replace(" ", "") == phrase2.replace(" ", ""):
                same_phrases.append(phrase2)
    print(same_phrases)
    write_result(same_phrases)
    write_gui_result(same_phrases)


def select_file():
    global list_files
    var = 0
    filetypes = (('Text file', '.txt'),
                 ('All files', '*.*')
                 )
    content = fd.askopenfile(
        title='Open file',
        initialdir='/',
        filetypes=filetypes
    )
    list_files.append(content.read())
    var += 1


def main():
    global list_files
    global file1
    global file2
    file1 = list_files[0]
    file2 = list_files[1]
    compare_files(file1, file2)


if __name__ == '__main__':
    window = Tk()
    window.geometry("800x800")
    window.title("Common Phrases")
    window.resizable(False, False)
    window.config(bg="#EF626C")

    btn_choose_1 = Button(window,
                          text="Choose first file!",
                          command=select_file,
                          font=("Times New Roman", 30),
                          borderwidth=0,
                          border=0,
                          bg="#84DCCF",
                          activebackground="#F6E8EA",
                          fg="#22181C",
                          activeforeground="#312F2F")
    btn_choose_1.place(x=200, y=30)

    btn_choose_2 = Button(window,
                          text="Choose second file!",
                          command=select_file,
                          font=("Times New Roman", 30),
                          borderwidth=0,
                          border=0,
                          bg="#84DCCF",
                          activebackground="#F6E8EA",
                          fg="#22181C",
                          activeforeground="#312F2F")
    btn_choose_2.place(x=160, y=130)

    btn_submit = Button(window, text="Apply",
                        command=main,
                        font=("Times New Roman", 30),
                        borderwidth=0,
                        border=0,
                        bg="#84DCCF",
                        activebackground="#F6E8EA",
                        fg="#22181C",
                        activeforeground="#312F2F")
    btn_submit.place(x=300, y=250)

    label_list = Label(window, text="Common Phrases are:",
                       font=("Times New Roman", 20),
                       bg="#EF626C",
                       fg="#22181C")
    label_list.place(x=100, y=400)

    frame_phrases = Frame(window, bg="#EF626C")
    frame_phrases.place(x=100, y=500)

    window.mainloop()
