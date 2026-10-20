<a id="inicio"></a>

<div align="center">

# 🧠 Kit IA Universal

### 19 especialidades para transformar pedidos em entregas verificáveis

**Skills portáveis · Agentes para Claude Code · Instalação pelo GitHub**

[![Validação](https://github.com/windson83/kit-ia-universal/actions/workflows/validate.yml/badge.svg)](https://github.com/windson83/kit-ia-universal/actions/workflows/validate.yml)
![Skills](https://img.shields.io/badge/skills-19-2563eb)
![Agentes Claude](https://img.shields.io/badge/agentes_Claude-19_opcionais-7c3aed)
[![Licença MIT](https://img.shields.io/badge/licen%C3%A7a-MIT-16a34a)](LICENSE)

**Do requisito à implementação. Do diagnóstico à correção. Da revisão à operação.**

[🚀 Instalar](#instalar) · [🧩 Conhecer as skills](#catalogo) · [🤖 Conhecer os agentes](#agentes) · [💬 Exemplos de uso](#exemplos) · [📚 Documentação](#documentacao)

</div>

---

## ✨ O que é este projeto?

O **Kit IA Universal** reúne 19 capacidades especializadas para orientar uma IA em tarefas de produto, desenvolvimento, design, qualidade, segurança, infraestrutura, documentação e contratações públicas brasileiras.

Cada capacidade explica **quando atuar, como analisar o problema, quais decisões tomar e quais evidências entregar**. Você pode instalar só a especialidade de que precisa ou usar o conjunto ao longo de um projeto.

| Você precisa… | O kit oferece… |
|---|---|
| Tirar uma ideia do papel | Requisitos, critérios de aceite, arquitetura e contratos entre componentes |
| Construir uma aplicação | Backend, frontend, modelagem de dados e interfaces completas |
| Melhorar a qualidade | Testes de comportamento, revisão de código e investigação de falhas |
| Reduzir riscos | Revisão de autorização, dados sensíveis, IAM, rede e pipelines |
| Preparar a operação | Containers, CI/CD, release, observabilidade e recuperação |
| Trabalhar com clareza | Organização de tarefas, Git, documentação e decisões rastreáveis |
| Analisar documentos contratuais | Método de análise, minutas e fundamentação com fontes verificáveis |

### 📦 O que vem em cada capacidade

- **`SKILL.md`** — descrição, procedimento principal e formato de entrega.
- **Guia operacional** — situações de uso, critérios de decisão, falhas relevantes e exemplos.
- **Referências sob demanda** — material de aprofundamento lido quando necessário.
- **Agente Claude opcional** — definição gerada a partir da mesma skill, sem manter duas versões diferentes do procedimento.

A instalação fornece instruções e recursos. O acesso a arquivos, terminal, navegador, APIs e execução de agentes é oferecido pela aplicação de IA utilizada.

<a id="instalar"></a>

## 🚀 Instalação rápida

### Opção 1 — escolher as skills e a IA pelo menu

Execute dentro do projeto em que deseja usar o kit:

```bash
npx skills add windson83/kit-ia-universal
```

Escolha as capacidades e os assistentes no menu. Esse caminho usa o gerenciador de terceiros [skills CLI](https://github.com/vercel-labs/skills) e requer Node.js compatível com ele.

### Opção 2 — todas as 19 skills para um assistente

**Codex:**

```bash
npx skills add windson83/kit-ia-universal --skill "*" -a codex -y
```

**Claude Code:**

```bash
npx skills add windson83/kit-ia-universal --skill "*" -a claude-code -y
```

Execute o comando do assistente desejado. Para instalar apenas uma capacidade, troque `"*"` pelo identificador, como `backend-dev`. O gerenciador instala no projeto por padrão; adicione `-g` para o escopo pessoal que ele suporta.

### Opção 3 — Git + instalador próprio

Esta opção inclui simulação, detecção de conflitos, atualização com backup e geração dos agentes Claude. Requer **Git e Python 3.10+**, sem bibliotecas Python adicionais.

```bash
git clone https://github.com/windson83/kit-ia-universal.git
cd kit-ia-universal
python scripts/kit.py validate
```

Escolha o perfil e substitua o destino pela raiz do seu projeto:

```bash
# Codex: instalar skills
python scripts/kit.py install --profile codex --dest "D:/meu-projeto" --apply

# Claude Code: instalar skills e gerar os 19 agentes nativos
python scripts/kit.py install --profile claude --dest "D:/meu-projeto" --agents --apply

# Outras IAs: exportar catálogo, instruções e referências
python scripts/kit.py install --profile generic --dest "D:/exportacao-ia" --apply
```

No Linux/macOS, use `python3` e o caminho real do seu projeto. Retire `--apply` para visualizar o plano sem gravar. Use `--only backend-dev debugger`, por exemplo, para selecionar capacidades.

**[📖 Guia completo de instalação](docs/INSTALACAO.md)** · **[🔄 Instalação e atualização pelo Git](docs/PUBLICACAO-GIT.md)**

<a id="catalogo"></a>

## 🧩 Catálogo das 19 skills

Os nomes abaixo são os identificadores usados na instalação. Clique em uma capacidade para abrir suas instruções e acessar o guia operacional correspondente.

### 🧭 Produto, arquitetura e coordenação

| Skill | O que faz | O que entrega |
|---|---|---|
| [📋 `product-analyst`](skills/product-analyst/SKILL.md) | Transforma uma ideia em requisitos. Identifica público, problema, escopo, jornadas, prioridades e ambiguidades que mudam a implementação. | Requisitos claros, critérios de aceite verificáveis, exclusões de escopo e decisões pendentes. |
| [🏛️ `arquiteto-de-software`](skills/arquiteto-de-software/SKILL.md) | Desenha ou revisa a estrutura de um sistema. Compara alternativas, define limites de módulos, ownership dos dados, contratos e estratégia de migração. | Decisões e trade-offs, ADR quando pertinente, diagramas, contratos e encaminhamento para implementação. |
| [🎼 `orquestramd`](skills/orquestramd/SKILL.md) | Organiza trabalho com várias etapas. Descobre capacidades disponíveis, identifica dependências, define responsabilidades e integra resultados. Usa delegação quando autorizada e suportada. | Plano proporcional à tarefa, sequência de execução, responsabilidades, validações e estado real das entregas. |

**Quando usar:** antes de começar uma feature, ao escolher a estrutura técnica ou ao coordenar frentes que dependem umas das outras.

### 💻 Desenvolvimento e experiência visual

| Skill | O que faz | O que entrega |
|---|---|---|
| [⚙️ `backend-dev`](skills/backend-dev/SKILL.md) | Implementa APIs, regras de negócio e integrações. Examina validação, autorização por recurso/tenant, transações, idempotência, concorrência e falhas externas. | Código de servidor, contratos de API, tratamento de erros e verificações do comportamento alterado. |
| [🖥️ `frontend-dev`](skills/frontend-dev/SKILL.md) | Implementa telas e fluxos conectados a APIs. Trata formulários, dados assíncronos, permissões, loading, vazio, erro e recuperação, seguindo a base existente. | Componentes e jornadas funcionais, estados de interface, acessibilidade e verificações disponíveis. |
| [🗄️ `database-admin`](skills/database-admin/SKILL.md) | Modela dados, escreve migrations e investiga consultas lentas. Avalia integridade, constraints, índices, locks, backfill, coexistência de versões e recuperação. | Schema ou migration, análise de impacto, plano de recuperação e evidências de integridade ou desempenho. |
| [🎨 `frontmd`](skills/frontmd/SKILL.md) | Conduz design e implementação de interfaces completas. Conecta público, hierarquia visual, tokens, componentes, responsividade e jornada de uso. | Interface implementada, direção visual, estados, decisões de dependências e validação visual/interativa quando disponível. |
| [🖌️ `ui-design-specialist`](skills/ui-design-specialist/SKILL.md) | Define a direção de UX/UI e a continuidade do design system. Especifica hierarquia, paleta semântica, tipografia, espaçamento, componentes e interação. | Tokens e direção visual implementáveis, especificação dos estados e orientação para manter consistência entre telas. |

**Como escolher no frontend:** use `ui-design-specialist` para definir a linguagem visual; `frontend-dev` para implementar fluxos na base existente; `frontmd` para conduzir o trabalho conjunto de design e implementação.

### 🧪 Qualidade, diagnóstico e segurança

| Skill | O que faz | O que entrega |
|---|---|---|
| [✅ `qa-tester`](skills/qa-tester/SKILL.md) | Planeja e executa testes pelo risco do comportamento. Escolhe camadas de teste, controla dados/tempo/rede e cobre bordas, isolamento e regressões relevantes. | Matriz de cenários, testes e resultados executados, bugs reproduzíveis e lacunas de cobertura. |
| [🔎 `code-reviewer`](skills/code-reviewer/SKILL.md) | Revisa mudanças e PRs no contexto dos chamadores. Procura regressões concretas de correção, compatibilidade, persistência, concorrência e manutenção. | Achados priorizados com localização, cenário de falha e correção sugerida; limites da revisão. |
| [🐛 `debugger`](skills/debugger/SKILL.md) | Investiga falhas pela causa raiz. Monta reprodução, testa hipóteses, isola o mecanismo do erro e aplica uma correção quando solicitada. | Diagnóstico sustentado por evidência, correção específica e verificação antes/depois. |
| [🛡️ `security-auditor`](skills/security-auditor/SKILL.md) | Audita segurança de aplicações: autorização, sessões, injeção, SSRF, arquivos, dependências e exposição de dados. Confere caminhos e pré-condições reais. | Achados de segurança com evidência, impacto, severidade, remediação e teste de correção proposto. |
| [🔐 `infra-security-specialist`](skills/infra-security-specialist/SKILL.md) | Audita IAM, redes, runners, pipelines, containers, segredos, IaC e recuperação. Distingue configuração declarada de configuração efetivamente verificada. | Mapa dos riscos de infraestrutura, caminhos de impacto, prioridades e plano de remediação verificável. |

**Como escolher na segurança:** `security-auditor` examina a aplicação; `infra-security-specialist` examina a infraestrutura e a cadeia operacional. `code-reviewer` faz a revisão geral da mudança, com achados acionáveis.

### ☁️ Infraestrutura, entrega e colaboração

| Skill | O que faz | O que entrega |
|---|---|---|
| [🚢 `devops-engineer`](skills/devops-engineer/SKILL.md) | Prepara operação, infraestrutura e releases. Considera readiness, observabilidade, configuração, estado persistente, rollout, rollback e resposta a incidentes. | Configuração ou plano operacional, procedimento de release/recuperação e runbook proporcional ao serviço. |
| [🔁 `ci-cd-specialist`](skills/ci-cd-specialist/SKILL.md) | Cria, revisa e depura pipelines. Examina gatilhos, dependências entre jobs, permissões, confiança de PRs, cache, artefatos e condições de publicação. | Workflow, explicação de gatilhos/permissões, correção de falhas e evidências da validação possível. |
| [🐳 `docker-container-specialist`](skills/docker-container-specialist/SKILL.md) | Cria e otimiza Dockerfiles e configurações de containers. Avalia base, build/runtime, cache, secrets, usuário, volumes, healthchecks e encerramento. | Arquivos de containerização, configuração de runtime e resultado de build/execução quando houver Docker disponível. |
| [🌿 `git-workflow-specialist`](skills/git-workflow-specialist/SKILL.md) | Organiza mudanças, commits, branches e PRs. Resolve conflitos pela intenção dos dois lados e preserva alterações locais e histórico compartilhado. | Histórico ou integração organizada, conflitos resolvidos, descrição de PR e estado confirmado do envio autorizado. |

**Como escolher na operação:** `ci-cd-specialist` cuida do pipeline; `docker-container-specialist` do empacotamento e runtime do container; `devops-engineer` da operação e do release do serviço.

### 📝 Documentação técnica

| Skill | O que faz | O que entrega |
|---|---|---|
| [📚 `tech-writer`](skills/tech-writer/SKILL.md) | Escreve documentação fiel ao código e à operação. Escolhe entre README, guia, referência de API, runbook e changelog, com exemplos e pré-requisitos. | Documentos utilizáveis, links coerentes, exemplos verificados quando possível e lacunas factuais identificadas. |

**Quando usar:** para permitir que alguém instale, use, mantenha ou recupere o sistema sem depender do contexto da conversa original.

### ⚖️ Contratações públicas brasileiras

| Skill | O que faz | O que entrega |
|---|---|---|
| [📜 `contratos-publicos-analise`](skills/contratos-publicos-analise/SKILL.md) | Analisa e revisa documentos contratuais. Relaciona fatos, obrigações e evidências, confere o regime aplicável e orienta a verificação de fontes oficiais. | Análise ou minuta, melhorias justificadas, fundamentação rastreável e pendências antes do uso oficial. |

**Quando usar:** em análise de contrato, TR, notificação, relatório de fiscalização, aditivo e documentos relacionados. A skill distingue fatos de alegações e decisão administrativa; não presume acesso ao SEI nem inventa prazos, valores ou fundamento legal.

<a id="agentes"></a>

## 🤖 Quais agentes existem e como funcionam?

**Skill** é o procedimento especializado que a IA consulta. **Agente** é um executor com contexto próprio oferecido pelo aplicativo. O kit mantém uma fonte de conteúdo e, no Claude Code, pode gerar **19 definições de agentes**, uma para cada especialidade do catálogo.

### Agentes nativos do Claude Code

Ao instalar com `--profile claude --agents`, o kit cria:

```text
.claude/
├── skills/
│   └── <especialidade>/SKILL.md
└── agents/
    └── <especialidade>.md
```

Os agentes têm **os mesmos identificadores e responsabilidades descritos no catálogo acima**:

| Equipe | Agentes disponíveis |
|---|---|
| 🧭 Planejamento | `product-analyst`, `arquiteto-de-software`, `orquestramd` |
| 💻 Desenvolvimento e design | `backend-dev`, `frontend-dev`, `database-admin`, `frontmd`, `ui-design-specialist` |
| 🧪 Qualidade e segurança | `qa-tester`, `code-reviewer`, `debugger`, `security-auditor`, `infra-security-specialist` |
| ☁️ Operação e colaboração | `devops-engineer`, `ci-cd-specialist`, `docker-container-specialist`, `git-workflow-specialist` |
| 📝 Documentação | `tech-writer` |
| ⚖️ Contratos públicos | `contratos-publicos-analise` |

Cada definição pré-carrega a skill correspondente e usa **`model: inherit`**, herdando o modelo da sessão. O acesso a ferramentas e a execução seguem as permissões do ambiente. A presença de 19 agentes não significa que todos serão executados juntos.

Exemplo de pedido no Claude Code:

> Use o agente `database-admin` para revisar esta migration. Avalie compatibilidade, locks, backfill e recuperação antes de propor a alteração.

### Codex e outras IAs

| Ambiente | Como o kit é usado |
|---|---|
| **Codex** | Skills em `.agents/skills/`; o instalador não cria agentes nativos Codex. |
| **Claude Code** | Skills em `.claude/skills/` e agentes nativos opcionais em `.claude/agents/`. |
| **Outros agentes com suporte a skills** | Use o gerenciador ou o diretório de skills documentado pelo produto. |
| **Chat sem acesso a arquivos** | Anexe ou cole a skill escolhida e apenas as referências necessárias. |
| **Aplicações próprias/API** | Use o perfil genérico para consumir catálogo, instruções e recursos no seu runtime. |

**[🔌 Compatibilidade e limites de cada ambiente](docs/COMPATIBILIDADE.md)**

<a id="exemplos"></a>

## 💬 Exemplos de uso

Depois de instalar, peça a capacidade pelo nome e forneça o objetivo e os arquivos relevantes.

| Situação | Exemplo de pedido |
|---|---|
| 📋 Ideia ainda vaga | “Use `product-analyst` para transformar esta ideia em requisitos e critérios de aceite. Separe o que já sabemos das decisões pendentes.” |
| 🏛️ Decisão de arquitetura | “Use `arquiteto-de-software` para comparar as opções de integração deste serviço e registrar os trade-offs.” |
| ⚙️ API com efeitos duplicados | “Use `backend-dev` para implementar este webhook com autorização, idempotência e recuperação de falhas.” |
| 🎨 Interface completa | “Use `frontmd` para redesenhar e implementar este fluxo, preservando a stack e incluindo estados de erro, loading e vazio.” |
| 🧪 Testes de comportamento | “Use `qa-tester` para verificar autorização entre duas contas e reportar qualquer acesso cruzado.” |
| 🐛 Erro intermitente | “Use `debugger` para reproduzir esta falha, testar hipóteses e corrigir a causa com uma verificação antes/depois.” |
| 🚢 Preparação de release | “Use `devops-engineer` para definir como publicar esta versão, observar saúde e recuperar em caso de falha.” |
| 📜 Documento administrativo | “Use `contratos-publicos-analise` para revisar esta notificação com base no contrato e nas evidências fornecidas.” |

### 🛤️ Como as especialidades podem se complementar

```text
Pedido ou ideia
    ↓
Requisitos e critérios de aceite → Decisões de arquitetura
    ↓
Dados + Backend + Frontend/Design
    ↓
Testes + Revisão + Segurança conforme o risco
    ↓
Containers / Pipeline / Operação conforme o projeto
    ↓
Documentação e entrega verificada
```

`orquestramd` pode coordenar esse trabalho quando o pedido exigir. Para uma tarefa pequena, use diretamente a capacidade adequada. Delegação e paralelismo dependem do suporte e da autorização do ambiente.

## 🔄 Atualização

Se instalou com o gerenciador:

```bash
npx skills check
npx skills update
```

Se usa a cópia Git e o instalador próprio, atualize a branch sem descartar edições locais e confira o plano antes de aplicar:

```bash
git pull --ff-only
python scripts/kit.py validate
python scripts/kit.py install --profile codex --dest "D:/meu-projeto"
python scripts/kit.py install --profile codex --dest "D:/meu-projeto" --apply --update
```

O instalador próprio recusa conflitos por padrão. Com `--update`, salva os arquivos substituídos em `.ia-kit-backups/`. Arquivos alheios ao plano são preservados. Evite manter os mesmos arquivos com dois gerenciadores diferentes.

## 🗂️ Estrutura do repositório

```text
kit-ia-universal/
├── skills/                    # 19 capacidades e seus guias operacionais
├── scripts/
│   ├── kit.py                 # Listar, validar, instalar e exportar
│   └── package.py             # Gerar ZIP independente
├── tests/                     # Testes de instalação e preservação
├── docs/                      # Guias, auditoria e histórico do legado
├── .github/workflows/         # Validação automatizada
├── catalogo.json              # Catálogo para programas e integrações
├── SHA256SUMS.json            # Integridade dos arquivos distribuídos
├── CONTRIBUTING.md            # Como contribuir
└── LICENSE                    # Licença MIT
```

<a id="documentacao"></a>

## 📚 Documentação

| Documento | Você encontra… |
|---|---|
| [🚀 Instalação](docs/INSTALACAO.md) | Perfis, seleção de capacidades, backup, recuperação e problemas comuns. |
| [🌿 Publicação e instalação Git](docs/PUBLICACAO-GIT.md) | Comandos de instalação, clone, versões e atualização. |
| [🧩 Catálogo](docs/CATALOGO.md) | Identificadores e visão resumida das capacidades. |
| [🔍 Aprofundamento](docs/APROFUNDAMENTO.md) | O que foi ampliado em cada especialidade e cenários para avaliar o comportamento. |
| [🔌 Compatibilidade](docs/COMPATIBILIDADE.md) | Como adaptar o kit a diferentes aplicativos e serviços próprios. |
| [🧪 Validação](docs/VALIDACAO.md) | Testes realizados e limites do que eles demonstram. |
| [🗃️ Auditoria](docs/AUDITORIA.md) | Problemas encontrados na coleção original e tratamento adotado. |
| [🧭 Mapeamento do legado](docs/MAPEAMENTO.md) | Relação entre os materiais anteriores e a distribuição organizada. |
| [🛠️ Manutenção](docs/MANUTENCAO.md) | Como revisar, validar e empacotar o kit. |
| [📝 Histórico](CHANGELOG.md) | Mudanças entre versões. |

## 🧪 Qualidade e verificações

O kit tem **16 testes automatizados** que cobrem instalação, seleção de capacidades, simulação, conflitos, backup, preservação de arquivos, reversão após falha e uso independente por ZIP ou clone Git. O workflow valida o pacote em Windows, Linux e macOS com Python 3.10 e 3.14. O resultado de cada execução está na [aba Actions](https://github.com/windson83/kit-ia-universal/actions).

Para verificar uma cópia local:

```bash
python scripts/kit.py validate
python -m unittest discover -s tests -v
```

Os testes validam a distribuição e o instalador. O comportamento de cada especialidade também depende do modelo, da tarefa, do contexto e das ferramentas disponíveis; não representa certificação de desempenho de uma IA.

## 🤝 Contribuição e autoria

Contribuições podem melhorar procedimentos, exemplos, compatibilidade e testes. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) antes de propor uma alteração.

**Autoria das revisões:** Elder Windson, com assistência de IA.

**Licença:** [MIT](LICENSE).

O material anterior permanece preservado como legado na pasta de origem. Os snapshots em `docs/origens/` mantêm as notas e atribuições presentes nas fontes e ficam fora da descoberta operacional de skills.

---

<div align="center">

**Escolha uma especialidade, forneça contexto e peça uma entrega com evidência.**

[⬆️ Voltar ao início](#inicio)

</div>
