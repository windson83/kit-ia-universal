# Contratos de API e Data Ownership

Carregado quando: definindo a interface entre dois componentes, times, ou agentes que vão
trabalhar em paralelo — sempre *antes* de liberar esse trabalho paralelo, nunca depois.

## Checklist de contrato

Ao definir um contrato (API, evento, ou interface entre módulos), especifique o que se
aplica:

```text
- [ ] Endpoint / canal
- [ ] Método
- [ ] Autenticação
- [ ] Autorização
- [ ] Request (schema)
- [ ] Response (schema)
- [ ] Códigos de erro e formato padrão de erro
- [ ] Versionamento
- [ ] Backward compatibility (o que quebra, o que não quebra)
- [ ] Idempotência
- [ ] Paginação
- [ ] Filtros e ordenação
- [ ] Rate limiting
- [ ] Timeout
- [ ] Retry e retry safety (é seguro repetir a chamada?)
- [ ] Correlation ID / trace ID
- [ ] Event version (para eventos/mensagens)
- [ ] Delivery semantics (at-most-once, at-least-once, exactly-once)
- [ ] Ownership — quem é a fonte da verdade desse dado/evento
```

Nem todo item se aplica a todo contrato — mas cada um ausente deve ser uma omissão
deliberada, não um esquecimento. Um contrato incompleto libera trabalho paralelo que volta
incompatível.

## Data ownership

Para todo dado compartilhado entre componentes, times ou serviços, responda:

```text
Quem cria o dado?
Quem tem permissão de alterar?
Quem é a fonte da verdade (source of truth)?
Quem só consome (read-only)?
Como a sincronização acontece, se houver múltiplas cópias?
Qual o modelo de consistência (forte, eventual)?
Quem pode excluir?
Qual a política de retenção?
```

O erro mais comum aqui é dois componentes acreditando, cada um, que são a fonte da
verdade do mesmo dado. Se a resposta não é óbvia e única, isso é uma decisão de
arquitetura que merece um ADR curto, não uma suposição implícita.
