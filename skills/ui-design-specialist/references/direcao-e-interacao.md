# Direção visual e UX implementável

## Ler produto e contexto

Identifique usuário, tarefa central, ambiente, frequência e consequência do erro. Interface operacional densa, serviço público e landing page podem exigir decisões diferentes. Inspecione tokens, marca, componentes e padrões de navegação antes de escolher estética nova.

## Decidir com critério

Defina hierarquia informacional e caminho da ação principal. Densidade precisa servir a tarefa: reduzir tudo a cards pode piorar comparação; tabela pode ser adequada quando o usuário precisa comparar registros. Em mobile, priorize informação e ações sem ocultar dados indispensáveis.

Estabeleça paleta semântica, escala tipográfica, ritmo de espaçamento, largura, raio e elevação. Reutilize as convenções existentes. Cor ou fonte popular não é defeito por si; problema é falta de contraste, hierarquia ou identidade adequada. Escolha um elemento de personalidade apenas quando servir ao produto.

## Especificar interação

Para cada componente importante, descreva padrão, foco, hover quando aplicável, disabled, loading, erro, vazio e seleção. Desabilitar ação sem explicar a causa pode impedir o usuário de concluir a tarefa. Texto de erro deve dizer como recuperar quando isso for possível.

Navegação por teclado, ordem de foco e nomes acessíveis fazem parte do desenho. Não dependa só de cor/ícone. Para modal/menu, considere abertura, foco e retorno à origem. Movimento precisa respeitar preferência por redução e não esconder informação.

## Handoff

```text
Público/tarefa e direção escolhida:
Hierarquia e estrutura de tela:
Tokens e usos semânticos:
Componentes reaproveitados/novos:
Estados e regras de interação:
Responsividade e conteúdo extremo:
Verificação visual e acessível:
```

Exemplo útil: token `--status-warning` aplicado ao estado que exige atenção, acompanhado de texto explícito; não apenas “usar amarelo para destacar”. Diferencie mockup de comportamento implementado e testado.

## Critério de conclusão

Decisões precisam permitir implementação consistente por outra pessoa. Mostre justificativas relevantes e limites de validação; aparência agradável não prova conformidade WCAG nem sucesso da tarefa. Para mudança pontual, entregue só os tokens/estados afetados.
