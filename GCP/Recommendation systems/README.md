# Sistema de Recomendação com Aprendizado por Reforço e TensorFlow

Este projeto utiliza técnicas de Aprendizado por Reforço para aprimorar sistemas de recomendação, com implementação em TensorFlow e armazenamento em nuvem.

## Objetivos de Aprendizado

1. **Configuração Inicial:**
   - Instalação e importação de bibliotecas necessárias.
   - Inicialização e configuração do ambiente MovieLens.

2. **Inicialização do Ambiente MovieLens:**
   - Carregamento do conjunto de dados MovieLens armazenado em nuvem.
   - Inicialização do ambiente MovieLens com parâmetros personalizados.

3. **Inicialização do Agente:**
   - Implementação de um agente de escolha de ações baseado em Epsilon-Greedy.
   - Configuração de uma rede neural profunda para estimar valores de Q.

4. **Definição e Vinculação de Métricas de Avaliação:**
   - Utilização de métricas como Regret e Suboptimal Arms para avaliar o desempenho.
   - Configuração de métricas para TensorBoard.

5. **Inicialização e Configuração do Buffer de Repetição:**
   - Uso do TFUniformReplayBuffer para armazenar trajetórias de experiência.
   - Configuração do buffer para armazenar e reutilizar dados de forma eficiente.

6. **Configuração e Treinamento do Modelo:**
   - Utilização do DynamicStepDriver para coletar experiência do ambiente.
   - Treinamento do agente com base nas trajetórias armazenadas no buffer de repetição.
   - Monitoramento e registro contínuo de métricas durante o treinamento.

7. **Inferência com Modelo Treinado e Avaliação no TensorBoard:**
   - Demonstração de como realizar inferências com o modelo treinado.
   - Envio dos logs do TensorBoard para análise e visualização do desempenho.

## Como Utilizar

1. Clone o repositório: `https://github.com/FlaysonSantos/Machine_Learning.git`
2. Navegue ate `https://github.com/FlaysonSantos/Machine_Learning/GCP/Recommendation systems`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o notebook Jupyter: `jupyter notebook exercise_movielens_notebook.ipynb`

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

