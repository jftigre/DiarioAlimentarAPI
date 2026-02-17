#  Daily Diet API

Uma API RESTful desenvolvida em **Python** com **Flask** para o gerenciamento de registros de dieta diária. Este projeto permite o controle total sobre as refeições, facilitando o monitoramento de hábitos alimentares de forma organizada e eficiente.


##  Tecnologias e Ferramentas

* **Linguagem:** Python 3.14
* **Framework:** Flask
* **Banco de Dados:** MySQL (executado via Docker)
* **ORM:** Flask-SQLAlchemy
* **Containerização:** Docker & Docker Compose

##  Como executar o projeto

### Pré-requisitos

* **Docker** e **Docker Compose** instalados.
* Um cliente API (como **Postman** ou **Insomnia**).

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/jftigre/DiarioAlimentar.git
   cd DiarioAlimentar
   ```

2. **Inicie o Banco de Dados:**
   ```bash
   docker-compose up -d
   ```
   *Este comando subirá o container MySQL configurado no Docker Compose para persistência dos dados.*

3. **Configure o Ambiente Virtual e Dependências:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

4. **Execute a aplicação:**
   ```bash
   python app.py
   ```
   *As tabelas do banco de dados serão criadas automaticamente na primeira execução através do `db.create_all()`.*

##  Endpoints da API

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `POST` | `/meals` | Registra uma nova refeição |
| `GET` | `/meals` | Lista todas as refeições cadastradas |
| `GET` | `/meals/<id>` | Visualiza os detalhes de uma refeição específica |
| `PUT` | `/meals/<id>` | Atualiza os dados de uma refeição existente |
| `DELETE` | `/meals/<id>` | Remove uma refeição do histórico |


### Exemplo de Payload (`POST /meals`):

```json
{
  "name": "Almoço",
  "description": "Arroz, feijão e peito de frango",
  "datetime": "2026-02-17 12:30:00",
  "is_diet": true
}
```

##  Funcionalidades Implementadas

* **CRUD Completo**: Gerenciamento total de registros de refeições (Criação, Leitura, Atualização e Exclusão).
* **Persistência em MySQL**: Dados armazenados de forma segura em banco de dados relacional via Docker.
* **Validação de Dados**: Tratamento de campos obrigatórios e tipos de dados no backend.
* **Tratamento de Datas**: Armazenamento e retorno de registros.