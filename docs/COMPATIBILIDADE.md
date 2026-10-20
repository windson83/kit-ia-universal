# Compatibilidade e limites

| Ambiente | Entrega | O que depende da aplicação |
|---|---|---|
| Codex | Skills de projeto em `.agents/skills` | Descoberta, ferramentas, autorização e agentes |
| Claude Code | Skills `.claude/skills`; agentes opcionais `.claude/agents` | Runtime Claude e permissões |
| Outros agentes com Agent Skills | Pastas `SKILL.md` e referências | Caminho e implementação do padrão no produto |
| Chat sem arquivos/ferramentas | Texto anexado ou colado da capacidade | Sem execução automática local |
| Serviço próprio/API | Catálogo e instruções pela exportação generic | Carregamento, execução de ferramentas, estado e aprovação implementados pelo serviço |
| Serviço que usa gRPC | Mesmo núcleo textual | gRPC transporta mensagens; não instala skills nem define uma API universal de agentes |

Se “gRPC” se referia a outro produto de IA, o perfil genérico permanece utilizável; um adaptador nativo exige conhecer o produto e sua especificação. Se “Cloud” se referia ao Claude, use o perfil Claude. Execução na nuvem depende de o provedor aceitar arquivos e instruções nesse formato.

## Integração de serviço próprio

1. Leia `catalogo.json` exportado e use descrições para escolher uma capacidade pertinente.
2. Carregue `skills/<id>/SKILL.md` como instrução de tarefa, subordinada às regras da aplicação.
3. Resolva referências relativamente à pasta da capacidade, somente quando necessárias.
4. Exponha ferramentas reais com suas permissões. Não transforme nome de ferramenta em chamada fictícia.
5. Registre o que foi executado, erros e evidência. Delegação é opcional e precisa de suporte real.

O kit não inclui servidor gRPC, SDK de modelo, serviço pago ou integração SEI. Isso evitaria prometer compatibilidade executável sem interface especificada. O conteúdo foi estruturado para esses adaptadores consumirem os mesmos arquivos sem reescrever os procedimentos.

## Fontes de instalação

Verificadas em 20/10/2026. O pacote usa os caminhos de projeto documentados e não depende de números de versões de modelos.

- [OpenAI: skills em repositórios e `.agents/skills`](https://developers.openai.com/blog/skills-agents-sdk)
- [OpenAI: migração de skills e distinção de agentes](https://developers.openai.com/cookbook/examples/agents_sdk/migrate-from-claude-agent-sdk/readme)
- [Claude Code: skills](https://code.claude.com/docs/en/skills)
- [Claude Code: agentes, escopo e skills pré-carregadas](https://code.claude.com/docs/en/sub-agents)

Instalações gerenciadas podem restringir caminhos ou carregar apenas skills aprovadas. Confira a política efetiva do seu ambiente. Os testes deste pacote não substituem um teste de descoberta dentro de cada produto.
