# Conceptos importantes

## Llave Candidata

Sea $K$ un conjunto de atributos $\set{A_1, A_2, ..., A_n}$ de una esquema relacional $R(U, F)$ es
llave candidata candidata del esquema si cumple las siguientes propiedades:

1. **Unicidad**: $K_F^+ = U$
2. **Minimalidad**: Ningún subconjunto propio de $K$ tiene la propiedad de unicidad.

## Atributo Primo

Si un atributo $X$ es **parte de alguna llave candidata** de un esquema relacional $R(U,F)$,
entonces se dice que $X$ es un **atributo llave o primo**.

## Atributo No Primo

Si un atributo $X$ no **contiene ni forma parte de ninguna llave candidata**, entonces se dice que $X$ es un **atributo no llave o no primo**
## Superllave

Dado un esquema relacional $R(U,F)$ un atributo $X \subseteq U$ es **superllave** de $R$ y existe un atributo $Y \subset X$ tal que $Y_F^+ = U$.
O sea, si algún subconjunto propio de él es llave candidata.

## Formas normales

Un esquema relacional $R(U,F)$ está en:
- **1FN**: Si todos los atributos simples toman un solo valor del dominio subyacente.
- **2FN**: Si está en **1FN** y todo [[#Atributo No Primo]] depende completamente de toda llave candidata.
- **3FN**: Si está en **2FN** y todos los atributos **no primos** son **mutuamente independientes**.
- **BCFN**: Si cada uno de sus determinantes es una [[#Superllave]] o [[#Llave Candidata]] del esquema.