# Relatório Técnico - DadoConcreto API

## Visão Geral
Este projeto implementa uma API REST usando Django para fornecer acesso a dados de eventos e artigos relacionados ao GDELT (Global Database of Events, Language and Tone). A aplicação é containerizada usando Docker e segue boas práticas de desenvolvimento moderno.

## Arquitetura

### Estrutura do Projeto
O projeto está organizado como uma aplicação Django padrão com os seguintes componentes principais:

- `dadoconcreto_api/`: Diretório raiz do projeto Django
  - `dadoconcreto_api/`: Configurações principais do Django
  - `events/`: Aplicação principal que gerencia os modelos e endpoints

### Modelos de Dados
A aplicação possui quatro modelos principais, todos configurados com `managed = False` para refletir tabelas existentes:

1. **Article**
   - Armazena informações sobre artigos de notícias
   - Campos:
     - title: CharField(255) - Título do artigo
     - url: CharField(1255) - URL original do artigo
     - url_mobile: CharField(255) - URL móvel (opcional)
     - socialimage: CharField(1255) - Imagem social (opcional)
     - seendate: DateField - Data de visualização
     - domain: CharField(255) - Domínio do site
     - country: CharField(255) - País (opcional)
     - language: CharField(255) - Idioma
     - theme: CharField(2550) - Tema (opcional)
     - hash_key: CharField(2550) - Chave única

2. **Fulltext**
   - Relacionado aos artigos através de chave estrangeira
   - Campos:
     - article: ForeignKey(Article)
     - content: CharField(5000) - Conteúdo completo
     - extracted_at: DateField - Data de extração
     - hash_key: CharField(255) - Chave única

3. **Tone**
   - Armazena análises de tom/sentimento
   - Campos:
     - query: CharField(255) - Consulta
     - date: DateField - Data
     - value: FloatField - Valor do tom
     - hash_key: CharField(255) - Chave única

4. **Volumetimeline**
   - Rastreia volumes de eventos ao longo do tempo
   - Campos:
     - keyword: CharField(255) - Palavra-chave
     - date: DateField - Data
     - volume: FloatField - Volume
     - top_articles: JSONField - Artigos principais
     - hash_key: CharField(255) - Chave única

### Banco de Dados
- Utiliza PostgreSQL como banco de dados principal
- Configurado com dois bancos:
  - default: SQLite para dados do Django
  - gdelt: PostgreSQL para dados da aplicação
- Roteador de banco personalizado (MyAppRouter) que:
  - Direciona leituras/escritas do app 'events' para 'gdelt'
  - Gerencia permissões de relações
  - Controla migrações

### API REST
- Implementada usando Django Ninja
- Endpoints RESTful planejados para cada modelo
- Autenticação e autorização preparadas via middleware Django

## Tecnologias Utilizadas

### Backend
- Python 3.12
- Django 5.1.3
- Django Ninja 1.3.0
- psycopg2-binary para PostgreSQL

### Infraestrutura
- Docker com imagem base Python 3.12 (slim)
- Docker Compose para orquestração
- Gunicorn como servidor WSGI
- UV para gerenciamento de dependências

## Desenvolvimento e Deployment

### Ambiente de Desenvolvimento
- Python 3.12 fixado via .python-version
- Dependências gerenciadas via pyproject.toml e uv.lock
- Ambiente isolado via Docker
- Suporte a hot-reload em desenvolvimento

### Deployment
- Dockerfile otimizado com:
  - Camadas cacheadas para dependências
  - Usuário não-root (appuser)
  - Compilação de bytecode habilitada
- Exposição na porta 9090
- Configuração Gunicorn para produção
- Rede bridge isolada via Docker Compose

### Segurança
- Configurações sensíveis separadas
- Usuário dedicado no container
- Princípio do menor privilégio
- Preparado para configurações de produção

## Monitoramento e Manutenção
- Logs estruturados
- Reinício automático de containers
- Healthchecks preparados
- Backup automatizado do banco de dados

## Conclusão
O projeto demonstra uma implementação robusta de uma API REST usando Django, com foco em:
- Boas práticas de desenvolvimento
- Containerização eficiente
- Escalabilidade
- Segurança
- Manutenibilidade

A arquitetura escolhida permite fácil manutenção e extensão do sistema, com clara separação de responsabilidades e componentes bem definidos.
