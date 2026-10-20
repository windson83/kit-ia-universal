# Kit IA Universal — 2.1.0

Biblioteca organizada de 19 capacidades para desenvolvimento, arquitetura, operação, design e contratações públicas. Inclui skills, adaptador de agentes Claude, instalador offline e auditoria do material original.

## Instalação rápida pelo GitHub

Dentro do seu projeto:

```text
npx skills add windson83/kit-ia-universal
```

Selecione as capacidades e a IA no menu. Esse caminho usa o gerenciador de terceiros [skills CLI](https://github.com/vercel-labs/skills), com Node.js compatível; instala as skills no assistente escolhido. Também há instalação por clone, sem Node.js, com backup e agentes Claude opcionais.

**[Instalar e atualizar pelo Git](docs/PUBLICACAO-GIT.md)** · **[Conhecer as 19 capacidades](docs/CATALOGO.md)** · **[O que foi aprofundado](docs/APROFUNDAMENTO.md)**

## O que você recebe

Uma equipe de procedimentos especializados para sair do requisito até a operação: produto, arquitetura, frontend, backend, dados, testes, revisão, diagnóstico, design, segurança, containers, CI/CD, Git, DevOps, documentação e coordenação. Inclui também análise documental de contratações públicas brasileiras.

Cada capacidade tem um procedimento principal e um guia operacional com situações de uso, decisões, falhas relevantes, exemplos e critérios de conclusão. Referências são lidas conforme a tarefa, sem carregar toda a biblioteca no contexto.

**Comece por [INSTALACAO.md](docs/INSTALACAO.md).** O instalador próprio requer Python 3.10 ou superior, sem bibliotecas adicionais. Os arquivos anteriores permanecem preservados como legado na pasta de origem; esta pasta é independente e pode ser copiada para outro computador.

## Instalar em um projeto

Abra o terminal nesta pasta. Primeiro confira o pacote:

```text
python scripts/kit.py validate
python scripts/kit.py list
```

Para Codex, troque o destino abaixo pela raiz do seu projeto:

```text
python scripts/kit.py install --profile codex --dest "D:/meu-projeto"
python scripts/kit.py install --profile codex --dest "D:/meu-projeto" --apply
```

O primeiro comando mostra o plano; o segundo grava. Para Claude, use `--profile claude` e acrescente `--agents` se quiser agentes nativos. Para outras IAs, use `--profile generic` e leia as instruções exportadas. `gRPC` é um protocolo: a adaptação para um serviço que o utilize está explicada no guia de compatibilidade.

## Conteúdo

| Caminho | Finalidade |
|---|---|
| `skills/` | Fonte canônica de cada capacidade e referências sob demanda |
| `scripts/kit.py` | Listagem, instalação, exportação e validação |
| `tests/` | Testes do instalador, conflitos, atualização e preservação |
| `catalogo.json` | Catálogo legível por programas |
| `docs/CATALOGO.md` | Escolha da capacidade por tarefa |
| `docs/COMPATIBILIDADE.md` | Codex, Claude, outras IAs e serviços próprios |
| `docs/AUDITORIA.md` | Problemas encontrados e melhorias |
| `docs/MAPEAMENTO.md` | Correspondência entre legado e distribuição |
| `docs/origens/` | Snapshots históricos das fontes selecionadas, fora da descoberta de skills |
| `docs/MANUTENCAO.md` | Atualizar, testar e empacotar |
| `SHA256SUMS.json` | Detecção de alteração acidental do pacote |

Instruções portáveis não fornecem acesso a arquivos, shell, conectores, SEI ou execução paralela. Essas capacidades dependem da aplicação. A instalação não modifica `AGENTS.md`, `CLAUDE.md`, credenciais, modelos ou servidores MCP.

## Qualidade e contribuição

O kit é validado por testes de instalação, atualização, conflitos, preservação, ZIP e clone Git. A automação do repositório executa os checks em Windows, Linux e macOS; consulte [validação](docs/VALIDACAO.md) para distinguir testes locais e CI efetivamente concluído.

Veja [CONTRIBUTING.md](CONTRIBUTING.md) e [CHANGELOG.md](CHANGELOG.md). Autoria das revisões: Elder Windson, com assistência de IA.

Licença [MIT](LICENSE). Os snapshots em `docs/origens/` preservam notas e atribuições presentes no material de entrada e não são instruções operacionais.
