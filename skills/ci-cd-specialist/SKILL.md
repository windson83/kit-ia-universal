---
name: ci-cd-specialist
description: "Cria e depura pipelines com permissões mínimas e validação de release."
---

# Integração e entrega contínuas

## Aprofundamento por situação

Para uma tarefa substancial, leia [pipelines confiaveis](references/pipelines-confiaveis.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Inspecione a plataforma e os gatilhos reais. Use sintaxe e versões verificadas na documentação oficial quando necessário.
2. Separe verificações independentes e dependências de release. Não obrigue uma ordem serial que só aumenta latência.
3. Minimize permissões e não disponibilize segredos em código não confiável de forks/PRs. Revise runners e contexto de execução.
4. Cache deve ter chave coerente com lockfile e runtime; cache não substitui artefato imutável de release.
5. Faça deploy depender dos gates relevantes e ambiente correto. Use timeout, controle de concorrência e credenciais temporárias quando disponíveis.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Workflow, gatilhos/permissões, dependências entre jobs, validação e limites do teste local.
