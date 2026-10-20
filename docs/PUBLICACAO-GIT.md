# Publicação e instalação pelo Git

## Repositório

O repositório desta distribuição é `https://github.com/windson83/kit-ia-universal`. A raiz do repositório é o conteúdo de `KIT-IA-UNIVERSAL`, com `README.md`, `skills/`, `scripts/` e demais recursos diretamente nela. Não publique a pasta inteira `D:/SKILL`, que contém o legado.

## Instalação pelo gerenciador de skills

O kit mantém `skills/<nome>/SKILL.md`, formato descoberto pelo [skills CLI](https://github.com/vercel-labs/skills/blob/main/README.md). Esse gerenciador é de terceiros e requer Node.js compatível com sua versão. Conforme a documentação consultada em 20/10/2026, requer Node.js 22.20+.

Dentro do projeto de destino:

```text
npx skills add windson83/kit-ia-universal
```

O menu permite selecionar skills e assistentes. Para escolher uma capacidade diretamente:

```text
npx skills add windson83/kit-ia-universal --skill backend-dev -a codex
npx skills add windson83/kit-ia-universal --skill backend-dev -a claude-code
```

Para instalar todas, escolha todas no menu. Adicione `-g` se quiser o escopo pessoal suportado pelo gerenciador. Consulte `npx skills --help` para opções da versão disponível. Não pressupomos que flags futuras continuarão iguais.

Todas as 19 skills para um assistente específico, sem perguntas interativas:

```text
npx skills add windson83/kit-ia-universal --skill "*" -a codex -y
npx skills add windson83/kit-ia-universal --skill "*" -a claude-code -y
```

Execute apenas o comando do assistente desejado. Para cópias independentes em vez de links, adicione `--copy`. O gerenciador tem sua própria política de atualização e substituição.

Esse caminho instala skills; os agentes nativos opcionais do Claude e a política de backup deste kit pertencem ao instalador Python abaixo. Evite usar dois gerenciadores para manter os mesmos arquivos.

Atualizações pelo gerenciador:

```text
npx skills check
npx skills update
```

## Instalação por clone, sem Node.js

Requer Git e Python 3.10+. Execute num diretório onde deseja guardar o kit:

```text
git clone https://github.com/windson83/kit-ia-universal.git
cd kit-ia-universal
python scripts/kit.py validate
python scripts/kit.py install --profile codex --dest "D:/meu-projeto" --apply
```

Linux/macOS: use `python3` e o caminho real do projeto. Claude com agentes nativos:

```text
python scripts/kit.py install --profile claude --dest "D:/meu-projeto" --agents --apply
```

Para usar uma versão publicada específica, faça checkout da tag correspondente, por exemplo `git checkout v2.1.0` quando essa tag existir no remoto. Não altere uma tag publicada para reutilizar o mesmo nome em outra revisão.

## Atualizar uma instalação mantida pelo kit

Na cópia clonada, preserve suas edições locais; não use reset destrutivo. Se estiver na branch principal e sem conflitos:

```text
git pull --ff-only
python scripts/kit.py validate
python scripts/kit.py install --profile codex --dest "D:/meu-projeto"
python scripts/kit.py install --profile codex --dest "D:/meu-projeto" --apply --update
```

O último comando substitui conteúdo diferente após backup. Consulte INSTALACAO.md para detalhes. Se estiver numa tag, escolha explicitamente a próxima tag desejada após `git fetch --tags`; `pull` não é mecanismo de atualização de um checkout destacado.

## Manutenção do repositório

Revise alterações, regenere hashes apenas após revisão e execute testes. `.gitattributes` mantém LF para que clone em Windows/Linux preserve os hashes. `.git`, caches, ambientes e ZIPs de release não participam do manifesto operacional.

O workflow `.github/workflows/validate.yml` usa permissões de leitura, sem credenciais persistidas, e executa validação/testes/pacote. Não publica releases nem faz deploy automaticamente.

Para enviar uma revisão já preparada, use o fluxo normal de branch/commit/push ou PR do projeto. Antes de publicar uma nova versão, atualize `catalogo.json`, README, changelog e hashes, valide e crie a tag correspondente. A autenticação pertence ao Git/GitHub CLI; não coloque token em arquivos ou comandos de documentação.
