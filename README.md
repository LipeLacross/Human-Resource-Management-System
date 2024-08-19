# Sistema de Gerenciamento de Recursos Humanos

O Sistema de Gerenciamento de Recursos Humanos (HR Management System) é uma aplicação web desenvolvida para gerenciar informações sobre funcionários, folhas de pagamento, benefícios e avaliações de desempenho. O sistema permite a administração eficiente de dados de recursos humanos, ajudando na organização e análise das informações dos colaboradores.

## 🔨 Funcionalidades do Projeto

- **Cadastro de Funcionários**: Adicione e gerencie informações sobre os funcionários da empresa, incluindo nome, e-mail, telefone, data de contratação, cargo e salário.
- **Folha de Pagamento**: Registre e visualize informações sobre os pagamentos dos funcionários, incluindo data do pagamento, salários brutos e líquidos, e deduções.
- **Benefícios**: Administre os benefícios oferecidos aos funcionários, como planos de saúde e bônus.
- **Avaliações de Desempenho**: Realize e registre avaliações de desempenho dos funcionários com notas e comentários.

### Exemplo Visual do Projeto
***

## ✔️ Técnicas e Tecnologias Utilizadas

- **Python**: Linguagem de programação usada para desenvolver a aplicação.
- **Django**: Framework web para desenvolvimento rápido e limpo da aplicação.
- **Microsoft SQL Server**: Sistema de gerenciamento de banco de dados usado para armazenar os dados da aplicação.
- **django-mssql-backend**: Pacote para integrar Django com o Microsoft SQL Server.
- **pyodbc**: Biblioteca para conectar o Django ao SQL Server.

## 📁 Estrutura do Projeto


- **`.gitignore`**: Arquivo para listar arquivos e diretórios a serem ignorados pelo Git, como arquivos de configuração local e diretórios de cache.
- **`LICENSE`**: Arquivo que contém a licença sob a qual o projeto é distribuído.
- **`manage.py`**: Script de gerenciamento do Django que permite executar comandos administrativos.
- **`README.md`**: Arquivo de documentação do projeto que fornece uma visão geral e instruções de uso.
- **`requirements.txt`**: Arquivo que lista as dependências do projeto para instalação com `pip`.
- **`Human-Resource-Management-System/`**: Diretório principal do projeto Django, contendo arquivos de configuração e inicialização do projeto:
   - **`__init__.py`**: Inicializador do pacote para tornar o diretório um módulo Python.
   - **`asgi.py`**: Interface ASGI para servidores assíncronos.
   - **`settings.py`**: Configurações do projeto, como banco de dados e aplicativos instalados.
   - **`urls.py`**: Arquivo de roteamento de URLs do projeto.
   - **`wsgi.py`**: Interface WSGI para servidores de aplicação.
- **`employees/`**: Aplicação Django para gerenciamento de funcionários:
   - **`__init__.py`**: Inicializador do pacote para tornar o diretório um módulo Python.
   - **`admin.py`**: Configurações para a administração do Django.
   - **`apps.py`**: Configurações específicas da aplicação.
   - **`models.py`**: Definição dos modelos de dados para a aplicação.
   - **`tests.py`**: Testes automatizados para a aplicação.
   - **`views.py`**: Lógica de visualização e manipulação das requisições.
   - **`migrations/`**: Diretório para arquivos de migração que refletem mudanças nos modelos de dados.
   - **`templates/`**: Diretório para templates HTML específicos da aplicação, contendo:
      - **`employee_list.html`**: Template para listar funcionários.


## 🛠️ Abrir e Rodar o Projeto

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/seu-usuario/Human-Resource-Management-System.git
    cd Human-Resource-Management-System
    ```

2. **Instale as dependências**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure o banco de dados**:
    - Edite `settings.py` para incluir suas credenciais do SQL Server.

4. **Execute as migrações**:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Inicie o servidor de desenvolvimento**:

    ```bash
    python manage.py runserver
    ```

6. **Acesse o aplicativo**:
    - Navegue para `http://127.0.0.1:8000/admin` para acessar o painel administrativo.

## 🌐 Deploy

Para realizar o deploy do projeto em um ambiente de produção:

1. **Configure o ambiente de produção** com o servidor web de sua escolha, como Nginx ou Apache, e um servidor WSGI como Gunicorn.
2. **Configure a base de dados de produção** e certifique-se de que as credenciais estejam corretas.
3. **Configurações adicionais** podem incluir a configuração de segurança, backups e certificados SSL.

Para mais detalhes sobre o deploy, consulte a [documentação oficial do Django](https://docs.djangoproject.com/en/stable/howto/deployment/).
