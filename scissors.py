from tkinter import *
import random

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.play()

    def play(self):
        #добавление текста, сообщающего о начале игры
        self.lb=Label(text='Начало игры!', fg='#1b6e6e', font=("Times New Roman", 20))
        self.lb.place(x=120,y=25,width=200)

        #добавление кнопок
        bt1=Button(text='Камень',bg='#1b6e6e',fg='white',font=("Times New Roman", 15), command=lambda my_choice='stone': self.clicked(my_choice))
        bt1.place(x=20, y=100, width=120,height=50)
        bt2=Button(text='Ножницы',bg='#1b6e6e',fg='white',font=("Times New Roman", 15), command=lambda my_choice='scissors': self.clicked(my_choice))
        bt2.place(x=160, y=100, width=120,height=50)
        bt3=Button(text='Бумага',bg='#1b6e6e',fg='white',font=("Times New Roman", 15), command = lambda my_choice='paper': self.clicked(my_choice))
        bt3.place(x=300, y=100, width=120,height=50)
    
    #добавление счётчиков по результатам игр
        self.win=0
        self.lose=0
        self.draw=0
        self.all=0
        self.lb2=Label(text=(f'Побед: {self.win} \nПроигрышей: {self.lose} \nНичьих: {self.draw} \nВсего игр: {self.all}'),bg='white', fg='#1b6e6e', font=("Times New Roman", 13),justify='left')
        self.lb2.place(x=20, y=190)
        #опытным путём я смогла разделить строчки, поставив win, lose и drow в фигурные скобки. Что они дают?

    def clicked(self, my_choice):
        comp_choice=random.choice(['stone','scissors','paper'])
        if my_choice==comp_choice:
            self.lb.configure(text='Ничья!')
            self.draw+=1
        elif (my_choice=='stone' and comp_choice=='scissors') or (my_choice=='scissors' and comp_choice=='paper') or (my_choice=='paper' and comp_choice=='stone'):
            self.lb.configure(text='Победа!')
            self.win+=1
        else:
            self.lb.configure(text='Проигрыш!')
            self.lose+=1
        self.all+=1
        self.lb2.configure(text=(f'Побед: {self.win} \nПроигрышей: {self.lose} \nНичьих: {self.draw} \nВсего игр: {self.all}'))

if __name__ == '__main__':
    root=Tk()                                  
    root.title('Камень, ножницы, бумага')      
    root.geometry('440x300')                   
    root['bg']='white'                         
    app = Main(root)
    app.pack()
    root.mainloop()
