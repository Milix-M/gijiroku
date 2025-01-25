import ollama
from oyama import oyama


def talk_llm(minutes: str):
    model_path = "https://huggingface.co/alfredplpl/gemma-2-baku-2b-it-gguf/resolve/main/gemma-2-baku-2b-it-Q8_0.gguf"
    model_name = oyama.run(model_path)

    prompt = """次の文章を議事録にしてください。
    議事録は各話題ごとに会話形式でまとめて下さい。議事録はマークダウン記法で作成してください。
    この文章を生成したのは文字起こしAIなので、誤った文字だと思われる場合には正しいと思える文章に修正して下さい。
    同じ人が話したと思われる文章は文章の先頭に[SPEAKER n]とつけてまとめて下さい。nには0からカウントアップした話者IDが入ります。
    話者ごとにIDは割り当てられます。話者の名前が分かる場合はその人の名前を入れて[話者の名前]としてください。
    この会議で決まった決定事項がある場合はそれもまとめて下さい。決定事項は誰が、いつまでに何をしなければいかないかをまとめて下さい。

    以下は議事録を文字起こしした文章です。
    """

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
