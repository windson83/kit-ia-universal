# Operação, release e recuperação

## Descoberta do ambiente

Identifique serviços, ambientes, IaC, configurações, estado persistente e mecanismo de publicação. Confira a conta/região/contexto de destino antes de qualquer aplicação. Comando local de validação e comando que altera recurso remoto precisam estar claramente separados.

## Projeto operacional

Defina como o serviço inicia, sinaliza readiness, observa dependências, encerra graciosamente e recupera falha. Liveness não deve reiniciar em cascata por dependência externa intermitente. Planeje limites de recursos e capacidade com medições ou requisitos disponíveis.

Artefato de release deve ser identificável por versão/digest e ter configuração externa documentada. Não reconstrua artefato diferente em cada ambiente sem motivo. Segredos não devem ir para imagem, log ou estado versionado; IaC pode armazenar valores sensíveis mesmo quando a saída os mascara.

## Release com estado

Liste pré-condições, gates, ordem de schema/código e critério de saúde. Para rollout gradual, verifique coexistência das versões e comportamento de jobs. Defina quando abortar e quem decide. Não proponha blue-green ou canary se a plataforma ou o estado não suportam o benefício esperado.

Rollback de código pode ser inviável após mudança irreversível de dados. Identifique quando recuperação precisa de migração compensatória ou restore. Backup precisa de escopo, retenção e teste de restauração apropriados à tarefa; “backup realizado” não demonstra recuperação.

## Incidente

Registre impacto e marco temporal. Priorize mitigação autorizada e preserve evidência. Limite mudanças simultâneas para poder atribuir efeito. Observe sinais de recuperação antes de encerrar. Depois, descreva causa confirmada ou hipóteses restantes e prevenção proporcional.

## Runbook mínimo

```text
Serviço/ambiente e versão:
Sintoma e impacto:
Sinais e comandos de diagnóstico sem segredos:
Condições para agir:
Procedimento de mitigação/release:
Critério de sucesso e tempo de observação justificado:
Recuperação, limitações e escalonamento:
```

Entrega distingue plano, validação e aplicação efetiva. Não reporte deploy executado se só gerou configuração.
