# Descoberta e critérios de aceite

## Calibrar a entrega

Pedido pequeno e claro pede critérios e execução direta. Feature ambígua pede descoberta curta. Novo produto ou mudança entre equipes pede visão de escopo, jornadas, prioridades, dependências e plano de validação. Não transforme falta de detalhe cosmético em bloqueio do projeto.

## Investigar o problema

Leia produto/documentos existentes e identifique papel, tarefa, gatilho, frequência, dor e resultado desejado. Diferencie pedido (“adicionar botão”) de necessidade (“reduzir tempo para aprovar”). Se houver métrica, registre linha de base e forma de medir; não invente números de negócio.

Separe: confirmado por fonte; premissa reversível; decisão pendente que muda a solução; exclusão de escopo. Faça perguntas só para decisões de alto impacto sem evidência disponível. Avance em trabalho independente enquanto essas respostas não chegam.

## Detalhar a jornada

Considere permissões e os estados reais: primeira utilização, ausência de dados, erro, recuperação, operação repetida e abandono. Descreva regras e invariantes, não apenas telas. Em fluxos com várias funções, diga quem inicia, quem decide, quem pode reverter e o que precisa de histórico.

Escreva critérios como observação verificável, usando Dado/Quando/Então quando ajudar:

```text
Dado um pedido pendente ao qual o aprovador tem acesso,
quando ele aprova e a gravação é bem-sucedida,
então o pedido passa a aprovado e registra autor e instante.
Se outra pessoa já decidiu, a interface informa o estado atual
e não sobrescreve silenciosamente a decisão anterior.
```

Não confunda critério com decisão técnica prematura (“usar Redis”). Requisito de latência, retenção, auditoria ou acessibilidade deve indicar contexto, limite e forma de verificar, quando houver base para defini-los.

## Priorizar e entregar

Organize o que viabiliza a jornada central primeiro e explicite dependências. Use fatias que entregam valor verificável; não prometa cronograma sem informação de capacidade. Registre trade-off de escopo quando prazo e qualidade não couberem juntos.

Entrega sugerida: problema e público; resultado; escopo/exclusões; jornada; regras; critérios; riscos e decisões pendentes. Para PRD completo, acrescente hipótese de valor, métrica, lançamento e acompanhamento sem exigir outra skill inexistente. Conclua quando quem implementa consegue distinguir aceite de rejeição e conhece as decisões ainda abertas.
