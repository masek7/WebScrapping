# Webscrapping com python


Esse projeto visa capturar o preço de um produto na KABUM ou no Mercado Livre, e o monitora, anotando-o em DataFrame, com datas, valores, id (caso seja na kabum) e variação de preço. Todos os dias, no horário em que você preferir, através do agendador de tarefas do windows.

Ele emite uma notificação no windows, quando o produto sobe de preço, baixa, ou atinge a mínima histórica (seu menor valor registrado).

Para fazer o agendamento com o Agendador de Tarefas basta seguir os seguintes passos:

## Agendando o script no agendador de tarefas do windows

### 1 - Pressione Win + S e procure por "Agendador de Tarefas" ou "Task Scheduler".

Abra o aplicativo quando aparecer nos resultados.
Criar uma Nova Tarefa:

### 2 - No painel direito, clique em Criar Tarefa.

Na aba Geral, nomeie a tarefa e adicione uma descrição, se desejar. 
Marque a opção Executar com privilégios mais altos se o script precisar de permissões administrativas.

### 3 - Configurar o Gatilho (Trigger):

Vá para a aba Gatilhos e clique em Novo.. para definir a frequência de execução do script.

Escolha a condição que desejar, como Diariamente, Semanalmente ou Ao iniciar o computador, e ajuste as configurações conforme necessário.

### 4 - Adicionar a Ação (Action):

Na aba Ações, clique em Novo....
Em Ação, selecione Iniciar um Programa.

No campo Programa/script, clique em Procurar... e selecione o arquivo do script.

Se o script for em Python, escreva o caminho para o executável Python (ex.: C:\Python39\python.exe) e, em Adicionar argumentos, insira o caminho do script.

### 5 - Configurações Opcionais:

Nas abas Condições e Configurações, ajuste outras condições de execução, como espera e reinício em caso de falha, conforme necessário.

### 6 - Salvar e Testar a Tarefa:

Clique em OK para salvar a tarefa.
No painel do Agendador de Tarefas, selecione a tarefa criada e clique em Executar para testar se o script é executado corretamente.

Após configurar, o script será executado automaticamente conforme a frequência configurada.



