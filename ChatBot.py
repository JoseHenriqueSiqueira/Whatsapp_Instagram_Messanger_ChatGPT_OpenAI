import openai

class ChatBot:
    def __init__(self, API_KEY:str):
        self.conversation = []
        openai.api_key = API_KEY

    def Question(self, question:str) -> str:
        try:
            if question+'\n' == self.conversation[-2]:
                return
        except:
            pass
        conversation_history = " ".join([str(item) for item in self.conversation])
        response = ""
        while response == "":
            try:
                response = openai.Completion.create(
                engine = "text-davinci-002",
                prompt = question + " " + conversation_history,
                max_tokens = 1024,
                n = 1,
                stop = None,
                temperature = 0.5,
                ).get("choices")[0].get("text").strip()
            except Exception as e:
                self.Reset()
                return "ChatGPT não conseguiu responder"
        self.conversation.append(question+'\n')
        self.conversation.append(response+'\n')
        return response

    def Reset(self):
        self.conversation = []