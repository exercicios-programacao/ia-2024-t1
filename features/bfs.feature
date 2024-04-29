Feature: Procura em grafo por Depth First Search

Scenario Outline: Encontrar um caminho em um grafo do arquivo "mini_map.txt" 
Given a descrição de um grafo a partir do arquivo "mini_map.txt"
    And vértice inicial é <start>
    And vértice final é <goal>
When eu procuro o menor caminho com BFS
Then o número de vértices analisados é <count>
    And o caminho encontrado é <path>
Examples:
    | start | goal | count | path            |
    |   0   |  7   |  5,6  | [0, 2, 9, 5, 7]; [0, 1, 2, 3, 5, 7] |
    |   0   |  9   |   1   | [0, 9] |
    |   3   |  7   |   4   | [3, 4, 7] |
    |   0   |  6   |  3,4  | [0, 2, 9, 6]; [0, 1, 2, 9 ,6] |

Scenario Outline: Encontrar um caminho em um grafo do arquivo "small_map.txt" 
Given a descrição de um grafo a partir do arquivo "small_map.txt"
    And vértice inicial é <start>
    And vértice final é <goal>
When eu procuro o menor caminho com BFS
Then o número de vértices analisados é <count>
    And o caminho encontrado é <path>
Examples:
    | start | goal | count | path            |
    |   0   | 764  |  717, 733  | [0, 383, 374, 999, 296, 252, 261, 868, 867, 866, 869, 872, 871, 870, 855, 856, 857, 862, 859, 858, 764];[0, 383, 374, 999, 296, 252, 261, 868, 866, 869, 855, 870, 871, 471, 472, 848, 845, 779, 858, 764] |
    |   230 | 850  |  511, 413  | [230, 231, 243, 281, 227, 228, 302, 999, 296, 252, 261, 868, 867, 866, 869, 872, 871, 870, 855, 850];[230, 231, 243, 232, 299, 999, 296, 252, 261, 868, 866, 869, 855, 850] |
    |   0   |  20  |   84, 50  | [0, 16, 459, 20]; [0, 1, 2, 13, 14, 15, 16, 17, 459, 20] |
    |   0   |  6   |   55, 43  | [0, 383, 396, 1, 418, 3, 5, 6]; [0, 1, 2, 3, 5, 6] |
