# Container Docker para execução de Projetos Spark

Neste projeto iremos criar um container Docker com Spark para que possamos executar os projetos de PySpark em nossa maquina ou em um container em nuvem

Estrutura do Projeto
```
- /conf => Arquivos de configuração do Spark
- /dados => Pasta para colocarmos nossos datasets, mapearemos esta pasta como um volume do nosso cluster
- /jobs => Arquivos PySpark para execução no cluster
- /requerimentes => arquivo para instalação dos módulos necessários para nosso projeto
- /.env.spark => Arquivo configuração de ambiente, possui uma única configuração: SPARK_NO_DAEMONIZE = true, Isso nos permite controlar se os processos Spark serão executados como daemons ou não. Estamos desativando isso, caso contrário, os contêineres serão simplesmente encerrados após a execução do script.
- /docker-compose.yaml => Arquivo de configuração do nosso cluster
- /Dockekrfile => Arquivo de configuração da imagem docker
- /entrypoint.sh => Serve como ponto de partida para o processo de tempo de execução de um contêiner Docker. Quando você cria uma imagem Docker e a instancia como um contêiner, o ENTRYPOINT é executado por padrão.
Permite definir a finalidade principal do contêiner, como executar um servidor web, banco de dados ou aplicativo . Também permite passar argumentos em tempo de execução para personalizar o comportamento do contêiner.
```

**Execução ambiente**

*Estou considerando que Ja tenha o Docker intalado no seu Ambiente, caso contrário antes de prosseguri instale o Docker*

Criando a Imagem

*Abra o terminal e digite os comando abaixo*
```
docker build -t tav-spark-master .
```

Explicando o comando:

- Docker => Comano para chamar o docker
- \-t => Opção para definir o nome(tag) da imagem
- tav-spark-master => Nome da imagem se for torcada precisa ser alterada no dockercompose.yml
- . => Define que a iagem vai ser criada no diretorio atual

```
docker-compose -f docker-compose.yml up -d
```

Explicando o Comando:
- docker-compose => O comando docker-compose codifica todos os dados de configuração em tempo de execução em um arquivo YAML apropriadamente denominado docker-compose.yaml 
- -f => Opção usada para informar o arquivo de Configuração do Container
- docker-compose.yml => Arquivo de Configuração do container
- up => Cria e Inicia o Container
- -d => Modo desanexado: execute contêineres em segundo plano

# Componentes de Cluster Criado

## Master (ou Spark Master):
- **Função:** O Master é o ponto central do cluster Spark que coordena a distribuição de 
aplicações (jobs) no cluster.
- **Responsabilidades:** Ele aloca recursos (como memória e CPU) para cada aplicação com 
base na configuração fornecida e nas demandas do cluster. Também rastreia a 
disponibilidade dos Workers e os recursos que eles têm.
- **UI (User Interface):** O Master também fornece uma interface web para visualização 
do status e gerenciamento do cluster.
- **Endereço padrão:** Por padrão, a UI do Spark Master pode ser acessada no endereço 
http://localhost:8080.

## Worker (ou Spark Worker):
- **Função:** Os Workers são os nós do cluster onde o trabalho é realizado.
- **Responsabilidades:** Cada Worker é responsável por executar as tarefas atribuídas a 
ele pelo Master. Os Workers também informam regularmente o Master sobre os 
recursos disponíveis e o status das tarefas.
- **Executor:** Dentro de cada Worker, os executores são inicializados para cada aplicação. 
Esses executores são processos JVM (Java Virtual Machine) separados que executam 
tarefas para uma aplicação Spark específica.
- **Armazenamento:** Os Workers também podem armazenar dados em cache ou 
intermediários em sua memória ou disco local, conforme instruído pela aplicação.

## History Server:
- **Função:** O Spark History Server fornece uma interface web para visualizar os logs e 
métricas de aplicações Spark concluídas.
- **Responsabilidades:** Depois que uma aplicação Spark é concluída, suas métricas e logs 
podem ser armazenados e analisados posteriormente através do History Server. Isso 
é útil para análises pós-execução, otimização e depuração.
- **Armazenamento:** Os logs das aplicações (também conhecidos como logs de eventos) 
são normalmente armazenados em um sistema de arquivos distribuído como o HDFS 
ou em um sistema de arquivos local, de onde o History Server pode lê-los.
- **Endereço por padrão:** A UI do History Server geralmente pode ser acessada no 
endereço http://localhost:18080



**Fontes:**

- [Data Science Academy](https://www.datascienceacademy.com.br/)
- [Docker](https://docs.docker.com/desktop/)
