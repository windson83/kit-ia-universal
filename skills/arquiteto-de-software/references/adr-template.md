# Template de ADR (Architecture Decision Record)

Carregado quando: a decisão em jogo é relevante o suficiente para registrar — troca de
tecnologia, mudança estrutural, ou qualquer decisão que outra pessoa vai questionar depois.

## Estados

```text
Proposto     — em avaliação, ainda não aprovado
Aceito       — decisão em vigor
Rejeitado    — avaliado e descartado (registre por quê; evita reavaliar o mesmo caminho)
Substituído  — estava em vigor, foi trocado por outro ADR
```

Nunca altere silenciosamente uma decisão antiga. Quando uma decisão muda:

- o ADR novo declara `## Substitui: ADR-XXX`
- o ADR antigo é editado só para atualizar `Status: Substituído` e `Substituído por: ADR-YYY`
  — o conteúdo histórico da decisão antiga permanece intacto

## Template completo

```markdown
# ADR-XXX — Título

## Status
Proposto | Aceito | Rejeitado | Substituído

## Data

## Owner

## Decisores

## Confiança
Alta | Média | Baixa — o quanto essa decisão se apoia em evidência real vs. julgamento

## Contexto
Situação e forças em jogo (prazo, escala, time, custo, restrições já existentes).

## Problema
O que precisa ser decidido, em uma frase sem ambiguidade.

## Drivers arquiteturais
Quality attributes que mais pesam nessa decisão específica (ver quality-attributes.md).

## Restrições
O que não pode mudar (orçamento, prazo, stack já fixada, contrato já assinado).

## Quality Attributes relevantes
Lista curta, só os que este ADR de fato move a agulha.

## Opções consideradas
Cada opção com sua avaliação nas dimensões que importam para o caso (ver trade-offs abaixo).

## Trade-offs
O raciocínio real — por que a opção escolhida venceu, não só "é melhor".

## Decisão
O que foi decidido, de forma direta.

## Justificativa
Por que essa decisão resolve o problema declarado, ligando de volta aos drivers.

## Consequências positivas

## Consequências negativas
Toda decisão real tem custo. Se essa lista está vazia, a análise não foi honesta.

## Riscos

## Mitigações

## Evidências / POCs
Links ou resumo de qualquer prova de conceito que sustente a decisão.

## Implementação
Passos de alto nível, não o código em si.

## Migração
Como sair do estado atual para o proposto (ver production-readiness.md).

## Rollback
Como desfazer se a decisão se provar errada, e o que fica perdido se não for 100% reversível.

## Observabilidade
Como saberemos que essa decisão está funcionando na prática depois de implementada.

## Revisar quando
Gatilho concreto para reabrir esta decisão (ex: "quando passar de 50 req/s" — não "no futuro").

## Substitui
ADR-XXX, se aplicável.

## Substituído por
ADR-YYY, se aplicável.

## Referências
Documentação oficial, RFC, ou material consultado — com data de consulta se a informação
pode mudar (versão, preço, limite de serviço).
```

## Proporcionalidade

Uma decisão pequena (ex: nome de uma coluna, escolha entre duas libs equivalentes e já
usadas no projeto) não precisa preencher todas as seções — use só Status/Contexto/Decisão/
Justificativa. Reserve o template completo para decisões que:

- são caras de reverter;
- afetam múltiplos componentes ou times;
- introduzem tecnologia nova no stack;
- têm risco de segurança, disponibilidade ou dado real.

Nunca transforme uma decisão trivial em documento de duas páginas — isso ensina o time a
ignorar ADRs.
