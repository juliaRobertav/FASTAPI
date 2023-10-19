---
description: 'REST: Conceitos e Fundamentos'
---

# REST/RESTful APIs

<figure><img src=".gitbook/assets/image (16).png" alt=""><figcaption></figcaption></figure>

### O que são APIs REST e RESTful?

#### <mark style="background-color:purple;">REST:</mark>

REST → Representational State Transfer → Transferência Representacional de Estado

É um modelo de arquitetura, onde o princípio fundamental é usar o protocolo HTTP para comunicação de dados.

REST é um conjunto de diretrizes que visa fornecer uma estrutura para a comunicação entre sistemas distribuídos.

#### APIs REST são baseadas em quatro conceitos principais:

1. Utilização dos métodos HTTP, como GET, POST, PUT e DELETE, para realizar operações em recursos.
2. Uso de URLs (Uniform Resource Locators) para identificar recursos específicos.
3. Transferência de dados entre cliente e servidor em um formato padrão, geralmente JSON ou XML.
4. Manutenção do estado da aplicação no cliente, em vez de armazená-lo no servidor.



#### <mark style="background-color:blue;">RESTful:</mark>

As APIs RESTful, por sua vez, são APIs que aderem estritamente aos princípios REST. Elas seguem as características mencionadas anteriormente e são consideradas uma implementação mais completa e rigorosa do modelo REST.

#### Critérios para enquadramento em cada tipo:

Para uma API ser considerada RESTful, ela deve atender a certos critérios adicionais além dos princípios REST. Esses critérios incluem:

* Interface uniforme: a API deve fornecer uma interface consistente e padronizada para acessar e manipular recursos.
* Clientes sem estado: cada solicitação enviada pelo cliente para o servidor deve conter todas as informações necessárias para entendê-la, sem depender de nenhum contexto armazenado no servidor.
* Operações baseadas em recursos: as ações realizadas pela API devem ser orientadas a recursos identificados por URLs únicas.

> Ou seja, as principais diferenças entre APIs REST e RESTful está no nível de aderência aos princípios REST. Enquanto as APIs REST seguem os princípios básicos do REST, as APIs RESTful são uma implementação mais completa e estrita desses princípios. APIs RESTful aderem a critérios adicionais, como a interface uniforme, clientes sem estado e operações baseadas em recursos.

Para saber mais:

{% embed url="https://www.dio.me/articles/entendendo-as-diferencas-entre-apis-rest-e-restful" %}
