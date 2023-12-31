---
description: Dicas/Comandos
---

# Requirements

Para ativar um ambiente virtual e instalar as dependências listadas em um arquivo "requirements.txt" em Python, siga os passos abaixo:

1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório do seu projeto onde está localizado o arquivo "requirements.txt" usando o comando "cd" (Change Directory). Por exemplo:

```
cd caminho/do/seu/projeto
```

Certifique-se de estar dentro do diretório correto onde o arquivo "requirements.txt" está localizado.

3. Crie um ambiente virtual (se ainda não tiver um) para isolar as dependências do projeto. Você pode usar a biblioteca "virtualenv" para isso. Caso você não tenha o "virtualenv" instalado, pode fazê-lo com o comando:

```
pip install virtualenv
```

4. Crie o ambiente virtual com o seguinte comando:

```
virtualenv nome_do_seu_ambiente
```

Substitua "nome\_do\_seu\_ambiente" pelo nome que você deseja dar ao ambiente virtual.

5.  Ative o ambiente virtual. A maneira de ativar o ambiente virtual varia de acordo com o sistema operacional:

    * No Windows:

    ```
    nome_do_seu_ambiente\Scripts\activate
    ```

    * No macOS e Linux:

    ```
    source nome_do_seu_ambiente/bin/activate
    ```
6. Com o ambiente virtual ativado, você verá o nome do ambiente virtual no prompt de comando, indicando que você está trabalhando dentro do ambiente isolado.
7. Agora, você pode instalar as dependências listadas no arquivo "requirements.txt" usando o comando pip:

```
pip install -r requirements.txt
```

Isso instalará todas as dependências especificadas no arquivo "requirements.txt" no ambiente virtual ativo.

8. Depois de instalar as dependências, você pode executar o seu projeto ou aplicação no ambiente virtual.
9. Quando terminar de trabalhar no projeto, você pode desativar o ambiente virtual usando o comando:

```
deactivate
```

Isso o levará de volta ao ambiente Python global do sistema.

Lembre-se de ativar o ambiente virtual sempre que você estiver trabalhando em seu projeto e precisar usar suas dependências específicas. Isso ajuda a manter as dependências do projeto isoladas de outras instalações Python em seu sistema.
