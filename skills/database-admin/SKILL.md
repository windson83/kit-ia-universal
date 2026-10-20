---
name: database-admin
description: "Modela dados e revisa migrations, integridade e consultas lentas."
---

# Dados e migrations

## Aprofundamento por situação

Para uma tarefa substancial, leia [migrations e desempenho](references/migrations-e-desempenho.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Identifique SGBD, versão, volume e padrões reais de consulta. Não proponha índice apenas por intuição.
2. Defina constraints e ownership. Para multi-tenancy, teste isolamento e unicidade no escopo correto.
3. Use expand/contract para alterações incompatíveis; planeje backfill em lotes, locks, compatibilidade e retomada.
4. Diferencie reversão de schema de recuperação de dados; downgrade não recupera automaticamente dado apagado.
5. Compare plano de execução e medições antes/depois em ambiente adequado. Execução destrutiva exige autorização e recuperação verificável.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Schema ou migration, impacto de locks, compatibilidade, recuperação e evidência de integridade/desempenho.
