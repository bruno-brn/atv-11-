def divisao(valor):
    try:
        resultado = 1 / valor
        print(f'O resultado da divisão é: {resultado}')
    except ZeroDivisionError:
        print('Erro: divisão por zero')
    except TypeError:
        print('Erro: tipo inválido')
    except Exception as e:
        print(f'Erro genérico: {e}')
    finally:
        print('Programa encerrado')


entrada = 0
divisao(entrada)

entrada = 'teste'
divisao(entrada)

entrada = 2
divisao(entrada)
