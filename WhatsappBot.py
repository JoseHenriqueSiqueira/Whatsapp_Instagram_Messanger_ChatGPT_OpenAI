from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
from subprocess import CREATE_NO_WINDOW
from ChatBot import ChatBot
import time, sys

class WhatsAppBotGPT:
    def __init__(self, Number:str, chatbot):
        self.numero = Number
        self.service = Service(ChromeDriverManager().install())
        self.service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.service)
        self.msgbreak = ""
        self.Conversa = chatbot

    def run(self):
        """
         Método que inicia a conversa com o número especificado pelo usuário.
        """
        self.driver.get(f"https://web.whatsapp.com/send?phone={self.numero}")  # Navega até a página de conversa
        while len(self.driver.find_elements(By.ID, 'side')) < 1: # Aguarda até a página ser carregada completamente
            time.sleep(1)
        time.sleep(2)
        print("Sincronizando Mensagens...")
        while (len(self.driver.find_elements(By.XPATH,r"/html/body/div[1]/div/div/div[4]/div/div[2]/div/div[2]/div[2]/button"))) > 0: # Esperando as mensagens serem Sincronizadas
            time.sleep(1)
        time.sleep(2)
        print("Mensagens Sincronizadas")
        self.messages = list() # Inicializa a lista de mensagens
        while True: # Loop infinito para verificar novas mensagens
            time.sleep(1)  # Aguarda 1 segundo entre cada verificação
            elements = self.driver.find_elements(By.XPATH, f"//span[@data-testid='conversation-info-header-chat-title']") # Encontra o elemento que contem o nome da pessoa
            Name = f"{elements[0].text}:" # Extrai o nome da pessoa
            divs = self.driver.find_elements(By.XPATH, f"//div[contains(@data-pre-plain-text, '{Name}')]") # Pegando os divs responsáveis por conter as mensagens do usuário
            if divs:
                last_parent = divs[-1] # Obtendo o div mais recente
                child_elements = last_parent.find_elements(By.XPATH, "./*[not(contains(@class, '_1hl2r'))]") # Obtendo os elementos filhos do Div
                last_child = child_elements[-1] # Obtendo elemento mais recente
                text = last_child.text.replace("\n","") # Extraindo o texto do elemento mais recente (Mensagem mais recente do usuário)
                if text in self.messages: # Verifica se o texto esta na lista self.menssages
                    resposta = self.Conversa.Question(text) # Manda a última mensagem do usuário para o método "Question" da classe "ChatBot"
                    if resposta: # Verifica o método 'Question' retornou uma resposta
                        time.sleep(2) # Aguarda 2 segundos, tornando o script mais humano
                        elemento = self.driver.find_element(By.XPATH, f'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p') # Obtendo elemento responsável por mandar as mensagens
                        elemento.clear() # Limpa a mensagem (Pratica comum para evitar mensagens não intencionais)
                        elemento.send_keys(resposta) # Escreve a mensagem no elemento
                        time.sleep(1) # Aguarda mais 1 segundo
                        elemento.send_keys(Keys.ENTER) # Manda a mensagem
                    continue # Verificação das mensagens recomeçando
                else:
                    self.messages.append(text) # Adiciona a ultima mensagem na lista self.messages
            else:
                print("Não há mensagens do usuário.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("Phone number and API_KEY is mandatory and must be passed as an argument.")
    phone_number = sys.argv[1]  # Obtém o número de telefone do destinatário da linha de comando
    Api_key = sys.argv[2] # Obtém a API KEY da linha de comando
    Chatbot = ChatBot(API_KEY=Api_key)
    WhatsappBot = WhatsAppBotGPT(Number=phone_number, chatbot=Chatbot)
    WhatsappBot.run()


