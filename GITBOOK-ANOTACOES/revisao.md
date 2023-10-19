# Revisão

**PERGUNTAS**

1. O que é o FastAPI e para que ele é usado?
2. Quais são as principais características do FastAPI que o tornam popular para o desenvolvimento web em Python?
3. Como você inicia um novo projeto FastAPI?
4. Qual é a diferença entre uma rota e um endpoint no FastAPI?
5. Como você define uma rota em uma aplicação FastAPI?
6. O que são modelos de dados (Pydantic models) e como eles são usados no FastAPI?
7. Quais são os métodos HTTP mais comuns e como você os associa a funções no FastAPI?
8. Como você valida dados de entrada em solicitações HTTP no FastAPI?
9. Como você lida com erros e exceções em uma aplicação FastAPI?
10. Qual é a função do sistema de documentação automática do FastAPI e como você pode acessá-lo?

**RESPOSTAS**

1. O FastAPI é um framework web moderno para Python usado para criar APIs de forma rápida e eficiente.
2. As principais características do FastAPI incluem: alto desempenho, suporte automático à documentação, validação de tipos de dados, geração automática de esquemas JSON, suporte a websockets, integração fácil com bancos de dados, e suporte a autenticação e autorização.
3. Para iniciar um novo projeto FastAPI, você precisa criar um ambiente virtual Python, instalar o FastAPI e outras dependências, criar um arquivo Python para sua aplicação, definir rotas e executar o servidor de desenvolvimento.
4. Uma rota é uma URL específica dentro de uma aplicação web que corresponde a uma função ou método no código. Um endpoint é uma implementação específica de uma rota que responde a um método HTTP específico.
5. Você define uma rota no FastAPI usando um decorador como `@app.get("/")`, onde `@app` é uma instância da sua aplicação e `"/"` é a URL da rota.
6. Os modelos de dados Pydantic são classes Python que descrevem a estrutura dos dados que sua aplicação recebe e envia. Eles são usados no FastAPI para validar dados de entrada e gerar automaticamente esquemas JSON para documentação.
7. Os métodos HTTP mais comuns são GET, POST, PUT e DELETE. No FastAPI, você associa métodos HTTP a funções Python usando decoradores, como `@app.get("/")`.
8. O FastAPI oferece validação automática de dados de entrada com base nos modelos de dados Pydantic que você define para seus endpoints. Qualquer dado que não corresponda ao modelo gerará um erro HTTP.
9. O FastAPI fornece uma maneira de lidar com erros e exceções usando manipuladores de exceção personalizados. Você pode criar funções para manipular erros específicos e personalizar as respostas de erro.
10. O FastAPI possui um sistema de documentação automática que gera documentação interativa para suas APIs. Você pode acessá-lo navegando para `/docs` ou `/redoc` na raiz da sua aplicação quando o servidor estiver em execução.
