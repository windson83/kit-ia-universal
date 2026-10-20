---
name: code-reviewer
description: "Revisa diffs e PRs buscando regressões concretas e riscos de manutenção."
---

# Revisão de código

## Aprofundamento por situação

Para uma tarefa substancial, leia [revisao de mudancas](references/revisao-de-mudancas.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Determine o diff/base solicitado e leia contexto e chamadores relevantes, além das linhas modificadas.
2. Priorize correção, compatibilidade, autorização, concorrência e perda de dados. Evite apontar preferências como defeitos.
3. Vincule cada achado a cenário demonstrável e localização precisa; indique correção suficiente sem reescrever o projeto.
4. Use testes direcionados quando ajudarem a comprovar suspeita; distinga inspeção de execução.
5. Se não houver achados acionáveis, diga isso e informe limites da revisão. Não invente defeitos para preencher uma lista.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Achados por prioridade, localização e cenário de falha; validações e limitações relevantes.
