# Langchain Models

- Facilitates interactions with various languages and embedding models
- abstracts the complexity of working directly with different LLM, chat models and embedding models thereby providing uniform interface to communicate with them
- facilitates building applications easily that relies on AI generated text, text embeddings for similarity search and Retrieval Augmented information (RAG)

## Types of Models

- Language Models

  - Understands text vi NLU and responsds with texts
  - use case like chatbot applications
  - can be closed source like (openai, claude, gemini) or open source like (hugging face)
  - **Language Models are of two types**

    - LLM - General Purpose models - used for raw text generation, text summarisation, code generations, questions / answers - input (text) --> output (text)
    - Chat Models - specialised language model for conversational tasks - takes sequences of messages as input and returns chat messages as output rather then plain text
    - <h6>Table summarising key differences</h6>

      | Feature                | LLMs (Large Language Models)                                                                                             | Chat Models                                                                                                                               |
      | ---------------------- | ------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
      | **Training Objective** | Trained on large corpora of text to predict the next token in a sequence, suitable for general text generation tasks.    | Fine-tuned on conversational datasets to handle dialogue-specific tasks, such as maintaining context and generating human-like responses. |
      | **Context Handling**   | Limited ability to handle multi-turn conversations or maintain context across interactions unless explicitly engineered. | Designed to handle multi-turn conversations, maintaining context across messages.                                                         |
      | **Fine-Tuning**        | Can be fine-tuned for specific tasks like summarization, translation, or domain-specific text generation.                | Often fine-tuned with Reinforcement Learning from Human Feedback (RLHF) to improve conversational quality and alignment with user intent. |
      | **Output Style**       | Outputs plain text without conversational structure.                                                                     | Outputs structured responses tailored for conversational interactions.                                                                    |
      | **Examples**           | GPT-3, GPT-4 (base models), Hugging Face Transformers.                                                                   | ChatGPT, Claude, Bard.                                                                                                                    |
      | **Memory and Context** | Treats each input as independent, with limited memory of prior interactions.                                             | Better at remembering and referencing prior parts of a conversation.                                                                      |
      | **User Interaction**   | Optimized for standalone tasks like summarization, text generation, or code generation.                                  | Optimized for interactive use cases like customer support, virtual assistants, and chatbots.                                              |
      | **Input Format**       | Accepts plain text as input.                                                                                             | Accepts structured inputs (e.g., a sequence of messages with roles like "user" and "assistant").                                          |
      | **Summary**            | Broader in scope, designed for general-purpose text processing.                                                          | Specialized versions of LLMs, fine-tuned and optimized for conversational tasks.                                                          |

- Embedding Model
  - input as text --> output is series of numbers knowns as embeddings (vector) representing contextual meaning of the text
  - use case like semantic search and helpful in building RAG based applications
