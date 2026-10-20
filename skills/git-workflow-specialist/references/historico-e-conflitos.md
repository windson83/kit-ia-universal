# Histórico, conflitos e publicação

## Estado antes da ação

Confirme raiz do repositório, branch, status staged/unstaged, remoto e upstream. Não assuma que pasta é Git. Em clone raso, certas referências não existem localmente; investigue antes de afirmar divergência. Evite ler ou registrar tokens de URLs remotas.

Escolha operação pelo resultado desejado: organizar mudanças locais, continuar branch, atualizar a partir da base ou revisar PR. Preserve alterações alheias. Não use stash, reset ou clean como passo invisível de conveniência.

## Commits e integração

Inclua apenas arquivos do objetivo autorizado. Leia o diff staged antes de criar commit e exclua credenciais/temporários. Commit pequeno deve ser coerente e testável, não fragmentado só por tipo de arquivo. Mensagem informa a mudança e motivo.

Merge preserva o grafo; rebase reescreve commits. Escolha conforme convenção e compartilhamento da branch. Não force push para “resolver” rejeição sem entender a divergência. Se reescrita compartilhada for explicitamente autorizada, valide a referência remota esperada e use proteção apropriada contra perda de atualizações.

## Conflitos

Leia base comum e intenção de ambos os lados. Resolva sem escolher tudo por `ours`/`theirs` quando isso perder comportamento. Para schema, configuração ou lockfile, use o gerador e ferramentas do projeto quando necessário. Verifique marcadores restantes e execute o teste de integração relevante.

Se o conflito revelar requisito incompatível, conclua as partes independentes e exponha a decisão faltante. Não invente prioridade de negócio para apagar um lado.

## PR e envio

Descrição apresenta problema, comportamento final e validação. Mostre impactos de migração ou configuração. URL e branch devem ser verificadas antes de publicar. Publicar, enviar comentário e criar repositório exigem escopo do usuário; preparar arquivos localmente não pressupõe esses efeitos externos.

## Recuperação e entrega

Antes de operação que altera histórico, conheça a referência de retorno. Reflog ajuda recuperar referência, mas não substitui preservação de arquivos não versionados. Informe branch/commits/PR realmente criados, estado do envio e trabalho local restante. Nunca confunda commit local com conteúdo já disponível no remoto.
