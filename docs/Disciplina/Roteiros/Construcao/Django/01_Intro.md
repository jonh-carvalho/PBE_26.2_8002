# Introdução ao Django

Roteiro para Desenvolvimento de Aplicação Web Django com SQLite no VS Code

## Pré-requisitos

- Visual Studio Code instalado
- Python instalado (versão 3.8 ou superior)
- Extensão Python para VS Code (recomendado)

## 1: Configurar Ambiente Virtual

1. Abra o terminal no VS Code (`Ctrl+` ou Terminal > Novo Terminal)
2. Navegue até a pasta onde deseja criar o projeto
3. Crie o ambiente virtual:

   ```
   ctrl +shift + P
   Python Create Enviroment
   ```

ou 

   ```bash
   python -m venv venv
   ```

4. Ative o ambiente virtual:
   - Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - Linux/MacOS:

     ```bash
     source venv/bin/activate
     ```

5. Verifique que o ambiente está ativo (deve aparecer `(venv)` no início da linha do terminal)

## 2: Instalar Django e Dependências

1. Com o ambiente virtual ativo, instale o Django:

   ```bash
   pip install django
   ```

## 3: Criar Projeto Django

1. Crie o projeto Django:

   ```bash
   django-admin startproject project .
   ```

   (O ponto no final cria o projeto no diretório atual)

2. Verifique a estrutura criada:

   ```
   project/
     __init__.py
     settings.py
     urls.py
     wsgi.py
   manage.py
   ```

## 4: Configurar o Banco de Dados SQLite

1. O Django já vem configurado para usar SQLite por padrão (verifique em `project/settings.py`):

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': BASE_DIR / 'db.sqlite3',
       }
   }
   ```

2. Execute as migrações iniciais:

   ```bash
   python manage.py migrate
   ```

## 5: Criar uma Aplicação Django

1. Crie uma nova aplicação:

   ```bash
   python manage.py startapp app
   ```

2. Adicione a aplicação ao `INSTALLED_APPS` em `project/settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       'app',
   ]
   ```

## 6: Criar Modelos e Migrações

1. Defina um modelo em `app/models.py`:

   ```python
   from django.db import models

   class Produto(models.Model):
       nome = models.CharField(max_length=100)
       preco = models.DecimalField(max_digits=6, decimal_places=2)
       descricao = models.TextField()
       disponivel = models.BooleanField(default=True)

       def __str__(self):
           return self.nome
   ```

2. Crie e aplique as migrações:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

## 7: Configurar o Painel de Administração

1. Crie um superusuário:

   ```bash
   python manage.py createsuperuser
   ```

2. Registre o modelo no admin (`app/admin.py`):

   ```python
   from django.contrib import admin
   from .models import Produto

   admin.site.register(Produto)
   ```


## 8: Executar o Servidor de Desenvolvimento

1. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

2. Acesse no navegador:

   - http://localhost:8000/ (página inicial)
   - http://localhost:8000/admin/ (painel admin)

---

# Introdução ao Django REST

Uma extensão do aplicativo Django inicial para incluir uma API RESTful usando Django REST Framework, mantendo a funcionalidade existente e adicionando endpoints API.

## 1. Instalação e Configuração Inicial

Primeiro, vamos instalar e configurar o DRF:

```bash
pip install djangorestframework
```

Adicione ao `INSTALLED_APPS` em `project/settings.py`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'app',
]
```

## 2. Criação dos Serializers

Crie um arquivo `serializers.py` na aplicação `app`:

```python
# app/serializers.py
from rest_framework import serializers
from app.models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'descricao', 'disponivel']
        read_only_fields = ['id']
```

## 3. Criação das Viewsets e API Views

Atualize ou crie um arquivo `api.py` na aplicação:

```python
# app/api.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from app.models import Produto
from app.serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
```

## 4. Configuração das URLs da API

Crie um arquivo `api_urls.py` na aplicação:

```python
# app/api_urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api import ProdutoViewSet

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet, basename='produto')

urlpatterns = [
    path('', include(router.urls)),
]
```

Atualize o `urls.py` principal do projeto:

```python
# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # URLs tradicionais
    path('api/', include('app.api_urls')),  # URLs da API
]
```

## 5. Testando a API

Agora você pode testar os endpoints da API:

1. **Listar todos os produtos**: `GET /api/produtos/`
2. **Criar novo produto**: `POST /api/produtos/`
3. **Detalhes de um produto**: `GET /api/produtos/1/`
4. **Atualizar produto**: `PUT /api/produtos/1/`
5. **Produtos disponíveis**: `GET /api/produtos/disponiveis/`
6. **Produtos baratos**: `GET /api/produtos/baratos/`
7. **Documentação Swagger**: `GET /swagger/`
8. **Documentação ReDoc**: `GET /redoc/`

Esta extensão transforma seu aplicativo Django em uma API RESTful poderosa enquanto mantém a funcionalidade web tradicional. Você agora pode:

- Consumir a API com frontends modernos (React, Vue, Angular)
- Oferecer serviços para aplicativos móveis
- Integrar com outros sistemas via API
- Manter uma arquitetura escalável e bem organizada
