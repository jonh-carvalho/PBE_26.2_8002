 # Caso de Uso Descritivo: Realizar Compra de Produtos

## 1. Identificação

- **Código:** UC01
- **Nome:** Realizar compra de produtos
- **Objetivo:** Permitir que um cliente selecione produtos, informe os dados de entrega, efetue o pagamento e receba a confirmação do pedido.
- **Ator principal:** Cliente
- **Atores secundários:** Sistema de pagamento, estoque e serviço de entrega
- **Prioridade:** Alta

## 2. Pré-condições

- O cliente deve estar cadastrado e autenticado no comércio, ou optar por realizar a compra como visitante.
- Os produtos devem estar cadastrados no sistema.
- O sistema de pagamento deve estar disponível.

## 3. Pós-condições

- O pedido é registrado com um número de identificação.
- O estoque dos produtos é atualizado.
- O pagamento é processado ou fica pendente, conforme o método escolhido.
- O cliente recebe a confirmação do pedido.

## 4. Fluxo principal

1. O cliente acessa o catálogo de produtos.
2. O sistema exibe os produtos, preços, descrições e disponibilidade.
3. O cliente pesquisa e seleciona um produto.
4. O sistema exibe os detalhes do produto.
5. O cliente informa a quantidade e adiciona o produto ao carrinho.
6. O sistema atualiza o carrinho e calcula o subtotal.
7. O cliente revisa o carrinho e seleciona a opção de finalizar compra.
8. O cliente informa ou confirma o endereço de entrega.
9. O sistema calcula o frete e exibe o valor total da compra.
10. O cliente escolhe a forma de pagamento e informa os dados necessários.
11. O sistema valida os dados e solicita a autorização do pagamento.
12. O sistema confirma a aprovação, registra o pedido e baixa os itens do estoque.
13. O sistema exibe o número do pedido e envia a confirmação ao cliente.

## 5. Fluxos alternativos e exceções

- **A1 — Produto indisponível:** O sistema informa que o produto não está disponível e impede sua inclusão ou conclusão da compra.
- **A2 — Quantidade insuficiente:** O sistema informa o limite disponível e solicita que o cliente ajuste a quantidade.
- **A3 — Dados de entrega inválidos:** O sistema informa os campos incorretos e solicita a correção.
- **A4 — Pagamento recusado:** O sistema informa a recusa e permite que o cliente escolha outro método de pagamento.
- **A5 — Falha no sistema:** O sistema informa a indisponibilidade, não confirma o pedido e orienta o cliente a tentar novamente.
- **A6 — Cancelamento:** O cliente pode cancelar a operação antes da confirmação do pagamento, e o sistema mantém o estoque inalterado.

## 6. Regras de negócio

- O pedido só pode ser confirmado após a validação dos produtos, endereço e pagamento.
- O preço e a disponibilidade considerados são os apresentados no momento da finalização da compra.
- O cliente deve ser informado sobre o prazo e o valor do frete antes de confirmar o pedido.
- Cada pedido deve possuir um identificador único.
- Produtos pagos devem ser reservados para separação e entrega.

## 7. Requisitos especiais

- Os dados pessoais e de pagamento devem ser protegidos.
- O sistema deve apresentar uma interface acessível e responsiva.
- As operações de criação do pedido e atualização do estoque devem preservar a consistência dos dados.
