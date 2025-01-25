import ollama
from oyama import oyama


def talk_llm(minutes: str, prompt: str) -> str:
    model_path = "https://huggingface.co/alfredplpl/gemma-2-baku-2b-it-gguf/resolve/main/gemma-2-baku-2b-it-Q8_0.gguf"
    model_name = oyama.run(model_path)

    response = ollama.chat(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": prompt + minutes,
            },
        ],
    )

    return response["message"]["content"]
