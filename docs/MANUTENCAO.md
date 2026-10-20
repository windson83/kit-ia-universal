# Manutenção

A fonte operacional é `skills/`, acompanhada de `catalogo.json`. Adaptadores são gerados durante instalação; não mantenha uma segunda cópia manual de cada agente.

Para editar uma capacidade, ajuste o procedimento específico, critérios de entrega e referências. Mantenha `SKILL.md` curto, com `name` igual à pasta e `description` como string JSON entre aspas (subconjunto YAML aceito pelo validador). Não fixe modelos ou nomes de ferramentas no núcleo neutro. Evite dependências obrigatórias em skills inexistentes. Use links Markdown relativos para referências.

Depois de uma mudança revisada:

```text
python scripts/kit.py validate --seal
python -m unittest discover -s tests -v
python scripts/kit.py validate
```

`--seal` é operação do mantenedor que recalcula hashes após revisar alterações; não é prova de autenticidade ou assinatura digital. O validador confere o formato estreito de YAML produzido por este kit, arquivos e links; não interpreta todo YAML possível nem certifica comportamento da IA. Para alterar descrições, preserve o formato gerado ou amplie o parser com testes.

Para empacotar, execute `python scripts/package.py`. O ZIP é criado em `releases/` a partir dos arquivos do manifesto, mantendo hierarquia e excluindo caches/temporários. O comando recusa sobrescrever um ZIP existente; use `--output` com outro nome para preservar a versão anterior. Não inclua projetos de teste, backups de usuários ou credenciais. Faça uma instalação em pasta temporária antes de distribuir. Atualize a versão em `README.md` e `catalogo.json` quando publicar uma revisão.

O inventário e os snapshots preservam a origem da versão 2.0.0. As fontes históricas em `docs/origens` não devem ser carregadas como instruções operacionais. A documentação jurídica de apoio exige conferência atual em fontes oficiais em cada caso; não recoloque tabelas anuais sem controle de data e aplicabilidade.

## Teste de uso no modelo

Além dos testes determinísticos, ao adotar uma IA diferente, dê uma tarefa pequena em projeto descartável, selecione uma capacidade e confira se ela leu as referências corretas e distinguiu análise de execução. Em agente sem ferramenta, o resultado esperado é uma orientação honesta sobre a limitação. O pacote não declara equivalência de comportamento entre fornecedores.
