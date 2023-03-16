from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
#from subprocess import CREATE_NO_WINDOW
from ChatBot import ChatBot
import sys

class InstagramBotGPT:
    def __init__(self, user:str, chatbot):
        self.BotGPT = chatbot
        self.service = Service(ChromeDriverManager().install())
        #self.service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get(f"https://ig.me/m/{user}")
        while len(self.driver.find_elements(By.CLASS_NAME, "_a9--._a9_1")) < 1:
            continue
        self.driver.find_element(By.CLASS_NAME, "_a9--._a9_1").click()
        self.wait = WebDriverWait(self.driver, 15)

    def BotStart(self) -> None: #Método para Iniciar o Bot.
        msginput = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea') # Obtem o elemento responsavel por mandar mensagens
        messages_element = self.driver.find_elements(By.CLASS_NAME, "_acqu") # Obtem as mensagens do usuario alvo
        ignoreTxt = messages_element[-1].text if messages_element else "" # Condição para ignorar a ultima mensagem do usuario, assim evitando o Bot responder uma duvida que ja foi respondida.
        while True:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "_acqu")))
            messages_element = self.driver.find_elements(By.CLASS_NAME, "_acqu") # Obtem as mensagens do usuario alvo
            last_message = messages_element[-1].text if messages_element else "" # Obtendo a ultima mensagem do usuario alvo
            if last_message == ignoreTxt: # Caso a ultima mensagem for igual ao texto ignorado no começo da função, o loop volta para o começo e fica esperando uma mensagem diferente.
                continue
            else:
                Resposta = self.BotGPT.Question(last_message) # Manda a mensagem para o método "Question(msg:str)" da classe "ChatBot" e obtém uma resposta.
                if Resposta: # Caso retorne uma resposta válida, manda para o usuário.
                    msginput.clear()
                    msginput.send_keys(Resposta)
                    msginput.send_keys(Keys.ENTER)

    def GetMessager(self, user_type:str) -> list[str]: # Método de Debug. Esse método obtem as mensagem do usuario alvo ou do author. Use "author" ou "user" como parâmetro, caso contrário retornara um erro.
        Types = {"author":"_acqv", 'user':'_acqu'}
        if not isinstance(user_type, str):
            raise ValueError("user_type must be an str")
        if user_type not in Types.keys():
            raise Exception("Invalid parameter, use 'author' or 'user'")
        user_type = Types.get(user_type)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, user_type)))
        messages_element = self.driver.find_elements(By.CLASS_NAME, user_type)
        dados = [element.text for element in messages_element]
        return dados
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("USER and API_KEY is mandatory and must be passed as an argument.")
    USER = sys.argv[1] 
    API_KEY = sys.argv[2] 
    BotGPT = ChatBot(API_KEY)
    InstBOT = InstagramBotGPT(user = USER, chatbot = BotGPT)
    InstBOT.BotStart()
