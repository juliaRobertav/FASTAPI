# ROTAS

## FASTAPI

### **ROTAS**

Rotas em um contexto de desenvolvimento web referem-se às URLs específicas que um aplicativo ou serviço web pode "escutar" e responder. Essas URLs são usadas para direcionar solicitações HTTP para funções ou manipuladores de código específicos que processam a solicitação e geram uma resposta apropriada.

Em frameworks web como o FastAPI, as rotas são definidas para mapear URLs específicas para funções Python que executam a lógica da aplicação. Por exemplo, uma aplicação web pode ter uma rota que corresponde à URL "/página-inicial" e outra rota que corresponde a "/sobre-nós". Quando um usuário acessa essas URLs em um navegador ou faz uma solicitação HTTP para essas URLs, o framework (neste caso, o FastAPI) encaminha a solicitação para a função correspondente que processará a solicitação e retornará uma resposta.

Exemplo de definição de rota em FastAPI:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def homepage():
    return {"message": "Bem-vindo à página inicial!"}

@app.get("/sobre-nós")
def about_us():
    return {"message": "Somos uma empresa incrível!"}
```

Neste exemplo, temos duas rotas: "/" e "/sobre-nós", cada uma mapeada para uma função específica. Quando um usuário acessa a URL "/", a função `homepage()` é chamada e retorna uma mensagem de boas-vindas. Quando a URL "/sobre-nós" é acessada, a função `about_us()` é chamada e retorna informações sobre a empresa.

As rotas são uma parte fundamental do desenvolvimento de aplicativos web, pois permitem que os aplicativos respondam a diferentes URLs e forneçam diferentes recursos e funcionalidades com base nas solicitações dos usuários.

### **REQUEST X RESPONSE**

Em desenvolvimento web, "request" (solicitação) e "response" (resposta) são dois conceitos essenciais que descrevem a comunicação entre um cliente (geralmente um navegador da web) e um servidor web. Eles representam as informações trocadas entre o cliente e o servidor durante uma interação HTTP. Aqui estão as principais diferenças entre "request" e "response":

1. **Request (Solicitação)**:

* **Origem**: A solicitação é gerada pelo cliente (por exemplo, um navegador da web) e enviada para o servidor.
* **Objetivo**: O cliente envia uma solicitação ao servidor para solicitar um recurso, como uma página da web, um arquivo, ou para realizar uma ação, como enviar um formulário.
* **Conteúdo**: Uma solicitação pode conter informações como o método HTTP (GET, POST, PUT, DELETE, etc.), a URL de destino, os cabeçalhos (headers) que incluem informações sobre o cliente e a solicitação, e, em muitos casos, um corpo (payload) que contém dados adicionais, como dados de formulário ou JSON.
* **Exemplo**: Uma solicitação GET para "[https://www.exemplo.com/pagina](https://www.exemplo.com/pagina)" é uma solicitação que pede ao servidor para enviar a página da web localizada na URL especificada.

1. **Response (Resposta)**:

* **Origem**: A resposta é gerada pelo servidor em resposta à solicitação do cliente.
* **Objetivo**: O servidor envia uma resposta de volta ao cliente para fornecer o recurso solicitado ou informar o resultado da ação solicitada.
* **Conteúdo**: Uma resposta inclui um status HTTP que indica se a solicitação foi bem-sucedida ou se ocorreu algum erro, cabeçalhos que contêm informações sobre a resposta e, em muitos casos, um corpo (payload) que contém o conteúdo real da resposta, como uma página da web, um arquivo ou dados JSON.
* **Exemplo**: Uma resposta bem-sucedida (status 200 OK) a uma solicitação GET para "[https://www.exemplo.com/pagina](https://www.exemplo.com/pagina)" incluiria o conteúdo da página da web como o corpo da resposta.

Resumindo, uma solicitação é uma mensagem enviada pelo cliente para solicitar informações ou ações, enquanto uma resposta é a mensagem enviada pelo servidor em resposta à solicitação, fornecendo os dados ou o resultado da ação solicitada. Essa troca de solicitação e resposta é o cerne da comunicação HTTP em aplicativos web e é fundamental para a interação entre clientes e servidores.

### **PATH X QUERY PARAMETERS**

Path parameters (parâmetros de caminho) e query parameters (parâmetros de consulta) são duas maneiras diferentes de passar dados para uma API web. Ambos são usados em URLs, mas eles têm finalidades e usos distintos:

1. **Path Parameters (Parâmetros de Caminho)**:

* **Definição**: São parte da própria URL e são usados para representar valores específicos no caminho da URL.
* **Formato**: Normalmente são definidos entre chaves `{}` na rota da URL.
* **Exemplo**: Em uma URL como `https://api.exemplo.com/users/{id}`, `{id}` é um parâmetro de caminho que pode representar o ID de um usuário específico. Exemplo de URL com valor: `https://api.exemplo.com/users/123`.
* **Uso**: Geralmente são usados para identificar recursos específicos, como um usuário com um ID específico, um produto com um SKU específico, ou uma postagem de blog com um slug específico.

1. **Query Parameters (Parâmetros de Consulta)**:

* **Definição**: São adicionados à URL após um ponto de interrogação (`?`) e são usados para passar informações adicionais para a solicitação.
* **Formato**: São especificados como pares chave-valor, separados por `&`. Por exemplo, `https://api.exemplo.com/search?q=termo&filtro=ativo`.
* **Exemplo**: Em `?q=termo`, `q` é o nome do parâmetro e `termo` é o valor do parâmetro de consulta.
* **Uso**: São frequentemente usados para filtrar, ordenar ou paginar resultados de uma consulta. Por exemplo, em uma pesquisa, você pode usar um parâmetro de consulta para especificar o termo de pesquisa ou um filtro para mostrar apenas resultados ativos.

Em resumo, a diferença fundamental entre path parameters e query parameters está na maneira como eles são incluídos na URL e em seus propósitos:

* **Path parameters** fazem parte do caminho da URL e são usados para identificar recursos específicos.
* **Query parameters** são adicionados à URL como pares chave-valor após um ponto de interrogação e são usados para passar informações adicionais ou opções de consulta.

### **ENDPOINTS**

Em arquitetura de APIs RESTful, os termos "endpoints de substantivo" e "endpoints de verbo" se referem a diferentes abordagens para a estruturação das URLs das suas APIs. Eles representam diferentes estilos de design de API que têm implicações na forma como você organiza e nomeia suas rotas. Vou explicar ambos os conceitos:

1. **Endpoints de Substantivo** (ou "Nomes de Recursos"):

* Nesse estilo de design, você organiza suas URLs em torno de recursos ou entidades que estão sendo manipulados pela API.
* Os substantivos são usados nas URLs para representar os recursos. Por exemplo, se você estiver criando uma API para gerenciar tarefas, você pode ter URLs como `/tasks` para listar todas as tarefas, `/tasks/{id}` para acessar uma tarefa específica, e assim por diante.
* Os verbos HTTP (GET, POST, PUT, DELETE) são usados para indicar a ação a ser realizada no recurso identificado pela URL.
* Esse estilo de design é considerado mais intuitivo e amigável para os desenvolvedores, pois as URLs são autoexplicativas.

Exemplo de endpoints de substantivo:

* GET `/tasks`: Retorna todas as tarefas.
* GET `/tasks/{id}`: Retorna uma tarefa específica.
* POST `/tasks`: Cria uma nova tarefa.
* PUT `/tasks/{id}`: Atualiza uma tarefa específica.
* DELETE `/tasks/{id}`: Exclui uma tarefa específica.

1. **Endpoints de Verbo**:

* Nesse estilo de design, as URLs são organizadas em torno das ações ou operações que você deseja realizar, e os verbos HTTP são usados para indicar a ação a ser executada no recurso.
* Os substantivos são minimizados nas URLs, e o foco está nos verbos que descrevem as ações.
* Isso pode levar a URLs mais curtas, mas menos autoexplicativas. Por exemplo, `/create-task` pode ser usado em vez de `/tasks` para criar uma tarefa.

Exemplo de endpoints de verbo:

* POST `/create-task`: Cria uma nova tarefa.
* GET `/get-task/{id}`: Obtém uma tarefa específica.
* PUT `/update-task/{id}`: Atualiza uma tarefa específica.
* DELETE `/delete-task/{id}`: Exclui uma tarefa específica.

Ambos os estilos têm seus prós e contras, e a escolha entre eles depende das preferências de design da API e das convenções da equipe de desenvolvimento. O importante é manter a consistência em toda a API para tornar a documentação e o uso mais intuitivos para os desenvolvedores que a utilizam.
