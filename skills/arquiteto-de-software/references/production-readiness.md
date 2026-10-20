# Production Readiness

Carregado quando: a arquitetura vai (ou já está) em produção — cobre segurança,
observabilidade, failure modes, migração/rollback, POC/spike, e validação contínua.

## Security by design

Considere, quando relevante: autenticação, autorização, gestão de segredos, criptografia
em trânsito e em repouso, least privilege, trust boundaries, dados sensíveis/PII, audit
logs, isolamento de tenant, superfície de ataque, risco de dependência.

Se a arquitetura apresenta risco de segurança significativo, isso é uma **capacidade
necessária** a sinalizar (segurança de aplicação ou de infraestrutura, dependendo do
caso) — não algo para decidir sozinho sem revisão especializada. Ver a seção de
descoberta de capacidades no `SKILL.md`.

## Data flow e trust boundaries

Quando segurança, privacidade ou integrações externas forem relevantes, documente o
caminho do dado: entrada → processamento → armazenamento → transmissão → saída →
retenção → deleção. Identifique onde o dado cruza um trust boundary (ex: sai do seu
controle e vai para um terceiro).

## Observabilidade

Arquitetura de produção deve responder, antes de ser considerada pronta:

```text
Como saberemos que o sistema está saudável?
Como detectaremos degradação antes que o usuário reclame?
Como encontraremos rapidamente a causa de uma falha?
```

Considere: logs, metrics, traces, correlation ID, dashboards, alertas, health checks,
SLIs, SLOs. Defina os que a resposta às três perguntas acima realmente exige — não uma
lista completa por padrão.

## Failure modes

Para os pontos que realmente importam no sistema em questão, pergunte:

```text
O que acontece se o banco cair?
O que acontece se uma API externa fica indisponível?
O que acontece se uma fila para?
O que acontece em timeout?
O que acontece com mensagens duplicadas?
O que acontece em processamento parcial?
O que acontece durante o deploy?
O que acontece se uma instância morre?
```

Considere mecanismos como timeout, retry com backoff exponencial, circuit breaker,
dead-letter queue, idempotência, graceful degradation — **só onde o failure mode
correspondente é real**. Não adicione esses mecanismos por precaução genérica.

## Migração e rollback

Para mudança estrutural em sistema existente, nunca descreva só o estado final. Responda:

```text
Como migrar do estado atual para o proposto?
Existe compatibilidade durante a transição, ou é um corte seco?
Deploy pode ser gradual?
Existe feature flag pra isolar o risco?
Existe rollback? Ele cobre o banco de dados também?
Há alguma etapa destrutiva/irreversível na migração?
Como os dados ficam protegidos durante a transição?
```

Padrões a considerar quando necessário — nunca introduza sem necessidade real:
expand/migrate/contract, APIs backward-compatible, dual-read, dual-write, blue/green,
canary, feature flags.

## POC / Spike

Uma POC nunca é "fazer POC de X". Ela responde uma pergunta específica com critério de
sucesso mensurável.

```text
Errado:  fazer POC de Kafka
Certo:   validar se a solução processa 15.000 eventos/minuto mantendo p95 < 2s,
         sem perda de eventos
```

Template:

```markdown
## POC: [nome]

**Hipótese:**
**Métrica:**
**Critério de sucesso:**
**Critério de falha:**
**Tempo máximo:**
**Resultado:**
**Decisão resultante:**
```

## Architecture fitness

Defina como as premissas arquiteturais serão validadas continuamente, não só na hora do
desenho. Quando aplicável: architecture tests (regras de dependência entre módulos),
contract tests, testes de performance/carga, testes de segurança, checks de
observabilidade, limites de custo. Quando possível, transforme uma decisão arquitetural
importante numa verificação executável (ex: um teste que falha se um módulo importar
algo que não devia) em vez de depender só de revisão manual futura.
