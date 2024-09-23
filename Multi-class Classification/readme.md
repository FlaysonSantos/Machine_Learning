Olá, meu nome é Flayson Santos e sou um especialista em Machine Learning. Hoje, vou guiá-los pelo processo de desenvolvimento de uma rede neural convolucional (CNN) para classificação de imagens em tons de cinza. Vamos começar com a visualização dos dados.

Visualizando os Arrays de Imagem
Para garantir que nossos dados estão prontos para serem utilizados, a primeira etapa foi converter os dados do formato CSV para arrays NumPy compatíveis com tarefas de visão computacional. Depois, visualizei uma amostra de 10 imagens do conjunto de dados de treino. Cada imagem foi rotulada com uma letra correspondente para facilitar o entendimento.

A função que criei, chamada plot_categories, desenha essas imagens utilizando o matplotlib e adiciona títulos mostrando as letras que representam. Com isso, tive uma visão clara de como o modelo verá os dados.

Criando os Geradores de Dados
A seguir, implementei os geradores de dados que irão alimentar minha rede neural. Isso foi feito utilizando a classe ImageDataGenerator do Keras, que me permitiu fazer aumentos de dados para o conjunto de treinamento. Implementei técnicas como rotação, deslocamento e espelhamento, que ajudaram a enriquecer a diversidade dos dados e, assim, evitar overfitting.

O gerador de validação, por outro lado, foi mais simples. Apenas normalizei os valores de pixel, já que não precisamos de aumentos no conjunto de validação.

Esses geradores foram cruciais para garantir que o modelo treinasse de forma eficiente e aproveitasse ao máximo os dados que possuímos.

Definindo a Arquitetura da CNN
Agora, chegamos à parte central: a criação do modelo da CNN. Para isso, decidi usar uma abordagem sequencial com duas camadas convolucionais e duas camadas de pooling. Essas camadas de convolução detectam padrões em diferentes partes da imagem, enquanto as camadas de pooling ajudam a reduzir a dimensionalidade e preservar os recursos mais importantes.

Após isso, adicionei uma camada totalmente conectada com 512 neurônios para melhorar a capacidade de aprendizado do modelo e, finalmente, a camada de saída, com 26 neurônios (um para cada letra do alfabeto), usando a função de ativação softmax para classificação multiclasse.

Compilando o modelo com o otimizador Adam e a função de perda sparse_categorical_crossentropy, estava pronto para treinar.

Treinando o Modelo
Com o modelo criado e compilado, executei o treinamento em 15 épocas. Durante o treinamento, acompanhei de perto a evolução da acurácia e da perda para os conjuntos de treino e validação.

Os primeiros resultados mostraram uma acurácia inicial de cerca de 19%, o que era esperado. Mas, conforme o modelo foi aprendendo, a acurácia subiu rapidamente, chegando a cerca de 86% no conjunto de treino e 94% no conjunto de validação ao final do treinamento. Esse progresso demonstrou que o modelo estava realmente capturando bem os padrões das imagens.

Visualizando os Resultados
Por fim, para analisar melhor o desempenho, criei gráficos de acurácia e perda para os conjuntos de treino e validação. Esses gráficos me permitiram observar de forma clara como o modelo foi se ajustando ao longo do tempo e quando começou a estabilizar.

Conclusão

Essa CNN demonstrou resultados promissores na classificação de imagens de letras do alfabeto. O uso de técnicas de aumento de dados, junto com uma arquitetura eficiente e o acompanhamento do desempenho, foi fundamental para o sucesso deste projeto.

Foi uma experiência incrível aplicar essas técnicas e observar o progresso ao longo das 15 épocas de treinamento. Agora, com os resultados em mãos, posso seguir para ajustes e possíveis otimizações no modelo.

Muito obrigado por me acompanharem nesta jornada!
