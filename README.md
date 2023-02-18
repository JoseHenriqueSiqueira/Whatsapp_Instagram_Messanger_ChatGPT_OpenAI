# WhatsApp, Instagram and Messenger ChatBot using OpenAI API
 This repository showcases a ChatBot integrated with WhatsApp, Instagram and Messenger, using OpenAI API (such as ChatGPT). With it, you can interact with a highly trained language model to answer your questions and perform specific tasks quickly and efficiently. Don't miss the opportunity to experience cutting-edge AI technology directly on your WhatsApp, Instagram or Messenger.
 
## Preview

### WhatsApp
<p float="left">
<p> Connect your whatsapp web. </p>
<img src="/Images/Login.png?raw=true">
<p> Wait for the messages to synchronize, after that the last message from the user will be read and a response will be returned. </p>
<img src="/Images/example.png?raw=true">
</p>

### Instagram

<p float="left">
<p> Instagram Login </p>
<img src="/Images/InstagramLogin.png?raw=true">
<p> Bot working </p>
<img src="/Images/Instaexample.png?raw=true">
</p>

### Messenger

<p float="left">
<p> Messenger Login </p>
<img src="/Images/MessengerLogin.png?raw=true">
<p> Bot working </p>
<img src="/Images/MessengerExample.png?raw=true">
</p>

## Getting Started
    To get started with the Whatsapp Bot, Instagram and Messenger(Facebook), you will need to clone this repository and have Python 3 installed on your system.

### Prerequisites
    To run this project, you will need to have the following dependencies installed:
    • selenium
    • subprocess
    • time
    • sys
    • webdriver_manager
    • openai

### Installing Dependencies
To install the dependencies, simply run the following command:
```console
 $ pip install -r requirements.txt
```

### Running the WhatsappBot
To run the WhatsappBot, navigate to the cloned repository and run the following command:
```console
 $ python WhatsappBot.py <phone_number> <api_key>
```

Where <phone_number> is the target phone number and <api_key> is your OpenAI API key.

### Running the InstagramBot
To run the InstagramBot, navigate to the cloned repository and run the following command:
```console
 $ python InstagramBot.py <user> <api_key>
```

Where <user> is the user target and <api_key> is your OpenAI API key.

### Running the MessengerBot
To run the MessengerBot, navigate to the cloned repository and run the following command:
```console
 $ python InstagramBot.py <user> <api_key>
```

Where <user> is the user target and <api_key> is your OpenAI API key.

## ChatBot Class
    The ChatBot class handles the connection with the OpenAI API and is responsible for sending and receiving messages.

## WhatsAppBotGPT Class
    The WhatsAppBotGPT class handles the interaction with Whatsapp and uses the ChatBot class to communicate with the OpenAI API.

## InstagramBotGPT Class
    The InstagramBotGPT class handles the interaction with Instagram and uses the ChatBot class to communicate with the OpenAI API.

## MessengerBotGPT Class
    The MessengerBotGPT class handles the interaction with Messenger and uses the ChatBot class to communicate with the OpenAI API.

## Built With
  [Python 3.9.X](https://www.python.org/downloads/) - The programming language used <br/>
  [Selenium](https://www.selenium.dev/) - The web automation framework used <br/>
  [ChromeDriver](https://chromedriver.chromium.org/home) - The web driver used for automating Google Chrome <br/>
  [OpenAI](https://openai.com) - The AI language model used for the bot's conversation. <br/>

## Contributing
    If you would like to contribute to this project, feel free to open a pull request with your changes.

## Authors
    José Henrique da Silva Siqueira

## License
   This project is licensed under the [MIT License](/LICENSE).

## Acknowledgements
    OpenAI - For providing the AI language model used in this project.




