# Relatório da atividade 04 - Boas práticas de programação

## Introdução
Neste projeto, a principal escolha foi utilizar **Python** como linguagem de desenvolvimento, em conjunto com as bibliotecas **unittest** para testes e **logging** para gerenciamento de logs. Essas escolhas foram motivadas pela familiaridade com a linguagem, sua simplicidade e praticidade, bem como pela robustez e versatilidade das bibliotecas para garantir a qualidade do código e facilitar a manutenção. Por estar usando bastante **Python** ultimamente, considerei que seria uma boa alternativa me familiarizar, também, com o processo de testes, verificações e logging nessa linguagem.
O foco do projeto esteve relacionado a boas práticas de desenvolvimento, incluindo o uso de testes, mocking, validações, geração de logs e técnicas de depuração. Para mim, essa atividade foi muito interessante, pois percebi, no meu cotidiano, que costumava focar muito mais no desenvolvimento do que nos testes. Assim, por meio dessa atividade, passei a dar mais atenção aos testes nos meus códigos e, consequentemente, a tornar meus códigos mais robustos.

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
