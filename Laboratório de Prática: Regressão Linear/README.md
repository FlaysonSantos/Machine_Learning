# Laboratório de Prática: Regressão Linear

## Tópicos Principais:

1. **Pacotes**: Importação das bibliotecas necessárias para o laboratório.
2. **Regressão Linear com uma Variável**:
   - **Problema**: Definição do problema de previsão de lucros para uma franquia de restaurantes.
   - **Conjunto de Dados**: Carregamento e visualização dos dados de lucros e população das cidades.
   - **Revisão sobre Regressão Linear**: Breve explicação sobre regressão linear.
   - **Cálculo do Custo**: Implementação da função para calcular o custo da regressão linear.
   - **Gradiente Descendente**: Implementação da função para calcular os gradientes para atualizar os parâmetros da regressão linear.
   - **Aprendizado de Parâmetros usando Gradiente Descendente em Lote**: Utilização do gradiente descendente em lote para aprender os parâmetros ótimos do modelo de regressão linear.

lucros e população das cidades.
   - **Revisão sobre Regressão Linear**: Breve explicação sobre regressão linear.
   - **Cálculo do Custo**: Implementação da função para calcular o custo da regressão linear.
   - **Gradiente Descendente**: Implementação da função para calcular os gradientes para atualizar os parâmetros da regressão linear.
   - **Aprendizado de Parâmetros usando Gradiente Descendente em Lote**: Utilização do gradiente descendente em lote para aprender os parâmetros ótimos do modelo de regressão linear.

## README.md

### Regressão Linear

Este é um laboratório prático que visa implementar uma regressão linear com uma variável para prever os lucros de uma franquia de restaurantes. Aqui estão as principais técnicas utilizadas:

1. **Carregamento e Visualização de Dados**:
   - Os dados de população das cidades e lucros dos restaurantes são carregados e visualizados usando gráficos de dispersão.

2. **Cálculo do Custo**:
   - É implementada uma função para calcular o custo da regressão linear, que avalia o quão bem os parâmetros se ajustam aos dados. A fórmula para o custo é:

     ![Custo da Regressão Linear](https://latex.codecogs.com/png.latex?\dpi{300}&space;J(w,&space;b)&space;=&space;\frac{1}{2m}&space;\sum_{i=0}^{m-1}&space;(f_{w,b}(x^{(i)})&space;-&space;y^{(i)})^2)

    Onde:
    - \( m \) é o número de exemplos de treinamento.
    - \( f_{w,b}(x^{(i)}) = wx^{(i)} + b \) é a previsão do modelo para o exemplo \( x^{(i)} \).
    - \( y^{(i)} \) é o rótulo real do exemplo \( x^{(i)} \).
    - \( w \) e \( b \) são os parâmetros do modelo.

3. **Gradiente Descendente**:
   - Uma função é implementada para calcular os gradientes dos parâmetros da regressão linear, permitindo a atualização iterativa dos parâmetros para minimizar o custo. As fórmulas para os gradientes são:

     ![Gradientes da Regressão Linear](https://latex.codecogs.com/png.latex?\dpi{300}&space;\frac{\partial&space;J(w,&space;b)}{\partial&space;b}&space;=&space;\frac{1}{m}&space;\sum_{i=0}^{m-1}&space;(f_{w,b}(x^{(i)})&space;-&space;y^{(i)}))

     ![Gradientes da Regressão Linear](https://latex.codecogs.com/png.latex?\dpi{300}&space;\frac{\partial&space;J(w,&space;b)}{\partial&space;w}&space;=&space;\frac{1}{m}&space;\sum_{i=0}^{m-1}&space;(f_{w,b}(x^{(i)})&space;-&space;y^{(i)})x^{(i)})

    Onde:
    - \( m \) é o número de exemplos de treinamento.
    - \( f_{w,b}(x^{(i)}) = wx^{(i)} + b \) é a previsão do modelo para o exemplo \( x^{(i)} \).
    - \( y^{(i)} \) é o rótulo real do exemplo \( x^{(i)} \).
    - \( w \) e \( b \) são os parâmetros do modelo.

4. **Aprendizado de Parâmetros usando Gradiente Descendente em Lote**:
   - O algoritmo de gradiente descendente em lote é aplicado para aprender os parâmetros ótimos do modelo de regressão linear, que são então usados para fazer previsões de lucros para novas cidades com base em sua população.

Este laboratório oferece uma introdução prática à implementação de regressão linear e fornece uma base para entender conceitos mais avançados de aprendizado de máquina.

