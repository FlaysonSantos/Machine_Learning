# 💡 Monitor de Produção com Lean Six Sigma e IA

Este projeto simula uma linha de produção industrial e utiliza Machine Learning para detectar anomalias e gargalos, com base em indicadores como volume, tempo de ciclo e refugo. 
Ideal para aplicação em ambientes industriais com foco em melhoria contínua (DMAIC).

## 🔧 Tecnologias Utilizadas
- Python (Pandas, Scikit-Learn, Joblib)
- Flask (API de inferência)
- Streamlit (Dashboard interativo)
- Lean Six Sigma (DMAIC aplicado ao fluxo de análise)
- Render.com ou HuggingFace Spaces (Deploy)

## 📁 Estrutura
- `data/`: dados simulados da linha de produção
- `modelo/`: modelo treinado com Isolation Forest
- `app/`: API Flask para previsão
- `dashboard/`: dashboard Streamlit para visualização

## 🚀 Como Rodar o Projeto Localmente
```bash
git clone https://github.com/SEU-USUARIO/leanai-producao.git
cd leanai-producao
pip install -r requirements.txt
streamlit run dashboard/streamlit_app.py
