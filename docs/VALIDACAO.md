# Validação da distribuição 2.0.0

## Revisão 2.1.0

Em 20/10/2026, os 16 testes automatizados foram aprovados no Windows/Python 3.14. Incluem um repositório temporário com commit, clone Git e instalação/verificação independente da cópia clonada, além de exclusão dos metadados `.git` do manifesto. Foram vinculados guias operacionais próprios às 19 capacidades e seus links foram validados. O gerenciador público `npx skills add . --list` descobriu as 19 skills sem instalação pessoal.

O workflow GitHub Actions foi configurado para Windows, Linux e macOS em Python 3.10/3.14. A conclusão remota desses jobs deve ser conferida na aba Actions; configuração de CI não significa execução já aprovada. O teste de clone precisou ser executado fora da restrição de processos local do ambiente, que bloqueava o subprocesso do Git. Não foi alterada a configuração global de confiança do Git.

O validador opcional `quick_validate.py` da skill-creator não pôde rodar no Python local por ausência de PyYAML. O validador sem dependências do próprio kit e os testes automatizados foram usados para conferir metadados, estrutura, links e integridade.

O aprofundamento foi revisado como conteúdo, sem ensaio de desempenho de 19 modelos/agentes em tarefas reais. Os cenários em APROFUNDAMENTO.md permitem avaliar esse comportamento na aplicação de destino.

## Histórico da validação inicial

Verificação realizada em 20/10/2026, em Windows com Python 3.14. A implementação usa apenas biblioteca padrão e sintaxe compatível com Python 3.10+, mas outros sistemas operacionais e versões não foram executados nesta entrega.

## Resultado

- 19 capacidades com nomes e metadados válidos.
- Links locais dos documentos de skills conferidos e referências presentes.
- 14 testes automatizados aprovados, incluindo os três perfis, agentes Claude, filtro de capacidades, simulação sem gravação, reinstalação sem regravar, conflito antes de qualquer alteração, backup, preservação de arquivos alheios, colisão de diretório, caminho com espaços, bloqueio de link que sai do destino, falha de escrita com reversão, metadados/referências inválidos, detecção de adulteração e instalação independente a partir do ZIP extraído.
- Os 48 arquivos físicos originais foram comparados aos hashes do inventário e permaneceram idênticos.
- Inventário: 156 itens incluindo contêineres e conteúdo de arquivos compactados; 126 ocorrências de conteúdo textual e 4 ocorrências de scripts originais.

Os testes usam projetos temporários ao lado da distribuição, conferem o caminho de limpeza e removem apenas esses projetos. Nenhum teste instala em configurações pessoais do usuário.

## Ajustes observados durante a validação

A primeira execução encontrou restrições de acesso ao temporário do sistema neste ambiente e diferença de codificação do terminal Windows. Os testes passaram a usar diretório temporário controlado junto à distribuição, e a CLI passou a emitir UTF-8 explicitamente. Todos os testes foram executados novamente após as correções.

## O que este resultado não demonstra

Não foi executada uma sessão real de Codex ou Claude carregando os pacotes, nem avaliadas as 19 capacidades contra tarefas de produção. A validação prova estrutura, integridade e comportamentos testados do instalador; qualidade de resposta depende do modelo, ferramentas, tarefa e contexto. Não há servidor gRPC implementado sem uma interface de serviço definida.

Para repetir os testes, siga MANUTENCAO.md. Hashes detectam alteração de arquivos, mas não substituem assinatura digital ou procedência confiável.
