# Aprofundamento da versão 2.1.0

A revisão inicial organizou o material, mas vários entrypoints da 2.0.0 ficaram restritos a cinco orientações e não tinham guia próprio. Esta revisão completa o conteúdo operacional das 19 capacidades, sem usar tamanho de arquivo como substituto de qualidade.

Cada skill agora encaminha tarefas substanciais a um guia específico, instalado junto com ela. O guia descreve situações, escolhas, cenários de falha e evidência de conclusão. Procedimentos pequenos continuam proporcionais ao pedido.

| Capacidade | Conteúdo aprofundado |
|---|---|
| [product-analyst](../skills/product-analyst/SKILL.md) | Calibrar a entrega; Investigar o problema; Detalhar a jornada; Priorizar e entregar |
| [arquiteto-de-software](../skills/arquiteto-de-software/SKILL.md) | Modos; Raciocínio arquitetural; Handoff utilizável |
| [backend-dev](../skills/backend-dev/SKILL.md) | Escolher o modo; Contrato antes de implementação; Consistência e efeitos externos; Integrações e observabilidade; Exemplo de aceite: criação de pedido; Conclusão |
| [database-admin](../skills/database-admin/SKILL.md) | Diagnóstico; Alteração de schema; Recuperação; Otimização com evidência; Entrega verificável |
| [frontend-dev](../skills/frontend-dev/SKILL.md) | Reconhecimento e modo; Estado e dados; Componentes e acessibilidade; Responsividade e desempenho; Cenário de exemplo: edição de cadastro; Entrega |
| [qa-tester](../skills/qa-tester/SKILL.md) | Planejar por risco; Matriz útil; Construir testes confiáveis; Reportar falhas; Critério de conclusão |
| [security-auditor](../skills/security-auditor/SKILL.md) | Escopo e confiança; Trilhas por superfície; Achados com utilidade; Conclusão e remediação |
| [code-reviewer](../skills/code-reviewer/SKILL.md) | Delimitar a base; Perguntas por tipo de mudança; Comprovar sem exagero; Exemplo de achado; Entregar |
| [debugger](../skills/debugger/SKILL.md) | Montar a reprodução; Escolher uma observação discriminante; Aplicar e verificar; Entrega |
| [devops-engineer](../skills/devops-engineer/SKILL.md) | Descoberta do ambiente; Projeto operacional; Release com estado; Incidente; Runbook mínimo |
| [ci-cd-specialist](../skills/ci-cd-specialist/SKILL.md) | Inspecionar antes de escrever; Grafo e confiança; Reprodutibilidade e desempenho; Falhas, concorrência e release; Validar e entregar |
| [git-workflow-specialist](../skills/git-workflow-specialist/SKILL.md) | Estado antes da ação; Commits e integração; Conflitos; PR e envio; Recuperação e entrega |
| [docker-container-specialist](../skills/docker-container-specialist/SKILL.md) | Escolher base e layout; Segredos e processo; Compose e dependências; Validar; Entrega |
| [infra-security-specialist](../skills/infra-security-specialist/SKILL.md) | Superfície efetiva; Trilhas de análise; Caminho de impacto; Relatório |
| [tech-writer](../skills/tech-writer/SKILL.md) | Escolher documento; Verificar comportamento; Contratos e operação; Revisão de qualidade |
| [ui-design-specialist](../skills/ui-design-specialist/SKILL.md) | Ler produto e contexto; Decidir com critério; Especificar interação; Handoff; Critério de conclusão |
| [frontmd](../skills/frontmd/SKILL.md) | Calibrar ao pedido; Reconhecimento e brief; Implementação por jornada; Validação e crítica; Entrega |
| [orquestramd](../skills/orquestramd/SKILL.md) | Descobrir e dimensionar; Pacote de trabalho; Acompanhar sem simular; Integrar e retrabalhar; Encerrar |
| [contratos-publicos-analise](../skills/contratos-publicos-analise/SKILL.md) | Definir escopo e regime; Ler e relacionar evidências; Modos de entrega; Modelo de achado; Minuta utilizável; Conferência final |

## Como avaliar na prática

- Backend: pedir integração que recebe webhook duplicado deve levar a examinar autenticação da origem, deduplicação, transação e recuperação, não apenas criar endpoint.
- Dados: pedir uma coluna em tabela grande deve levar a verificar locks, compatibilidade, backfill e recuperação na versão real do banco.
- QA: pedir testes de autorização deve incluir duas identidades e isolamento, sem declarar “passou” quando o ambiente não foi executado.
- Git: conflito com edições locais deve preservar as duas intenções e verificar a integração, sem reset destrutivo como atalho.
- Design: fluxo de formulário deve incluir erro, loading, foco e recuperação, além da aparência.
- Contratos: minuta deve distinguir fato, alegação e decisão, com fundamento rastreável e verificação de regime; não inventar prazo ou limite anual.
- Orquestração: ambiente sem agentes deve levar à execução individual honesta, não a relatos de especialistas fictícios.

Estes são cenários para avaliação do comportamento; não foram executados como ensaios de modelos independentes. Os testes automatizados cobrem instalador, estrutura, referências, integridade e transporte por ZIP/Git. Um modelo deve ser avaliado também em tarefas reais do ambiente de adoção.
