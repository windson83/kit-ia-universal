# Revisão de mudanças

## Delimitar a base

Use a referência, PR ou diff solicitado. Sem alvo explícito, inspecione estado local e explique qual conjunto está revisando; se não houver mudança, peça o alvo. Diferencie arquivos novos, mudanças staged e unstaged, sem editar ou descartar trabalho do autor.

Leia o comportamento anterior e o novo, chamadores e testes relacionados. Bugs de integração podem depender de linhas não alteradas. Não limite o raciocínio às linhas verdes, mas vincule o achado à mudança e a uma localização precisa.

## Perguntas por tipo de mudança

| Tipo | Verificar |
|---|---|
| API/schema | Clientes antigos, null/default, serialização, migração |
| Estado/async | Corrida, cancelamento, duplicação, resultado fora de ordem |
| Persistência | Atomicidade, rollback de dados, concorrência e restrições |
| Permissão | Ownership, tenant, caminhos alternativos e falha fechada |
| Erro/retry | Perda de erro, efeito repetido e recuperação |
| UI | Estados antes/depois, teclado e operação central |

Estilo e abstração só viram achado quando trazem problema de manutenção concreto no escopo. Não solicite refatoração ampla para resolver gosto pessoal. Falta de teste é acionável quando há risco ou comportamento específico não coberto.

## Comprovar sem exagero

Para uma suspeita, descreva entrada, fluxo e resultado incorreto. Consulte contrato e testes antes de concluir. Execute verificação mínima quando ela resolver a dúvida; não afirme que teste passou por ter lido seu código. Se falta evidência, faça pergunta objetiva ou classifique a observação como hipótese.

Prioridade: P0 para impedimento imediato de operação ou dano amplo incondicional; P1 para falha grave em condição realista; P2 para defeito relevante de alcance menor; P3 para melhoria pequena com efeito concreto. Ajuste à convenção do repositório quando existente.

## Exemplo de achado

```text
[P1] Restrinja a consulta ao tenant do solicitante
Quando um usuário fornece o ID de outro tenant, a busca por ID global
devolve o recurso antes de qualquer checagem de ownership. Isso permite
ler os dados alheios. Filtre pelo tenant autorizado e teste duas contas.
Local: caminho verificado e linhas mínimas pertinentes.
```

## Entregar

Liste achados por prioridade e informe validações relevantes. Diferencie bloqueio demonstrado de sugestão. Se não encontrar achados, entregue esse resultado com limites; não preencha tabelas vazias nem invente problema. Uma revisão não autoriza merge, push ou publicação.
