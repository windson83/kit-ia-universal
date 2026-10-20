# Auditoria e melhorias — 20/10/2026

## Cobertura

156 itens inventariados, incluindo contêineres e membros aninhados; 126 documentos/scripts UTF-8 lidos; 4 ocorrências de scripts preservadas para revisão. Não executamos scripts do legado nem modificamos os originais. A contagem inclui cópias repetidas, não capacidades distintas.

## Problemas encontrados e tratamento

| Problema observado | Tratamento na distribuição |
|---|---|
| Agentes de cerca de 1 KB coexistiam com versões de vários KB em .skill e ZIP | Comparação de fontes e 19 capacidades canônicas com rastreabilidade |
| ZIP dentro de ZIP e referências ausentes nos .skill isolados | Inventário recursivo e referências completas recuperadas dos pacotes |
| Nomes architect/arquiteto e backend/desenvolvedor-back-end divergentes | Nomes únicos e aliases documentados |
| Modelos opus/sonnet/haiku e nomes de ferramentas amarrados ao Claude | Núcleo neutro; adaptador Claude com modelo herdado e catálogo portátil |
| Dependências de skills inexistentes como write-spec/system-design | Procedimentos autossuficientes; descoberta de capacidade quando necessária |
| Instalação com cp/unzip sobrescrevia destinos sem checagem | Planejamento, conflito antes de gravação, atualização explícita e backup |
| Instalador Bash aceitava argumentos desconhecidos e escopos conflitantes | CLI com argumentos tipados e validação de destino |
| Temporário de unzip sem limpeza confiável e extração sem fronteira | Instalador novo não extrai arquivos arbitrários e não precisa de unzip |
| Uso de plugin validate para pastas de agentes/skills | Validador específico de estrutura, nomes, referências e integridade |
| Validadores antigos conferiam versão fixa e palavras no texto | Validação de arquivos/links reais e testes do instalador |
| FrontMD impunha processo longo e preferência de bibliotecas | Fluxo proporcional e respeito à stack; detalhes em referências sob demanda |
| Revisão restrita só às linhas novas poderia perder contexto | Leitura de chamadores e cenário concreto de regressão |
| Separação rígida de QA/debugger parava correções autorizadas | Papel ajustado ao pedido; diagnóstico ou correção conforme escopo |
| Referência contratual trazia valores anuais e afirmação ampla de regime único | Fonte jurídica precisa ser verificada no caso; tabela histórica removida do material operacional |
| Alegações sobre terceiros, estrelas de repositórios e limites sem validade garantida | Não replicadas no guia operacional |

## Profundidade das melhorias

As capacidades agora exigem entregas e evidências específicas: isolamento e idempotência no backend; locks e recuperação de dados em migrations; confiança de PRs e permissões no CI; sinais/segredos em containers; contexto em revisão; estados e acessibilidade no frontend; fonte e regime em contratos. Aumentar texto indiscriminadamente não melhora o agente: os detalhes extensos ficam em referências.

## Limites

A auditoria é estática e os testes validam a distribuição e o instalador. Não é certificação do comportamento de um modelo nem teste de acesso ao SEI, serviços externos ou execução de pipelines reais. Referências técnicas recuperadas são material de apoio histórico e devem ser confrontadas com documentação atual quando versões ou recursos importarem. Não foi feita análise jurídica de um caso concreto nem certificação de todas as normas citadas nos originais. Snapshots em origens/ são histórico, não instruções ativas.
