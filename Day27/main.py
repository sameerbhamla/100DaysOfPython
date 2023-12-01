import tkinter

window = tkinter.Tk()
window.title('MyProgram')
window.minsize(width=500, height=300)
window.config(padx=20,pady=20)


my_label = tkinter.Label(text='I am a Label', font=('Arial', 24, 'bold'))
my_label['text'] = 'New Text'
my_label.config(text='New Text')
my_label.grid(column=0, row=0)

def button_clicked():
    print('I got clicked')
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text='ClickMe',command=button_clicked)
button.grid(column=1, row=1)

input = tkinter.Entry(width=10)
input.grid(column=3, row=3)

newbutton = tkinter.Button(text='No!ClickME', command=button_clicked)
newbutton.grid(row=0,column=2)

window.mainloop()
