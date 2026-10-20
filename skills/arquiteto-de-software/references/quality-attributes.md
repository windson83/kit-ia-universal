# Quality Attributes — triagem de requisitos não funcionais

Carregado quando: definindo arquitetura nova, revisando arquitetura existente, ou qualquer
decisão onde um requisito não funcional pode mudar a resposta certa.

## Lista de atributos a considerar

Segurança, Privacidade, Confiabilidade, Disponibilidade, Resiliência, Escalabilidade,
Performance, Latência, Capacidade, Custo, Observabilidade, Operabilidade,
Manutenibilidade, Evolutibilidade, Portabilidade, Compliance, Recuperação de desastre
(RTO/RPO), Sustentabilidade.

Nem todos se aplicam a todo problema. Triagem primeiro, profundidade depois.

## Classificação

Para cada atributo, classifique:

```text
CRÍTICO       — o sistema falha no propósito se isso não for atendido
RELEVANTE     — importa, mas não é o que define a arquitetura
NÃO RELEVANTE — pode ser ignorado neste contexto sem prejuízo real
```

Para todo atributo classificado como **CRÍTICO**, busque uma métrica objetiva antes de
prosseguir. Se a métrica não existe ainda, registre a lacuna explicitamente em vez de
inventar um número ou seguir sem ela.

## Vago vs. objetivo

Nunca aceite (nem escreva) isto como requisito final:

```text
deve ser rápido
deve escalar bem
deve ter alta disponibilidade
```

Prefira sempre que possível:

```text
p95 < 300 ms
99,9% de disponibilidade
RPO <= 5 minutos
RTO <= 30 minutos
10.000 requisições/minuto
```

Se o usuário ou o time ainda não tem esse número, isso é uma **questão em aberto**, não uma
suposição para preencher sozinho. Pergunte ou registre a lacuna — não adivinhe um número
"razoável" e o trate como fato.

## Como usar na prática

1. Rode a triagem completa uma vez, no início de uma decisão de arquitetura relevante.
2. Descarte rápido os "não relevantes" — não gaste tempo neles.
3. Para os "relevantes", mantenha em mente ao comparar opções (vira linha de comparação nos
   trade-offs), mas não force métrica objetiva se ninguém vai cobrar isso.
4. Para os "críticos", a métrica objetiva é obrigatória antes de declarar a arquitetura
   pronta — eles são o que de fato vai definir a decisão certa.
