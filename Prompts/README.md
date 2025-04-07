# Prompts

- Instructions provided to model to guide its outputs

 # Types of Prompts
 - Text Based
   - Static Prompts
     - Example at ```static_prompt_ui.py```
     - In static prompts, User need to provide complete prompt, thereby giving complete control to user which is not ideal
   - Dynamic Prompts
     - use prompt template `from langchain_core.prompts import PromptTemplate`
     - use ChatPrompt template from multiple messages `langchain_core.prompts import ChatPromptTemplate`
     - use of prompt templates
        - Prompt template in langchain is a structured way to create prompts dynamically by inserting variables into a predefined template instead of hardcoding templates
        - allows you to define placeholders that can be filled at runtime with different inputs, making it reusable, flexible, and easy to manage specifically when working with dynamic user inputs             or automated workflow
     - but why not <em>f-strings</em>
       - default validation out of box using prompt template (see `dynamic_prompt_ui`)
       - Makes it reusable i.e. allows you to save template external to code (see `dynamic_prompt_ui`)
       - Tied with langchain components like chains
 - MultiModal

# Type of Messages in Langchain
 - System Message
 - Human Message
 - AI Message

# Message Placeholder
- Message placeholder in langchain is a special placeholder used inside a ChatPrompt Template to dynamically insert chat history or list of messages at run time

   
