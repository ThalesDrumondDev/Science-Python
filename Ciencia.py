import random

# Banco de dados de perguntas e respostas
perguntas_e_respostas = [
    {
        'pergunta': 'Qual é a maior lua de Marte?',
        'opcoes': ['Fobos', 'Deimos', 'Ganimedes', 'Europa'],
        'resposta': 'Fobos'
    },
    {
        'pergunta': 'Qual é o símbolo químico para o ouro?',
        'opcoes': ['Au', 'Ag', 'Fe', 'Hg'],
        'resposta': 'Au'
    },
    {
        'pergunta': 'Qual é a unidade básica da vida?',
        'opcoes': ['Átomo', 'Célula', 'Proteína', 'Vírus'],
        'resposta': 'Célula'
    },
    {
        'pergunta': 'Qual é a maior lua de Marte?',
        'opcoes': ['Fobos', 'Deimos', 'Ganimedes', 'Europa'],
        'resposta': 'Fobos'
    },
    {
        'pergunta': 'Qual é o símbolo químico para o ouro?',
        'opcoes': ['Au', 'Ag', 'Fe', 'Hg'],
        'resposta': 'Au'
    },
    {
        'pergunta': 'Qual é a unidade básica da vida?',
        'opcoes': ['Átomo', 'Célula', 'Proteína', 'Vírus'],
        'resposta': 'Célula'
    },
    {
        'pergunta': 'Qual é a fórmula química da água?',
        'opcoes': ['H2O', 'CO2', 'NaCl', 'HCl'],
        'resposta': 'H2O'
    },
    {
        'pergunta': 'Qual é a unidade de medida de corrente elétrica?',
        'opcoes': ['Watt', 'Ampere', 'Volt', 'Ohm'],
        'resposta': 'Ampere'
    },
    {
        'pergunta': 'O que é a mitose?',
        'opcoes': ['Divisão celular que produz gametas', 'Divisão celular que forma células filhas idênticas',
                   'Processo de formação de esporos', 'Tipo de respiração celular'],
        'resposta': 'Divisão celular que forma células filhas idênticas'
    },
{
    'pergunta': 'O que é necessário para que uma planta realize a fotossíntese?',
    'opcoes': ['Água, luz solar e dióxido de carbono', 'Solo fértil e adubo', 'Ar puro e luz solar', 'Água e solo'],
    'resposta': 'Água, luz solar e dióxido de carbono'
}
]


def apresentar_pergunta(pergunta):
    print(pergunta['pergunta'])
    for i, opcao in enumerate(pergunta['opcoes'], 1):
        print(f"{i}. {opcao}")
    resposta_usuario = int(input("Escolha a opção correta (1/2/3/4): "))
    return resposta_usuario


def verificar_resposta(pergunta, resposta_usuario):
    resposta_correta = pergunta['opcoes'].index(pergunta['resposta']) + 1
    if resposta_usuario == resposta_correta:
        print("Resposta correta!\n")
        return True
    else:
        print(f"Resposta incorreta. A resposta correta era a opção {resposta_correta}: {pergunta['resposta']}\n")
        return False


def jogo_ciencia_quiz():
    random.shuffle(perguntas_e_respostas)
    pontuacao = 0

    print("Bem-vindo ao Ciência Quiz!")
    print("Teste seu conhecimento em várias áreas da ciência.\n")

    for pergunta in perguntas_e_respostas:
        resposta_usuario = apresentar_pergunta(pergunta)
        if verificar_resposta(pergunta, resposta_usuario):
            pontuacao += 1

    print(f"Jogo encerrado! Sua pontuação final: {pontuacao}/{len(perguntas_e_respostas)}")

    if pontuacao == 5:
        print("Parabéns! Você acertou 5 perguntas, continue assim!")
    elif pontuacao == 10:
        print("Parabéns! Você acertou todas as perguntas, você foi incrível!")
    else:
        print("Bom jogo! Tente novamente para obter uma pontuação melhor!")


if __name__ == "__main__":
    jogo_ciencia_quiz()
