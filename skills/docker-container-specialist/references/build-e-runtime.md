# Containers do build à operação

## Escolher base e layout

Confirme runtime, arquitetura e dependências nativas. Avalie compatibilidade de libc e pacotes; imagem menor pode aumentar manutenção ou quebrar módulos nativos. Separe build/runtime quando isso eliminar ferramentas desnecessárias sem complicar o fluxo.

Use lockfile e contexto mínimo. Revise `.dockerignore` para excluir segredos, histórico Git, dependências locais e artefatos irrelevantes, preservando arquivos necessários. Ordene camadas por estabilidade para aproveitar cache sem comprometer a reprodutibilidade.

## Segredos e processo

Credenciais em build args, ENV ou comandos podem ficar no histórico de camadas mesmo quando apagadas depois. Use mecanismos de secret do builder e injeção de runtime disponíveis. Não copie `.env` real para a imagem.

Defina usuário com permissões necessárias sobre diretórios graváveis. Avalie filesystem somente leitura e volumes conforme estado real. Processo principal precisa receber sinais e encerrar dentro do grace period; confira forma de execução do entrypoint e comportamento de processos filhos.

## Compose e dependências

Documente portas, redes, volumes, variáveis e requisitos. `depends_on` pode controlar início em certos modos, mas não garante disponibilidade contínua. Aplicação deve tolerar reconexão. Evite publicar porta de banco por padrão quando apenas serviços internos precisam acessá-lo.

Healthcheck deve medir capacidade relevante sem expor dados nem gerar carga excessiva. Diferencie saúde de processo e dependência. Em Swarm ou outra plataforma, verifique suporte real às opções, segredos e política de atualização; sintaxe Compose não garante mesma semântica em qualquer runtime.

## Validar

1. Conferir configuração renderizada sem despejar segredos.
2. Construir com contexto real e dependências corretas.
3. Executar operação central e healthcheck.
4. Testar persistência, reinício e encerramento se fazem parte da alteração.
5. Conferir usuário/permissões e conteúdo final da imagem.

Build concluído não prova que a aplicação sobe. Sem Docker disponível, entregue revisão estática e comandos a executar, indicando que não foram rodados.

## Entrega

Informe base e motivo, arquivos, configuração, resultado de build/runtime, estado persistente e limitações. Não faça push de imagem ou alteração em cluster como consequência implícita de criar um Dockerfile.
