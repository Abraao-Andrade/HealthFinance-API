# Projeto de API Privada para Setor Financeiro na Área da Saúde

## Pré-requisitos

- **Docker**: versão 24.0.7 ou superior

## Instalação e Execução

1. **Clonar o repositório:**

   ```bash
   git clone git@github.com:Abraao-Andrade/HealthFinance-API.git

2. **Acessar o repositório:**

    ```bash
    cd HealthFinance-API

3. **Construir e iniciar o contêiner via Docker Compose:**

    ```bash
    docker-compose up -d

4. **Acessar a aplicação:**

    Acesse a aplicação em `http://localhost:3000`.

## Endpoints

*   `/users`: Cadastra um usuário no banco. Necessario passar os seguintes dados no body:{"username", "email"}.
*   `/users/find?username=`: Lista informações dos usuários com base no username informado. Retorna ID, email.
*   `/patients`: Lista informações dos pacientes. Retorna ID, nome, sobrenome e data de nascimento, caso queira buscar um paciente    especifico basta enviar o ?first_name= na url.
*   `/pharmacies`: Lista informações das farmácias. Retorna ID, nome e cidade.
*   `/transactions`: Lista informações das transações. Retorna ID do paciente, nome do paciente, sobrenome do paciente, data de nascimento do paciente, ID da farmácia, nome da farmácia, cidade da farmácia, ID da transação, quantidade da transação e data da transação.