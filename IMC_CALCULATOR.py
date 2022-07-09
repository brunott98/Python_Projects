from tkinter import *
from tkinter import messagebox

janela = Tk()

def recupera_input():
    print("\n\nlog:\n")
    inputPeso = float(textBox1.get())
    print(inputPeso)

    inputAltura = float(textBox2.get())
    print(inputAltura)

    inputIdade = float(textBox3.get())
    print(inputIdade)

    inputSexo = (sexo_var.get())
    print(inputSexo)

    inputFator = fator_var.get()
    print(inputFator)

    fatorando = 0
    if inputFator == 1:
        fatorando = 1.2
    elif inputFator == 2:
        fatorando = 1.375
    elif inputFator == 3:
        fatorando = 1.55
    elif inputFator == 4:
        fatorando = 1.725
    else:
        print("Valores inválidos")

    
    imc = 10000*(inputPeso / (inputAltura **2))
    
    if inputSexo == "F":
        caloria = fatorando*((10*inputPeso)+(6.25*inputAltura)-(5*inputIdade)-161)
        
    else:
        inputSexo == "M"
        caloria = fatorando*((10*inputPeso)+(6.25*int(inputAltura))-(5*inputIdade)+5)
        

    messagebox.showinfo("IMC:",imc)
    messagebox.showinfo("CALORIAS",caloria)
    
    



    if imc < 18.5:
        print("Você está abaixo do peso")
    elif 18.5 <= imc < 25:
        print("Parabéns você está na faixa de \033[1;32mPESO NORMAL\033[m")
    elif 25 <= imc < 30:
        print("Você está com Pré-obesidade")
    elif 30 <= imc < 35:
        print("Você está com Obesidade Grau 1")
    else:
        print("Você está com Obesidade Grau 2")

    

    
    



'''----------------------------------------------------------------------------'''

janela.title("Stay Healthy")

janela.geometry('600x435')


cabeçalho_label = Label(janela,text="Stay Healthy, o programa que calcula seu IMC e gasto calórico diário em um instante!",width=75,font=("bold",10))
cabeçalho_label.place(x=0, y= 20)

info_label = Label(janela,text="Informe os dados abaixo",width=20,font=("bold",20))
info_label.place(x=90, y= 70)


'''----------------------------------------------------------------------------'''

peso_titulo = Label(janela,text="Peso(KG):",width=20,font=("bold",10))
peso_titulo.place(x=80, y= 125)

textBox1 = Entry(janela)
textBox1.place(x=240,y=130)

'''----------------------------------------------------------------------------'''

altura_label = Label(janela,text="Altura(CM):",width=20,font=("bold",10))
altura_label.place(x=80, y= 149)

textBox2 = Entry(janela)
textBox2.place(x=240,y=150)

'''----------------------------------------------------------------------------'''

idade = Label(janela,text="Idade:",width=20,font=("bold",10))
idade.place(x=80, y= 170)

textBox3 = Entry(janela)
textBox3.place(x=240,y=170)

'''----------------------------------------------------------------------------'''

sexo = Label(janela,text="Sexo:",width=20,font=("bold",10))
sexo.place(x=80,y=200)
sexo_var = StringVar()

Radiobutton(janela,text="Masculino",padx=5,variable=sexo_var,value = "M").place(x=235,y=200)
Radiobutton(janela,text="Feminino",padx=20,variable=sexo_var,value = "F").place(x=320,y=200)

'''----------------------------------------------------------------------------'''

fator = Label(janela,text="Tipo de atividade física:",width=20,font=("bold",10))
fator.place(x=100,y=230)
fator_var = IntVar()

Radiobutton(janela,text="Sedentário",padx=5,variable=fator_var,value = 1).place(x=260,y=230)
Radiobutton(janela,text="1 a 3 Exercícios por semana",padx=5,variable=fator_var,value = 2).place(x=260,y=250)
Radiobutton(janela,text="3 a 5 Exercícios por semana",padx=5,variable=fator_var,value = 3).place(x=260,y=270)
Radiobutton(janela,text="6 a 7 Exercícios por semana",padx=5,variable=fator_var,value = 4).place(x=260,y=290)

'''----------------------------------------------------------------------------'''


buttonConmit = Button(janela,width=30,bg="green",fg="white",text="Gerar IMC e calorias diárias",command=lambda: recupera_input()).place(x=160,y=340)




janela.mainloop()