# Laboratorio Usando dados do mundo real

## Introdução

- Até agora, o trabalho foi feito com dados gerados.
- Agora, os dados do conjunto de dados "[Daily Minimum Temperatures in Melbourne](https://github.com/jbrownlee/Datasets/blob/master/daily-min-temperatures.csv)" serão usados.
- Os dados contêm as temperaturas mínimas diárias registradas em Melbourne de 1981 a 1990.
- Além das camadas de processamento de dados de sequência do Tensorflow, como camadas Recurrent ou LSTMs, as camadas Convolutional também serão usadas para melhorar o desempenho do modelo.

## Análise dos Dados

- Exibição da estrutura do arquivo CSV que contém os dados.
- Cada ponto de dados é composto pela data e pela temperatura mínima registrada para essa data.

## Função para Ler Dados

- Uma função chamada `parse_data_from_file` é apresentada para ler os dados do arquivo CSV.
- A função remove o cabeçalho do arquivo e armazena os dados em listas.
- Os tempos são armazenados como uma sequência de números ordenados, enquanto as temperaturas são armazenadas como números de ponto flutuante.

## Visualização dos Dados

- Os dados são lidos usando a função `parse_data_from_file`, e os tempos e temperaturas são armazenados como arrays numpy na classe `G`.
- Uma visualização das séries temporais é exibida.

## Processamento dos Dados

- Funções `train_val_split` e `windowed_dataset` são fornecidas para dividir os dados em conjuntos de treinamento e validação e criar conjuntos de dados em janelas.
- As funções usam TensorFlow Dataset para criar janelas deslizantes e configurar os dados para treinamento.

## Definição da Arquitetura do Modelo

- A função `create_uncompiled_model` é apresentada para definir a arquitetura do modelo.
- O modelo é uma sequência de camadas, incluindo camadas Conv1D, LSTMs e camadas Dense.
- As camadas são usadas para processar as sequências de dados.

## Ajuste da Taxa de Aprendizado (Opcional)

- Uma função chamada `adjust_learning_rate` é apresentada para ajustar dinamicamente a taxa de aprendizado durante o treinamento.
- Os otimizadores Adam e SGD com momento são sugeridos.
- O modelo é compilado com a função de perda Huber e a taxa de aprendizado é ajustada ao longo das épocas.

## Compilação do Modelo

- A função `create_model` é definida para compilar o modelo.
- O modelo é compilado com a função de perda Huber e o otimizador SGD com momento.

## Avaliação da Previsão

- A função `compute_metrics` é usada para calcular métricas de avaliação, como erro quadrático médio (MSE) e erro médio absoluto (MAE).

## Previsão do Modelo

- A função `model_forecast` é definida para fazer previsões usando o modelo treinado.
- O modelo é usado para prever lotes de dados.
- As previsões são calculadas para o conjunto de validação.

## Resultados da Previsão

- As previsões do modelo são plotadas junto com os dados reais de validação.
- As métricas MSE e MAE são calculadas para avaliar o desempenho do modelo.

