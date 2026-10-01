# Proposta - Papéis de Usuário e Requisitos de Acesso

## Objetivo

Antes de implementar o Django Admin ou proteger os endpoints da API, definir quais tipos de usuário existem no sistema e quais ações cada um deve poder realizar. Nesta etapa, papéis e acessos são requisitos do produto; ainda não serão configurados em código.

## Conceitos

- **Usuário:** pessoa com uma conta na plataforma.
- **Papel:** categoria que representa a responsabilidade do usuário no domínio do sistema.
- **Ação:** operação que o usuário pode tentar realizar, como criar uma playlist ou publicar conteúdo.
- **Autenticação:** processo que identifica quem está usando o sistema.
- **Autorização:** decisão sobre se aquele usuário pode executar uma ação específica.

Ter uma conta ou estar autenticado não significa, por si só, ter autorização para todas as ações. Nesta atividade, vamos definir as regras esperadas sem escolher ainda como implementá-las.

## Papéis iniciais propostos

| Papel | Responsabilidade no sistema |
| --- | --- |
| Ouvinte | Consome conteúdos disponíveis e organiza playlists próprias. |
| Criador | Publica conteúdos e gerencia os conteúdos que criou. |
| Administrador | Mantém a plataforma e pode atuar sobre conteúdos e contas quando necessário. |

Esses papéis são uma proposta inicial baseada nos requisitos do projeto. A equipe pode ajustar nomes, responsabilidades ou quantidade de papéis, desde que registre as decisões.

## Matriz inicial de ações

Use a matriz como ponto de partida. “Próprio” significa que a ação só se aplica a recursos pertencentes ao usuário; “público” significa recurso disponibilizado para todos conforme as regras do produto.

| Ação | Visitante | Ouvinte | Criador | Administrador |
| --- | --- | --- | --- | --- |
| Consultar conteúdo público | Sim | Sim | Sim | Sim |
| Criar e gerenciar playlists próprias | Não | Sim | Sim | Sim |
| Enviar conteúdo | Não | Não | Sim | Sim |
| Editar ou remover conteúdo próprio | Não | Não | Sim | Sim |
| Editar ou remover conteúdo de outra pessoa | Não | Não | Não | Sim |
| Gerenciar contas e papéis | Não | Não | Não | Sim |

Esta matriz descreve o comportamento esperado do produto. Ela não define ainda permissões do Django Admin, classes de permissão do Django REST Framework, grupos, campos de modelo ou autenticação por token.

## Requisitos que devem ficar explícitos

1. Conteúdo público pode ser consultado sem que o usuário seja criador.
2. Somente criadores podem enviar conteúdo.
3. Um criador pode editar ou remover os próprios conteúdos, mas não os de outros criadores.
4. Ouvintes e criadores podem gerenciar apenas as próprias playlists.
5. Administradores podem atuar sobre recursos de qualquer usuário e gerenciar contas, conforme a política definida pela equipe.
6. As regras para conteúdos privados, exclusão de contas, suspensão de usuários e mudança de papel devem ser decididas antes da implementação, caso façam parte do escopo.

## Atividade

Em equipe:

1. Revisem os papéis propostos e indiquem se há responsabilidades duplicadas ou ausentes.
2. Completem a matriz com as ações necessárias ao projeto, incluindo leitura, criação, alteração e exclusão.
3. Para cada ação sobre um recurso, indiquem se a regra vale para qualquer recurso, apenas para recursos públicos ou apenas para recursos próprios.
4. Registrem decisões e dúvidas em linguagem de negócio, sem usar ainda nomes de classes ou configurações do Django.

## Entrega esperada

Uma matriz de papéis e ações revisada pela equipe, acompanhada de uma lista curta de regras e dúvidas em aberto. Essa entrega servirá de referência para etapas posteriores: o roteiro de Admin aplicará regras à interface administrativa, e o roteiro da API tratará separadamente da autorização dos endpoints.

## Relação com os roteiros seguintes

- **Django Admin:** decidirá como as regras relevantes se aplicam às operações administrativas.
- **Autenticação:** ensinará como identificar o usuário que faz uma requisição.
- **Autorização da API:** decidirá, em cada endpoint, quais ações o usuário identificado pode realizar.

Os mecanismos dessas etapas não são intercambiáveis. A matriz de requisitos é comum como referência de negócio, mas cada camada precisa implementar e validar suas próprias regras.