# Contribuir

As capacidades operacionais ficam em `skills/`; adaptadores são derivados delas. Cada mudança deve ter objetivo, procedimento específico, modos relevantes e evidência de conclusão. A descrição ajuda selecionar a capacidade sem carregar todo seu conteúdo.

Para mudança relevante, acrescente ou revise o guia em `references/` e mantenha seu link no `SKILL.md`. Não aumente texto apenas para tornar uma skill maior: detalhe as decisões que ela não pode tomar corretamente só com orientações genéricas. Preserve a autorização do usuário e adapte o fluxo à complexidade.

Antes de propor uma alteração:

```text
python scripts/kit.py validate --seal
python -m unittest discover -s tests -v
python scripts/kit.py validate
```

Registre no PR o comportamento alterado, exemplo de uso e validação. Não inclua segredos, dados pessoais, caches ou pacotes ZIP. O CI valida três sistemas operacionais em Python 3.10 e 3.14. Procedimentos jurídicos exigem fontes oficiais verificáveis no caso concreto; não fixe limites anuais como se fossem universais.
