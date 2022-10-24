from kivy.app import App
from kivy.lang import Builder
import requests

InterfaceGUI= Builder.load_file("tela.kv")

class Meu_Projeto(App):
    def build(self):
        return InterfaceGUI
    
    
    def on_start(self):
        self.root.ids["Dollar"].text = f"Dollar R${self.cotacao('USD')}"
        self.root.ids["Euro"].text = f"Euro R${self.cotacao('EUR')}"
        self.root.ids["Yen"].text = f"Iene R${self.cotacao('JPY')}"
        self.root.ids["Pounds"].text = f"Libra R${self.cotacao('GBP')}"
    def cotacao(self, Moeda):
        link= f"https://economia.awesomeapi.com.br/last/{Moeda}-BRL"
        requisicao= requests.get(link)
        dic_requisicao= requisicao.json()
        cotacao1= dic_requisicao[f"{Moeda}BRL"]["bid"]
        return cotacao1

Meu_Projeto().run()