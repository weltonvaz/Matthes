import os
os.system('clear')

from survey import AnonymousSurvey

# Define uma pergunta e cria um pesquisa
question = "What language did you first learn to speak"
my_survey = AnonymousSurvey(question)

# Mostra a pergunta e Armazena as respostas a pergunta
my_survey.show_question()

print("Enter 'q' at any time to quit.\n")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Exibe os resultados da pesquisa
print("\nThanks you to everyone who participated in the survey!")
my_survey.show_results()
