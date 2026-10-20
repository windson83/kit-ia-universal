# Decisões e execução de backend

## Escolher o modo

- Endpoint/regra nova: parta do contrato e das invariantes do domínio; implemente uma fatia vertical e valide sua fronteira.
- Integração: investigue entrega, ordenação, duplicação e indisponibilidade do provedor antes de escolher retries.
- Correção: reproduza a falha e preserve o comportamento público fora do defeito.
- Evolução de API: identifique consumidores, política de versão e janela de coexistência.

## Contrato antes de implementação

Para cada operação relevante, registre método/rota ou mensagem, identidade do chamador, autorização sobre o recurso, esquema de entrada, respostas, códigos de erro e efeitos persistentes. Defina formato e limites de paginação; em paginação por cursor, use ordenação determinística. Não exponha stack traces ao cliente.

Validação sintática não substitui regra de negócio. A existência do identificador não autoriza acesso: obtenha o recurso no escopo do usuário/tenant ou aplique verificação equivalente. Teste leitura e escrita cruzadas entre tenants. Preserve serialização de datas, precisão monetária e compatibilidade com clientes reais.

## Consistência e efeitos externos

Defina a unidade transacional e as invariantes garantidas por constraints. Validação prévia sem constraint não evita corrida. Em leitura-modificação-escrita, avalie controle otimista, locks ou atualização condicional pelo custo e contenção esperados.

Para operação repetível, determine chave de idempotência, escopo, expiração e comportamento quando a mesma chave recebe payload diferente. O resultado precisa sobreviver ao retry e à concorrência relevante. Não declare “exactly once” apenas porque há fila. Quando evento externo e gravação local precisam ser coordenados, considere outbox e deduplicação, sem introduzir infraestrutura desnecessária.

## Integrações e observabilidade

Estabeleça timeout total e por tentativa. Retry tem limite, backoff e jitter quando apropriado; não repita efeito não idempotente sem proteção. Considere rate limit e indisponibilidade parcial. Nos webhooks, valide assinatura, política contra replay e duplicatas conforme o protocolo real.

Registre identificação da operação e duração sem tokens, credenciais ou payload pessoal desnecessário. Use métricas que mostrem erro, latência e saturação do caminho alterado. Redação de dados sensíveis deve preservar informação diagnóstica útil.

## Exemplo de aceite: criação de pedido

| Cenário | Evidência esperada |
|---|---|
| Payload válido | Pedido e itens consistentes; resposta conforme contrato |
| Mesmo pedido reenviado | Política de idempotência observada, sem cobrança dupla |
| Duas requisições concorrentes | Invariantes de estoque/total preservadas |
| Recurso de outro tenant | Acesso negado sem revelar dados do proprietário |
| Provedor falha após aceite | Estado recuperável e retomada definida |

## Conclusão

Entregue comportamento, arquivos, alterações de contrato e comando/resultado das verificações. Indique migrações, configuração, compatibilidade e o que não foi testado. Se a tarefa for só revisão, entregue os achados e não implemente mudanças de escopo adicional.
