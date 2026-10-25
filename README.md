Cofree

Aplicativo de controle financeiro pessoal desenvolvido em Python, com interface gráfica e armazenamento local de dados.

«Versão: 0.1.0
Status: Em desenvolvimento»

Sobre o projeto

O Cofree é um aplicativo de controle financeiro pessoal que tem como objetivo ajudar o usuário a organizar suas finanças por meio do registro manual de informações financeiras.

O sistema permite que o usuário informe seus valores financeiros e, a partir dos dados registrados, acompanhe seu saldo, organize movimentações, visualize categorias de gastos e planeje metas financeiras.

O projeto está sendo desenvolvido em Python, com uma interface gráfica construída utilizando CustomTkinter e armazenamento local de dados em JSON.

Escopo do projeto

O Cofree funciona como uma ferramenta de organização e acompanhamento financeiro. Ele não realiza transações financeiras nem mantém ou movimenta dinheiro real.

O aplicativo trabalha com os valores informados pelo próprio usuário, utilizando esses registros para realizar cálculos e apresentar informações financeiras.

O que o Cofree faz

- Registra informações financeiras fornecidas pelo usuário.
- Calcula e apresenta valores com base nos dados armazenados.
- Organiza entradas e saídas financeiras.
- Permite acompanhar categorias e metas financeiras.
- Ajuda o usuário a visualizar e planejar suas finanças pessoais.

O que o Cofree não faz

- Não realiza transferências ou pagamentos.
- Não mantém dinheiro ou fundos dos usuários.
- Não se conecta a contas bancárias.
- Não consulta automaticamente saldos bancários reais.
- Não verifica se os valores informados correspondem ao dinheiro efetivamente disponível.

A precisão das informações apresentadas depende dos dados registrados e atualizados pelo usuário.

Funcionalidades implementadas

- [x] Interface gráfica desenvolvida com CustomTkinter.
- [x] Janela principal com barra lateral, cabeçalho e área de conteúdo.
- [x] Navegação entre as páginas Painel, Movimentações, Categorias e Metas.
- [x] Tela inicial para cadastro do saldo inicial.
- [x] Validação do saldo inicial informado pelo usuário.
- [x] Armazenamento local de dados utilizando JSON.
- [x] Estrutura inicial das páginas do aplicativo.
- [x] Componentes visuais para apresentação de informações financeiras.
- [x] Organização do código em módulos separados.
- [x] Centralização das cores da interface.
- [x] Exibição da versão do aplicativo na barra lateral.

Observação: algumas páginas e ações ainda possuem apenas componentes visuais ou funcionalidades parciais. A implementação completa da lógica financeira continua em andamento.

Tecnologias utilizadas

- Python: linguagem de programação utilizada no desenvolvimento.
- CustomTkinter: biblioteca utilizada para a construção da interface gráfica.
- JSON: formato utilizado para o armazenamento local de dados.
- Git: sistema de controle de versão.
- GitHub: plataforma de hospedagem do repositório.

Estrutura do projeto

O projeto está organizado em módulos com responsabilidades distintas, separando a interface gráfica, as operações financeiras, as validações e o armazenamento de dados.

Cofree/
├── main.py
├── versão.py
├── cofree/
│   ├── armazenamento/
│   │   └── json_maneger.py
│   ├── financeiro/
│   │   ├── operacoes.py
│   │   └── validacoes.py
│   └── interface/
│       ├── painel.py
│       ├── menu.py
│       ├── pagina.py
│       ├── cartoes.py
│       └── tela_inicial.py
└── utils/
    └── cores.py

Nota: esta árvore apresenta os principais arquivos conhecidos do projeto. A estrutura pode conter outros módulos e arquivos.

Como executar

Pré-requisitos

- Python instalado.
- Git, caso deseje clonar o repositório.

Instalação

1. Clone o repositório:

git clone URL_DO_REPOSITORIO

2. Acesse a pasta do projeto:

cd Cofree

3. Instale a dependência da interface gráfica:

python -m pip install customtkinter

4. Execute o aplicativo:

python main.py

Substitua "URL_DO_REPOSITORIO" pelo endereço real do repositório no GitHub.

Próximas etapas

Os próximos objetivos de desenvolvimento incluem:

- [ ] Implementar o registro funcional de entradas e saídas.
- [ ] Integrar as movimentações aos cálculos do saldo registrado.
- [ ] Implementar o gerenciamento funcional de categorias.
- [ ] Desenvolver o acompanhamento de metas financeiras.
- [ ] Aprimorar os relatórios e indicadores financeiros.
- [ ] Melhorar as validações e o tratamento de erros.
- [ ] Implementar testes para verificar a confiabilidade dos cálculos.
- [ ] Avaliar melhorias no armazenamento e na integridade dos dados.

Esta lista representa objetivos futuros e poderá ser atualizada conforme o desenvolvimento avançar.

Versionamento

O Cofree utiliza versionamento no formato "MAJOR.MINOR.PATCH".

A versão "0.1.0" representa uma etapa inicial do desenvolvimento. A numeração será atualizada conforme novas funcionalidades forem implementadas, melhorias forem realizadas e problemas forem corrigidos.

Autor

Desenvolvido como projeto pessoal para aprendizado e prática de programação em Python.