# Architecture Review — dimensões e formato de achado

Carregado quando: o pedido é revisar uma arquitetura ou sistema já existente, não desenhar
um novo.

## Dimensões a avaliar

Boundaries, coupling, cohesion, data ownership, dependencies, single points of failure,
scalability, security, observability, operability, maintainability, deployability,
testability, cost, complexity, technical debt.

Não avalie todas com o mesmo peso em toda revisão — priorize as dimensões que a *queixa*
ou o *objetivo* da revisão sugerem. Uma revisão motivada por lentidão pega pesado em
scalability/cost/complexity; uma motivada por incidente recorrente pega pesado em
single points of failure/observability/operability.

## Formato de achado

Para cada problema relevante encontrado, retorne nesse formato — nunca só a observação
solta:

```markdown
### Achado: [nome curto]

**Problema:** o que está errado, especificamente.

**Evidência:** o que no código/sistema real confirma isso — não "parece que", mostre onde.

**Impacto:** o que isso custa hoje, ou vai custar, em termos concretos.

**Severidade:** Crítica | Alta | Média | Baixa

**Alternativa:** o que fazer em vez disso.

**Custo da correção:** esforço estimado para resolver — ajuda a priorizar.

**Prioridade:** onde isso entra na fila em relação aos outros achados.
```

## Saída consolidada

```markdown
## Revisão de arquitetura: [sistema/escopo]

### Resumo
[1-3 frases: estado geral, e se há algum risco que precisa de ação imediata]

### Achados
[um bloco por achado, no formato acima, ordenados por severidade]

### O que já está bem construído
[não pule isso — uma revisão que só lista problemas sem contexto do que funciona bem
não ajuda quem vai decidir prioridade]
```

Nunca liste um achado sem evidência real extraída do sistema. Se a suspeita não pôde ser
confirmada, registre como "questão em aberto — precisa de investigação", não como achado.
