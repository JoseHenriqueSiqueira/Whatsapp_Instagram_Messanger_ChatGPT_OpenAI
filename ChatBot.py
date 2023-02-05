import openai

class ChatBot:
    def __init__(self, API_KEY:str):
        self.conversation = []
        openai.api_key = API_KEY
        self.stop = ""

    def Question(self, question:str):
        try:
            if question == "" or question in self.conversation[-1]:
                return
        except:
            pass
        conversation_history = " ".join(self.conversation)
        response = ""
        while response == "":
            try:
                response = openai.Completion.create(
                engine="text-davinci-002",
                prompt= question+" "+conversation_history,
                max_tokens=1024,
                n=1,
                stop=None,
                temperature=0.5,
                ).get("choices")[0].get("text").strip()
            except Exception as e:
                self.Reset()
                return "ChatGPT não conseguiu responder"
        self.conversation.append(question + "\n" + response+ "\n")
        return response

    def Reset(self):
        self.conversation = []
