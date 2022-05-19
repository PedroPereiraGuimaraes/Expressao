#biblioteca para a criação do GUI
import tkinter as tk
from tkinter import font as tkfont
#biblioteca para reproduzir o video
import cv2

def reproduzirVideo(nome):

    cap = cv2.VideoCapture(nome)

    # Verificar se o video foi aberto
    if (cap.isOpened() == False):
        print("Error opening video  file")

    # Ler até o video terminar
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow('Frame', frame)
            # Aperte Q para sair
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    cap.release()

    # Fecha a aba de video
    cv2.destroyAllWindows()


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Righteous', size=16)
        self.base_font = tkfont.Font(family='Righteous', size=13)

        # o recipiente é onde vamos empilhar um monte de quadros em cima do outro,
        # então o que queremos visível será levantada acima dos outros
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.propagate(0)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (InicialWhite, InicialBlack, HomeWhite, HomeBlack, ExpressaoWhite,
                  ExpressaoBlack, AudiosWhite, AudiosBlack, CadastroWhite, CadastroBlack,
                  FonemasWhite, FonemasBlack):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # definindo a pagina de inicio
        self.show_frame("InicialWhite")

    def show_frame(self, page_name):
        # mostrando o frame da pagina de inicio
        frame = self.frames[page_name]
        frame.tkraise()


class InicialWhite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        controller.geometry("%dx%d+%d+%d" % (
            1280, 720, (controller.winfo_screenwidth() / 2 - 640), (controller.winfo_screenmmheight() / 2 - 100)))
        controller.title('Expressão')
        controller.resizable(0, 0)

        # definindo as imagens como globais
        global img
        img = list(range(67))

        # entrada das imagens
        img[0] = tk.PhotoImage(file="./imagens/inicial/white/fundo_entrada_white.png")
        img[1] = tk.PhotoImage(file="./imagens/inicial/white/botao_tema_white.png")
        img[2] = tk.PhotoImage(file="./imagens/inicial/white/botao_entrar_white.png")

        # fundo
        tk.Label(self, image=img[0], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_tema
        tk.Button(self, image=img[1], bd=0, bg='#FFF500', activebackground='#FFF500',
                  command=lambda: controller.show_frame("InicialBlack")).place(x=1180, y=10)
        # botao_entrar
        tk.Button(self, image=img[2], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("HomeWhite")).place(x=585, y=420)
        # entrada_texto_nome
        user = tk.StringVar(self)
        user.set("Digite seu nome")
        tk.Entry(self, textvariable=user, width=19, foreground='black', font=controller.title_font, bd=0, relief="ridge",
                 bg='#FDFDF4').place(x=545, y=340)
        # nome_fono
        OptionList = [
            "Selecione um nome",
            "Elisa",
            "Pedro",
            "Carla"
        ]
        variable = tk.StringVar(self)
        variable.set(OptionList[0])
        fono = tk.OptionMenu(self, variable, *OptionList)
        fono.config(width=17, font=controller.title_font, bg="#FDFDF4", activebackground="#FDFDF4", border=0, relief="ridge")
        fono.place(x=540, y=265)


class InicialBlack(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[3] = tk.PhotoImage(file="./imagens/inicial/black/fundo_inicial_black.png")
        img[4] = tk.PhotoImage(file="./imagens/inicial/black/botao_tema_black.png")
        img[5] = tk.PhotoImage(file="./imagens/inicial/black/botao_entrar_black.png")

        # fundo
        tk.Label(self, image=img[3], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_tema
        tk.Button(self, image=img[4], bd=0, bg='#424242', activebackground='#424242',
                  command=lambda: controller.show_frame("InicialWhite")).place(x=1180, y=10)
        # botao_entrar
        tk.Button(self, image=img[5], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("HomeBlack")).place(x=585, y=420)
        # entrada_texto_nome
        user = tk.StringVar(self)
        user.set("Digite seu nome")
        tk.Entry(self, textvariable=user, width=19, foreground='white', font=controller.title_font, bd=0,
                 bg='#5D5D5D').place(x=545, y=340)
        # nome_fono
        OptionList = [
            "Selecione um nome",
            "Elisa",
            "Pedro",
            "Carla"
        ]
        variable = tk.StringVar(self)
        variable.set(OptionList[0])
        fono = tk.OptionMenu(self, variable, *OptionList)
        fono.config(width=17, font=controller.title_font, foreground='white', activeforeground='white', bg="#5D5D5D", activebackground="#5D5D5D", border=0,
                    relief="ridge")
        fono.place(x=540, y=265)


class HomeWhite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[6] = tk.PhotoImage(file="./imagens/home/white/fundo_home_white.png")
        img[7] = tk.PhotoImage(file="./imagens/home/white/botao_tema_white.png")
        img[8] = tk.PhotoImage(file="./imagens/home/white/botao_ajuda.png")
        img[9] = tk.PhotoImage(file="./imagens/home/white/botao_sobre_white.png")
        img[10] = tk.PhotoImage(file="./imagens/home/white/botao_fonemas_white.png")
        img[11] = tk.PhotoImage(file="./imagens/home/white/botao_audios_white.png")
        img[12] = tk.PhotoImage(file="./imagens/home/white/botao_expressao_white.png")

        # fundo
        tk.Label(self, image=img[6], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_tema
        tk.Button(self, image=img[7], bd=0, bg='#169E00', activebackground='#169E00',
                  command=lambda: controller.show_frame("HomeBlack")).place(x=1180, y=10)
        # botao_ajuda
        tk.Button(self, image=img[8], bd=0, bg='#FFFFFF', activebackground='#FFFFFF').place(x=10, y=10)
        # botao_sobre
        tk.Button(self, image=img[9], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("")).place(x=110, y=50)
        # botao_fonemas
        tk.Button(self, image=img[10], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("FonemasWhite")).place(x=410, y=50)
        # botao_audios
        tk.Button(self, image=img[11], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("AudiosWhite")).place(x=680, y=370)
        # botao_expressao
        tk.Button(self, image=img[12], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("ExpressaoWhite")).place(x=980, y=370)


class HomeBlack(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[13] = tk.PhotoImage(file="./imagens/home/black/fundo_home_black.png")
        img[14] = tk.PhotoImage(file="./imagens/home/black/botao_tema_black.png")
        img[15] = tk.PhotoImage(file="./imagens/home/black/botao_ajuda.png")
        img[16] = tk.PhotoImage(file="./imagens/home/black/botao_sobre_black.png")
        img[17] = tk.PhotoImage(file="./imagens/home/black/botao_fonemas_black.png")
        img[18] = tk.PhotoImage(file="./imagens/home/black/botao_audios_black.png")
        img[19] = tk.PhotoImage(file="./imagens/home/black/botao_expressao_black.png")

        # fundo
        tk.Label(self, image=img[13], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_tema
        tk.Button(self, image=img[14], bd=0, bg='#424242', activebackground='#424242',
                  command=lambda: controller.show_frame("HomeWhite")).place(x=1180, y=10)
        # botao_ajuda
        tk.Button(self, image=img[15], bd=0, bg='#5D5D5D', activebackground='#5D5D5D').place(x=10, y=10)
        # botao_sobre
        tk.Button(self, image=img[16], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=110, y=50)
        # botao_fonemas
        tk.Button(self, image=img[17], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("FonemasBlack")).place(x=410, y=50)
        # botao_audios
        tk.Button(self, image=img[18], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("AudiosBlack")).place(x=680, y=370)
        # botao_expressao
        tk.Button(self, image=img[19], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("ExpressaoBlack")).place(x=980, y=370)


class ExpressaoWhite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[20] = tk.PhotoImage(file="./imagens/expressao/white/fundo_expressao_white.png")
        img[21] = tk.PhotoImage(file="./imagens/expressao/white/homebutton.png")
        img[22] = tk.PhotoImage(file="./imagens/expressao/white/botao_ajuda.png")
        img[23] = tk.PhotoImage(file="./imagens/expressao/white/botao_gravar_white.png")
        img[24] = tk.PhotoImage(file="./imagens/expressao/white/botao_escutar_white.png")
        img[25] = tk.PhotoImage(file="./imagens/expressao/white/botao_enviar_white.png")
        img[26] = tk.PhotoImage(file="./imagens/expressao/white/certo_white.png")
        img[27] = tk.PhotoImage(file="./imagens/expressao/white/botao_go_white.png")
        img[28] = tk.PhotoImage(file="./imagens/expressao/white/botao_back_white.png")

        # fundo
        tk.Label(self, image=img[20], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_home
        tk.Button(self, image=img[21], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("HomeWhite")).place(x=1180, y=10)
        # botao_ajuda
        tk.Button(self, image=img[22], bd=0, bg='#FF109F', activebackground='#FF109F',
                  command=lambda: controller.show_frame("")).place(x=10, y=10)
        # botao_gravar
        tk.Button(self, image=img[23], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("")).place(x=250, y=500)
        # botao_escutar
        tk.Button(self, image=img[24], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=560, y=500)
        # botao_enviar
        tk.Button(self, image=img[25], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=870, y=500)
        # certo/errado
        tk.Label(self, image=img[26], bd=0, bg='#FFFFFF', activebackground='#FFFFFF').place(x=610, y=600)
        # botao_go
        tk.Button(self, image=img[27], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("")).place(x=710, y=600)
        # botao_back
        tk.Button(self, image=img[28], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("")).place(x=500, y=600)


class ExpressaoBlack(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[29] = tk.PhotoImage(file="./imagens/expressao/black/fundo_expressao_black.png")
        img[30] = tk.PhotoImage(file="./imagens/expressao/black/homebutton.png")
        img[31] = tk.PhotoImage(file="./imagens/expressao/black/botao_ajuda.png")
        img[32] = tk.PhotoImage(file="./imagens/expressao/black/botao_gravar_black.png")
        img[33] = tk.PhotoImage(file="./imagens/expressao/black/botao_escutar_black.png")
        img[34] = tk.PhotoImage(file="./imagens/expressao/black/botao_enviar_black.png")
        img[35] = tk.PhotoImage(file="./imagens/expressao/black/certo_black.png")
        img[36] = tk.PhotoImage(file="./imagens/expressao/black/botao_go_black.png")
        img[37] = tk.PhotoImage(file="./imagens/expressao/black/botao_back_black.png")

        # fundo
        tk.Label(self, image=img[29], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_home
        tk.Button(self, image=img[30], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("HomeBlack")).place(x=1180, y=10)
        # botao_ajuda
        tk.Button(self, image=img[31], bd=0, bg='#424242', activebackground='#424242',
                  command=lambda: controller.show_frame("")).place(x=10, y=10)
        # botao_gravar
        tk.Button(self, image=img[32], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=250, y=500)
        # botao_escutar
        tk.Button(self, image=img[33], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=560, y=500)
        # botao_enviar
        tk.Button(self, image=img[34], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=870, y=500)
        # certo/errado
        tk.Label(self, image=img[35], bd=0, bg='#5D5D5D', activebackground='#5D5D5D').place(x=610, y=600)
        # botao_go
        tk.Button(self, image=img[36], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=710, y=600)
        # botao_back
        tk.Button(self, image=img[37], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=500, y=600)


class AudiosWhite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[38] = tk.PhotoImage(file="./imagens/audios/white/fundo_audios_white.png")
        img[39] = tk.PhotoImage(file="./imagens/audios/white/homebutton.png")
        img[40] = tk.PhotoImage(file="./imagens/audios/white/botao_ajuda.png")


        # fundo
        tk.Label(self, image=img[38], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_home
        tk.Button(self, image=img[39], bd=0, bg='#169E00', activebackground='#169E00',
                  command=lambda: controller.show_frame("HomeWhite")).place(x=1180, y=10)
        # botao_ajuda
        tk.Button(self, image=img[40], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("")).place(x=10, y=10)


class AudiosBlack(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[41] = tk.PhotoImage(file="./imagens/audios/black/fundo_audios_black.png")
        img[42] = tk.PhotoImage(file="./imagens/audios/black/homebutton.png")
        img[43] = tk.PhotoImage(file="./imagens/audios/black/botao_ajuda.png")

        # fundo
        tk.Label(self, image=img[41], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_home
        tk.Button(self, image=img[42], bd=0, bg='#424242', activebackground='#424242',
                  command=lambda: controller.show_frame("HomeBlack")).place(x=1180, y=10)
        # botao_ajuda
        tk.Button(self, image=img[43], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=10, y=10)


class CadastroWhite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[44] = tk.PhotoImage(file="./imagens/cadastro/white/fundo_cadastro_white.png")
        img[45] = tk.PhotoImage(file="./imagens/cadastro/white/botao_ajuda.png")
        img[46] = tk.PhotoImage(file="./imagens/cadastro/white/botao_tema_white.png")
        img[47] = tk.PhotoImage(file="./imagens/cadastro/white/botao_criar_white.png")

        # fundo
        tk.Label(self, image=img[44], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_ajuda
        tk.Button(self, image=img[45], bd=0, bg='#FF109F', activebackground='#FF109F').place(x=55, y=10)
        # botao_tema
        tk.Button(self, image=img[46], bd=0, bg='#FFF500', activebackground='#FFF500',
                  command=lambda: controller.show_frame("CadastroBlack")).place(x=1180, y=10)
        # botao_criar_usuario
        tk.Button(self, image=img[47], bd=0, bg='#FFFFFF', activebackground='#FFFFFF').place(x=315, y=420)
        # botao_criar_fono
        tk.Button(self, image=img[47], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',).place(x=855, y=420)
        # nome_fono
        OptionList = [
            "Selecione um nome",
            "Elisa",
            "Pedro",
            "Carla"
        ]
        variable = tk.StringVar(self)
        variable.set(OptionList[0])
        fono = tk.OptionMenu(self, variable, *OptionList)
        fono.config(width=17, font=controller.title_font, bg="#FFFFFF", activebackground="#FFFFFF", border=0,
                    relief="ridge")
        fono.place(x=270, y=260)
        # entrada_texto_nome
        user = tk.StringVar(self)
        user.set("Digite seu nome")
        tk.Entry(self, textvariable=user, width=19, foreground='black', font=controller.title_font, bd=0,
                 relief="ridge",
                 bg='#FFFFFF').place(x=275, y=330)
        # entrada_texto_nome_fonoaudiologo
        fono = tk.StringVar(self)
        fono.set("Digite seu nome")
        tk.Entry(self, textvariable=fono, width=19, foreground='black', font=controller.title_font, bd=0,
                 relief="ridge",
                 bg='#FFFFFF').place(x=815, y=270)
        # entrada_texto_id
        id = tk.StringVar(self)
        id.set("Digite seu id")
        tk.Entry(self, textvariable=id, width=19, foreground='black', font=controller.title_font, bd=0,
                 relief="ridge",
                 bg='#FFFFFF').place(x=815, y=330)


class CadastroBlack(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[48] = tk.PhotoImage(file="./imagens/cadastro/black/fundo_cadastro_black.png")
        img[49] = tk.PhotoImage(file="./imagens/cadastro/black/botao_ajuda.png")
        img[50] = tk.PhotoImage(file="./imagens/cadastro/black/botao_tema_black.png")
        img[51] = tk.PhotoImage(file="./imagens/cadastro/black/botao_criar_black.png")

        # fundo
        tk.Label(self, image=img[48], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_ajuda
        tk.Button(self, image=img[49], bd=0, bg='#00B4B4', activebackground='#00B4B4').place(x=55, y=10)
        # botao_tema
        tk.Button(self, image=img[50], bd=0, bg='#424242', activebackground='#424242',
                  command=lambda: controller.show_frame("CadastroWhite")).place(x=1180, y=10)
        # botao_criar_usuario
        tk.Button(self, image=img[51], bd=0, bg='#5D5D5D', activebackground='#5D5D5D').place(x=320, y=420)
        # botao_criar_fono
        tk.Button(self, image=img[51], bd=0, bg='#5D5D5D', activebackground='#5D5D5D', ).place(x=855, y=420)
        # nome_fono
        OptionList = [
            "Selecione um nome",
            "Elisa",
            "Pedro",
            "Carla"
        ]
        variable = tk.StringVar(self)
        variable.set(OptionList[0])
        fono = tk.OptionMenu(self, variable, *OptionList)
        fono.config(width=17, font=controller.title_font, bg="#5D5D5D", foreground='white',
                    activeforeground='white', activebackground="#5D5D5D", border=0,
                    relief="ridge")
        fono.place(x=270, y=260)
        # entrada_texto_nome
        user = tk.StringVar(self)
        user.set("Digite seu nome")
        tk.Entry(self, textvariable=user, width=19, foreground='white', font=controller.title_font, bd=0,
                 relief="ridge",
                 bg='#5D5D5D').place(x=275, y=330)
        # entrada_texto_nome_fonoaudiologo
        fono = tk.StringVar(self)
        fono.set("Digite seu nome")
        tk.Entry(self, textvariable=fono, width=19, foreground='white', font=controller.title_font, bd=0,
                 relief="ridge",
                 bg='#5D5D5D').place(x=815, y=270)
        # entrada_texto_id
        id = tk.StringVar(self)
        id.set("Digite seu id")
        tk.Entry(self, textvariable=id, width=19, foreground='white', font=controller.title_font, bd=0,
                 relief="ridge",
                 bg='#5D5D5D').place(x=815, y=330)


class FonemasWhite(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[52] = tk.PhotoImage(file="./imagens/fonemas/white/fundo_fonemas_white.png")
        img[53] = tk.PhotoImage(file="./imagens/fonemas/white/botao_ajuda.png")
        img[54] = tk.PhotoImage(file="./imagens/fonemas/white/homebutton.png")
        img[55] = tk.PhotoImage(file="./imagens/fonemas/white/botao_consoantes_white.png")
        img[56] = tk.PhotoImage(file="./imagens/fonemas/white/botao_verbais_white.png")
        img[57] = tk.PhotoImage(file="./imagens/fonemas/white/botao_go_white.png")
        img[58] = tk.PhotoImage(file="./imagens/fonemas/white/botao_back_white.png")



        # fundo
        tk.Label(self, image=img[52], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_ajuda
        tk.Button(self, image=img[53], bd=0, bg='#FF109F', activebackground='#FF109F').place(x=55, y=10)
        # botao_home
        tk.Button(self, image=img[54], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("HomeWhite")).place(x=1180, y=10)
        # botao_consoantes
        tk.Button(self, image=img[55], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("")).place(x=100, y=100)
        # botao_verbais
        tk.Button(self, image=img[56], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: controller.show_frame("")).place(x=100, y=390)
        # botao_go
        tk.Button(self, image=img[57], bd=0, bg='#FF003D', activebackground='#FF003D',
                  command=lambda: controller.show_frame("")).place(x=940, y=240)
        # botao_back
        tk.Button(self, image=img[58], bd=0, bg='#FF003D', activebackground='#FF003D',
                  command=lambda: controller.show_frame("")).place(x=800, y=240)


class FonemasBlack(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # entrada das imagens
        img[59] = tk.PhotoImage(file="./imagens/fonemas/black/fundo_fonemas_black.png")
        img[60] = tk.PhotoImage(file="./imagens/fonemas/black/botao_ajuda.png")
        img[61] = tk.PhotoImage(file="./imagens/fonemas/black/homebutton.png")
        img[62] = tk.PhotoImage(file="./imagens/fonemas/black/botao_consoantes_black.png")
        img[63] = tk.PhotoImage(file="./imagens/fonemas/black/botao_verbais_black.png")
        img[64] = tk.PhotoImage(file="./imagens/fonemas/black/botao_go_black.png")
        img[65] = tk.PhotoImage(file="./imagens/fonemas/black/botao_back_black.png")
        img[66] = tk.PhotoImage(file="./imagens/fonemas/black/botao_play_black.png")


        # fundo
        tk.Label(self, image=img[59], bd=0, bg='#1D1D1D').place(x=0, y=0)
        # botao_ajuda
        tk.Button(self, image=img[60], bd=0, bg='#424242', activebackground='#424242').place(x=55, y=10)
        # botao_home
        tk.Button(self, image=img[61], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("HomeBlack")).place(x=1180, y=10)
        # botao_consoantes
        tk.Button(self, image=img[62], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=100, y=100)
        # botao_verbais
        tk.Button(self, image=img[63], bd=0, bg='#5D5D5D', activebackground='#5D5D5D',
                  command=lambda: controller.show_frame("")).place(x=100, y=390)
        # botao_go
        tk.Button(self, image=img[64], bd=0, bg='#05F4F4', activebackground='#05F4F4',
                  command=lambda: controller.show_frame("")).place(x=940, y=240)
        # botao_back
        tk.Button(self, image=img[65], bd=0, bg='#05F4F4', activebackground='#05F4F4',
                  command=lambda: controller.show_frame("")).place(x=800, y=240)
        # botao_reproduzir
        tk.Button(self, image=img[66], bd=0, bg='#FFFFFF', activebackground='#FFFFFF',
                  command=lambda: reproduzirVideo('./videos/consoantes/ch.mp4')).place(x=490, y=215)
        # texto
        tk.Label(self, text="Nome do fonema aparece aqui", font=controller.title_font, bg="#FFFFFF").place(x=750, y=168)
        # texto2
        tk.Label(self, text="Fonema decomposto", font=controller.title_font, bg="#FFFFFF").place(x=800, y=328)


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
