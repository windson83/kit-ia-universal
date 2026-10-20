# Investigação e correção de falhas

## Montar a reprodução

Registre sintoma, esperado, início, ambiente e mudanças correlatas. Capture a primeira exceção relevante e contexto; a última linha do log pode ser consequência. Reduza a entrada e dependências sem remover a condição que causa o erro.

Se a reprodução local não existir, use evidência permitida: logs mascarados, teste de contrato, histórico da mudança ou comparação de configuração. Não peça credenciais para compensar ferramenta ausente. Registre o grau de confiança e a evidência que falta.

## Escolher uma observação discriminante

Mantenha uma lista curta de hipóteses. Para cada uma: qual observação a confirmaria e qual a refutaria? Exemplo: resposta antiga sobrescreve seleção nova versus servidor entrega dado errado. Um log de correlation ID e contexto no recebimento distingue as duas causas melhor que alterar o timeout aleatoriamente.

| Sintoma | Investigar primeiro |
|---|---|
| Só falha no CI | Runtime, sistema, ordem, locale, dados e permissões |
| Falha intermitente | Concorrência, relógio, recursos, rede e estado compartilhado |
| Lentidão | Distribuição de latência e gargalo medido, não só média |
| Falha após release | Diferença de configuração, schema e compatibilidade |
| Crash sem log | Inicialização, sinais, limite de memória e canal de erro |

## Aplicar e verificar

Mude o mecanismo da causa, não só o sintoma. Não esconda erro, aumente timeout ou desative assertion sem explicar por que isso corrige o requisito. Preserve comportamento adjacente. Introduza teste de regressão quando representar risco real e não uma cópia da implementação.

Reexecute reprodução e testes afetados. Se uma primeira hipótese falhar, registre o que foi refutado e escolha outra observação; evite acumular patches especulativos. Remova instrumentação temporária que exponha dados ou degrade operação. Não reverta mudanças alheias enquanto investiga.

## Entrega

Informe causa com evidência, mudanças, resultado antes/depois, verificações e riscos. Se não houve confirmação, diga “hipótese” e delimite a próxima evidência necessária. Em incidente, diferencie mitigação temporária de correção permanente e não declare uma como a outra.
