from customtkinter  import *
import sqlite3


class Produto:
    def __init__(self, cod, nome, preco):
        self.cod = cod
        self.nome = nome
        self.preco = preco

class Cardapio:
    def __init__(self):
        self.lista_cardapio = []
    
    def adicionar_produto_cardapio(self, produto):
        self.lista_cardapio.append(produto)
    
    def exibir_cardapio(self):
        pass
        #print('Cardapio:')
        #for produto in self.lista_cardapio:
        #print(f'{produto.cod} - {produto.nome} : R$ {produto.preco}')

class Pedido:
    def __init__(self):
        self.lista_pedido = []
    
    def adicionar_produto(self, produto):
        self.lista_pedido.append(produto)
    
    def exibir_pedido(self):
        pass
        #total = 0
       # for produto in self.lista_pedido:

        #    total += produto.preco
            #print(f'{produto.nome} : R$ {produto.preco}')
        #print(f'Total: R$ {total}')

class Menu(CTk):
    def __init__(self):
        super(Menu, self).__init__()
        self.title("Lanchonete")
        self.geometry("600x500")
        self.config(padx=10, pady=10)
        set_default_color_theme("tema.json")
        self.iconbitmap("heisenburger.ico")
        self.grid_columnconfigure(0, weight=1)


        #Menu Inicial
        self.lb_menu = CTkLabel(self, text="Acessar como:", font=("Helvetica", 20))
        self.lb_menu.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        self.bt_menu1 = CTkButton(self, text="Administrador", command=lambda: [app.destroy(), self.janela_adm()])
        self.bt_menu1.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.bt_menu2 = CTkButton(self, text="Atendente", command=lambda: [app.destroy(), self.janela_atend()])
        self.bt_menu2.grid(row=2, column=0, padx=5, pady=5, sticky="ew")


        self.pedido = Pedido()
        self.cardapio = Cardapio()


    def janela_adm(self):
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
        in_acesso1 = CTkEntry(frame_adm1, placeholder_text="Seu primeiro nome")
        in_acesso1.grid(row=1, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        lb_acesso2 = CTkLabel(frame_adm1, text="E-mail:", anchor="e")
        lb_acesso2.grid(row=2, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso2 = CTkEntry(frame_adm1, placeholder_text="usuario@exemplo.com")
        in_acesso2.grid(row=2, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        lb_acesso3 = CTkLabel(frame_adm1, text="Senha:", anchor="e")
        lb_acesso3.grid(row=3, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso3 = CTkEntry(frame_adm1, placeholder_text="Deve conter # dígitos")
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



    def janela_atend(self):
        jan_atend = CTk()
        jan_atend.title("Lanchonete - Atendente")
        jan_atend.geometry("600x700")
        jan_atend.config(padx=10, pady=10)
        set_default_color_theme("tema.json")
        jan_atend.iconbitmap("heisenburger.ico")

        lb_atend = CTkLabel(jan_atend, text="Menu de Atendente", font=("Helvetica", 20))
        lb_atend.grid(row=0, column=1, columnspan=2)

        frame_atend1 = CTkFrame(jan_atend)
        frame_atend1.grid(row=1, column=0, sticky="news", padx=5, pady=5)
        lb_title = CTkLabel(frame_atend1, text="Cadastro", font=("Helvetica", 15))
        lb_title.grid(row=0, column=1, padx=5, pady=5, sticky="news")

        lb_acesso1 = CTkLabel(frame_atend1, text="Nome:", anchor="e")
        lb_acesso1.grid(row=1, column=0, sticky="we", padx=5, pady=5)
        in_acesso1 = CTkEntry(frame_atend1, placeholder_text="Seu primeiro nome")
        in_acesso1.grid(row=1, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        lb_acesso2 = CTkLabel(frame_atend1, text="E-mail:", anchor="e")
        lb_acesso2.grid(row=2, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso2 = CTkEntry(frame_atend1, placeholder_text="usuario@exemplo.com")
        in_acesso2.grid(row=2, column=1, columnspan=1, sticky="we", padx=5, pady=5)
        lb_acesso3 = CTkLabel(frame_atend1, text="Senha:", anchor="e")
        lb_acesso3.grid(row=3, column=0, columnspan=1, sticky="we", padx=5, pady=5)
        in_acesso3 = CTkEntry(frame_atend1, placeholder_text="Deve conter # dígitos")
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



    
    def produtos_predefinidos(self):

        produto1 = Produto(1, "Hamburguer", 10.0)
        produto2 = Produto(2, "Batata Frita", 5.0)
        produto3 = Produto(3, "Refrigerante", 3.0)

        self.cardapio.adicionar_produto_cardapio(produto1)
        self.cardapio.adicionar_produto_cardapio(produto2)
        self.cardapio.adicionar_produto_cardapio(produto3)
    
    def executar_menu(self):
        pass


        def executar_menu_admin(self):
            pass


Menu().executar_menu()
app = Menu()
app.mainloop()

if __name__ == "__main__":
    app()
