# Documentação que permite executar a tarefa

## Escolher documento

- README: propósito, instalação, primeiro uso e ponte para detalhes.
- Guia: caminho completo para uma tarefa, com pré-requisitos e resultado.
- Referência: contrato preciso de comandos, campos ou API.
- Runbook: diagnóstico e ação operacional, com critério de sucesso/recuperação.
- Changelog: mudança percebida pelo usuário e ação necessária ao atualizar.

Não transforme README em cópia de todos os documentos. Defina uma fonte de verdade para cada informação e use links relativos quando fizer parte do mesmo pacote.

## Verificar comportamento

Leia código, testes e configuração; identifique versão e ambiente que sustentam a afirmação. Rode exemplos relevantes quando possível. Se um comando é só ilustrativo, identifique os campos que o leitor precisa substituir. Não use “pronto” para arquivo com configuração essencial desconhecida.

Comandos devem ter diretório de partida, dependências e resultado esperado. Em Windows/Linux, indique diferenças reais de shell, caminhos e executável; não prometa portabilidade sem teste. Não esconda etapas de autenticação ou custo quando fazem parte necessária da tarefa documentada.

## Contratos e operação

API: método/rota, autenticação, campos com tipos e obrigatoriedade, exemplo coerente com schema, resposta e erros relevantes. Não exponha credenciais nem dados reais. Mostre paginação ou idempotência quando mudam o modo correto de consumir.

Runbook: sintoma, impacto, evidência, condições para agir, comandos, risco, sucesso e recuperação. Diga quais passos só produzem um plano e quais alteram o ambiente. Guia de atualização informa migração de dados/configuração e incompatibilidades.

## Revisão de qualidade

Siga o documento como leitor sem contexto. Resolva links e nomes de arquivos, execute o primeiro uso em ambiente descartável e compare saída. Procure placeholders esquecidos, versão divergente, comando que depende de diretório implícito e passo ausente.

Entrega identifica documentos, exemplos realmente testados e dúvidas factuais pendentes. Correção de redação pode ser concluída sem inventar a resposta para uma dúvida de produto. Mudança de documentação não autoriza enviar mensagens ou publicar conteúdo externo sem escopo.
