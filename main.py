import tkinter
import customtkinter


customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("800x300")
app.resizable(width = False,height=False)
app.title("Conversor de unidades")

list_op =[
    "Mili (m)",
    "Micro (u)",
    "Nano (n)",
    "Pico (p)",
    "Unideade",
    "Quilo (K)",
    "Mega (M)",
    "Giga (G)",
    "Tera (T)"
]


list_pot= [
    10**-3,
    10**-6,
    10 ** -9,
    10 ** -12,
    1,
    10** 3,
    10** 6,
    10 ** 9,
    10 ** 12,

]
resultado = customtkinter.StringVar()
calculo = 0
def converter():
    try:
        op1 = caixa_entrada.get()
        op2 = caixa_saida.get()
        entrada = float(ent_valor.get())

        pos1 = list_op.index(op1)
        pos2 = list_op.index(op2)
        calculo = (list_pot[pos1]/list_pot[pos2])*entrada
        resultado.set(str(calculo))
        saida_valor["textvariable"] =f"{resultado}.1E"
        #limpar()
    except ValueError:
        resultado.set(str("OPS!!! DÊ UM NÚMERO"))
        saida_valor["textvariable"] = f"{resultado}"



def limpar():
    ent_valor.delete(0,'end')
    saida_valor.delete(0,"end")



#frame principal
frame = customtkinter.CTkFrame(master=app,width=797,height=297,corner_radius=10)
frame.pack(padx=10, pady=10, )
#frame de titulo
frame = customtkinter.CTkLabel(master=frame,text= "CONVERSOR DE UNIDADES",text_font=("Calibri",24,"bold"),
                                width=750,height=20,corner_radius=10)
frame.pack(padx=10, pady=10)
#valor de entrada
ent_valor= customtkinter.CTkEntry(master=app,text_font=("Calibri",16,"bold"),width=250,height=45,corner_radius=10,justify="right")
ent_valor.place(x=20,y=90)
#valor saída
saida_valor= customtkinter.CTkEntry(master=app,text_font=("Calibri",16,"bold") ,textvariable=resultado,width=250,height=45,corner_radius=10,justify="right")
saida_valor.place(x=530,y=90)
#caixa de entradas
caixa_entrada = customtkinter.CTkComboBox(master=app,text_font=("Calibri",16,"bold"),values=list_op,width=180,height=45)
caixa_entrada.place(x=50, y=170)
#caixa de saída
caixa_saida = customtkinter.CTkComboBox(master=app,text_font=("Calibri",16,"bold"),values=list_op,width=180,height=45)
caixa_saida.place(x=570, y=170)
#botão de limpar saida
button_limpa = customtkinter.CTkButton(master=app,width=120,height=32,border_width=0,command=limpar,corner_radius=8,text="LIMPAR",)
button_limpa.place(x=130, y=260, anchor=tkinter.CENTER)
#Botão conerter
button_convert = customtkinter.CTkButton(master=app,bg="#bf514b",width=120,height=32,border_width=0,command=converter,corner_radius=8,text="CONVERTER",)
button_convert.place(x=650, y=260, anchor=tkinter.CENTER)


app.mainloop()
