import tkinter as tk
import Natural as nat
import Integer as itg

root = tk.Tk()
root.title("Система Компьютерной Алгебры")
root.geometry('800x600')

mainmenu = tk.Menu(root)
root.config(menu=mainmenu)
filemenu = tk.Menu(mainmenu, tearoff=0)
filemenu.add_command(label="О программе")

mainmenu.add_cascade(label="Help",
                     menu=filemenu)



def Nat_to_mas(a):
    b=len(a)
    c=[0]*b
    for i in range (b):
        c[i]=int(a[i])
    return c

def Mas_to_str(b):
    a=len(b)
    c=''
    for i in range (a):
        c=c+str(b[i])
    return c

def Int_to_mas(a):
    if a[0]=='-':
        a=a[1:]
        b=len(a)
        c=[0]*b
        for i in range (b):
            c[i]=int(a[i])
        return 1,c
    else:
        b = len(a)
        c = [0] * b
        for i in range(b):
            c[i] = int(a[i])
        return 0,c



def Nat_ssum():
    Nat_ssum = tk.Toplevel(root)
    Nat_ssum.geometry('500x400')
    Nat_ssum.title("Cумма Натуральных")
    Nat_ssum['background']='#33A2FF'
    Nat_ssum.focus
    Nat_ssum.grid

    vvod1 = tk.Entry(Nat_ssum, width=18, fg='black')
    vvod1.place(x=30, y=50)
    vvod2 = tk.Entry(Nat_ssum, width=18, fg='black')
    vvod2.place(x=250, y=50)
    rest = tk.Label(Nat_ssum,text='Ожидание действия' ,width=18,bg='white', fg='black',height=1 )
    znk = tk.Label(Nat_ssum, text='+', width=10, fg='black',bg='#33A2FF', height=1)


    res= tk.Button(Nat_ssum,text="Результат",bg='white', fg='black', height=1, width=12)
    res.place(x=400, y=50)
    rest.place(x=30, y=100)
    znk.place(x=155, y=50)
    res.bind('<Button-1>', func=lambda event: check())

    def check():
        a= vvod1.get()
        aa=a
        b=vvod2.get()
        bb=b
        a=Nat_to_mas(a)
        b=Nat_to_mas(b)
        c= nat.ADD_NN_N(a,b)
        c= Mas_to_str(c)
        d=aa+" + "+bb+" = "+c
        rest.config(text=d)



def Nat_razn():
    Nat_razn = tk.Toplevel(root)
    Nat_razn.geometry('500x400')
    Nat_razn.title("Разность Натуральных")
    Nat_razn['background'] = '#33A2FF'
    Nat_razn.focus
    Nat_razn.grid

    vvod1 = tk.Entry(Nat_razn, width=18, fg='black')
    vvod1.place(x=30, y=50)
    vvod2 = tk.Entry(Nat_razn, width=18, fg='black')
    vvod2.place(x=250, y=50)
    rest = tk.Label(Nat_razn,text='Ожидание действия' ,width=18,bg='white', fg='black',height=1 )
    znk = tk.Label(Nat_razn, text='-', width=10, fg='black',bg='#33A2FF', height=1)


    res= tk.Button(Nat_razn,text="Результат",bg='white', fg='black', height=1, width=12)
    res.place(x=400, y=50)
    rest.place(x=30, y=100)
    znk.place(x=155, y=50)
    res.bind('<Button-1>', func=lambda event: check())

    def check():
        a= vvod1.get()
        aa=a
        b=vvod2.get()
        bb=b
        a=Nat_to_mas(a)
        b=Nat_to_mas(b)
        c= nat.SUB_NN_N(a,b)
        c= Mas_to_str(c)
        if int(aa)>int(bb):
            d = aa + " - " + bb + " = " + c
        else:
            d = bb + " - " + aa + " = " + c
        rest.config(text=d)


def Nat_umn():
    Nat_umn = tk.Toplevel(root)
    Nat_umn.geometry('500x400')
    Nat_umn.title("Умножение Натуральных")
    Nat_umn['background']='#33A2FF'
    Nat_umn.focus
    Nat_umn.grid

    vvod1 = tk.Entry(Nat_umn, width=18, fg='black')
    vvod1.place(x=30, y=50)
    vvod2 = tk.Entry(Nat_umn, width=18, fg='black')
    vvod2.place(x=250, y=50)
    rest = tk.Label(Nat_umn,text='Ожидание действия' ,width=18,bg='white', fg='black',height=1 )
    znk = tk.Label(Nat_umn, text='Умножить на', width=10, fg='black',bg='#33A2FF', height=1)


    res= tk.Button(Nat_umn,text="Результат",bg='white', fg='black', height=1, width=12)
    res.place(x=400, y=50)
    rest.place(x=30, y=100)
    znk.place(x=155, y=50)
    res.bind('<Button-1>', func=lambda event: check())

    def check():
        a= vvod1.get()
        aa=a
        b=vvod2.get()
        bb=b
        a=Nat_to_mas(a)
        b=Nat_to_mas(b)
        c= nat.MUL_NN_N(a,b)
        c= Mas_to_str(c)
        d=aa+" * "+bb+" = "+c
        rest.config(text=d)



def Nat_del():
    Nat_del = tk.Toplevel(root)
    Nat_del.geometry('500x400')
    Nat_del.title("Деление Натуральных")
    Nat_del['background']='#33A2FF'
    Nat_del.focus
    Nat_del.grid

    vvod1 = tk.Entry(Nat_del, width=18, fg='black')
    vvod1.place(x=30, y=50)
    vvod2 = tk.Entry(Nat_del, width=18, fg='black')
    vvod2.place(x=250, y=50)
    rest = tk.Label(Nat_del,text='Ожидание действия' ,width=18,bg='white', fg='black',height=1 )
    rest1 = tk.Label(Nat_del, text='Ожидание действия', width=18, bg='white', fg='black', height=1)
    znk = tk.Label(Nat_del, text='Разделить на', width=10, fg='black',bg='#33A2FF', height=1)


    res= tk.Button(Nat_del,text="Результат",bg='white', fg='black', height=1, width=12)
    res.place(x=400, y=50)
    rest.place(x=30, y=100)
    rest1.place(x=30, y=130)
    znk.place(x=155, y=50)
    res.bind('<Button-1>', func=lambda event: check())

    def check():
        a= vvod1.get()
        aa=a
        b=vvod2.get()
        bb=b

        a=Nat_to_mas(a)
        b=Nat_to_mas(b)
        k = [0] * len(a)
        n = [0] * len(b)
        for i in range(len(a)):
            k[i] = a[i]
        for i in range(len(b)):
            n[i] = b[i]
        c= nat.DIV_NN_N(a,b)
        d =nat.MOD_NN_N(k,n)
        c= Mas_to_str(c)
        d=Mas_to_str(d)
        if (int(aa) > int(bb)):
            dk=aa+" \ "+bb+" = "+str(c)
        else:
            dk = bb + " \ " + aa + " = " + str(c)
        f="Остаток: "+str(d)
        rest.config(text=dk)
        rest1.config(text=f)
    

def Nat_nod():
    Nat_nod = tk.Toplevel(root)
    Nat_nod.geometry('500x400')
    Nat_nod.title("НОД Натуральных")
    Nat_nod['background']='#33A2FF'
    Nat_nod.focus
    Nat_nod.grid

    vvod1 = tk.Entry(Nat_nod, width=18, fg='black')
    vvod1.place(x=30, y=50)
    vvod2 = tk.Entry(Nat_nod, width=18, fg='black')
    vvod2.place(x=250, y=50)
    rest = tk.Label(Nat_nod,text='Ожидание действия' ,width=18,bg='white', fg='black',height=1 )
    znk = tk.Label(Nat_nod, text='и', width=10, fg='black',bg='#33A2FF', height=1)


    res= tk.Button(Nat_nod,text="Результат",bg='white', fg='black', height=1, width=12)
    res.place(x=400, y=50)
    rest.place(x=30, y=100)
    znk.place(x=155, y=50)
    res.bind('<Button-1>', func=lambda event: check())

    def check():
        a= vvod1.get()
        aa=a
        b=vvod2.get()
        bb=b
        a=Nat_to_mas(a)
        b=Nat_to_mas(b)
        c= nat.GCF_NN_N(a,b)
        if c=="No common dividers":
            d="No common dividers"
        else:
            c= Mas_to_str(c)
            d="НОД("+aa+":"+bb+")"+" = "+c
        rest.config(text=d)

def Nat_nok():
    Nat_nok = tk.Toplevel(root)
    Nat_nok.geometry('500x400')
    Nat_nok.title("НОК Натуральных")
    Nat_nok['background']='#33A2FF'
    Nat_nok.focus
    Nat_nok.grid

    vvod1 = tk.Entry(Nat_nok, width=18, fg='black')
    vvod1.place(x=30, y=50)
    vvod2 = tk.Entry(Nat_nok, width=18, fg='black')
    vvod2.place(x=250, y=50)
    rest = tk.Label(Nat_nok,text='Ожидание действия' ,width=18,bg='white', fg='black',height=1 )
    znk = tk.Label(Nat_nok, text='и', width=10, fg='black',bg='#33A2FF', height=1)


    res= tk.Button(Nat_nok,text="Результат",bg='white', fg='black', height=1, width=12)
    res.place(x=400, y=50)
    rest.place(x=30, y=100)
    znk.place(x=155, y=50)
    res.bind('<Button-1>', func=lambda event: check())

    def check():
        a= vvod1.get()
        aa=a
        b=vvod2.get()
        bb=b
        a=Nat_to_mas(a)
        b=Nat_to_mas(b)
        c= nat.LCM_NN_N(a,b)
        c= Mas_to_str(c)
        d="НОК("+aa+":"+bb+")"+" = "+c
        rest.config(text=d)
#----------------------------------------------------------------------
def Int_abs():
    Int_abs = tk.Toplevel(root)
    Int_abs.geometry('500x400')
    Int_abs.title("Абсолютная величина Целого")
    Int_abs['background']='#33A2FF'
    Int_abs.focus
    Int_abs.grid

    vvod1 = tk.Entry(Int_abs, width=18, fg='black')
    vvod1.place(x=30, y=50)
    vvod2 = tk.Entry(Int_abs, width=18, fg='black')
    vvod2.place(x=250, y=50)
    rest = tk.Label(Int_abs,text='Ожидание действия' ,width=18,bg='white', fg='black',height=1 )
    znk = tk.Label(Int_abs, text='+', width=10, fg='black',bg='#33A2FF', height=1)


    res= tk.Button(Int_abs,text="Результат",bg='white', fg='black', height=1, width=12)
    res.place(x=400, y=50)
    rest.place(x=30, y=100)
    znk.place(x=155, y=50)
    res.bind('<Button-1>', func=lambda event: check())

    def check():
        n1=0
        n2=0
        a= vvod1.get()
        aa=a


        d=aa+" + "+bb+" = "+c
        rest.config(text=d)


nat1 = tk.Button(text="Сумма", bg='white', fg='black', height=2, width=12)
nat1.place(x=50, y=50)
nat1.bind('<Button-1>', func=lambda event: Nat_ssum())
nat2 = tk.Button(text="Разность", bg='white', fg='black', height=2, width=12)
nat2.place(x=50, y=110)
nat2.bind('<Button-1>', func=lambda event: Nat_razn())
nat3 = tk.Button(text="Умножение", bg='white', fg='black', height=2, width=12)
nat3.place(x=50, y=180)
nat3.bind('<Button-1>', func=lambda event: Nat_umn())
nat4 = tk.Button(text="Деление", bg='white', fg='black', height=2, width=12)
nat4.place(x=50, y=250)
nat4.bind('<Button-1>', func=lambda event: Nat_del())
nat6 = tk.Button(text="НОД", bg='white', fg='black', height=2, width=12)
nat6.place(x=50, y=320)
nat6.bind('<Button-1>', func=lambda event: Nat_nod())
nat7 = tk.Button(text="НОК", bg='white', fg='black', height=2, width=12)
nat7.place(x=50, y=390)
nat7.bind('<Button-1>', func=lambda event: Nat_nok())
nat8 = tk.Label(text="Натуральные", fg='black')
nat8.place(x=50, y=20)

integ1 = tk.Button(text="Модуль", bg='white', fg='black', height=2, width=12)
integ1.place(x=200, y=50)
integ2 = tk.Button(text="Сложение", bg='white', fg='black', height=2, width=12)
integ2.place(x=200, y=110)
integ3 = tk.Button(text="Вычитание", bg='white', fg='black', height=2, width=12)
integ3.place(x=200, y=180)
integ4 = tk.Button(text="Умножение", bg='white', fg='black', height=2, width=12)
integ4.place(x=200, y=250)
integ5 = tk.Button(text="DIV", bg='white', fg='black', height=2, width=12)
integ5.place(x=200, y=320)
integ6 = tk.Button(text="MOD", bg='white', fg='black', height=2, width=12)
integ6.place(x=200, y=390)
integ7 = tk.Button(text="Степень", bg='white', fg='black', height=2, width=12)
integ7.place(x=200, y=460)
integ8 = tk.Button(text="a= n*q +r", bg='white', fg='black', height=2, width=12)
integ8.place(x=200, y=530)
integ9 = tk.Label(text="Целые", fg='black')
integ9.place(x=200, y=20)

rat1 = tk.Button(text="Сокращение", bg='white', fg='black', height=2, width=12)
rat1.place(x=350, y=50)
rat2 = tk.Button(text="Сложение", bg='white', fg='black', height=2, width=12)
rat2.place(x=350, y=110)
rat3 = tk.Button(text="Вычитание", bg='white', fg='black', height=2, width=12)
rat3.place(x=350, y=180)
rat4 = tk.Button(text="Умножение", bg='white', fg='black', height=2, width=12)
rat4.place(x=350, y=250)
rat5 = tk.Button(text="Деление", bg='white', fg='black', height=2, width=12)
rat5.place(x=350, y=320)
rat6 = tk.Label(text="Рациональные", fg='black')
rat6.place(x=350, y=20)

pol1 = tk.Button(text="Сложение", bg='white', fg='black', height=2, width=12)
pol1.place(x=500, y=50)
pol2 = tk.Button(text="Разность", bg='white', fg='black', height=2, width=12)
pol2.place(x=500, y=110)
pol3 = tk.Button(text="Умножени", bg='white', fg='black', height=2, width=12)
pol3.place(x=500, y=180)
pol4 = tk.Button(text="Производная", bg='white', fg='black', height=2, width=12)
pol4.place(x=500, y=250)
pol5 = tk.Button(text="Целая часть", bg='white', fg='black', height=2, width=12)
pol5.place(x=500, y=320)
pol6 = tk.Button(text="Остаток", bg='white', fg='black', height=2, width=12)
pol6.place(x=500, y=390)
pol7 = tk.Button(text="НОД", bg='white', fg='black', height=2, width=12)
pol7.place(x=500, y=460)
pol8 = tk.Button(text="Кратные корни", bg='white', fg='black', height=2, width=12)
pol8.place(x=500, y=530)
pol8 = tk.Label(text="Многочлены", fg='black')
pol8.place(x=500, y=20)



root.mainloop()

