from oyama import oyama
import ollama


# Model Path
model_path = "https://huggingface.co/alfredplpl/gemma-2-baku-2b-it-gguf/resolve/main/gemma-2-baku-2b-it-Q8_0.gguf" # @param {type:"string"}
model_name = oyama.run(model_path)

response = ollama.chat(model=model_name, messages=[
  {
    'role': 'user',
    'content': '日本でお薦めの観光地を5つあげてください。',
  },
])
print(response['message']['content'])
