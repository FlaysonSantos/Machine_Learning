
# Aprendizado de Máquina Supervisionado: Regressão e Classificação

## [Notebook do projeto Logistic_Regression](https://github.com/FlaysonSantos/Machine_Learning/blob/main/Supervised%20Machine%20Learning%3A%20Regression%20and%20Classification/Logistic_Regression.ipynb)

Este projeto é uma implementação prática de conceitos de aprendizado de máquina, especificamente focado em regressão logística regularizada. Aqui, o especialista em machine learning Flayson Santos apresenta uma série de exercícios resolvidos, abordando desde a implementação de funções básicas até a aplicação de gradient descent para aprender parâmetros ótimos e visualização dos resultados.

Nesta exploração, você vai:

- Compreender os conceitos fundamentais do aprendizado supervisionado.
- Conhecer algoritmos de regressão para prever resultados contínuos.
- Explorar métodos de classificação para categorizar dados em classes distintas.
- Aplicar técnicas avançadas para lidar com conjuntos de dados complexos e melhorar o desempenho do modelo.
- Descobrir aplicações do mundo real onde os algoritmos de aprendizado supervisionado desempenham um papel crucial na resolução de problemas diversos.
- Embarque nesta jornada enriquecedora para desbloquear o potencial do aprendizado de máquina supervisionado, abrindo caminho para soluções inovadoras e tomadas de decisão informadas.


## Exercício 1 - Função de Custo

Neste exercício, implementamos a função de custo para regressão logística. A função de custo é essencial para avaliar o desempenho do modelo de regressão logística e é definida como a média da perda logarítmica sobre todos os exemplos de treinamento.


### Descrição:
- Implementação da função de custo para regressão logística.
- A função `compute_cost` recebe os dados de entrada, os valores alvo, os parâmetros do modelo (pesos `w` e viés `b`) e calcula o custo usando a fórmula da entropia cruzada.
- O custo é a média da perda logarítmica sobre todos os exemplos de treinamento.

## Exercício 2 - Gradiente Descendente

Neste exercício, implementamos o algoritmo de gradiente descendente para otimizar os parâmetros de um modelo de regressão logística. O gradiente descendente é uma técnica de otimização amplamente utilizada para encontrar os parâmetros que minimizam a função de custo.

### Descrição:
- Implementação do algoritmo de gradiente descendente para otimizar os parâmetros de um modelo de regressão logística.
- A função `gradient_descent` recebe os dados de entrada, os valores alvo, os parâmetros iniciais do modelo (pesos `w` e viés `b`), a função de custo e a taxa de aprendizado.
- O algoritmo atualiza iterativamente os parâmetros em direção ao gradiente negativo da função de custo até convergir para o mínimo global ou atingir o número máximo de iterações.

## Exercício 3 - Predição

Neste exercício, implementamos a função de predição para um modelo de regressão logística. A função de predição calcula as probabilidades de classe para os exemplos de entrada e faz previsões com base nessas probabilidades.

### Descrição:
- Implementação da função de predição para um modelo de regressão logística.
- A função `predict` recebe os dados de entrada, os pesos `w` e o viés `b` do modelo e retorna previsões binárias (0 ou 1) com base nas probabilidades calculadas pelo modelo.

## Exercício 4 - Predição com Limiar

Neste exercício, implementamos a função de predição usando um limiar de decisão para um modelo de regressão logística. A função de predição classifica os exemplos de entrada como positivos ou negativos com base na probabilidade calculada pelo modelo.

### Descrição:
- Implementação da função de predição usando um limiar de decisão para um modelo de regressão logística.
- A função `predict` recebe os dados de entrada, os pesos `w` e o viés `b` do modelo e retorna previsões binárias (0 ou 1) com base nas probabilidades calculadas pelo modelo.

## Exercício 5 - Custo Regularizado

Neste exercício, implementamos a função de custo para regressão logística com regularização. A regularização é uma técnica usada para prevenir o overfitting ao adicionar uma penalidade aos parâmetros do modelo.

### Descrição:
- Implementação da função de custo para regressão logística com regularização.
- A função `compute_cost_reg` recebe os dados de entrada, os valores alvo, os parâmetros do modelo (pesos `w` e viés `b`), e a constante de regularização `lambda_` e calcula o custo regularizado.

## Exercício 6 - Gradiente Regularizado

Neste exercício, implementamos o gradiente para regressão logística com regularização. O gradiente regularizado é usado para otimizar os parâmetros do modelo, levando em consideração a regularização.


### Descrição:
- Implementação do gradiente para regressão logística com regularização.
- A função `compute_gradient_reg` recebe os dados de entrada, os valores alvo, os parâmetros do modelo (pesos `w` e viés `b`), a constante de regularização `lambda_` e calcula o gradiente da função de custo com regularização.

Cada exercício é acompanhado por uma descrição detalhada e testes unitários para verificar a implementação.
