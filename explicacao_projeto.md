# O que faz este projeto?

## RAGExemplo - Sistema de Perguntas e Respostas sobre Documentos PDF

Este projeto implementa um sistema **RAG (Retrieval-Augmented Generation)** que permite fazer perguntas sobre o conteúdo de documentos PDF e receber respostas inteligentes geradas por IA.

### Como funciona:

1. **Carregamento de PDF**: O sistema carrega um arquivo PDF e extrai todo o texto
2. **Divisão em Chunks**: O documento é dividido em pequenos pedaços (chunks) de texto para facilitar o processamento
3. **Criação de Embeddings**: Cada chunk é convertido em representações vetoriais (embeddings) usando OpenAI
4. **Armazenamento Vetorial**: Os embeddings são salvos em um banco de dados vetorial (Chroma) para busca eficiente
5. **Sistema de Perguntas**: Quando você faz uma pergunta:
   - O sistema busca os chunks mais relevantes no banco de dados
   - Usa um modelo de linguagem (GPT-3.5-turbo) para gerar uma resposta baseada no contexto encontrado

### Tecnologias utilizadas:

- **LangChain**: Framework para construção de aplicações com LLMs
- **OpenAI**: Para embeddings e modelo de linguagem (GPT-3.5-turbo)
- **Chroma**: Banco de dados vetorial para armazenar embeddings
- **PyPDFLoader**: Para extrair texto de arquivos PDF

### Objetivo:

Permitir que usuários façam perguntas específicas sobre documentos PDF longos e recebam respostas precisas e contextualizadas, sem precisar ler todo o documento manualmente.

Este é um exemplo prático de como implementar um sistema de busca semântica e geração de respostas aumentada por recuperação (RAG).