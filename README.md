## 🌐 [English Version of README](README_EN.md)

# Human Resource Management System

O **Human Resource Management System** é um projeto desenvolvido para gerenciar e automatizar processos de recursos humanos, como a gestão de funcionários, folhas de pagamento, benefícios e avaliações de desempenho. O sistema tem como objetivo fornecer uma solução eficiente e prática para empresas que buscam otimizar suas operações de RH.

## 🔨 Funcionalidades do Projeto

- **Gerenciamento de Funcionários**: Cadastro, edição e exclusão de funcionários.
- **Folhas de Pagamento**: Controle de salários e geração de folhas de pagamento.
- **Benefícios**: Administração de benefícios oferecidos aos funcionários.
- **Avaliações de Desempenho**: Registro e acompanhamento de avaliações de desempenho dos funcionários.

### Exemplo Visual do Projeto

![image](https://github.com/user-attachments/assets/dbf3ef75-aa1c-4734-8e15-5f4d024077be)
![image](https://github.com/user-attachments/assets/3d9f0dd0-a493-4a17-9272-d922dd3e8e47)
![image](https://github.com/user-attachments/assets/6bae1612-f60b-4cb8-b667-9c442de56e51)

## ✔️ Técnicas e Tecnologias Utilizadas

- **Django**: Framework para o desenvolvimento rápido e seguro de aplicações web.
- **SQLite**: Banco de dados relacional leve utilizado para armazenar dados.
- **DRF (Django Rest Framework)**: Framework para construir APIs RESTful.
- **drf_yasg**: Biblioteca para geração de documentação Swagger/OpenAPI para APIs Django.

## 📁 Estrutura do Projeto

- **db.sqlite3**: Banco de dados SQLite.
- **employees/**: Aplicativo responsável pelo gerenciamento de funcionários.
    - `admin.py`: Configurações do painel administrativo.
    - `apps.py`: Configurações da aplicação.
    - **migrations/**: Arquivos de migração do banco de dados.
        - `0001_initial.py`: Arquivo de migração inicial.
    - `models.py`: Definição dos modelos de dados.
    - `serializers.py`: Serializadores para a API.
    - **templates/**: Templates HTML.
        - `employee_list.html`: Template para exibir a lista de funcionários.
    - `tests.py`: Testes automatizados.
    - `urls.py`: URLs da aplicação.
    - `views.py`: Lógica de visualização.
    - `__init__.py`: Inicialização do módulo.
- **Human-Resource-Management-System/**: Diretório principal do projeto.
    - `asgi.py`: Configurações ASGI para o projeto.
    - `settings.py`: Configurações do Django.
    - `urls.py`: URLs do projeto.
    - `wsgi.py`: Configurações WSGI para o projeto.
    - `__init__.py`: Inicialização do módulo.
- **LICENSE**: Arquivo de licença.
- **manage.py**: Utilitário de linha de comando do Django.
- **README.md**: Documento de instruções do projeto.
- **README_EN.md**: Documento de instruções em inglês.
- **requirements.txt**: Lista de dependências do projeto.

## 🛠️ Abrir e rodar o projeto

Para iniciar o projeto localmente, siga os passos abaixo:

1. **Certifique-se de que o Python está instalado**:
    - O [Python](https://www.python.org/) é necessário para rodar o projeto. Você pode verificar se já o tem instalado com:

      ```bash
      python --version
      ```

    - Se não estiver instalado, baixe e instale a versão recomendada.

2. **Clone o Repositório**:
    - Copie a URL do repositório e execute o comando abaixo no terminal:

      ```bash
      git clone <URL_DO_REPOSITORIO>
      ```

3. **Instale as Dependências**:
    - Navegue até o diretório do projeto e instale as dependências utilizando o pip:

      ```bash
      cd Human-Resource-Management-System
      pip install -r requirements.txt
      ```

4. **Configure o Banco de Dados**:
    - Execute as migrações para configurar o banco de dados:

      ```bash
      python manage.py migrate
      ```

5. **Inicie o Servidor de Desenvolvimento**:
    - Execute o servidor de desenvolvimento do Django:

      ```bash
      python manage.py runserver
      ```

    - Acesse a aplicação em `http://127.0.0.1:8000/` no seu navegador.

## 🌐 Deploy

Para informações sobre o deploy da aplicação em ambientes de produção, consulte a documentação específica do Django para [Deploying Django](https://docs.djangoproject.com/en/stable/howto/deployment/).

https://human-resource-management-system-l96i.onrender.com

## 📜 Documentação da API

A documentação da API está disponível no Swagger Hub: [Human Resource Management System API Documentation](https://app.swaggerhub.com/apis-docs/FelipeM./Human-Resource-Management-System/1.0.0)
