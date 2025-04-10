# What is structured output

- practice of having language model return responses in well defined data format rather then free form text
- makes it easier to parse and work
- can interact with other systems as the output is structured (i.e. llm --> machines/system)
- some llms can return structured outputs like (openai)
  - use function `with_structured_output`
  - can be done in three ways
    - typed dict
      - specify what key and value should exists
      - what keys are required and what type of values they should have
      - does not validate data at run time... in shorty type hints
    - pydantic
      - data validation and data parsing library for python
      - ensure data you work with is correct, structured and type safe
    - json_schema
- and some llms dont have this capability
  - use output parsers
  - classes written in langchain to convert unstructured to structured output

# Sample use cases

- Data Extraction - storing outputs from llm in some data store
- API building
- Agents
