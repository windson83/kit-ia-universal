# Modelagem, migrations e consultas

## Diagnóstico

Identifique SGBD e versão, schema, volume, taxa de escrita, padrões de consulta e disponibilidade exigida. Relacione entidades a invariantes: unicidade, pertencimento, estados válidos e referências. Defina representação de dinheiro, timezone e exclusão/retencão conforme o domínio.

## Alteração de schema

Classifique a mudança por compatibilidade de leitores e escritores antigos. Em rollout gradual, considere:

1. Expandir schema com campos/estruturas compatíveis.
2. Publicar código que conviva com os formatos necessários.
3. Fazer backfill limitado, observável, retomável e com carga controlada.
4. Verificar integridade e completar a mudança dos consumidores.
5. Remover formato antigo somente após a janela de recuperação.

Esta sequência não é obrigatória para migration pequena em banco descartável. Em produção, confirme comportamento de DDL, transações e índices na versão real do SGBD. Não suponha que adicionar default ou índice é operação sem lock.

Para backfill, estabeleça chave de progresso, limites por lote, condições de retomada e concorrência com escritas atuais. Teste interrupção no meio. Preserve dados inválidos para análise em vez de convertê-los silenciosamente.

## Recuperação

Um `down` que recria coluna não recupera seu conteúdo. Diga se é rollback de código, reversão de schema, restauração de backup ou correção compensatória. Inclua RPO/RTO somente quando definidos. Verifique restore quando ele for o mecanismo de recuperação exigido; arquivo de backup existente não prova restaurabilidade.

Não execute exclusão, truncamento ou mudança de ambiente por inferência. Analise o plano e o impacto antes de pedir autorização para uma operação destrutiva, quando necessária.

## Otimização com evidência

Parta da query exata e dos parâmetros representativos. Analise plano, seletividade, cardinalidade, sort, joins e leituras. EXPLAIN ANALYZE pode executar a consulta; avalie efeitos e custo antes de rodá-lo. Compare ambiente e cache para evitar conclusão enganosa.

Índice composto depende de filtros e ordenação; também tem custo de escrita e armazenamento. Verifique paginação, N+1 e excesso de dados transferidos antes de criar índices em massa. Não imponha normalização ou desnormalização sem considerar consultas e integridade.

## Entrega verificável

```text
Mudança e motivo:
Compatibilidade de aplicações:
Invariantes e constraints:
Lock/carga esperados e como foram verificados:
Backfill e retomada:
Recuperação e limites:
Comandos executados, ambiente e resultados:
```

Para consulta lenta, acrescente evidência antes/depois e custo introduzido. Se não houver acesso ao banco, diferencie análise estática de desempenho medido.
