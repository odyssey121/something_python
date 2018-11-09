#интерфейс аля меню ресторана с подсчётом заказа))
from tkinter import *
import random
class Aplication(Frame):
    def __init__(self,master):
        super().__init__(master)
        self.grid()
        self.create_widget()
    def create_widget(self):
        Label(self,text='Супы==>').grid(row=1,column=0,sticky=W)
        Label(self,text='Добро пожаловать в ресторан Рублевский!').grid(row=0,column=0,columnspan=2,sticky=N)
        Label(self,text='Гарниры==>').grid(row=2,column=0,sticky=W)
        Label(self,text='Десерты==>').grid(row=3,column=0,sticky=W)
        Label(self,text='Напитки==>').grid(row=4,column=0,sticky=W)
        self.soup=StringVar()
        self.soup.set(False)
        soup=['суп харчо=100р','Щи с капустой=80р','картофельный пюре=80р','окрошка(квас)=100р']
        Radiobutton(self,text='суп харчо=100р',variable=self.soup,value='суп харчо\n').grid(row=1,column=1,sticky=W)
        Radiobutton(self,text='Щи с капустой=80р',variable=self.soup,value='Щи с капустой\n').grid(row=1,column=2,sticky=W)
        Radiobutton(self,text='картофельный пюре=80р',variable=self.soup,value='картофельный пюре\n').grid(row=1,column=3,sticky=W)
        Radiobutton(self,text='окрошка(квас)=100р',variable=self.soup,value='окрошка=квас\n').grid(row=1,column=4,sticky=W)
        garnir=['рис с мясом=100р','гречка с тефтелей=80р','макароны по флотский=80р','пюре с курицей=100р']
        variable=['self.rise_meat','self.gre4_teft','self.flotskiy','self.chiken']
        
            
        self.rise_meat=BooleanVar()
        self.gre4_teft=BooleanVar()
        self.flotskiy=BooleanVar()
        self.chiken=BooleanVar()
        Checkbutton(self,text=garnir[0],variable=self.rise_meat).grid(row=2,column=1,sticky=W)
        Checkbutton(self,text=garnir[1],variable=self.gre4_teft).grid(row=2,column=2,sticky=W)
        Checkbutton(self,text=garnir[2],variable=self.flotskiy).grid(row=2,column=3,sticky=W)
        Checkbutton(self,text=garnir[3],variable=self.chiken).grid(row=2,column=4,sticky=W)
        
        
        desert=['кекс с мёдом=75р','мороженное разн.=50р','пироженное разн.=50р','кроусан на выб.=50р']
        variable1=['self.keks','self.morosh','self.pirosh','self.krous']
        
        self.keks=BooleanVar()
        self.morosh=BooleanVar()
        self.pirosh=BooleanVar()
        self.krous=BooleanVar()

        Checkbutton(self,text=desert[0],variable=self.keks).grid(row=3,column=1,sticky=W)
        Checkbutton(self,text=desert[1],variable=self.morosh).grid(row=3,column=2,sticky=W)
        Checkbutton(self,text=desert[2],variable=self.pirosh).grid(row=3,column=3,sticky=W)
        Checkbutton(self,text=desert[3],variable=self.krous).grid(row=3,column=4,sticky=W)
        
        self.drinks=StringVar()
        self.drinks.set(False)
        drinks=['Чай зел.черн.','кофе','лимонад на выб.','пиво класич.']
        Radiobutton(self,text='Чай зел.черн=25р.',variable=self.drinks,value='Чай зел.черн.\n').grid(row=4,column=1,sticky=W)
        Radiobutton(self,text='кофе=25р',variable=self.drinks,value='кофе').grid(row=4,column=2,sticky=W)
        Radiobutton(self,text='лимонад на выб.=15р',variable=self.drinks,value='лимонад на выб.\n').grid(row=4,column=3,sticky=W)
        Radiobutton(self,text='пиво класич.=50р',variable=self.drinks,value='пиво класич.\n').grid(row=4,column=4,sticky=W)
        self.text=Text(self,width=25,height=25,wrap=WORD)
        self.text.grid(row=5,column=0,columnspan=4,sticky=W)
        Button(self,text='Счёт пожалуйста!',command=self.cashe).grid(row=5,column=2,sticky=N)
    def cashe(self):
        dic={'суп харчо':100,'Щи с капустой':80,'картофельный пюре':80,
     'окрошка=квас':100,'рис с мясом':100,'гречка с тефтелей':80,
     'макароны по флотский':80,'пюре с курицей':100,'кекс с мёдом':75,
     'мороженное(на выб.)':50,'пироженное(на выб.)':50,'круасан(на выб.)':50,
     'Чай зел.черн.':25,'кофе':25,'лимонад на выб.':15,'пиво класич.':50}
        total=0
        drink=self.drinks.get()
        soup=self.soup.get()
        message='Вы заказали:\n'
        if self.soup.set==False:
            message+='-------\n'
        else:
            message+=self.soup.get()
            
        
        if self.rise_meat.get():
            message+='рис с мясом\n'
        
        if self.gre4_teft.get():
            message+='гречка с тефтелей\n'
        if self.flotskiy.get():
            message+='макароны по флотский\n'
        if self.chiken.get():
            message+='пюре с курицей\n'
        if self.keks.get():
            message+='кекс с мёдом\n'
        if self.morosh.get():
            message+='мороженное(на выб.)\n'
        if self.pirosh.get():
            message+='пироженное(на выб.)\n'
        if self.krous.get():
            message+='круасан(на выб.)\n'
        if self.drinks.set==False:
            message+='-------\n'
        else:
            message+=self.drinks.get()
        for key in dic:
            if key in message:
                total+=dic[key]
                print(total)
        import sys
        print(sys.argv)    
        self.text.delete(0.0,END)
        self.text.insert(0.0,message)
        self.text.insert(100.0,'\n\nВы заказали на '+str(total)+' руб')

root=Tk()
root.title('Закажите себе обед!')
root.geometry('800x350')

app=Aplication(root)
root.mainloop()

            
            
            
        
        
            
            
        
        
