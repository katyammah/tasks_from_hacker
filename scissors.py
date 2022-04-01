from tkinter import *
window=Tk()
window.title('Камень, ножницы, бумага')
window.geometry('440x300')
window['bg']='white'

#добавление текста, сообщающего о начале игры
lb=Label(text='Начало игры!', fg='#1b6e6e', font=("Times New Roman", 20))
lb.place(x=120,y=25,width=200)

#добавление кнопок                                                                                                                                                                                                                             
bt1=Button(text='Камень',bg='#1b6e6e',fg='white',font=("Times New Roman", 15), command=lambda my_choise='stone': clicked(my_choise))
bt1.place(x=20, y=100, width=120,height=50)
bt2=Button(text='Ножницы',bg='#1b6e6e',fg='white',font=("Times New Roman", 15), command=lambda my_choise='scissors': clicked(my_choise))
bt2.place(x=160, y=100, width=120,height=50)                                                                                                                                                                                                   
bt3=Button(text='Бумага',bg='#1b6e6e',fg='white',font=("Times New Roman", 15),command=lambda my_choise='paper': clicked(my_choise))
bt3.place(x=300, y=100, width=120,height=50)                                                                                                                                                                                                   

#добавление счётчиков по результатам игр
win=0
lose=0
drow=0
lb2=Label(text=(f'Побед: {win} \nПроигрышей: {lose} \nНичьих: {drow}'),bg='white', fg='#1b6e6e', font=("Times New Roman", 13),justify='left')
lb2.place(x=20, y=190)
#опытным путём я смогла разделить строчки, поставив win, lose и drow в фигурные скобки. Что они дают?

import random                         
def clicked(my_choise):
    comp_choise=random.choice(['stone','scissors','paper'])
    win=0
    lose=0
    drow=0

    if my_choise==comp_choise:
        drow=+1
        lb.configure(text='Ничья!')
    elif (my_choise=='stone' and comp_choise=='scissors') or (my_choise=='scissors' and comp_choise=='paper') or (my_choise=='paper' and comp_choise=='stone'):
        win=+1
        lb.configure(text='Победа!')
    else:
        lose+=1
        lb.configure(text='Проигрыш!')

    lb2.configure(text=(f'Побед: {win} \nПроигрышей: {lose} \nНичьих: {drow}'))




























    


window.mainloop()