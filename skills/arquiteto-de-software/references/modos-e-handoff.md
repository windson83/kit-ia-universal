# Escolher profundidade e encaminhar arquitetura

## Modos

| Pedido | Entrega suficiente | Consultar |
|---|---|---|
| Decisão reversível local | Recomendação, alternativa e critério | Evidência do projeto |
| Decisão estrutural | Contexto, opções, trade-offs e ADR | Template ADR |
| Sistema novo | Limites, dados, interfaces e atributos críticos | C4 e quality attributes |
| Revisão existente | Achados com evidência, impacto e alternativas | Architecture review |
| Migração | Coexistência, transição, recuperação e validação | Production readiness |
| Integração entre equipes | Contratos e ownership explícitos | API contract checklist |

Não apresente toda a documentação como pré-requisito para uma decisão pequena. Também não reduza migração com dados persistentes a uma escolha de framework.

## Raciocínio arquitetural

Separe requisitos confirmados, restrições, suposições, decisões e questões abertas. Compare a solução atual e pelo menos a alternativa plausível que muda custo/risco; não crie opções artificiais para justificar preferência. Transforme atributos críticos em cenários: carga, operação, condição, resposta e medida, quando houver informação para isso.

Classifique reversibilidade e custo operacional. Se um novo serviço resolve apenas crescimento hipotético, avalie modularidade na arquitetura existente. Para fronteiras distribuídas, explicite latência, falha parcial, consistência e ownership de dados; separar código em serviços não resolve essas questões automaticamente.

Dados compartilhados precisam de autoridade definida. Contrato especifica identidade, schema, erros, idempotência, ordenação e evolução conforme o protocolo. Em migração, confira compatibilidade de versões durante o rollout e como desfazer efeitos de dados; rollback de deploy não desfaz todas as mudanças.

## Handoff utilizável

Entregue decisões propostas/aprovadas com estado correto, componentes e responsáveis por dados, contratos, dependências, sequência de implementação, trabalho que pode coexistir, riscos e validações. Um POC tem pergunta, hipótese e critério observável; “testar escalabilidade” sem carga ou limite não decide nada.

Se faltar capacidade especializada real, descreva a necessidade e impacto. Não invente nome de agente nem trate revisão independente indisponível como razão automática para interromper uma tarefa simples. Quando houver delegação autorizada, forneça contratos e ownership antes de iniciar frentes simultâneas.
