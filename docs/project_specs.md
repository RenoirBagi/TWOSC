# Especificação do Projeto TWOSC

## 1. Visão Geral e Problema
Atualmente, o setor de TI (Renoir e Marcos) realiza solicitações de compras de equipamentos e insumos através de formulários, sem um sistema de registro persistente acessível a eles.
Isso gera os seguintes problemas:
•	Perda de Rastreabilidade: Esquecimento sobre o que foi pedido e quando.
•	Dúvida na Quantidade: Incerteza se a quantidade solicitada supre a necessidade atual.
•	Falta de Parâmetros para Cobrança: Dificuldade em cobrar o setor de compras por não saber a data exata da solicitação original (SLA).

## 2. Objetivo do Projeto
Desenvolver uma aplicação web simples (Single Page Application) para centralizar o registro, acompanhamento de status e histórico das solicitações de compras feitas pelo departamento de TI. O sistema servirá como um "espelho de controle" para os solicitantes.

## 3. Declaração de Escopo

### 3.1. O que faz parte do escopo (In-Scope)
•	Interface web para cadastro de novas solicitações de compra.
•	Painel de visualização (Dashboard/Lista) de todas as solicitações.
•	Funcionalidade para alteração manual de status (ex: de "Solicitado" para "Chegou").
•	Indicadores visuais de atraso (pedidos abertos há muito tempo).
•	Histórico de itens cancelados ou concluídos.

### 3.2. O que NÃO faz parte do escopo (Out-Scope)
•	Acesso de usuários do setor de Compras ou Financeiro (uso exclusivo do TI).
•	Integração automática com ERPs ou sistemas de e-mail.
•	Controle de Estoque/Inventário (o foco é a aquisição, não o armazenamento).
•	Aprovação de alçada/gestores dentro do sistema.

## 4. Requisitos Funcionais (RF)
| ID | Requisito | Descrição |
|---|---|---|
| RF001 | Cadastrar Solicitação | O sistema deve permitir registrar um pedido informando: Item, Link de Referência, Quantidade, Prioridade e Observações. A data deve ser capturada automaticamente. |
| RF002 | Listar Solicitações | O sistema deve apresentar uma listagem de pedidos, permitindo filtros por Status (Pendente, Entregue) e ordenação por Data. |
| RF003 | Atualizar Status | O usuário deve poder alterar o status do pedido para refletir a realidade (Ex: Marcar que o setor de compras já realizou o pedido). |
| RF004 | Editar Solicitação | Permitir a correção de informações (quantidade/link) enquanto o pedido ainda estiver em fase inicial. |
| RF005 | Cancelar Solicitação | Permitir que um pedido seja cancelado, mantendo-o no histórico mas removendo-o da lista de "Pendências". |
| RF006 | Alerta de Atraso | O sistema deve destacar visualmente (cor ou ícone) solicitações que estão com status "Pendente" há mais de X dias (configurável, padrão 5 dias). |

## 5. Requisitos Não-Funcionais (RNF)
| ID | Requisito | Descrição |
|---|---|---|
| RNF001 | Stack Tecnológico | O Backend deve ser desenvolvido em Python e o Frontend em React. |
| RNF002 | Usabilidade | A interface deve ser limpa e focada em produtividade (poucos cliques para registrar). |
| RNF003 | Disponibilidade | O sistema deve ser acessível via navegador web. |

## 6. Regras de Negócio (RN)
•	**RN01 - Fluxo de Status**: Uma solicitação deve seguir, preferencialmente, o fluxo:
    1.	PENDENTE (Solicitei, mas compras ainda não confirmou/cotou).
    2.	AGUARDANDO ENTREGA (Compras confirmou que comprou).
    3.	CONCLUÍDO (Item chegou no TI).
    4.	CANCELADO (Item não é mais necessário).
•	**RN02 - Imutabilidade Histórica**: Não deve ser possível excluir fisicamente (delete do banco) registros de compras "Concluídas", para garantir histórico futuro.
•	**RN03 - Definição de Atraso**: Uma solicitação é considerada "Atrasada/Esquecida" se estiver com status PENDENTE por mais de 5 dias corridos sem alteração.
