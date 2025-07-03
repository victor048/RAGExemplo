# 🤖 RAG Solution para Análise de Dados de RH

## 📋 Visão Geral

Este projeto utiliza **RAG (Retrieval-Augmented Generation)** para analisar dados de recursos humanos e predizer turnover de funcionários. O sistema combina inteligência artificial com análise de dados para fornecer insights valiosos sobre retenção de talentos.

## 🎯 Funcionalidades Principais

### 🔍 **Análise Inteligente de Turnover**
- Predição de quais funcionários podem deixar a empresa
- Análise de fatores que influenciam a saída de funcionários
- Identificação de padrões em dados de RH

### 📊 **Base de Conhecimento**
- **Dataset**: 1.470 funcionários com 35 variáveis
- **Taxa de Turnover**: 16.12% (237 funcionários)
- **Modelos ML**: Regressão Logística (85.6%) e Random Forest (82%)

### 🤖 **Sistema RAG**
- Busca semântica em dados e códigos de ML
- Respostas contextualizadas sobre RH
- Análise baseada em evidências dos dados

## 🔬 Principais Descobertas

### **Taxa de Turnover**
- **16.12%** dos funcionários deixaram a empresa
- **83.88%** permaneceram na organização

### **Fatores de Risco**
- 👤 **Estado Civil**: Solteiros saem mais
- 💼 **Cargo**: Representantes de vendas têm maior turnover
- 📍 **Distância**: Funcionários que moram longe
- 😊 **Satisfação**: Baixa satisfação no trabalho
- ⭐ **Envolvimento**: Menos envolvidos no trabalho

### **Modelos de Predição**
- **Regressão Logística**: 85.60% de acurácia
- **Random Forest**: 82% de acurácia
- **Métricas**: Precision, Recall, F1-Score

## 🛠️ Tecnologias Utilizadas

### **IA e Machine Learning**
- ![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
- ![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-blue)
- ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)

### **Dados e Visualização**
- ![Pandas](https://img.shields.io/badge/Pandas-Data-purple)
- ![Chroma](https://img.shields.io/badge/Chroma-VectorDB-red)
- ![Seaborn](https://img.shields.io/badge/Seaborn-Viz-lightblue)

### **Ambiente**
- ![Python](https://img.shields.io/badge/Python-3.8+-yellow)
- ![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

## 🚀 Como Usar

### **1. Pré-requisitos**
```bash
# Instalar dependências
pip install langchain langchain-community langchain-openai
pip install chromadb pandas scikit-learn seaborn matplotlib
```

### **2. Configurar API Key**
```bash
export OPENAI_API_KEY="sua-api-key-aqui"
```

### **3. Executar Análise**

#### **Opção A: Script Python**
```bash
python3 drh_rag_analysis.py
```

#### **Opção B: Jupyter Notebook**
```bash
jupyter notebook RAGSolution.ipynb
```

### **4. Fazer Perguntas**
O sistema pode responder perguntas como:
- "Qual a porcentagem de funcionários que pode deixar a empresa?"
- "Quais fatores influenciam o turnover?"
- "Qual a acurácia dos modelos implementados?"

## 📁 Estrutura do Projeto

```
📦 RAGExemplo/
├── 📄 README.md                    # Este arquivo
├── 📊 RAGSolution.ipynb           # Notebook original
├── 📊 RAGSolution_DRH.ipynb       # Notebook adaptado para RH
├── 🐍 drh_rag_analysis.py         # Script de análise
├── 📁 drh_ml_repo/                # Repositório DRH_ML
│   ├── 📊 MACHINE_LEARNING_para_DRH.ipynb
│   └── 📄 README.md
└── 📁 .git/                       # Controle de versão
```

## 🎯 Casos de Uso

### **Para Gestores de RH**
- 📈 Identificar funcionários em risco de saída
- 🎯 Focar estratégias de retenção
- 📊 Monitorar indicadores de turnover

### **Para Cientistas de Dados**
- 🔬 Analisar padrões em dados de RH
- 🤖 Implementar modelos preditivos
- 📋 Gerar relatórios automatizados

### **Para Executivos**
- 💰 Reduzir custos de recrutamento
- 🏆 Melhorar retenção de talentos
- 📊 Tomar decisões baseadas em dados

## 🔗 Links Relacionados

- 🗂️ **Dataset Original**: [Kaggle - Human Resources](https://www.kaggle.com/datasets/varunbarath/human-resources)
- 🔗 **Repositório DRH_ML**: [GitHub - victor048/DRH_ML](https://github.com/victor048/DRH_ML)
- 📚 **LangChain**: [Documentação Oficial](https://docs.langchain.com/)

## 📊 Resultados Esperados

Ao executar o sistema, você obterá:

```
📊 ANÁLISE DE TURNOVER DE FUNCIONÁRIOS - RESULTADOS
================================================================================

🔍 Pergunta 1: Qual a porcentagem de funcionários que pode deixar a empresa?
💡 Resposta: 16.12% dos funcionários podem deixar a empresa...

🔍 Pergunta 2: Quais são os principais fatores de influência?
💡 Resposta: Estado civil, satisfação no trabalho, distância de casa...

📋 Resumo dos achados principais:
   • 16.12% de taxa de turnover na empresa
   • Modelos implementados: Regressão Logística (85.6%) e Random Forest (82%)
   • Principais fatores: idade, estado civil, satisfação e cargo
   • Dataset com 1470 funcionários e 35 variáveis
```

## 🤝 Contribuição

Sinta-se à vontade para contribuir com:
- 🐛 Correções de bugs
- ✨ Novas funcionalidades
- 📚 Melhorias na documentação
- 🔬 Novos modelos de análise

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

**Desenvolvido por**: [victor048](https://github.com/victor048)  
**Tecnologia**: RAG + Machine Learning para RH  
**Ano**: 2024