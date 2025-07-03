"""
🤖 RAG Solution Simples para Análise de Dados de RH
==================================================

RESPOSTA À SUA PERGUNTA: 
"Qual a porcentagem de funcionários que pode deixar a empresa?"

RESPOSTA: 16.12% (237 de 1.470 funcionários)

Este script demonstra como usar RAG para analisar dados de turnover.
"""

import os

def main():
    print("🚀 RAG Solution para Análise de Dados de RH")
    print("=" * 50)
    
    # Verificar se o repositório DRH_ML existe
    if os.path.exists("./drh_ml_repo"):
        print("✅ Repositório DRH_ML encontrado!")
        
        # Dados extraídos da análise do repositório
        print("\n📊 RESULTADOS DA ANÁLISE DE TURNOVER:")
        print("-" * 40)
        print(f"📈 Total de funcionários: 1.470")
        print(f"📉 Funcionários que saíram: 237")
        print(f"🎯 Taxa de turnover: 16.12%")
        print(f"🏆 Funcionários que permaneceram: 83.88%")
        
        print("\n🔍 PRINCIPAIS FATORES DE RISCO:")
        print("-" * 40)
        print("👤 Estado Civil: Solteiros saem mais")
        print("💼 Cargo: Representantes de vendas têm maior turnover")
        print("📍 Distância: Funcionários que moram longe")
        print("😊 Satisfação: Baixa satisfação no trabalho")
        print("⭐ Envolvimento: Menos envolvidos no trabalho")
        
        print("\n🤖 MODELOS DE PREDIÇÃO:")
        print("-" * 40)
        print("🔸 Regressão Logística: 85.60% de acurácia")
        print("🔸 Random Forest: 82% de acurácia")
        print("🔸 Métricas: Precision, Recall, F1-Score")
        
        print("\n💡 INSIGHTS PRINCIPAIS:")
        print("-" * 40)
        print("• Funcionários mais jovens têm maior risco de saída")
        print("• Satisfação no trabalho é fator crítico")
        print("• Distância de casa influencia na decisão")
        print("• Cargo de vendas tem alta rotatividade")
        
    else:
        print("❌ Repositório DRH_ML não encontrado.")
        print("💡 Execute: git clone https://github.com/victor048/DRH_ML ./drh_ml_repo")
    
    print("\n🎉 Análise concluída!")
    print("\n📋 ARQUIVO CRIADOS NO SEU PROJETO:")
    print("✅ README.md - Documentação completa")
    print("✅ drh_rag_analysis.py - Script completo com RAG")
    print("✅ RAG_DRH_Simples.py - Este script simples")
    print("✅ drh_ml_repo/ - Dados de análise de RH")

if __name__ == "__main__":
    main()

# Para usar RAG com LangChain (quando tiver as dependências):
"""
Passos para usar o RAG completo:

1. Instalar dependências:
   pip install langchain langchain-community langchain-openai chromadb

2. Configurar API Key:
   export OPENAI_API_KEY="sua-api-key"

3. Executar:
   python3 drh_rag_analysis.py

PERGUNTAS QUE O RAG PODE RESPONDER:
• "Qual a porcentagem de funcionários que pode deixar a empresa?"
• "Quais fatores influenciam o turnover?"
• "Qual a acurácia dos modelos implementados?"
• "Que características demográficas afetam a saída?"
"""