---
name: frontend-dev
description: "Implementa interfaces e fluxos acessíveis integrados a APIs e ao design system."
---

# Desenvolvimento frontend

## Aprofundamento por situação

Para uma tarefa substancial, leia [fluxos e qualidade](references/fluxos-e-qualidade.md) antes de decidir a abordagem. O guia detalha modos de atuação, decisões, cenários de falha e evidências de conclusão. Para ajuste pontual, use apenas as partes pertinentes; não imponha o fluxo inteiro a uma mudança simples.

## Procedimento

1. Inspecione framework, componentes e gerenciador de pacotes. Preserve o design system e contratos existentes.
2. Modele loading, vazio, sucesso, erro, permissão negada e retomada. Evite estados impossíveis e dados antigos após troca de contexto.
3. Use semântica HTML, rótulos, foco e teclado. Valide navegação e formulários sem mouse.
4. Trate cache, cancelamento e falhas de rede; não armazene segredos no cliente.
5. Verifique fluxos e tamanhos de tela representativos. Declare quando a verificação visual ou browser não estiver disponível.

## Condições de execução

Use somente ferramentas realmente disponíveis e respeite a autorização e as instruções do ambiente. Não simule comandos, consultas ou delegações. Em edição compartilhada, preserve mudanças de outros executores. Registre validações realizadas e limitações concretas. Consulta ou sugestão não autoriza publicação ou alteração externa.

## Entrega

Fluxos implementados, estados, acessibilidade, verificações realizadas e limitações observadas.
