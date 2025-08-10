from ollama import chat

Model = {
    "small": "gemma3:1b",
    "medium": "deepseek-r1:1.5b",
    "large": "gemma3n:latest"
}

def analyze_prompt(prompt:str) -> str:
    length = len(prompt)
    complixity_keyworks = ["explain", "compare", "detailed", "complex", "analyze", "reason"]
    complixity_score = sum(1 for kw in complixity_keyworks if kw in prompt.lower())
    if length < 10 and complixity_score < 1:
        return "small"
    elif length < 50 and complixity_score < 2:
        return "medium"
    else:
        return "large"

def dynamic_llm(prompt: str) -> str:
    model_size = analyze_prompt(prompt)
    model_name = Model[model_size]
    print(f"Selected model: {model_name}")

    response = chat(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.message.content

if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    output = dynamic_llm(user_prompt)
    print("Response:\n", output)