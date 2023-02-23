from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from subprocess import CREATE_NO_WINDOW
from ChatBot import ChatBot
import sys, time

class MessengerBotGPT:
    def __init__(self, user:str, chatbot: ChatBot):
        if not (isinstance(user, str) or isinstance(chatbot, ChatBot)):
            raise ValueError("'user' must be a str and 'chatbot' must be an Instance")
        self.BotGPT = chatbot
        self.service = Service(ChromeDriverManager().install())
        self.service.creationflags = CREATE_NO_WINDOW
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get(f"https://m.me/{user}")
        while len(self.driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div[1]/div/div/div/div/div[1]/span[1]/a')) < 1:
            continue
        self.wait = WebDriverWait(self.driver, 15)

    def BotStart(self) -> None: #Método para Iniciar o Bot.                                               
        msginputXPATH = r'/html/body/div[1]/div/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]/div[2]/div/div/div[1]/p'
        messages_element = self.driver.find_elements(By.CSS_SELECTOR, '.xcrg951.x1r145dm')
        ignoreTxt = messages_element[-1].text if messages_element else ""
        while True:
            messages_element = self.driver.find_elements(By.CSS_SELECTOR, '.xcrg951.x1r145dm')
            last_message = messages_element[-1].text if messages_element else ""
            if last_message == ignoreTxt: # Caso a ultima mensagem for igual ao texto ignorado no começo da função, o loop volta para o começo e fica esperando uma mensagem diferente.
                continue
            else:
                Resposta = self.BotGPT.Question(last_message) # Manda a mensagem para o método "Question(msg:str)" da classe "ChatBot" e obtém uma resposta.
                if Resposta: # Caso retorne uma resposta válida, manda para o usuário.
                    self.wait.until(EC.presence_of_element_located((By.XPATH, msginputXPATH)))
                    msginput = self.driver.find_element(By.XPATH, msginputXPATH)
                    msginput.send_keys(Resposta)
                    time.sleep(2)
                    msginput.send_keys(Keys.ENTER)

    def GetMessager(self, UserType:str) -> list[str]: # Método de Debug. Esse método obtem as mensagem do usuario alvo ou do author. Use "author" ou "user" como parâmetro, caso contrário retornara um erro.
        Types = {"author":".x1n2onr6.xuk3077", 'user':'.xcrg951.x1r145dm'}
        if not isinstance(UserType, str):
            raise ValueError("UserType must be an str")
        if UserType not in Types.keys():
            raise Exception("Invalid parameter, use 'author' or 'user'")    
        UserType = Types.get(UserType)
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, UserType)))
        messages_element = self.driver.find_elements(By.CSS_SELECTOR, UserType)
        dados = [element.text for element in messages_element]
        return dados



if __name__ == "__main__":
    if len(sys.argv) < 3:
        raise Exception("USER and API_KEY is mandatory and must be passed as an argument.")
    USER = sys.argv[1] 
    API_KEY = sys.argv[2] 
    BotGPT = ChatBot(API_KEY)
    MessengerBot = MessengerBotGPT(user=USER, chatbot=BotGPT)
    MessengerBot.BotStart()

