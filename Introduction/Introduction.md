# What is Langchain

- Open Source framework for developing applications powered by Large Language Model (LLM)

# Why do you need Langchain or challenges?

- Understaning NLP + context aware response generation
  - solved with LLM + exposure of LLM via API
- how to handle computation requirements of LLM
  - solved with major companies like openai
  - hosted on company server and exposed llm via api for communication
- workflow orchestration (based on sample usecase of finding results in a book based on user query
  - S3, Text Splitter, Embedding, Database, LLM
  - Langchain provides e2e orchestration for all the components involved in llm application
 
# Additional Benefits

- Chains
  - pipleine of different components / tasks
  - output of one component becomes input for next steps

- Model Agnostic development
   - Flexibility of using any LLM model, think of this like terraform

- Ecosystem
   - Lot of batteries available out of box for components

- Memory and state handling
   - retains conversations states (conversations happened in the past)
 
# Sample Use cases

- Conversation chat bots
- AI Knowledge assistants
- AI Agents
   - Chatbots on steroids
   - Not only conversations but can also perform tasks in the background
   - 
- Workflow automation
- Summarize / Research Helpers

# Alternates

- llamaindex
- haystack
