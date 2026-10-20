# Estratégia de testes e evidência

## Planejar por risco

Identifique comportamento, criticidade, fronteiras e regressões prováveis. Escolha unidade para regra isolada, integração para persistência/contrato e ponta a ponta para jornada essencial. Evite testar o mesmo detalhe em todas as camadas sem ganho. Não use porcentagem de cobertura como prova de correção.

Registre baseline antes de alterar testes: commit/contexto, ambiente e falhas existentes. Se a suíte já falha, localize o que impede avaliar a mudança e rode subconjunto relevante sem esconder o restante.

## Matriz útil

| Risco | Cenário | Oráculo | Ambiente/dados |
|---|---|---|---|
| Acesso indevido | Usuário de outro tenant consulta item | Negação e nenhuma exposição | Duas identidades independentes |
| Duplicação | Repetir solicitação após timeout | Regra de idempotência atendida | Dependência controlada |
| Perda de dados | Gravação falha a meio caminho | Invariantes preservadas | Banco de teste |
| Estado incorreto | Resposta antiga chega depois da nova | Contexto mais recente prevalece | Rede/relógio controlados |

Adapte a matriz ao pedido. Concorrência, horário de verão, limite numérico, payload grande e internacionalização entram quando o domínio justificar.

## Construir testes confiáveis

Defina o oráculo: qual resultado diferencia correto de incorreto? Assert sobre efeito observável e invariantes, não nome de método interno. Fixtures precisam expressar o domínio e isolar cada teste; não dependa da ordem. Controle tempo, IDs aleatórios e rede sem mascarar justamente a integração a avaliar.

Para teste assíncrono, aguarde condição observável com limite, evitando sleeps arbitrários. Ao detectar flake, registre frequência e condição; não “corrija” apenas aumentando timeout. Não enfraqueça assertion para tornar o build verde.

Ambiente com gravação deve usar dados e credenciais de teste. Preserve logs necessários e remova dados sensíveis. Não dispare pagamento, envio de mensagem ou operação externa real como efeito colateral de teste local.

## Reportar falhas

Cada bug precisa de título, severidade justificada, pré-condições, passos mínimos, esperado, observado, evidência e ambiente. Separe causa confirmada de hipótese de localização. Se solicitado a corrigir, reproduza, aplique a correção e reexecute o cenário, observando consequências relacionadas.

## Critério de conclusão

Entregue comandos executados e resultados, bugs e limitações do ambiente. Distinga: aprovado, falhou, ignorado e não executado. “Não executado por indisponibilidade” não pode aparecer como “passou”. Em revisão de testes, a entrega pode ser uma lacuna demonstrada, sem criar suíte excessiva para alteração trivial.
