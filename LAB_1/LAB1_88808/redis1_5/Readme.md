
# Bases de Dados Chave-Valor


## 1.5 Sistema de mensagens

Neste exercíco começei por tentar utilizar a arquitetura Publish/Susbcribe fornecida pelo Redis.
Cheguei a conclusão que não era adequada para as funcionalidades pedidas pelo enunciado e por isso decidi criar a arquitetura de raiz.

Usei 2 tipos de dados diferentes em relação ao Redis:

 1. A estrutura de dados Hash é usada para armazenar toda a informação associada a cada utilizador, a key esta formatada da seguinte forma "RedisMS:nome_de_login" e além disso tenho um campo name onde está guardado o nome do utilizador e um campo following onde guardo os nomes dos utilizadores que estou a seguir separados por ";" exemplo:


    RedisMS:jmnmv12 following "vasco99;antonio12" name "Joao"

 2. A estrutura de dados List é usada para armazenar as mensagens enviada por cada utilizador para o sistema,a key está formatada da seguinte forma "RedisMSmessageList:nome_de_login".Sempre que o utilizador envia uma nova mensagem para o sistema realizo um lpush e assim as mensagens mais recentes estão sempre na cabeça da lista.

Com estas duas estruturas permito que o utilizador envie mensagens,veja as mensagens das pessoas que segue e siga novas pessoas.
