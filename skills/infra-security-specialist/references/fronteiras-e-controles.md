# Revisão de segurança de infraestrutura

## Superfície efetiva

Defina ambiente e autorização. Mapeie identidade humana, identidade de workload, CI, rede, dados, estado IaC e artefatos. Separe configuração declarada de configuração aplicada; ausência de acesso ao ambiente precisa aparecer no relatório.

## Trilhas de análise

| Fronteira | Investigar | Evidência útil |
|---|---|---|
| Identidade | Permissões diretas, herdadas e relações de confiança | Política efetiva e principal que a usa |
| Rede | Exposição pública, caminho lateral e administração | Regras, rotas e serviço que escuta |
| Pipeline | Forks, runners, tokens e promoção de artefato | Gatilho, permissões e origem do código |
| Containers | Usuário, privilégios, mounts e socket de runtime | Manifesto e configuração aplicada |
| Segredos | Armazenamento, entrega, log e rotação | Referências/configuração sem valor secreto |
| Recuperação | Retenção, isolamento e restore | Exercício de recuperação e limites |

Não trate CIDR permissivo como exposição confirmada sem verificar rotas, serviço e controles intermediários. Por outro lado, não conclua segurança apenas porque não existe IP público; CI, credenciais e redes internas também atravessam fronteiras.

## Caminho de impacto

Para cada achado, identifique ponto de entrada, identidade obtida, ação permitida e dado/serviço afetado. Diferencie permissão excessiva hipotética de caminho viável com pré-condições conhecidas. Leitura de segredo pode permitir impacto muito além do recurso inicial; registre essa cadeia sem reproduzir o valor.

Avalie correção mínima e dependências. Reduzir uma policy sem mapear consumidores pode derrubar serviço; proponha como validar antes e depois. Rotação de segredo exige atualizar os consumidores e invalidar o anterior conforme o mecanismo real.

## Relatório

Inclua recurso e ambiente, evidência, pré-condições, impacto, prioridade e plano de remediação. Liste lacunas de acesso e configurações não verificadas. Se a tarefa permitir execução, faça apenas a mudança autorizada, com plano de recuperação e observação de efeito. Auditoria, por si, não autoriza alterar IAM, firewall ou produção.
