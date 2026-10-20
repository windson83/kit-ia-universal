---
name: security-auditor
description: "Audita autorização, entradas, sessões, dependências e exposição de dados em aplicações."
---

# Segurança de aplicação

## Aprofundamento por situação

Para uma tarefa substancial, leia [auditoria appsec](references/auditoria-appsec.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Defina escopo, ativos e fronteiras de confiança. Siga o caminho da entrada até o uso sensível.
2. Verifique autorização por objeto/tenant, sessões, injeção, SSRF, upload e saída contextual contra XSS.
3. Para dependências, confirme versão e advisory oficial; versão antiga isoladamente não prova vulnerabilidade explorável.
4. Demonstre pré-condições e impacto com evidência local. Não exponha segredos nem execute exploração externa sem escopo autorizado.
5. Ordene achados por impacto e probabilidade, com correção e como verificar. Diferencie hipótese de falha confirmada.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Achados com arquivo/linha, pré-condição, impacto, evidência, severidade, remediação e lacunas da análise.
