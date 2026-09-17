````markdown
# Brainstorm — Plataforma de Agendamento Multidisciplinar

## Funcionalidades para clientes
- Cadastro, login e recuperação de senha.
- Pesquisa de profissionais por especialidade.
- Visualização de perfil, serviços e horários disponíveis.
- Agendamento, reagendamento e cancelamento de atendimentos.
- Visualização de agenda integrada com todos os profissionais.
- Recebimento de lembretes de atendimentos.
- Entrada em lista de espera para horários indisponíveis.
- Histórico de atendimentos realizados.

## Funcionalidades para profissionais
- Cadastro de especialidade, serviços e duração dos atendimentos.
- Configuração de horários e dias disponíveis.
- Visualização da própria agenda.
- Confirmação ou recusa de atendimentos.
- Bloqueio de horários por férias, reuniões ou indisponibilidade.
- Visualização dos clientes vinculados aos atendimentos.
- Criação de sessões recorrentes.

## Funcionalidades administrativas
- Cadastro e gerenciamento de clientes, profissionais e recepcionistas.
- Cadastro de serviços e especialidades.
- Cadastro de salas, espaços e equipamentos.
- Definição de permissões por perfil de usuário.
- Acompanhamento dos agendamentos da organização.
- Emissão de relatórios de atendimentos e ocupação de espaços.

## Regras de negócio
- Um horário não pode ser ocupado por mais de um atendimento para o mesmo profissional.
- Um espaço ou equipamento não pode ser reservado simultaneamente.
- O cliente não pode possuir atendimentos conflitantes.
- O agendamento será confirmado somente se cliente, profissional e recurso estiverem disponíveis.
- Cancelamentos devem liberar automaticamente o horário.
- Clientes na lista de espera devem ser avisados quando houver vaga.
- Atendimentos recorrentes devem validar conflitos em todas as datas.

## Possíveis melhorias futuras
- Pagamento online.
- Integração com WhatsApp, e-mail e notificações.
- Avaliação dos profissionais pelos clientes.
- Prontuário ou registro de evolução do cliente.
- Dashboard com indicadores de atendimentos e cancelamentos.
- Integração com calendário externo, como Google Calendar.
- Aplicativo mobile.

## Prioridades para o MVP
1. Cadastro e autenticação de usuários.
2. Controle de perfis e permissões.
3. Cadastro de profissionais, serviços e espaços.
4. Configuração de disponibilidade.
5. Agendamento, reagendamento e cancelamento.
6. Agenda do cliente e do profissional.
7. Validação de conflitos de horário e espaço.
```<!-- filepath: c:\PE\PBE_26.2_8002\puml\brainstorm.md -->

# Brainstorm — Plataforma de Agendamento Multidisciplinar

## Funcionalidades para clientes
- Cadastro, login e recuperação de senha.
- Pesquisa de profissionais por especialidade.
- Visualização de perfil, serviços e horários disponíveis.
- Agendamento, reagendamento e cancelamento de atendimentos.
- Visualização de agenda integrada com todos os profissionais.
- Recebimento de lembretes de atendimentos.
- Entrada em lista de espera para horários indisponíveis.
- Histórico de atendimentos realizados.

## Funcionalidades para profissionais
- Cadastro de especialidade, serviços e duração dos atendimentos.
- Configuração de horários e dias disponíveis.
- Visualização da própria agenda.
- Confirmação ou recusa de atendimentos.
- Bloqueio de horários por férias, reuniões ou indisponibilidade.
- Visualização dos clientes vinculados aos atendimentos.
- Criação de sessões recorrentes.

## Funcionalidades administrativas
- Cadastro e gerenciamento de clientes, profissionais e recepcionistas.
- Cadastro de serviços e especialidades.
- Cadastro de salas, espaços e equipamentos.
- Definição de permissões por perfil de usuário.
- Acompanhamento dos agendamentos da organização.
- Emissão de relatórios de atendimentos e ocupação de espaços.

## Regras de negócio
- Um horário não pode ser ocupado por mais de um atendimento para o mesmo profissional.
- Um espaço ou equipamento não pode ser reservado simultaneamente.
- O cliente não pode possuir atendimentos conflitantes.
- O agendamento será confirmado somente se cliente, profissional e recurso estiverem disponíveis.
- Cancelamentos devem liberar automaticamente o horário.
- Clientes na lista de espera devem ser avisados quando houver vaga.
- Atendimentos recorrentes devem validar conflitos em todas as datas.

## Possíveis melhorias futuras
- Pagamento online.
- Integração com WhatsApp, e-mail e notificações.
- Avaliação dos profissionais pelos clientes.
- Prontuário ou registro de evolução do cliente.
- Dashboard com indicadores de atendimentos e cancelamentos.
- Integração com calendário externo, como Google Calendar.
- Aplicativo mobile.

## Prioridades para o MVP
1. Cadastro e autenticação de usuários.
2. Controle de perfis e permissões.
3. Cadastro de profissionais, serviços e espaços.
4. Configuração de disponibilidade.
5. Agendamento, reagendamento e cancelamento.
6. Agenda do cliente e do profissional.
7. Validação de conflitos de horário e espaço.
