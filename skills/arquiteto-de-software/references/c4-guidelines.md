# C4 Model — quando e como usar cada nível

Carregado quando: a arquitetura em jogo é grande ou complexa o suficiente para se
beneficiar de um diagrama formal, além de um simples ASCII de módulos.

## Regra geral

Use o nível mínimo que comunica boundaries, responsabilidades, dependências e fluxos com
clareza. Não produza documentação visual em excesso — cada nível extra é mais um artefato
pra manter atualizado.

```text
C4 Level 1 — System Context
  Use quase sempre que o sistema interage com outros sistemas ou atores externos.
  Mostra: o sistema como uma caixa, quem/o que interage com ele.

C4 Level 2 — Container
  Use quando o sistema tem múltiplos componentes deployáveis separadamente
  (serviços, bancos, filas, front-end).
  Mostra: os containers e como se comunicam.

C4 Level 3 — Component
  Use só quando o nível de detalhe interno de um container específico agrega valor real
  para a decisão em jogo — ex: quando o boundary interno de um serviço grande é o próprio
  motivo da discussão.
  Não produza Component para todo container só por completude.
```

## Formato

ASCII é suficiente na maioria dos casos:

```text
┌─────────────┐      HTTPS       ┌──────────────┐
│  Front-end  │ ───────────────► │   API REST   │
└─────────────┘                  └──────┬───────┘
                                         │
                              ┌──────────┴──────────┐
                              │                     │
                        ┌─────▼─────┐         ┌─────▼─────┐
                        │  Postgres │         │   Redis   │
                        └───────────┘         └───────────┘
```

Use Mermaid quando o ambiente suporta renderização (ex: artifact publicado) e o diagrama
tem complexidade suficiente para justificar. Não force Mermaid onde ASCII já é claro.

Todo diagrama, independente do nível, deve deixar explícito:

- boundaries (onde um componente termina e outro começa);
- responsabilidade de cada caixa (uma frase, não um nome genérico);
- dependências (o que depende do quê, e a direção);
- fluxos principais (como uma requisição/evento atravessa o sistema).
