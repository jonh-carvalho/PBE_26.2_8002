# Cenário de Aula: Backend GAAP

## 1. Contexto e desafio

Uma escola de treinamento esportivo precisa organizar alunos, profissionais e sessões de Treino, Fisioterapia, Psicologia e Nutrição. Atualmente, a operação depende de controles dispersos e não possui uma fonte confiável para acompanhar vagas, presenças e relatórios de treino.

A turma deverá projetar e entregar, em quatro meses, o backend de um recorte inicial do GAAP (Gestão de Atletas de Alta Performance). A proposta parte da análise do ambiente PKZ & One to One, mas o produto acadêmico não deve tentar reproduzir todos os módulos clínicos, financeiros, de BI ou mobile observados. O foco é entregar uma API funcional, testada e documentada para sustentar a operação de agenda e treino.

## 2. Objetivos pedagógicos

- Aplicar programação orientada a objetos na modelagem das regras do domínio.
- Projetar um banco de dados relacional normalizado e implementar persistência com ORM.
- Produzir e manter diagramas UML de casos de uso, classes e sequência.
- Construir uma API REST com validação, tratamento de erros, autenticação e autorização por perfil.
- Trabalhar de forma iterativa com RUP/UP, Git, GitHub Issues, pull requests e GitHub Projects.

## 3. Escopo do MVP

### Perfis de usuário

| Perfil | Responsabilidades iniciais |
|---|---|
| Administrador | Mantém alunos, profissionais, serviços, horários e bloqueios; consulta pendências. |
| Treinador | Consulta a agenda sob sua responsabilidade, registra presença/falta e cria relatórios de treino. |
| Profissional de saúde | Consulta apenas os atendimentos atribuídos ao seu serviço e agenda. |

### Funcionalidades iniciais

1. Autenticação de usuários e autorização por perfil.
2. 
3.
4.
5.

### Fora do escopo desta entrega

- Pagamentos, gateway, cobrança recorrente e ledger financeiro completo.
- Prontuário clínico detalhado, assinatura digital e cálculos de força por sexo e idade.
- Aplicativo mobile, QR Code, notificações por WhatsApp/e-mail e operação offline.
- Dashboards analíticos, data warehouse, multi-tenancy e integrações públicas.
- Geração de PDF e upload de fotos; a API deve deixar pontos de extensão documentados para essas evoluções.

## 4. Modelo inicial do domínio

As entidades mínimas são...

O banco relacional deve usar chaves primárias, chaves estrangeiras, restrições de unicidade e índices para consultas de agenda. A equipe deve justificar as cardinalidades no diagrama de classes e no diagrama entidade-relacionamento. Dados de autenticação não devem ser armazenados em texto puro; senhas devem ser protegidas por hash.

## 5. Regras de negócio prioritárias

| ID | Regra |
|---|---|
| RN01 |  |
| RN02 | |
| RN03 |  |


## 6. Requisitos não funcionais

- 
-
-
-

## 7. Fases RUP/UP e cronograma de quatro meses

| Fase | Semanas | Entregáveis e marco |
|---|---:|---|
| Incepção | 1-5 | Visão do produto, stakeholders, backlog inicial, 5w3h, brainstorm e mapa mental|
| Elaboração | 6-8 |  casos de uso prioritários, critérios de aceitação e repositório configurado. Marco: escopo do MVP aprovado. , Modelo de domínio, DER, diagramas UML, arquitetura, protótipo de rotas, riscos e plano de iteração. Marco: arquitetura validada e base de dados modelada. |
| Construção - Iteração 1 | 9-10 | Autenticação, perfis, cadastros de aluno/profissional/serviço, migrações e testes de domínio. Marco: base administrativa utilizável pela API. |
| Construção - Iteração 2 | 11-12 | Regras de disponibilidade, bloqueios, agendamento, consulta de agenda e testes de concorrência/validação. Marco: agenda funcional. |
| Construção - Iteração 3 | 13-14 | Presença, aula ministrada, relatórios de treino, dashboard simples, auditoria e documentação de endpoints. Marco: fluxo operacional completo. |
| Construção - Iteração 3 | 15-16 | Presença, aula ministrada, relatórios de treino, dashboard simples, auditoria e documentação de endpoints. Marco: fluxo operacional completo. |
| Transição | 17-18 | Testes de aceitação, correção de defeitos, demonstração, release, retrospectiva e apresentação técnica. Marco: aplicativo entregue. |

## 8. Artefatos UML obrigatórios

1. Diagrama de casos de uso com os três perfis e os casos prioritários.
2. Diagrama de classes do domínio, com atributos relevantes, associações, multiplicidades e responsabilidades.
3. Diagrama de sequência para o caso "Confirmar agendamento", evidenciando validação de capacidade, conflito e bloqueio.
4. Diagrama de sequência para o caso "Finalizar relatório de treino".
5. Diagrama entidade-relacionamento compatível com as migrações implementadas.

Os diagramas devem ser versionados no repositório e atualizados sempre que uma decisão de modelagem mudar.

## 9. Gestão com GitHub

### Repositório

- Adotar estratégia de branches com `main` protegida e branches por issue, no formato `feature/123-agendamento` ou `fix/123-capacidade`.
- Todo código deve chegar à `main` por pull request, com revisão de pelo menos um integrante.
- Configurar modelo de issue, modelo de pull request, `.gitignore`, instruções de execução e integração contínua para testes.

### GitHub Issues

Cada requisito, defeito, dívida técnica ou decisão relevante deve ser uma issue. As issues funcionais precisam conter descrição, critérios de aceitação, regras de negócio afetadas, tarefas técnicas e responsável.

Rótulos mínimos: `tipo:feature`, `tipo:bug`, `tipo:documentacao`, `area:api`, `area:dominio`, `area:database`, `area:testes`, `prioridade:alta`, `prioridade:media` e `prioridade:baixa`.

### GitHub Projects

Criar um Project em quadro com as colunas `Backlog`, `Pronto para desenvolvimento`, `Em andamento`, `Em revisão`, `Em teste` e `Concluído`. Cada item deve apontar para uma issue, ter fase RUP/UP, prioridade, responsável e iteração. A cada semana, a equipe revisa o quadro, remove bloqueios e ajusta o plano da próxima iteração.

## 10. Critérios de aceite da entrega

- O projeto sobe localmente por instruções reproduzíveis e aplica as migrações em banco relacional.
- Um administrador consegue cadastrar dados de base e configurar ao menos um serviço.
- A API recusa agendamentos conflitantes, bloqueados ou acima da capacidade.
- Um profissional autorizado consegue consultar a agenda, registrar presença/falta e criar/finalizar relatório.
- Usuários sem permissão não acessam agendas ou operações administrativas indevidas.
- Os testes automatizados passam no pipeline e cobrem as regras prioritárias.
- A documentação, os diagramas UML e o GitHub Project refletem o que foi efetivamente entregue.

## 11. Evoluções sugeridas após o MVP

Após a entrega, a turma pode selecionar uma evolução para estudo ou próxima edição: extrato de créditos e pagamentos, lista de espera, notificações de vencimento, perfil unificado do aluno, avaliação física, dashboards de BI, integração por webhooks ou aplicativo mobile.
