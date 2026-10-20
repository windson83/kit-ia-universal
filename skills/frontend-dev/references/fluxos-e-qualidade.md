# Implementar fluxos frontend completos

## Reconhecimento e modo

Descubra framework, roteamento, renderização, estado, formulários, estilos e testes existentes. Em alteração pontual, preserve composição e convenções. Em fluxo novo, modele navegação, dados e estados antes de multiplicar componentes. Design novo sem sistema existente pode usar a capacidade visual disponível, mas sua ausência não impede implementação coerente.

## Estado e dados

Mapeie loading inicial, atualização em segundo plano, vazio, erro recuperável, permissão negada e sucesso. Não substitua dados válidos por vazio durante refetch sem intenção de UX. Evite resposta atrasada sobrescrevendo seleção nova; cancele ou descarte resultados de contexto anterior. Não exiba dados do usuário anterior após logout/troca de conta.

Em formulários, trate validação por campo e erro geral, envio duplicado, preservação de entrada após falha e navegação com alteração não salva quando relevante. Atualização otimista exige reversão e reconciliação com servidor; ocultar botão não substitui autorização no backend.

## Componentes e acessibilidade

Use componentes existentes antes de criar variantes divergentes. Separe lógica de domínio de apresentação quando isso simplificar testes e reutilização. Prefira elementos nativos e nomes acessíveis. Em diálogo, confira entrada/restauração de foco e fechamento previsível; em tabela, cabeçalhos e leitura em densidades reais.

Verifique fluxo por teclado: ordem de foco, indicador visível, ações acionáveis e erro associado ao campo. Não use somente cor para estado. Considere zoom, texto longo, reduced-motion e tamanhos de toque. Não declare conformidade abrangente se só verificou contraste.

## Responsividade e desempenho

Teste a tarefa central em viewport pequena e tela de operação. Para conteúdo extenso, confira overflow, truncamento e alternativas de leitura. Investigue tamanho de bundle, imagens, trabalho no cliente e listas grandes quando afetarem o uso; não aplique memoização indiscriminada.

## Cenário de exemplo: edição de cadastro

- Carregar dados existentes sem apagar edição por refetch tardio.
- Erro de campo aponta o problema e conserva os demais valores.
- Erro de rede permite tentar novamente sem efeito duplicado.
- Troca de registro não mostra confirmação referente ao registro anterior.
- Usuário com teclado conclui e entende o resultado.

## Entrega

Informe fluxo e estados entregues, impacto em API/configuração, verificações de build/testes, interação e inspeção visual. Screenshots demonstram aparência, não funcionamento de salvamento. Se não houver browser, reporte exatamente essa limitação.
