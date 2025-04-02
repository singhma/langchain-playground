# Langchain components

- Models
  - Core interface (API) through which you interact with AI Models (LLM)
    - Different AI company exposes API for LLM Models in a different manner
    - Langchain solved this problem by developing an interface (API) where you can talk to multiple models from different companies with little changes to code.
    - Langchain you can interact with two types of models
      - Language Models
        - LLM (text input --> text output)
      - Embedding Models
        - text as input --> returns vector as outputs
        - main use case: semantic search
          
- Prompts
  - inputs provided to LLM
  - outputs of LLM is dependent on how well the prompts are created
  - different types of prompts
    
    - Dynamic and Reusable prompts
      ```python
      from langchain_core.prompts import PromptTemplate
      prompt = PromptTemplate.from_template('Summarise {topic} in {emotion} tone')
      print(prompt.format(topic='Cricket', emotion='fun'))
      ```
      
    - Role Based Prompts
     ```python
     # Define the ChatPromptTemplate using from_template

     chat_promot = ChatPromptTemplate([
    ("system","Hi you are a experience {profession}),
    ("user"."Tell me about {topic}),
     ])

     formatted_message = chat_prompt.format_messages(profession='doctor',topic='viral fever')
     ```
    - Few Shots Prompting
      
- Chains
  - chains helps in building pipelines
  - example
    - input -> large text
    - output -> Summarise in less then 100 words
    - potential tasks that can be defined as pipeline
      - input --> llm --> transalation --> another llm --> summarise in other language
      - if chains are not used, you will have to take care of outputs of every stage and then use that as input for next stage (chains take care of this out of box)
      - can handle complex pipeline like parallel chains, sequential chains, conditional

- Indexes
  - Connects your application to external sources such as pdf, websites or databases
  - what makes indexes
    - Document Loader
    - Text Splitter
    - Vector Store
    - Retrievers
      
- Memory
  - LLM API calls are stateless
  - Type of Memory
    - Conversation Buffer Memory
      - Store a transcript of recent message. Great for short chats but can grow large quickly
    - Conversation Buffer Window Memory
      - only keeps last N interactions to avoid excessive token usage
    - Summarizer based Memory
      - periodically summarizes older chat segments to keep a condensed memory footprint, that is we sent summary to api call
    - Custom Memory
      - For advanced use cases, you can store specialised state (eg user preference or key facts) in a custom memory class
     
        
- Agents
  - helps in building AI Agents
  - allows to perform some task (other then understanding NLU + text generation)
  - has reasoning capabilities
  - tool access
