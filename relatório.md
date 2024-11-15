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
A aplicação possui quatro modelos principais:

1. **Article**
   - Armazena informações sobre artigos de notícias
   - Campos incluem título e outros metadados relacionados

2. **Fulltext**
   - Relacionado aos artigos através de chave estrangeira
   - Armazena o conteúdo completo dos artigos

3. **Tone**
   - Armazena análises de tom/sentimento
   - Inclui campos para consultas e métricas relacionadas

4. **Volumetimeline**
   - Rastreia volumes de eventos ao longo do tempo
   - Inclui palavras-chave e métricas temporais

### Banco de Dados
- Utiliza um roteador de banco de dados personalizado (`MyAppRouter`)
- Configurado para usar um banco de dados específico 'gdelt' para a aplicação 'events'
- Separação clara entre operações de leitura e escrita

### API REST
- Implementada usando schemas baseados em modelos
- Serialização automática de modelos usando ModelSchema
- Endpoints RESTful para cada modelo principal

## Tecnologias Utilizadas

### Backend
- Django: Framework web principal
- Django REST framework: Para implementação da API REST
- Marshmallow: Para serialização de dados

### Infraestrutura
- Docker: Containerização da aplicação
- Docker Compose: Orquestração de serviços
- uv: Gerenciamento de dependências Python moderno

## Desenvolvimento e Deployment

### Ambiente de Desenvolvimento
- Gerenciamento de versão Python usando `.python-version`
- Dependências gerenciadas via `pyproject.toml` e `uv.lock`
- Ambiente isolado via Docker

### Deployment
- Containerização completa via Dockerfile
- Orquestração multi-container via docker-compose.yml
- Configuração ASGI para deploy moderno

## Testes e Qualidade de Código
- Estrutura de testes integrada
- Modelos de dados bem definidos com validações
- Schemas para garantir integridade dos dados

## Conclusão
O projeto demonstra uma implementação robusta de uma API REST usando Django, com foco em boas práticas de desenvolvimento, containerização e escalabilidade. A arquitetura escolhida permite fácil manutenção e extensão do sistema.
