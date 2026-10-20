---
name: backend-dev
description: "Implementa APIs, regras de negócio, autorização e integrações de servidor."
---

# Desenvolvimento backend

## Aprofundamento por situação

Para uma tarefa substancial, leia [engenharia backend](references/engenharia-backend.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Leia rotas, modelos, contratos e padrões de erros existentes. Preserve compatibilidade pública ou explicite a migração.
2. Valide entradas na fronteira e autorização por recurso e tenant. Não confunda autenticação com autorização.
3. Defina transações, concorrência, unicidade e idempotência nas operações que modificam estado.
4. Nas integrações, estabeleça timeout e cancelamento; limite retries a falhas transitórias e operações seguras. Evite retry em cascata.
5. Use consultas parametrizadas, paginação e logs sem segredos. Teste regra crítica e falhas externas com doubles controlados.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Comportamento entregue, contratos alterados, arquivos, testes executados e implicações de migração.
