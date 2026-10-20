---
name: debugger
description: "Investiga causa raiz de erros e aplica correções com reprodução e verificação."
---

# Diagnóstico e correção

## Aprofundamento por situação

Para uma tarefa substancial, leia [investigacao causa raiz](references/investigacao-causa-raiz.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Capture sintoma, versão, ambiente e reprodução mínima. Proteja dados em logs.
2. Formule hipóteses e escolha a observação que as diferencia. Não altere várias causas presumidas de uma vez.
3. Siga o fluxo de dados e a primeira falha relevante, não apenas a última exceção.
4. Aplique correção estreita e teste a regressão quando houver benefício duradouro; não mascare erro com catch vazio.
5. Se não conseguir reproduzir, reporte o que foi eliminado e a menor evidência ainda necessária; não declare causa confirmada.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Causa e evidência, correção, reprodução antes/depois e risco restante.
