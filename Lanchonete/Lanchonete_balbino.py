import sqlite3
from customtkinter import *
from datetime import datetime
import tkinter


class Menu(CTk):
    def __init__(self):
        super(Menu, self).__init__()
        self.title("Lanchonete")
        self.geometry("400x300")
        self.config(padx=10, pady=10)
        set_default_color_theme("tema.json")
        self.iconbitmap("heisenburger.ico")
        self.grid_columnconfigure(0, weight=1)

        #Menu Inicial
        self.lb_menu = CTkLabel(self, text="Acessar como:", font=("Helvetica", 20))
        self.lb_menu.grid(row=0, column=0, columnspan=2, sticky="we")
        self.bt_menu1 = CTkButton(self, text="Administrador", command=lambda: [self.destroy(), self.senha_admin()])
        self.bt_menu1.grid(row=1, column=0, padx=5, pady=5, sticky="we")
        self.bt_menu2 = CTkButton(self, text="Atendente", command=lambda: [self.destroy(), Cardapio_Menu()])
        self.bt_menu2.grid(row=2, column=0, padx=5, pady=5, sticky="we")

        self.cardapio = Cardapio().gerar_cardapio()

        self.mainloop()
    def senha_admin(self):
        jan_adm = CTk()
        jan_adm.title("Lanchonete - Adm")
        jan_adm.geometry("600x700")
        jan_adm.config(padx=10, pady=10)
        set_default_color_theme("tema.json")
        jan_adm.iconbitmap("heisenburger.ico")
        lb_adm = CTkLabel(jan_adm, text="Menu de Administração", font=("Helvetica", 20))
        lb_adm.grid(row=0, column=1, columnspan=2)

        frame_adm1 = CTkFrame(jan_adm)
        frame_adm1.grid(row=1, column=0, sticky="news", padx=5, pady=5)
        lb_title1 = CTkLabel(frame_adm1, text="Senha Administrativa", font=("Helvetica", 15))
        lb_title1.grid(row=0, column=1, padx=5, pady=5, sticky="news")

        lb_acesso1 = CTkLabel(frame_adm1, text="Senha:", anchor="e")
        lb_acesso1.grid(row=1, column=0, sticky="we", padx=5, pady=5)
        in_acesso1 = CTkEntry(frame_adm1)
        in_acesso1.grid(row=1, column=1, columnspan=1, sticky="we", padx=5, pady=5)

        bt_acesso1 = CTkButton(frame_adm1, text="Entrar",command=lambda: [jan_adm.destroy, self.Menu_adm() if in_acesso1.get() == "0000" else None])
        bt_acesso1.grid(row=2, column=0, sticky="we", padx=5, pady=5, columnspan=2)

        jan_adm.mainloop()


    def login_adm(self):
            jan_adm = CTk()
            jan_adm.title("Lanchonete - Adm")
            jan_adm.geometry("600x700")
            jan_adm.config(padx=10, pady=10)
            set_default_color_theme("tema.json")
            jan_adm.iconbitmap("heisenburger.ico")
            lb_adm = CTkLabel(jan_adm, text="Menu de Administração", font=("Helvetica", 20))
            lb_adm.grid(row=0, column=1, columnspan=2)

            frame_adm1 = CTkFrame(jan_adm)
            frame_adm1.grid(row=1, column=0, sticky="news", padx=5, pady=5)
            lb_title1 = CTkLabel(frame_adm1, text="Cadastro", font=("Helvetica", 15))
            lb_title1.grid(row=0, column=1, padx=5, pady=5, sticky="news")

            lb_acesso1 = CTkLabel(frame_adm1, text="Nome:", anchor="e")
            lb_acesso1.grid(row=1, column=0, sticky="we", padx=5, pady=5)
            in_acesso1 = CTkEntry(frame_adm1)
            in_acesso1.grid(row=1, column=1, columnspan=1, sticky="we", padx=5, pady=5)
            lb_acesso2 = CTkLabel(frame_adm1, text="E-mail:", anchor="e")
            lb_acesso2.grid(row=2, column=0, columnspan=1, sticky="we", padx=5, pady=5)
            in_acesso2 = CTkEntry(frame_adm1)
            in_acesso2.grid(row=2, column=1, columnspan=1, sticky="we", padx=5, pady=5)
            lb_acesso3 = CTkLabel(frame_adm1, text="Senha:", anchor="e")
            lb_acesso3.grid(row=3, column=0, columnspan=1, sticky="we", padx=5, pady=5)
            in_acesso3 = CTkEntry(frame_adm1)
            in_acesso3.grid(row=3, column=1, columnspan=1, sticky="we", padx=5, pady=5)
            bt_acesso1 = CTkButton(frame_adm1, text="Salvar")
            bt_acesso1.grid(row=4, column=0, sticky="we", padx=5, pady=5, columnspan=2)

            frame_adm2 = CTkFrame(jan_adm)
            frame_adm2.grid(row=2, column=0, sticky="news", padx=5, pady=5)
            lb_title2 = CTkLabel(frame_adm2, text="Login", font=("Helvetica", 15))
            lb_title2.grid(row=0, column=1, padx=5, pady=5, sticky="news")

            lb_acesso3 = CTkLabel(frame_adm2, text="E-mail:", anchor="e")
            lb_acesso3.grid(row=2, column=0, columnspan=1, sticky="we", padx=5, pady=5)
            in_acesso3 = CTkEntry(frame_adm2)
            in_acesso3.grid(row=2, column=1, columnspan=1, sticky="we", padx=5, pady=5)
            lb_acesso4 = CTkLabel(frame_adm2, text="Senha:", anchor="e")
            lb_acesso4.grid(row=3, column=0, columnspan=1, sticky="we", padx=5, pady=5)
            in_acesso4 = CTkEntry(frame_adm2)
            in_acesso4.grid(row=3, column=1, columnspan=1, sticky="we", padx=5, pady=5)
            bt_acesso2 = CTkButton(frame_adm2, text="Entrar")
            bt_acesso2.grid(row=4, column=0, sticky="we", padx=5, pady=5, columnspan=2)




            jan_adm.mainloop()

    def Menu_adm(self):
        menu_adm = CTk()
        menu_adm.title("Menu - Adm")
        menu_adm.geometry("600x700")
        menu_adm.config(padx=10, pady=10)
        set_default_color_theme("tema.json")
        menu_adm.iconbitmap("heisenburger.ico")
        frame_inserir = CTkFrame(menu_adm)
        frame_inserir.grid(row=0,column=0,pady=10)

        frame_deletar = CTkFrame(menu_adm)
        frame_deletar.grid(row=1, column=0,pady=10)

        lb_titulo_salvar = CTkLabel(frame_inserir, text='Inserir produto', anchor="center", font=("Helvetica", 20))
        lb_titulo_salvar.grid(row=0, column=0, sticky='we', rowspan=1, columnspan=3)

        entry_nome = CTkEntry(frame_inserir, placeholder_text='Nome', width=200)
        entry_nome.grid(row=1, column=0, columnspan=1, pady=5)

        entry_preco = CTkEntry(frame_inserir, placeholder_text='Preço', width=200)
        entry_preco.grid(row=2, column=0, columnspan=1, pady=5)

        bt_salvar = CTkButton(frame_inserir, text='Salvar Produto',command=lambda: [Cardapio().adcionar_produto(entry_nome.get(),float(entry_preco.get())),atualizar_cardapio()])
        bt_salvar.grid(row=1, column=2, padx=10, sticky='we', rowspan=2, )

        lb_titulo_deletar = CTkLabel(frame_deletar, text='Deletar Produto', anchor="center", font=("Helvetica", 20))
        lb_titulo_deletar.grid(row=0, column=0, sticky='we', rowspan=1, columnspan=3)

        entry_nome_deletar = CTkEntry(frame_deletar, placeholder_text='Nome', width=200)
        entry_nome_deletar.grid(row=1, column=0, columnspan=1, pady=5)

        bt_deletar = CTkButton(frame_deletar, text='Deletar Produto',command=lambda: [Cardapio().deletar_produto(entry_nome_deletar.get()),atualizar_cardapio()])
        bt_deletar.grid(row=1, column=2, padx=10, sticky='we', rowspan=2, )

        bt_notas_fiscais = CTkButton(menu_adm, text='Ver histórico de notas', command=lambda: Nota_Fiscal().notas_adm())
        bt_notas_fiscais.grid(row=2, column=0, padx=10,pady=10, rowspan=2 )

        frame_saida = CTkFrame(menu_adm)
        frame_saida.grid(row=6, column=0, padx=10, pady=10)

        lb_saida = CTkLabel(frame_saida, text='', anchor="center", font=("Helvetica", 15), width=30)
        lb_saida.grid(row=0, column=10,padx=10)

        lb_saida_nome = CTkLabel(frame_saida, text='', anchor="center", font=("Helvetica", 15), width=135)
        lb_saida_nome.grid(row=0, column=1, sticky='e',padx=10)

        def atualizar_cardapio():
            self.cardapio = Cardapio().gerar_cardapio()

            clientes_str = ""
            for cliente in self.cardapio:
                clientes_str += f"{cliente[1]}\n"
            lb_saida.configure(text="Preço \n    \n" + clientes_str,anchor="e")
            clientes_str = ""
            for cliente in self.cardapio:
                clientes_str += f"{cliente[0]}\n"
            lb_saida_nome.configure(text="Nome \n    \n" + clientes_str,anchor="w")

        atualizar_cardapio()

        menu_adm.mainloop()


    def janela_atendente(self):
        jan_atend = CTk()
        jan_atend.title("Lanchonete - Cliente")
        jan_atend.geometry("600x700")
        jan_atend.config(padx=10, pady=10)
        set_default_color_theme("tema.json")
        jan_atend.iconbitmap("heisenburger.ico")
        lb_atend = CTkLabel(jan_atend, text="Menu de Cliente", font=("Helvetica", 20))
        lb_atend.grid(row=0, column=1, columnspan=2)

        frame_atend1 = CTkFrame(jan_atend)
        frame_atend1.grid(row=1, column=0, sticky="news", padx=5, pady=5)
        lb_title = CTkLabel(frame_atend1, text="Cadastro", font=("Helvetica", 15))
        lb_title.grid(row=0, column=1, padx=5, pady=5, sticky="news")

        lb_acesso1 = CTkLabel(frame_atend1, text="Nome:", anchor="e")
        lb_acesso1.grid(row=1, column=0, sticky="we", padx=5, pady=5)
        in_acesso1 = CTkEntry(frame_atend1)
        in_acesso1.grid(row=1, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        lb_acesso2 = CTkLabel(frame_atend1, text="E-mail:", anchor="e")
        lb_acesso2.grid(row=2, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso2 = CTkEntry(frame_atend1)
        in_acesso2.grid(row=2, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        lb_acesso3 = CTkLabel(frame_atend1, text="Senha:", anchor="e")
        lb_acesso3.grid(row=3, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso3 = CTkEntry(frame_atend1)
        in_acesso3.grid(row=3, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        bt_acesso = CTkButton(frame_atend1, text="Salvar")
        bt_acesso.grid(row=4, column=0, sticky="we", padx=5, pady=5, columnspan=2)

        frame_atend2 = CTkFrame(jan_atend)
        frame_atend2.grid(row=2, column=0, sticky="news", padx=5, pady=5)
        lb_title2 = CTkLabel(frame_atend2, text="Login", font=("Helvetica", 15))
        lb_title2.grid(row=0, column=1, padx=5, pady=5, sticky="news")

        lb_acesso3 = CTkLabel(frame_atend2, text="E-mail:", anchor="e")
        lb_acesso3.grid(row=2, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso3 = CTkEntry(frame_atend2)
        in_acesso3.grid(row=2, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        lb_acesso4 = CTkLabel(frame_atend2, text="Senha:", anchor="e")
        lb_acesso4.grid(row=3, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso4 = CTkEntry(frame_atend2)
        in_acesso4.grid(row=3, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        bt_acesso2 = CTkButton(frame_atend2, text="Entrar")
        bt_acesso2.grid(row=4, column=0, sticky="we", padx=5, pady=5, columnspan=2)


        jan_atend.mainloop()

class Nota_Fiscal:
    def __init__(self):
        conexao = sqlite3.connect('lanchonete.db')
        cursor = conexao.cursor()
        cursor.execute('''
                            CREATE TABLE IF NOT EXISTS nota_fiscal (data_hora TEXT,produtos TEXT, valor FLOAT) 
                        ''')
        cursor.execute("SELECT*FROM nota_fiscal")
        # cursor.execute('DELETE FROM nota_fiscal')
        self.tudo = cursor.fetchall()
        # print(self.tudo)
        conexao.commit()
        conexao.close()

    def salvar_nota(self,comprados,total):
        self.comprados = comprados
        self.total = total
        self.data = datetime.now().strftime('%d/%m/%Y')
        self.hora = datetime.now().strftime('%H:%M')
        conexao = sqlite3.connect('lanchonete.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO nota_fiscal (data_hora, produtos, valor) VALUES(?,?,?)',
                       (f"{self.data} {self.hora}", self.comprados, self.total,))
        cursor.execute("SELECT*FROM nota_fiscal")
        # cursor.execute('DELETE FROM nota_fiscal')
        self.tudo = cursor.fetchall()
        #print(self.tudo)
        conexao.commit()
        conexao.close()
        self.nota_cliente()

    def nota_cliente(self):
        tela_nota = CTk()
        frame1 = CTkFrame(tela_nota)
        frame1.grid(row=0,column=0,sticky="we",padx=15,pady=15)
        palavras = self.comprados.split("| ")

        label_data = CTkLabel(frame1, text=f"Data/Hora",font=("Helvetica", 16),width=90,fg_color="#9c37a3")
        label_data.grid(row=0, column=0)

        label_produtos = CTkLabel(frame1, text="Produtos",font=("Helvetica", 16),width=130,fg_color="#9c37a3")
        label_produtos.grid(row=0, column=1)

        label_preco = CTkLabel(frame1, text="Total",font=("Helvetica", 16),width=90,fg_color="#9c37a3")
        label_preco.grid(row=0, column=2)

        label1 = CTkLabel(frame1, text=self.data)
        label1.grid(row=1, column=0,padx=10,sticky="w")

        label2 = CTkLabel(frame1, text=self.hora,anchor="w")
        label2.grid(row=2, column=0,sticky="w",padx=10)

        for i in range(0, len(palavras)):
            label3 = CTkLabel(frame1, text=palavras[i])
            label3.grid(row=i+1, column=1)

        label4 = CTkLabel(frame1,text=f"R$ {round(self.total,2)}")
        label4.grid(row=1, column=2,padx=10)

        botao_voltar = CTkButton(tela_nota, text="Voltar",command=lambda: [tela_nota.destroy(),Cardapio_Menu()])
        botao_voltar.grid(row=1,column=0,columnspan=1,pady=5)

        tela_nota.mainloop()

    def notas_adm(self):
        tela_nota = CTk()
        frame1 = CTkScrollableFrame(tela_nota,label_text="Data/Hora                           Produtos                                 Total",width=360,height=500,label_fg_color="#9c37a3",label_anchor="w",fg_color="#212121")
        frame1.grid(row=0, column=0, sticky="we", padx=15, pady=15)
        datas = []
        valores = []
        print(self.tudo)
        for notas in self.tudo:
            datas.append(notas[0])
            valores += str(notas[2])
        print(datas)
        i = 0
        y = 0
        for x in self.tudo:
            produtos = x[1].split(" | ")
            if y %2==0:
                label1 = CTkLabel(frame1, text=x[0], width=110,fg_color="#4a4a4a")
                label1.grid(row=i, column=0,rowspan=len(produtos),sticky="ns")
                contador = i
                for produto in produtos:
                    label2 = CTkLabel(frame1, text=produto, width=150,fg_color="#4a4a4a")
                    label2.grid(row=contador, column=1)
                    contador += 1

                label4 = CTkLabel(frame1, text=f"R$ {round(x[2], 2)}", width=100,fg_color="#4a4a4a")
                label4.grid(row=i, column=2,sticky="ns",rowspan=len(produtos))

            else:
                label1 = CTkLabel(frame1, text=x[0], width=110)
                label1.grid(row=i, column=0, rowspan=len(produtos), sticky="ns")
                contador = i
                for produto in produtos:
                    label2 = CTkLabel(frame1, text=produto, width=130)
                    label2.grid(row=contador, column=1)
                    contador += 1

                label4 = CTkLabel(frame1, text=f"R$ {round(x[2], 2)}", width=100)
                label4.grid(row=i, column=2, sticky="ns", rowspan=len(produtos))
            y +=1 # contador ultilizado para deixar a linha preta ou branca
            i += len(produtos) #contador ultilizado para saber qual sera a próxima linha do CTk a ser impressa o label



        botao_voltar = CTkButton(tela_nota, text="Voltar", command=lambda: [tela_nota.destroy(), Cardapio_Menu()])
        botao_voltar.grid(row=1, column=0, columnspan=1, pady=5)

        tela_nota.mainloop()

class Cardapio:
    def __init__(self):
        pass
    def gerar_cardapio(self):
        conexao = sqlite3.connect('lanchonete.db')
        cursor = conexao.cursor()
        cursor.execute('''
                    CREATE TABLE IF NOT EXISTS cardapio (nome TEXT PRIMARY KEY, preco FLOAT) 
                ''')
        cursor.execute("SELECT*FROM cardapio")
        cardapio = cursor.fetchall()
        return cardapio
        conexao.commit()
        conexao.close()
    def adcionar_produto(self, nome, preco):
        conexao = sqlite3.connect('lanchonete.db')
        cursor = conexao.cursor()
        cursor.execute('INSERT INTO cardapio (nome, preco) VALUES(?,?)',(nome,preco))
        conexao.commit()
        conexao.close()

    def deletar_produto(self, nome):
        conexao = sqlite3.connect('lanchonete.db')
        cursor = conexao.cursor()
        cursor.execute('DELETE FROM cardapio WHERE nome = ?', (nome,))
        conexao.commit()
        conexao.close()

class Cardapio_Menu(CTk):
    def __init__(self):
        super().__init__()
        self.cardapio = Cardapio().gerar_cardapio()
        self.entradas_quantidade = {}
        set_default_color_theme("tema.json")
        self.contador = 0
        for i in self.cardapio:
            # Crie uma variável de controle para cada entrada
            self.contador += 1
            var = StringVar()
            frame = CTkFrame(self)
            frame.grid(row=self.contador, column=0,columnspan=2,sticky="we",pady=3,padx=7)

            texto = CTkLabel(frame, text=(i[0]),width=150,anchor="w", font=("Helvetica", 15))
            texto.grid(column=0, row=0, padx=5)

            preco = CTkLabel(frame, text=(f"R$ {i[1]}"), width=150, anchor="w", font=("Helvetica", 11))
            preco.grid(column=0, row=1, padx=5, pady=1)

            entrada = CTkComboBox(frame, values=["0","1","2","3","4","5","6","7","8","9"],width=60)
            entrada.grid(row=0, column=1,sticky="e", rowspan=2,padx=5)

            # Adicione a variável ao dicionário para acessá-la posteriormente
            self.entradas_quantidade[i] = entrada

        # Botão para imprimir os valores
        botao_imprimir = CTkButton(self, text="Finalizar compra", command=self.imprimir_valores)
        botao_imprimir.grid(row=(len(self.entradas_quantidade) + 1), column=1,pady=5,padx=5)

        botao_voltar = CTkButton(self, text="Voltar",command=lambda: [self.destroy(),Menu()],width=90)
        botao_voltar.grid(row=(len(self.entradas_quantidade) + 1),column=0,pady=5,padx=5)

        self.protocol("WM_DELETE_WINDOW", self.fechar_janela)

        self.mainloop()

    def imprimir_valores(self):
        #print(self.entradas_variaveis.items())
        comprados = ""
        total = 0
        print(len(self.entradas_quantidade.items()))

        for i, var in self.entradas_quantidade.items():
            quantidade = var.get()
            if int(quantidade) > 0:
                comprados += (f"{quantidade} X {i[0]} R${i[1]} | ")
                total += float(i[1])*float(quantidade)
        comprados = comprados[:-3]
        print(comprados)
        if total >0:
            self.fechar_janela()
            Nota_Fiscal().salvar_nota(comprados,total)

    def fechar_janela(self):
        self.destroy()
        self.quit()



    

if __name__ == "__main__":
    Menu().executar_menu()
