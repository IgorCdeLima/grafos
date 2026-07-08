# Executando o Projeto com Docker

## Pré-requisitos

Antes de iniciar, certifique-se de que o **Docker** esteja instalado em sua máquina.

* **Windows:** abra o **Docker Desktop** e aguarde até que o status seja **Running**.
* **Linux:** verifique se o serviço do Docker está em execução.

## Como executar

Abra um terminal na pasta raiz do projeto (onde está localizado o arquivo `docker-compose.yml`) e siga os passos abaixo.

### 1. Construir a imagem Docker

Este comando instala todas as dependências do projeto definidas no `requirements.txt` e cria a imagem Docker.

```bash
docker compose build
```

### 2. Acessar o container

Após a construção da imagem, inicie um terminal dentro do container.

```bash
docker compose run --rm graph-app bash
```

### 3. Executar o algoritmo

Dentro do terminal do container, execute:

```bash
python app/main.py
```

O programa será iniciado e exibirá o menu com os algoritmos implementados.

## Estrutura dos arquivos utilizados

* `docker-compose.yml` — Configuração dos serviços Docker.
* `docker/Dockerfile` — Define a imagem utilizada pelo projeto.
* `requirements.txt` — Lista das dependências Python instaladas durante a construção da imagem.

## Observações

* Sempre que houver alterações no arquivo `requirements.txt` ou no `Dockerfile`, execute novamente:

```bash
docker compose build
```

* Caso apenas o código-fonte tenha sido alterado, não é necessário reconstruir a imagem. Basta iniciar um novo container e executar o programa novamente.

```bash
docker compose run --rm graph-app bash
```

## Encerrando

Ao finalizar a execução, basta sair do terminal do container com:

```bash
exit
```

Como o container foi iniciado com a opção `--rm`, ele será removido automaticamente após o encerramento.
