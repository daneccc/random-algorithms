# Graph Algorithms

## Breath-first search (BFS)
<b>Resumo:</b> ao descobrir um vértice <i><b>s</b></i>, visite todos os seus vizinhos não visitados (ou seja, brancos), antes de visitar os vizinhos de seus vizinhos. Em seguida, visite os vizinhos, aplicando o mesmo princípio de busca. 
Nesse algoritmo, visitamos apenas os vértices alcançáveis a partir de <i><b>s</b></i>. Logo, o Grafo é uma árvore.

```
Algorithm 1: Algoritmo de Busca em Largura – ABL
Input: Um grafo (ou digrafo) G = (V, E) e um vértice s ∈ V (G)
Output: Vetores d e pai
  1 for todo v ∈ V(G) do
  2   cor[v] = branca;
  3   pai[v] = T;
  4   d[v] = ∞
  5 end
  6 Q = ∅;
  7 d[s] = 0;
  8 cor[s] = cinza
  9 Enfila(Q, s);
 10   while Q != ∅ do
 11   u = Desenfila(Q);
 12   for todo v ∈ Adj[u] do
 13     if cor[v] == branca then
 14       pai[v] = u;
 15       d[v] = d[u] + 1;
 16       cor[v] = cinza;
 17       Enfila(Q, v);
 18   end
 19   cor[u] = preta;
 20 end
```
