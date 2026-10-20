---
name: arquiteto-de-software
description: "Define arquitetura, ADRs, contratos entre componentes e planos de migração."
---

# Arquitetura de software

## Aprofundamento por situação

Para uma tarefa substancial, leia [modos e handoff](references/modos-e-handoff.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Inspecione código, restrições de operação e requisitos antes de escolher stack. Compare alternativas incluindo manter a solução atual.
2. Defina limites dos módulos, fonte da verdade dos dados, fronteiras de confiança e modos de falha.
3. Especifique atributos críticos com metas verificáveis. Justifique complexidade por requisito concreto e custo operacional.
4. Defina contratos antes do trabalho simultâneo dependente: autenticação, payloads, erros, versionamento e idempotência.
5. Registre decisões relevantes em ADR; para migração, detalhe coexistência, backfill, validação, corte e reversão. Não marque proposta como aprovada.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Decisão e alternativas, diagrama proporcional ao sistema, contratos, riscos, plano de implementação e validação.

## Referências sob demanda

Leia somente a referência pertinente ao modo de trabalho:

- [references/production-readiness.md](references/production-readiness.md)
- [references/c4-guidelines.md](references/c4-guidelines.md)
- [references/quality-attributes.md](references/quality-attributes.md)
- [references/architecture-review.md](references/architecture-review.md)
- [references/api-contract-checklist.md](references/api-contract-checklist.md)
- [references/adr-template.md](references/adr-template.md)
