import tkinter as tk

JanelaLogin = tk.Tk()

class LoginView():
    def __init__(self):
        self.janelaLogin = JanelaLogin
        self.login_tela()
        self.janelaLogin.mainloop()

    def login_tela(self):
        self.janelaLogin.title('Login')
        self.janelaLogin.configure(background= '#736e8f')