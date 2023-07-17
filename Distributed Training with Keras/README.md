**Visão geral**

A API tf.distribute.Strategy fornece uma abstração para distribuir seu treinamento em várias unidades de processamento.
O objetivo é permitir que os usuários habilitem o treinamento distribuído usando modelos e código de treinamento existentes, com alterações mínimas.

Este laboratório usa o tf.distribute.MirroredStrategy, que faz replicação no gráfico com treinamento síncrono em várias GPUs em uma máquina.
Essencialmente, ele copia todas as variáveis ​​do modelo para cada processador. Em seguida, ele usa all-reduce para combinar os gradientes de todos
os processadores e aplica o valor combinado a todas as cópias do modelo.

MirroredStrategy é uma das várias estratégias de distribuição disponíveis no núcleo do TensorFlow. 
Para obter mais informações sobre estratégias, consulte o guia de estratégia de distribuição .

**Objetivos de aprendizado**

1. Como definir a estratégia de distribuição e definir o pipeline de entrada.
2. Como criar o modelo Keras.
3. Como definir os callbacks.
4. Como treinar e avaliar o modelo.
