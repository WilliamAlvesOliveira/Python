from random import randint
import customtkinter as ctk


class JogoAdvinhacao:
    def __init__(self, master):
        self.master = master
        self.computador = randint(0, 1000)
        self.setup_ui()

    def setup_ui(self):
        self.master.title('Advinhação')
        self.master.geometry("400x300")

        frame = ctk.CTkFrame(self.master, width=400, height=300, fg_color='lightblue')
        frame.pack(fill="both", expand=True)

        titulo = ctk.CTkLabel(frame, text="Tente adivinhar o número!", font=("Arial", 22, "underline"))
        titulo.pack(pady=20)

        div_entrada = ctk.CTkFrame(frame, width=300, fg_color='lightblue')
        div_entrada.pack(pady=10)

        mensagem = ctk.CTkLabel(div_entrada, text='Palpite: ', font=('Arial', 16, 'bold'))
        mensagem.pack(side='left', padx=5)

        self.input_palpite = ctk.CTkEntry(div_entrada, placeholder_text='Número de 0 a 1000', width=200)
        self.input_palpite.pack(side='left', padx=5)
        self.input_palpite.bind("<Return>", self.verificar_palpite)

        botao_verificar = ctk.CTkButton(div_entrada, width=50, text='Verificar', command=self.verificar_palpite)
        botao_verificar.pack(side='left', padx=5)

        mensagem_result = ctk.CTkLabel(frame, text="Resultado", font=('Arial', 22, 'bold'))
        mensagem_result.pack(pady=10)

        self.label_feedback = ctk.CTkLabel(frame, text="", font=("Arial", 22))
        self.label_feedback.pack(pady=10)

        botao_novo_jogo = ctk.CTkButton(frame, text='Novo Jogo', command=self.novo_jogo)
        botao_novo_jogo.pack(pady=10)

    def novo_jogo(self):
        self.computador = randint(0, 1000)
        self.label_feedback.configure(text='')
        self.input_palpite.delete(0, 'end')

    def verificar_palpite(self, event=None):
        try:
            palpite = int(self.input_palpite.get())
            if self.computador > palpite:
                self.label_feedback.configure(text='Errou! meu número é maior')
            elif self.computador < palpite:
                self.label_feedback.configure(text='Errou! meu número é menor')
            else:
                self.label_feedback.configure(text='PARABÉNS! Você acertou.')
            self.input_palpite.delete(0, 'end')
        except ValueError:
            self.label_feedback.configure(text='ERRO! Digite um número válido.')
            self.input_palpite.delete(0, 'end')


if __name__ == "__main__":
    janela = ctk.CTk()
    jogo = JogoAdvinhacao(janela)
    janela.mainloop()
