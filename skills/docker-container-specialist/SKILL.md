---
name: docker-container-specialist
description: "Cria e revisa Dockerfiles e Compose com builds reproduzíveis e operação verificável."
---

# Containers

## Aprofundamento por situação

Para uma tarefa substancial, leia [build e runtime](references/build-e-runtime.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Identifique runtime, arquitetura, dependências nativas e requisitos antes de escolher base. Alpine não é escolha obrigatória.
2. Separe build e runtime quando útil; use lockfiles, contexto mínimo e .dockerignore.
3. Não incorpore credenciais em ARG, ENV ou camadas. Use secrets de build/runtime oferecidos pelo ambiente.
4. Configure usuário, sinais de encerramento, filesystem e healthcheck conforme a aplicação; não simule saúde com comando sempre verdadeiro.
5. Valide configuração, build e comportamento quando Docker estiver disponível. depends_on não substitui tolerância a indisponibilidade em runtime.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Arquivos, build/configuração verificados, execução, requisitos de runtime e limitações.
