# Fluxo completo de design e implementação

## Calibrar ao pedido

Componente isolado: reutilize tokens e comportamento do projeto, implemente e confira estados relevantes. Tela/fluxo novo: brief curto, hierarquia, estados, composição e validação. Redesign amplo: compare jornadas e componentes existentes, proponha evolução e migração visual coerente. Auditoria: entregue achados e prioridades em vez de reimplementar sem solicitação.

## Reconhecimento e brief

Inspecione stack real, roteamento, renderização, componentes e público. Estabeleça ação central, densidade, tom e conteúdo. A direção visual deve decorrer dessas decisões. Não imponha fonte, cor, framework ou biblioteca porque aparece numa referência histórica. Consulte versões e compatibilidade oficiais quando introduzir dependências.

Defina tokens semânticos e ritmo visual antes que estilos locais divergentes se espalhem. Para projeto existente, preserve padrões úteis e documente exceções. Ícones e animações precisam ajudar leitura/ação; decoração não compensa conteúdo sem hierarquia.

## Implementação por jornada

Construa a fatia que o usuário conclui: entrada, validação, resultado e recuperação. Inclua estados de carregamento, vazio, falha e permissão. Mantenha fronteira de dados e componentes clara. Dados fictícios devem ser reconhecíveis e não simular persistência real.

Avalie layout em conteúdos curtos/longos e densidades reais. Confira teclado, foco, nomes acessíveis, contraste e reduced-motion. Em telas operacionais, teste comparação, filtros e ações em lote; em páginas públicas, hierarquia, leitura e conversão da tarefa relevante.

## Validação e crítica

Execute checks do projeto, navegue a jornada e faça inspeção visual nos tamanhos representativos quando houver ferramenta. Screenshot não prova salvamento, e build não prova aparência. Faça crítica específica: o que compete pela atenção, onde falta feedback e qual elemento torna a tarefa mais difícil.

Corrija o que tiver efeito observado, sem ciclos ilimitados de polimento subjetivo. Use as referências de stack/estética como apoio contextual, não como regra para trocar uma base saudável. Se ferramenta visual não existir, entregue implementação e limite de verificação explicitamente.

## Entrega

Relate interface e fluxo, direção/tokens, dependências novas e motivo, validações e limitações. Não anuncie “pronto para produção” só porque o mockup é bonito. Em trabalho incremental, não exija documento extenso quando diff e evidência resolvem a necessidade.
