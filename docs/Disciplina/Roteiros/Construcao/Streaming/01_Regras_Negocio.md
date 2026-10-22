# 01 — Regras de negócio

## Objetivo

Este documento reúne as regras de negócio propostas para o aplicativo de streaming. Elas orientam a modelagem, a implementação da API e os testes. Os limites numéricos, os critérios de moderação e as políticas comerciais que ainda não foram definidos devem ser acordados antes da implementação; não devem ser tratados como valores implícitos.

## 1. Usuários, contas e permissões

1. O cadastro deve exigir dados de conta válidos e verificação do endereço de e-mail antes de habilitar as funcionalidades que dependem de uma conta confirmada.
2. A plataforma deve distinguir, no mínimo, usuários básicos, criadores de conteúdo e administradores:
   - Usuários básicos podem criar e gerenciar as próprias playlists, mas não podem publicar conteúdo.
   - Criadores podem publicar conteúdo e gerenciar as próprias publicações.
   - Administradores podem administrar usuários, conteúdos e playlists conforme as permissões administrativas definidas para a plataforma.
3. Cada usuário pode consultar e gerenciar os próprios dados e recursos. Um usuário não pode alterar ou excluir a playlist de outra pessoa; a exceção é uma ação administrativa autorizada.
4. A identidade do proprietário deve ser determinada pelo sistema a partir da conta autenticada, e não confiada a um identificador enviado pelo cliente.

## 2. Conteúdos e publicação

1. Somente criadores autorizados podem publicar conteúdos, nos formatos aceitos pela plataforma, como áudio e vídeo.
2. Cada conteúdo deve ter título, descrição e miniatura. O título deve ser único entre os conteúdos do mesmo criador.
3. O criador pode definir o conteúdo como público ou privado. Conteúdos públicos podem ser descobertos e reproduzidos conforme as permissões da plataforma. Conteúdos privados só podem ser acessados pelo criador e por usuários explicitamente autorizados.
4. Antes da publicação, o conteúdo deve passar pelo processo de moderação definido pela plataforma, para verificar conformidade com as regras de uso e direitos autorais. O método e os critérios de aprovação precisam ser especificados.
5. O conteúdo deve possuir um estado de publicação, como rascunho, publicado ou bloqueado, para distinguir itens ainda não disponíveis, disponíveis ao público e impedidos de circular.

## 3. Playlists

1. Usuários autenticados podem criar e gerenciar playlists próprias.
2. O título de uma playlist deve ser único no conjunto de playlists do mesmo proprietário.
3. Um mesmo conteúdo não pode aparecer mais de uma vez na mesma playlist.
4. O proprietário pode definir uma playlist como pública ou privada. Uma playlist pública só pode incluir conteúdos públicos; uma playlist privada pode incluir conteúdos públicos ou privados que o proprietário tenha permissão para acessar.
5. Conteúdos privados incluídos em playlists privadas não se tornam acessíveis a outros usuários por meio da playlist.
6. O proprietário pode alterar a ordem dos conteúdos da playlist.
7. Limites para a quantidade de playlists por usuário, quando aplicáveis, devem ser configurados e comunicados pela plataforma.

## 4. Consumo e interação com conteúdos

1. Conteúdos públicos podem ser reproduzidos por usuários que atendam às permissões de acesso da plataforma. Conteúdos privados só podem ser reproduzidos por usuários autorizados.
2. Se houver download, o acesso poderá ser restrito a assinantes premium, com limites por período. As condições e os limites devem ser definidos antes da implementação.
3. Usuários podem favoritar conteúdos para encontrá-los posteriormente. Caso exista um limite para contas básicas, o valor deve ser definido e comunicado.
4. Se comentários e avaliações forem habilitados, eles devem estar associados ao usuário e ao conteúdo correspondente e seguir as regras de convivência da plataforma.
5. Usuários podem reportar conteúdos que considerem impróprios ou que violem as regras. A plataforma deve definir como esses relatos serão analisados e quais ações podem resultar da análise.

## 5. Notificações

1. Usuários que acompanham um criador podem receber uma notificação quando ele publicar um novo conteúdo.
2. A plataforma pode notificar usuários sobre alterações relevantes em playlists ou conteúdos que acompanham, incluindo exclusão ou mudança de visibilidade.
3. Os eventos que geram notificações, os canais utilizados e as preferências de recebimento devem ser definidos para cada implementação.

## 6. Assinaturas e recursos premium

1. A plataforma pode oferecer planos premium com benefícios como acesso a conteúdos exclusivos, acesso antecipado, limites maiores para playlists e favoritos ou permissão de download.
2. Se houver cobrança recorrente, a assinatura deve registrar seu período e estado, permitir cancelamento e aplicar as regras de renovação acordadas.
3. O acesso a recursos premium deve ser concedido apenas enquanto a assinatura estiver válida, de acordo com as condições do plano.
4. Planos, benefícios, limites, cobrança, renovação e efeitos do cancelamento devem ser especificados antes de integrar um serviço de pagamento.

## 7. Segurança, privacidade e conformidade

1. Dados pessoais devem ser tratados conforme a legislação aplicável e a política de privacidade da plataforma.
2. Dados pessoais devem ser acessíveis somente ao próprio usuário e a administradores autorizados, respeitando o princípio do menor privilégio.
3. A autenticação deve proteger as contas, utilizar senhas armazenadas de forma segura e aplicar os mecanismos de proteção definidos para os perfis e operações.
4. A plataforma deve limitar requisições abusivas e definir medidas contra uso automatizado ou excessivo da API.
5. Dados e conteúdos privados devem permanecer protegidos em todas as operações, incluindo listagem, busca, playlists e reprodução.

## Orientações para implementação e validação

- Converter cada regra aplicável em critérios de aceitação verificáveis.
- Aplicar as regras nos pontos adequados: validação da API, autorização, modelo de domínio e restrições do banco de dados.
- Testar os casos permitidos e negados, incluindo acesso anônimo, acesso por outro usuário, conteúdo privado e ações administrativas.
- Documentar como cada regra se relaciona com os modelos, endpoints e testes.
- Confirmar com os responsáveis pelo produto os limites numéricos e as políticas ainda abertas antes de implementá-los.
