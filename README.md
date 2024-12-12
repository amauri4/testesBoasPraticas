# Relatório da atividade 04 - Boas práticas de programação

## Introdução
Neste projeto, a principal escolha foi utilizar **Python** como linguagem de desenvolvimento, em conjunto com as bibliotecas **unittest** para testes e **logging** para gerenciamento de logs. Essas escolhas foram motivadas pela familiaridade com a linguagem, sua simplicidade e praticidade, bem como pela robustez e versatilidade das bibliotecas para garantir a qualidade do código e facilitar a manutenção. Por estar usando bastante **Python** ultimamente, considerei que seria uma boa alternativa me familiarizar, também, com o processo de testes, verificações e logging nessa linguagem.
O foco do projeto esteve relacionado a boas práticas de desenvolvimento, incluindo o uso de testes, mocking, validações, geração de logs e técnicas de depuração. Para mim, essa atividade foi muito interessante, pois percebi, no meu cotidiano, que costumava focar muito mais no desenvolvimento do que nos testes. Assim, por meio dessa atividade, passei a dar mais atenção aos testes nos meus códigos e, consequentemente, a tornar meus códigos mais robustos.

## Funcionamento geral do sistema 

O sistema é composto por três principais classes: `Produto`, `Catalogo` e `Pedido`, que interagem entre si para gerenciar um catálogo de produtos e processar pedidos de clientes.

- **Classe Produto**: Representa um produto com atributos como `id`, `nome` e `preço`. Essa classe é utilizada tanto para representar os itens do catálogo e nos pedidos.

- **Classe Catalogo**: Gerencia um catálogo de produtos. Possui métodos para adicionar produtos, listar os produtos existentes e buscar produtos pelo seu ID. O catálogo valida a duplicação de IDs ao adicionar um novo produto e gera logs de erro ou sucesso para essas ações.

- **Classe Pedido**: Representa um pedido feito por um cliente, contendo uma lista de produtos e o nome desse cleinte. A classe permite adicionar produtos ao pedido e calcular o total, aplicando um desconto de 10% para valores acima de R$100. Ela também gera logs informativos e de erro durante essas operações.

### Interação entre as Classes
- O `Catalogo` gerencia os produtos disponíveis, e o `Pedido` permite que os produtos sejam adicionados a um pedido. 
- Quando um produto é adicionado ao catálogo, o método `adicionarProduto` da classe `Catalogo` verifica se o produto já existe no pedido, garantindo que não haja duplicações e nem produtos nulos.
- A classe `Pedido` também utiliza os produtos do `Catalogo` para calcular o valor total do pedido, aplicando descontos quando necessário.

### Testes de Integração e Unitários
- **Testes Unitários**: Foram realizados testes para validar individualmente os métodos de cada classe. Para o `Catalogo`, os testes verificaram a adição de produtos, a verificação de duplicação de IDs e o tratamento de erros. Para o `Pedido`, foram testados a adição de produtos, o cálculo do total e a aplicação ou não de descontos.
  
- **Testes de Integração**: Validaram a interação entre as classes `Catalogo` e `Pedido`. Isso incluiu a adição de produtos ao catálogo e a posterior inclusão desses produtos em um pedido, verificando se os comportamentos das classes funcionam conforme esperado em conjunto.

## Escolha da Linguagem: Python
A escolha do Python como linguagem para o desenvolvimento deste projeto foi baseada nas seguintes razões:

- **Familiaridade**: Python é uma linguagem com a qual tenho uma experiência considerável. Sua sintaxe simples e clara facilita o desenvolvimento rápido e eficiente, sem a necessidade de gastar tempo com detalhes complexos. Ademais, tenho noção do quão importante o processo de testes e logging é, com isso, considerei uma boa ideia escolher uma linguagem a qual eu possuo afinidade.
- **Produtividade**: Python oferece uma abordagem pragmática para desenvolvimento de software. A rapidez com que é possível escrever código e implementar funcionalidades é uma grande vantagem para a execução de projetos ágeis.
- **Ecossistema e Suporte**: O Python possui um vasto ecossistema de bibliotecas, o que permite que se resolvam problemas de forma simples e rápida, utilizando ferramentas bem documentadas e amplamente suportadas pela comunidade. Assim, percebi que não teria problemas para usar as bibliotecas e ferramentas disponíveis.

## Escolha das Bibliotecas

### Biblioteca de Testes: unittest
A biblioteca `unittest` foi escolhida para a realização dos testes devido à sua integração nativa com o Python e às suas características robustas para a criação e execução de testes automatizados. O uso de `unittest` oferece as seguintes vantagens:

- **Integração Nativa**: O Python possui suporte interno à biblioteca unittest, o que elimina a necessidade de instalar pacotes adicionais e facilita a configuração do ambiente de testes.
- **Estrutura Clara e Simples**: unittest permite a organização de testes de forma estruturada, criando classes de teste com métodos de setup e teardown que facilitam o controle do ambiente de testes. Gostei bastante da simplicidade de escrever testes para validar funcionalidades, como a adição de produtos ao catálogo e ao pedido, conforme foi requisitado.
- **Facilidade de Execução**: Usando o comando `python3 -m unittest discover`, é possível realizar a execução de testes de forma simples e eficiente.
- **Mocking integrado**: A biblioteca unittest também oferece suporte a mocks, permitindo que funções externas, como o registro de logs, sejam testadas sem a necessidade de interagir com sistemas reais ou coisas externas.

### Biblioteca de logging
A biblioteca `logging` do Python foi uma ferramenta muito simples de se usar, percebi vantagens como:

- **Facilidade de uso**: O `logging` é simples de configurar e utilizar, permitindo registrar informações de diferentes níveis (INFO, DEBUG, ERROR, etc.) com pouco código.

- **Controle de níveis de log**: A biblioteca permite a configuração de diferentes níveis de severidade para os logs, como `DEBUG`, `INFO`, `WARNING`, `ERROR` e `CRITICAL`, facilitando o controle do que é registrado em diferentes ambientes (desenvolvimento, testes, produção).

- **Redirecionamento de logs**: Os logs podem ser direcionados para diferentes destinos, como o terminal, arquivos, ou servidores remotos, de maneira flexível e configurável.

- **Configurabilidade**: A biblioteca oferece flexibilidade para personalizar a formatação dos logs e os comportamentos de gravação, o que permite adaptar os logs às necessidades específicas do projeto.

## Conclusão

O objetivo principal deste projeto foi ensinar sobre boas práticas de desenvolvimento, como o uso de testes automatizados, mocking para isolar dependências externas, validações de dados, geração de logs para monitoramento e técnicas de depuração para identificar e corrigir erros de forma eficiente. Diante disso, foi possível criar mais proximidade com ferramentas fundamentais para cenários de desenvolvimento reais.

## Executar os Testes com `unittest`

Para executar os testes no projeto, utilize o seguinte comando:

```bash
python3 -m unittest discover testes
```

## Rodar o arquivo main com exemplos

Para rodar o arquivo principal e ver o código em funcionamento, use o seguinte comando:

```bash
python3 main.py
```
