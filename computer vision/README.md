# LAB **Classificação de imagens usando aumento de dados**

**Visão geral**

- Neste laboratório, terei como foco como configurar o pré-processamento para garantir a reprodutibilidade na produção e, em seguida, se aprofundar nas maneiras de implementar diversas operações de pré-processamento no Keras/TensorFlow. também abordaremos como realizar o aumento de dados para melhorar a resiliência e a precisão do modelo.

- A criação de conjuntos de dados de treinamento para aprendizado de máquina é a primeira etapa do pipeline de processamento de imagem padrão. A próxima etapa é o pré-processamento das imagens brutas para alimentá-las no modelo para treinamento ou inferência. Antes que as imagens brutas possam ser alimentadas em um modelo de imagem, elas geralmente precisam ser pré-processadas. Esse pré-processamento tem vários objetivos sobrepostos: transformação de forma, qualidade de dados e qualidade de modelo.

- O aumento de dados pode ser usado com eficácia para treinar os modelos de aprendizado profundo. Algumas das transformações simples aplicadas à imagem são; transformações geométricas como inversão, rotação, translação, corte e dimensionamento.

## task 1 Iniciar uma instância do Notebooks

- Clonar um repositório de curso  clonar o notebook do analista de dados de treinamento em sua instância do JupyterLab:

-- No JupyterLab, para abrir um novo terminal, clique no ícone Terminal .

-- No prompt da linha de comando, execute o seguinte comando:

git clone https://github.com/GoogleCloudPlatform/training-data-analyst

- Para confirmar que você clonou o repositório, clique duas vezes no diretório training-data-analyst e certifique-se de ver seu conteúdo.
Os arquivos de todos os laboratórios baseados em notebook Jupyter ao longo deste curso estão disponíveis neste diretório.

## task 2 Classificar imagens usando aumento de dados

- Na interface do notebook, navegue até training-data-analyst > course > machine_learning > deepdive2 > computer_vision_fun > labs e abra classifying_images_using_data_augmentation.ipynb .

- Na interface do notebook, clique em Editar > Limpar todas as saídas .

- Iremos preencha as linhas marcadas com #TODO onde iremos completar o código.

- Dica : Para executar a célula atual, clique na célula e pressione SHIFT+ENTER. Outros comandos de célula estão listados na interface do notebook em Run .



