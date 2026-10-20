# Instalação e atualização

Para baixar diretamente do GitHub e instalar pelo gerenciador de skills, veja [PUBLICACAO-GIT.md](PUBLICACAO-GIT.md). Este guia descreve o instalador Python próprio e seu mecanismo de backup.

## Pré-requisitos

Python 3.10+ disponível como `python` no Windows ou `python3` no Linux/macOS. Verifique com `python --version`. Use uma pasta de projeto à qual tenha acesso. Nenhum pacote, rede, chave de API ou permissão administrativa é necessário para instalar. A IA de destino deve existir separadamente.

Nos exemplos, execute a partir da pasta `KIT-IA-UNIVERSAL`. Linux/macOS: substitua `python` por `python3` e use o caminho real do seu projeto.

## Codex — projeto

```text
python scripts/kit.py install --profile codex --dest "D:/projetos/app"
python scripts/kit.py install --profile codex --dest "D:/projetos/app" --apply
```

Grava `.agents/skills/<id>/SKILL.md` e recursos. Não cria agentes nativos Codex nem altera configurações do modelo. Abra nova sessão e peça: “Use a capacidade backend-dev para revisar esta API”. A interface de descoberta depende da versão do aplicativo. Para localização pessoal/global, consulte a documentação da sua versão; esta distribuição usa o caminho de projeto documentado, evitando adivinhar caminhos globais.

## Claude Code — projeto ou pessoal

```text
python scripts/kit.py install --profile claude --dest "D:/projetos/app" --agents --apply
```

Grava `.claude/skills/` e, com `--agents`, `.claude/agents/`. O adaptador pré-carrega a skill correspondente e herda o modelo da sessão. Não fixa Opus/Sonnet/Haiku. Para instalar pessoalmente, use como `--dest` a sua pasta pessoal, por exemplo `C:/Users/SEU-USUARIO`. Isso resulta em `~/.claude/skills` e `~/.claude/agents`.

Abra nova sessão no projeto e peça explicitamente a capacidade ou agente; consulte `/agents` para conferir agentes na sua versão. Não use `claude plugin validate` para validar uma simples pasta de agentes: use o validador deste kit e a descoberta no aplicativo.

## Outras IAs e chat

```text
python scripts/kit.py install --profile generic --dest "D:/exportacao-ia" --apply
```

Leia `D:/exportacao-ia/ia-kit/INSTRUCOES.md`. A exportação contém catálogo e recursos sem metadados específicos de fornecedor. Em uma IA sem acesso a arquivos, anexe o `SKILL.md` da capacidade escolhida e referências necessárias; não envie o acervo inteiro a cada tarefa. Em aplicações com suporte a Agent Skills, escolha o diretório de skills documentado pelo fabricante e copie as pastas de `skills/` para ele. Não presuma instalação automática universal.

## Selecionar apenas algumas capacidades

```text
python scripts/kit.py install --profile codex --dest "D:/projetos/app" --only backend-dev debugger --apply
```

Use os identificadores exatos de `python scripts/kit.py list`. Não duplique aliases históricos.

## Atualizar com preservação

Instalar novamente conteúdo igual não regrava arquivos. Se houver conteúdo diferente no destino, a instalação com `--apply` recusa todos os conflitos antes de gravar arquivos do kit. Revise a simulação e, para substituir explicitamente:

```text
python scripts/kit.py install --profile codex --dest "D:/projetos/app" --apply --update
```

Arquivos substituídos são copiados para `.ia-kit-backups/<data-UTC>/`, conservando o caminho relativo. Arquivos que não pertencem ao plano ficam preservados. O instalador não exclui capacidades antigas ou arquivos extras: isso exige revisão manual. Em falha durante a escrita, tenta restaurar os arquivos que gravou sem apagar alterações concorrentes detectadas. Isso não é uma transação resistente a desligamento abrupto; o backup permanece disponível.

Para restaurar, feche sessões que possam editar o destino, compare o backup com os arquivos atuais e copie apenas os arquivos desejados de volta ao mesmo caminho relativo. Arquivos novos não têm backup anterior. Para remover uma instalação, exclua manualmente apenas as pastas de capacidades do kit que você reconhece; preserve recursos alheios e alterações próprias.

## Atalhos de terminal

Windows: `./install.ps1 list` (se a política local permitir scripts). Linux/macOS: `sh install.sh list`. Ambos repassam os mesmos argumentos ao instalador. O comando Python direto funciona sem mudar políticas de execução.

## Conferência e problemas comuns

- `python` não encontrado: use o executável Python instalado ou `py -3` no Windows.
- Integridade divergente: compare alterações e obtenha uma cópia confiável; não regenere hashes só para esconder erro.
- Conflito no destino: revise diferenças; use `--update` apenas se deseja substituir com backup.
- Capacidade não aparece: confira projeto, caminho e nova sessão. Em interfaces sem skills, use exportação genérica.
- Arquivo/pasta ou link no destino: o instalador recusa colisões e redirecionamentos para não escrever fora da raiz.
- Sem browser/shell/conector: a skill continua como orientação; execução depende das ferramentas oferecidas pelo aplicativo.
