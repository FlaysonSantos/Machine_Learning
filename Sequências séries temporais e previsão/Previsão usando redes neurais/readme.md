# Previsão de Séries Temporais com Redes Neurais Profundas

Este projeto demonstra o uso de redes neurais profundas para prever séries temporais sintéticas. A rede neural é treinada e avaliada usando TensorFlow, uma biblioteca popular de aprendizado de máquina e aprendizado profundo. 

[Codigo do projeto](https://github.com/FlaysonSantos/Machine_Learning/blob/main/Sequ%C3%AAncias%20s%C3%A9ries%20temporais%20e%20previs%C3%A3o/Previs%C3%A3o%20usando%20redes%20neurais/Previs%C3%A3o%20usando%20redes%20neurais.ipynb)

## Resumo do Código

1. **Introdução**
   - Este projeto utiliza uma rede neural profunda para fazer previsões em séries temporais.
   - Os dados são gerados internamente no código.

2. **Geração de Dados**
   - O código define funções para gerar e plotar séries temporais sintéticas.
   - As séries temporais geradas possuem tendência, sazonalidade e ruído.

3. **Divisão dos Dados**
   - Os dados são divididos em conjuntos de treinamento e validação.

4. **Processamento de Dados**
   - O código contém uma função `windowed_dataset` que processa os dados para treinamento da rede.
   - Essa função cria janelas deslizantes de dados para treinamento.

5. **Definição da Arquitetura do Modelo**
   - A função `create_model` define a arquitetura da rede neural, com camadas densas.

6. **Treinamento do Modelo**
   - O modelo é treinado com os dados de treinamento usando um otimizador SGD (Gradiente Descendente Estocástico).

7. **Avaliação das Previsões**
   - O código contém uma função `compute_metrics` para calcular métricas de erro, como MSE e MAE.
   - As previsões do modelo são geradas e avaliadas em relação aos dados de validação.

8. **Salvar o Modelo**
   - O modelo treinado é salvo em um arquivo HDF5 para uso futuro.

9. **Tecnologias Utilizadas**
   - Python: A linguagem de programação principal em que o código está escrito.
   - TensorFlow: Uma biblioteca de aprendizado de máquina e aprendizado profundo utilizada para construir e treinar redes neurais.
   - NumPy: Uma biblioteca para computação numérica em Python, frequentemente usada para manipulação de dados.
   - Matplotlib: Uma biblioteca para criação de gráficos e visualização de dados em Python, usada para plotar séries temporais e resultados.
   - Jupyter Notebook: Um ambiente interativo que combina código, texto explicativo e visualizações, ideal para desenvolvimento e documentação de projetos em Python.

Para executar este código e criar previsões em séries temporais, siga as instruções fornecidas neste README.md.

---

**Observação**: Certifique-se de ter as dependências do Python instaladas para executar o código com sucesso.

Para informações detalhadas sobre a implementação, leia o código-fonte e consult
