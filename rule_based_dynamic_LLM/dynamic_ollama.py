import subprocess

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

def query_ollama_model(model_name: str , prompt: str ) -> str:
    try:
        result = subprocess.run(
            ["ollama", "run", model_name, "--prompt", prompt],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error calling model: {e}"


def dynamic_llm(prompt: str) -> str:
    model_size = analyze_prompt(prompt)
    model_name = Model[model_size]
    print(f"Selected model: {model_name}")
    response = query_ollama_model(model_name, prompt)
    return response


if __name__ == "__main__":
    user_prompt = input("Enter your prompt: ")
    output = dynamic_llm(user_prompt)
    print("Response:\n", output)