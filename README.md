# Projeto de Entrevista de Anime

Este projeto é um script Python que realiza uma entrevista sobre preferências de anime. O script faz várias perguntas ao usuário, coleta as respostas e as grava em um arquivo CSV.

## Como usar

1. Execute o script Python no seu terminal ou IDE preferido.
2. O script fará várias perguntas sobre suas preferências de anime, como seu gênero de anime favorito, sua produtora de anime favorita, etc.
3. Insira suas respostas para cada pergunta conforme solicitado.
4. As respostas serão salvas em um arquivo CSV chamado "saída.csv".
5. Para encerrar o programa, insira '00' quando solicitado a inserir a idade do entrevistado.

## Detalhes do Código

O código consiste em uma classe chamada `Entrevista` e uma função global `clear`.

A classe `Entrevista` tem os seguintes métodos:

- `__init__`: Inicializa a instância da classe com uma idade e uma lista vazia.
- `create_csv`: Cria um arquivo CSV com um cabeçalho específico se o arquivo não existir ou estiver vazio.
- `add_to_list`: Adiciona vários argumentos à lista da instância.
- `add_to_csv`: Adiciona a lista da instância ao arquivo CSV.
- `interview`: Realiza a entrevista, coletando várias informações do usuário e adicionando-as à lista e ao arquivo CSV.

A função `clear` limpa o console.

## Requisitos

Este script requer Python 3 e as seguintes bibliotecas Python: `csv`, `datetime`, `os`, e `time`.

Espero que isso ajude! Se você tiver mais perguntas, fique à vontade para perguntar. 😊
