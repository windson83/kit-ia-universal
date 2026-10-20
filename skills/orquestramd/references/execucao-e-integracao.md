# Execução, delegação e integração

## Descobrir e dimensionar

Leia objetivo e estado atual. Descubra capacidades pelo catálogo real do ambiente, começando por nome/descrição. Skill é procedimento; agente é executor com contexto próprio; ferramenta realiza operação. A existência de um não implica os demais.

Tarefa simples pode seguir diretamente. Para trabalho composto, registre entregáveis, dependências e critérios. Use grafo quando houver paralelismo e caminho crítico que mereçam controle; não crie cerimônia para edição pontual.

## Pacote de trabalho

```text
Objetivo e resultado observável:
Contexto mínimo e decisões já tomadas:
Escopo de arquivos/artefatos sob responsabilidade:
Entradas, contratos e dependências:
Critérios de aceite e validação:
Restrições e autorização:
Forma de integração e evidência esperada:
```

Em delegação autorizada, informe que o executor não está sozinho, deve preservar alterações alheias e não pode reverter trabalho fora da própria tarefa. Defina dono para arquivos compartilhados. Paralelize apenas frentes suficientemente independentes; contrato indefinido vira retrabalho.

## Acompanhar sem simular

Use estados como aguardando dependência, em execução, em revisão e concluído quando ajudarem. Acompanhe evidência e artefato, não só mensagem de sucesso. Se não houver agentes ou autorização de delegação, execute sequencialmente; nunca invente que especialistas trabalharam em paralelo.

Guarde registro curto de decisões, responsáveis, bloqueios e validações. Não carregue todas as skills em cada contexto. Encaminhe só as entradas que alteram a decisão do executor.

## Integrar e retrabalhar

Leia entregas e valide interfaces, comportamento e conflitos. Um teste local de módulo não prova fluxo integrado. Ao falhar, determine causa/dono, aplique correção estreita e reexecute gates afetados. Repetição sem nova evidência não é progresso; reformule hipótese ou delimite dependência externa.

## Encerrar

Compare o resultado com o objetivo original, incluindo documentação/operação quando necessárias. Não marque completo com trabalho obrigatório aberto. Entrega informa realizado, integrado, verificado, limitações e o próximo passo concreto se houver bloqueio externo. Não confunda instrução preparada, ação executada e resultado confirmado.
