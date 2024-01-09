from tkinter import *
import keyboard
import pyperclip
import time
import pyautogui as pya

inp_text = []
input_def_text = []
t = 0
def copy_clipboard_ua():
    global inp_text
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    inp_text = pyperclip.paste()
    swap_let_ua()
def man_swap_ua():
    global t
    global input_def_text
    t = 1
    input_def_text = inp_man_text.get("1.0", "end")
    print(input_def_text)
    swap_let_ua()
def swap_let_ua():
    global t
    global input_def_text
    global inp_text
    outp_word.delete("1.0", "end")
    if t != 1:
        input_def_text = inp_text
    ukrainian_layout = {
        'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г', 'i': 'ш',
        'o': 'щ', 'p': 'з', 'a': 'ф', 's': 'і', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р',
        'j': 'о', 'k': 'л', 'l': 'д', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
        'n': 'т', 'm': 'ь', '[': 'х', ']': 'ї', ';': 'ж', "'": 'є', ',': 'б', '.': 'ю',
        'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г',
        'I': 'Ш', 'O': 'Щ', 'P': 'З', 'A': 'Ф', 'S': 'І', 'D': 'В', 'F': 'А', 'G': 'П',
        'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М',
        'B': 'И', 'N': 'Т', 'M': 'Ь', '{': 'Х', '}': 'Ї', ':': 'Ж', '"': 'Є', '<': 'Б',
        '>': 'Ю', '/': '.', '?': ','
    }
    swapped_word = str('')
    for i in str(input_def_text):
        if i in ukrainian_layout:
            swapped_word += ukrainian_layout[i]
        else:
            swapped_word += i
    outp_word.insert(END, swapped_word)
    t = 0
def copy_clipboard_en():
    global inp_text
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    inp_text = pyperclip.paste()
    swap_let_en()
def man_swap_en():
    global t
    global input_def_text
    t = 1
    input_def_text = inp_man_text.get("1.0", "end")
    print(input_def_text)
    swap_let_en()
def swap_let_en():
    global t
    global input_def_text
    global inp_text
    outp_word.delete("1.0", "end")
    if t != 1:
        input_def_text = inp_text
    ukrainian_layout = {
        'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y', 'г': 'u', 'ш': 'i',
        'щ': 'o', 'з': 'p', 'ф': 'a', 'і': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h',
        'о': 'j', 'л': 'k', 'д': 'l', 'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b',
        'т': 'n', 'ь': 'm', 'х': '[', 'ї': ']', 'ж': ';', "є": "'", 'б': ',', 'ю': '.',
        'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y', 'Г': 'U',
        'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Ф': 'A', 'І': 'S', 'В': 'D', 'А': 'F', 'П': 'G',
        'Р': 'H', 'О': 'J', 'Л': 'K', 'Д': 'L', 'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V',
        'И': 'B', 'Т': 'N', 'Ь': 'M', 'Х': '{', 'Ї': '}', 'Ж': ':', 'Є': '"', 'Б': '<',
        'Ю': '>', '.': '/', ',': '?'
    }
    swapped_word = str('')
    for i in str(input_def_text):
        if i in ukrainian_layout:
            swapped_word += ukrainian_layout[i]
        else:
            swapped_word += i
    outp_word.insert(END, swapped_word)
    t = 0


keyboard.add_hotkey('Ctrl + y', lambda: copy_clipboard_ua())
keyboard.add_hotkey('Ctrl + q', lambda: copy_clipboard_en())

win = Tk()
win.geometry()
win.resizable(True, True)
win.title(" TRANSLANATOR ")

welcome_text = Label(text="Enter text here \tor \nCtrl+Y for EN-UA    or \nCtrl+Q for UA-EN")
inp_man_text = Text(win, height=10, width=25, bg="light yellow")
outp_word = Text(win, height=10, width=25, bg="light cyan")
display_ua = Button(win, height=2, width=20, text="Convert EN-UA", command=lambda: man_swap_ua())
display_en = Button(win, height=2, width=20, text="Convert UA-EN", command=lambda: man_swap_en())

welcome_text.pack()
inp_man_text.pack()
display_ua.pack()
display_en.pack()
outp_word.pack()

mainloop()