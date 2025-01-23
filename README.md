# Projeto API de Países

Este é um pequeno projeto em Python para interagir com a API pública `restcountries.com` e obter informações sobre países, como população e moeda. O projeto foi criado como uma maneira simples para iniciantes aprenderem a trabalhar com APIs em Python, utilizando a biblioteca `requests`.

## Funcionalidades

- **Contagem de países**: Exibe o número total de países registrados na API.
- **Mostrar população**: Exibe a população de um país específico.
- **Mostrar moeda**: Exibe as moedas de um país específico.

## Requisitos

- Python 3.x
- Biblioteca `requests` (pode ser instalada via `pip`)

## Instalação

1. Clone o repositório:
   ```git clone https://github.com/seu-usuario/nome-do-repositorio.git```

2. Instale as dependências:
```pip install requests```

## Como Usar
Este projeto pode ser executado diretamente pelo terminal, passando parâmetros específicos para realizar as ações desejadas.

### Ações Disponíveis:
- contagem: Exibe o número total de países.
- moeda: Exibe a moeda de um país.
- população: Exibe a população de um país.

## Exemplos de uso:
Contar o número de países:
```python paises.py contagem```

Mostrar a população de um país (substitua <nome_do_pais> pelo nome real de um país):
```python paises.py população <nome_do_pais>```

Mostrar a moeda de um país:
```python paises.py moeda <nome_do_pais>```

Exemplo:
```$ python paises.py população Brasil```
```Brasil: 211000000 habitantes```

## Como Contribuir

Faça o fork deste repositório.
Crie uma branch para sua modificação:
```git checkout -b minha-modificacao```
Faça as alterações desejadas e envie um pull request.
