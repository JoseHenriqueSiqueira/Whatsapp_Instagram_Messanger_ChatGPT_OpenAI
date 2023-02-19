import openai


class ChatBot:
    def __init__(self, api_key: str, engine: str = "text-davinci-002", max_tokens: int = 1024, temperature: float = 0.5):
        self.conversation = []
        openai.api_key = api_key
        self.engine = engine
        self.max_tokens = max_tokens
        self.temperature = temperature

    def question(self, question: str, engine: str = None, max_tokens: int = None, temperature: float = None, tone: str = None, domain: str = None) -> str:
        # Verifica se a pergunta atual é igual à pergunta anterior, caso sim, retorna
        if len(self.conversation) > 0 and question + '\n' == self.conversation[-2]:
            return self.conversation[-1]

        # Concatena as conversas anteriores em uma única string
        conversation_history = " ".join(map(str, self.conversation))

        # Verifica se os parâmetros foram definidos pelo usuário, caso contrário, utiliza os parâmetros padrões
        engine = engine or self.engine
        max_tokens = max_tokens or self.max_tokens
        temperature = temperature or self.temperature

        # Define a configuração do modelo de linguagem
        model_config = {
            "engine": engine,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "prompt": question + " " + conversation_history
        }

        # Adiciona configurações adicionais com base nas entradas do usuário
        if tone:
            model_config["tone"] = tone
        if domain:
            model_config["metadata"] = {
                "domain": domain
            }

        try:
            # Faz a requisição à API da OpenAI para gerar uma resposta
            response = openai.Completion.create(
                **model_config).choices[0].text.strip()
        except Exception as e:
            # Caso haja algum erro na geração da resposta, reseta a conversa e retorna uma mensagem de erro
            self.reset()
            return "ChatGPT não conseguiu responder"

        # Verifica se a resposta é ofensiva ou inadequada
        if self.is_offensive(response):
            # Gera uma nova resposta apropriada
            response = self.generate_appropriate_response(tone)

        # Adiciona a pergunta atual e a resposta à conversa
        self.conversation.append(question + '\n')
        self.conversation.append(response + '\n')
        return response

    def reset(self):
        # Limpa a conversa
        self.conversation.clear()

    def is_offensive(self, response: str) -> bool:
        # Faz a requisição à API da OpenAI para verificar se a resposta é ofensiva ou inadequada
        response = openai.Completion.create(
            engine="content-filter-alpha-1",
            prompt=response,
            temperature=0.0,
            max_tokens=1,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        ).choices[0].text.strip()

        return response == "2"

    def generate_appropriate_response(self, tone: str) -> str:
        # Define um dicionário de respostas apropriadas para cada tom
        appropriate_responses = {
            "formal": "Desculpe-me, não entendi sua pergunta. Você poderia reformulá-la, por favor?",
            "friendly": "Desculpe, não consegui compreender o que você quis dizer. Poderia tentar explicar de outra forma?",
            "assertive": "Não entendi. Tente ser mais claro na sua pergunta, por favor."
        }

        # Retorna a resposta apropriada com base no tom selecionado
        return appropriate_responses.get(tone, "Desculpe-me, não entendi sua pergunta. Você poderia reformulá-la, por favor?")
