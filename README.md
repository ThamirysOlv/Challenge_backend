# \<pt-BR> Desafio back-end alura / Challenge backend alura

Objetivo: criar uma api para controle de orçamento.

Goal: to create an api for budget control.


To run:

Create container: docker-compose up --build and access http://localhost:5000/


## Routes:

- /
- /profile
- /login
- /signup
- /logout
- /despesas
- /receitas
- /resumo


Para acessar ou cadastrar despesas: /despesas

Para acessar ou cadastrar receitas: /receitas

Para acessar, alterar, ou deletar uma despesa: /despesas/{id}

Para acessar, alterar, ou deletar uma receita: /receitas/{id}

Para buscar uma despesa pela descrição: /despesas?descricao={descricao}

Para buscar uma receita pela descrição: /receitas?descricao={descricao}

Para buscar despesas de um determinado mês: /receitas/{ano}/{mes}

Para buscar receitas de um determinado mês: /receitas/{ano}/{mes}

Para buscar o resumo de um determinado mês: /resumo/{ano}/{mes}

Para logout: /logout
