from tkinter import *
import keyboard
import pyperclip
import time
import pyautogui as pya

inp_text = []
input_def_text = []
t = 0
def copy_clipboard():
    global inp_text
    pya.hotkey('ctrl', 'c')
    time.sleep(.01)
    inp_text = pyperclip.paste()
    swap_let()
def man_swap():
    global t
    global input_def_text
    t = 1
    input_def_text = inp_man_text.get("1.0", "end")
    print(input_def_text)
    swap_let()
def swap_let():
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
        '`': 'є', 'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н', 'U': 'Г',
        'I': 'Ш', 'O': 'Щ', 'P': 'З', 'A': 'Ф', 'S': 'І', 'D': 'В', 'F': 'А', 'G': 'П',
        'H': 'Р', 'J': 'О', 'K': 'Л', 'L': 'Д', 'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М',
        'B': 'И', 'N': 'Т', 'M': 'Ь', '{': 'Х', '}': 'Ї', ':': 'Ж', '"': 'Є', '<': 'Б',
        '>': 'Ю', '~': 'Є', '/': '.', '?': ','
    }
    swapped_word = str('')
    for i in str(input_def_text):
        if i in ukrainian_layout:
            swapped_word += ukrainian_layout[i]
        else:
            swapped_word += i
    outp_word.insert(END, swapped_word)
    t = 0


keyboard.add_hotkey('ctrl + y', lambda: copy_clipboard())

win = Tk()
win.geometry()
win.resizable(True, True)
win.title(" TRANSLANATOR ")

welcome_text = Label(text="Enter text here or select it and use Ctrl+Y combination")
inp_man_text = Text(win, height=10, width=25, bg="light yellow")
outp_word = Text(win, height=10, width=25, bg="light cyan")
display = Button(win, height=2, width=20, text="Convert", command=lambda: man_swap())

welcome_text.pack()
inp_man_text.pack()
display.pack()
outp_word.pack()

mainloop()