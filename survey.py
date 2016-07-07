class AnonymousSurvey():
    """ Coleta resposta anôninas para uma pergunta de uma pesquisa."""

    def __init__(self, question):
        """ Armazena um pergunta e se prepara para armazenar as resposta."""
        self.question = question
        self.responses = []

    def show_question(self):
        """ Mostra a pergunta da pesquisa. """
        print(self.question)

    def store_response(self, new_response):
        """ Mostra um única resposta da pesquisa."""
        self.responses.append(new_response)

    def show_results(self):
        """ Mostra todas as resposta dadas."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)
