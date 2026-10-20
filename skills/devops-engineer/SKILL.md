---
name: devops-engineer
description: "Configura infraestrutura e operação, release, observabilidade e recuperação."
---

# Operação e infraestrutura

## Aprofundamento por situação

Para uma tarefa substancial, leia [operacao e recuperacao](references/operacao-e-recuperacao.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Identifique ambiente, IaC, dependências e limites da autorização. Separe plano, validação local e aplicação no ambiente.
2. Use artefatos reprodutíveis e configuração versionada sem segredos. Documente variáveis obrigatórias.
3. Defina health/readiness, métricas, alertas acionáveis e runbook proporcional ao serviço.
4. Planeje rollout, rollback e compatibilidade de dados; teste restore quando recuperação fizer parte da tarefa.
5. Em incidente, priorize mitigação autorizada com evidência e preserve dados para diagnóstico. Mudança em produção segue autorização do usuário.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Plano ou mudança aplicada, ambiente, validação, operação e procedimento de recuperação.
