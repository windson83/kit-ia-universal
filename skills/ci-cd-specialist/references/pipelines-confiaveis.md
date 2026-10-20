# Pipelines confiáveis

## Inspecionar antes de escrever

Determine plataforma, eventos, branches, runners, artefatos e destinos. Em pipeline falhando, encontre o primeiro job com causa própria e diferencie erro de execução de cancelamento por dependência. Reproduza instalação/build com runtime e lockfile reais quando possível.

## Grafo e confiança

Modele dependências pelo artefato e pela autorização, não por uma ordem genérica de etapas. Lint e testes independentes podem correr juntos; publicação só acontece após os gates necessários. O evento importa: código de fork, configuração de PR e branch protegido têm níveis de confiança diferentes.

Não exponha segredos ou token de escrita a código não confiável. Em GitHub Actions, examine interações de `pull_request_target`, checkout do PR e execução de scripts do contribuidor; privilégios do contexto não tornam esse código seguro. Restrinja permissões por job. Não imprima contextos completos para depurar segredo.

## Reprodutibilidade e desempenho

Use versão de runtime explícita e instalação coerente com lockfile. Ações e dependências devem seguir política de pin do repositório; confira atualizações oficiais, sem copiar versão histórica de exemplos. Cacheie somente material reaproveitável e escolha chave com lockfile, sistema e runtime conforme necessário.

Cache restaurado não comprova artefato válido. Promova o mesmo artefato imutável para release quando a plataforma permitir. Defina retenção e nome de artefatos para impedir consumo da execução errada.

## Falhas, concorrência e release

Use timeout e trate exit code real. Não acrescente `continue-on-error` a gate obrigatório para tornar o pipeline verde. Cancelar runs obsoletos pode ajudar CI, mas interromper deploy com estado exige avaliar consistência e recuperação. Use grupos de concorrência por ambiente e mecanismo de aprovação já adotado.

Em publicação, verifique condição de branch/tag, identidade, credenciais e destino. Prefira credenciais temporárias quando suportadas. Registro de release precisa mostrar o que foi publicado e como recuperar.

## Validar e entregar

Valide sintaxe, comandos e cenários de gatilho: push, PR interno, fork e tag, conforme aplicável. Execução local não reproduz segredos e permissões da plataforma. Informe verificações reais, jobs alterados, impacto de tempo e riscos residuais. Não dispare release real como teste sem autorização.
