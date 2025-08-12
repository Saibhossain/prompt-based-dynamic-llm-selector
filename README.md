# Dynamic LLM Selector Using Ollama Local Models


## Description
This project implements a dynamic large language model (LLM) selector that intelligently routes user prompts to different local Ollama models based on prompt complexity and content. The system balances efficiency and accuracy by selecting the most appropriate model from three options:

* Small model: gemma3:1b — fast and lightweight, for simple queries.

* Medium model: deepseek-r1:1.5b — balanced for moderate complexity and creative tasks.

* Large model: gemma3n:latest — powerful, for complex, technical, or multi-step reasoning prompts.
* 

## How It Works
* Prompt Analysis: The system analyzes the input prompt’s length, sentence complexity, and presence of keywords related to reasoning, technical topics, or creativity.

* Few-shot Detection: It detects if the prompt contains examples or input/output pairs to prioritize larger models for pattern recognition.

* Model Selection: Based on the analysis, the system dynamically selects the most suitable model size.

* Prompt Optimization: It automatically enhances the prompt with instructions (e.g., “Think step-by-step” for complex tasks, or “Be creative” for creative writing) to improve the LLM response quality.

* Chat Execution: The prompt is sent to the chosen model via the local Ollama API, and the response is returned.

* Session History: The program tracks prompt characteristics, model used, tokens, and response time for logging and future improvements.

### Features
> Intelligent multi-model routing for optimized performance and quality.

> Automatic prompt rephrasing for better prompt engineering.

> Session history logging for analysis of usage patterns and model performance.

> Command-line interface with continuous prompt input and exit option.

### Requirements

    Python 3.9 or higher   

    Ollama Python client

    Local Ollama models installed: gemma3:1b, deepseek-r1:1.5b, and gemma3n:latest

#### Usage
    python dynamic_llm_selector.py

### Future Improvements

Integration with web or API interfaces.
## Licence 
Feel free to customize it with your project name or additional instructions
