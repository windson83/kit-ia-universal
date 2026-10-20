---
name: orquestramd
description: "Coordena tarefas com dependências e capacidades disponíveis, em execução individual ou com agentes."
---

# Coordenação de trabalho

## Aprofundamento por situação

Para uma tarefa substancial, leia [execucao e integracao](references/execucao-e-integracao.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Descubra capacidades pelo catálogo do ambiente, lendo primeiro nome e descrição. Não suponha agentes, conectores ou ferramentas instalados.
2. Decomponha só o necessário. Defina entregáveis, dependências e critérios observáveis; tarefa pequena pode ser executada diretamente.
3. Delegue somente se o usuário e as regras do ambiente permitirem. Sem delegação disponível, execute as mesmas frentes sequencialmente.
4. Antes de paralelizar, defina contrato e ownership de arquivos. Informe a cada executor que não está sozinho e que deve preservar mudanças alheias.
5. Integre entregas e valide comportamento; retorno de um agente não é prova de conclusão. Limite retrabalho por evidência e peça dado externo apenas quando indispensável.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Objetivo, trabalho concluído, integração e evidências, pendências concretas e próximos passos necessários.

## Referências sob demanda

Leia somente a referência pertinente ao modo de trabalho:

- [references/workflow-patterns.md](references/workflow-patterns.md)
- [references/delegation-contract.md](references/delegation-contract.md)
- [references/capability-discovery.md](references/capability-discovery.md)
