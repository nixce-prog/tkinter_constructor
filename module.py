from tkinter import *
from tkinter import messagebox

def lobby():
    lobby = Tk()
    lobby.title('Constructor')
    lobby.geometry('900x500+200+100')
    lobby.resizable(False, False)
    lobby['bg'] = '#020736'
    #Destory func
    def destroy_main():
        lobby.destroy()
        main()


    # Labels
    bglb = Label(lobby, width=50, height=24, bg='#0c5794')
    bglb.place(x=250,y=30)

    txt1 = Label(lobby, text='Constructor', font=('italic', 20))
    txt1.place(x=350,y=50)
    #Buttons
    btn = Button(lobby, text='Start', font=('italic', 20), command=destroy_main)
    btn.place(x=380,y=200)

    lobby.mainloop()


def main():
    main = Tk()
    main.title('Constructor')
    main.geometry('900x500+200+100')
    main.resizable(False, False)
    main['bg'] = '#03012e'
    def get():
        ex = ent1.get()
        zapr = ['hello world', 'хелло ворлд', 'выведи хелло ворлд', 'калькулятор', 'calculator']
        if ex.lower() in zapr:
            with open('user_code.py', 'w', encoding='utf-8') as py:
                code = """print('Hello World')"""
                py.write(code)
        elif ex.lower() in zapr:
            with open('user_code.py', 'w', encoding='utf-8') as py:
                code = """
while True:
    try:
        x = int(input('First num: '))
        y = int(input('Second num: '))
    except ValueError:
        print('Enter num!!!')
        exit()
    
    d = input('Enter operator (+, -, /, *): ')
    if d == '+':
        print(x + y)
    elif d == '-':
        print(x - y)
    elif d == '/':
        try:
            print(x / y)
        except ZeroDivisionError:
            print('Error: division by zero.')
    elif d == '*':
        print(x * y)
    else:
        print('Unknown error.')
            """
                py.write(code)
        else:
            messagebox.showinfo('Информация', 'Я ещё не натренерован для такого(')

    #Entry
    ent1 = Entry(main, width=40)
    ent1.place(x=280,y=50)
    #Button
    accbtn = Button(main, text='Accept', font=('italic', 10), command=get)
    accbtn.place(x=550,y=50)

    main.mainloop()