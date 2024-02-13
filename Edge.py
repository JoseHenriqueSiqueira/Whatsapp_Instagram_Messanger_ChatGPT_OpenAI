from selenium import webdriver
from subprocess import CREATE_NO_WINDOW
from selenium.webdriver.edge.service import Service

class EdgeDriver():

    def __init__(self):
        options = webdriver.EdgeOptions()
        service = Service()
        service.creation_flags = CREATE_NO_WINDOW
        self.driver = webdriver.Edge(options=options, service=service)