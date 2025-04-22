from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
import random
import string

class GeradorDeSenhasApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.label = Label(text='Gerador de Senhas', font_size=24)
        self.layout.add_widget(self.label)

        self.senha_input = TextInput(hint_text='Clique no botão para gerar uma senha', readonly=True, font_size=18)
        self.layout.add_widget(self.senha_input)

        self.gerar_button = Button(text='Gerar Senha', size_hint_y=None, height=50)
        self.gerar_button.bind(on_press=self.gerar_senha)
        self.layout.add_widget(self.gerar_button)

        return self.layout

    def gerar_senha(self, instance):
        tamanho = 12
        caracteres = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
        self.senha_input.text = senha

if __name__ == '__main__':
    GeradorDeSenhasApp().run()