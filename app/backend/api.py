import os
from flask import Flask, request
from flask_cors import CORS
from lib.ai.llm import gemma
from lib.ai.stt import whisper
from util.converter import convert_mp4_to_mp3

app = Flask(__name__, instance_relative_config=True)
CORS(app)

prompt = """あなたは議事録の作成者です。
議事録は各話題ごとに会話形式でまとめて下さい。話で出てこなかったことは議事録に書かないで下さい。議事録はマークダウン記法で作成してください。
この文章を生成したのは文字起こしAIなので、誤った文字だと思われる場合には正しいと思える文章に修正して下さい。
同じ人が話したと思われる文章は文章の先頭に[SPEAKER n]とつけてまとめて下さい。nには0からカウントアップした話者IDが入ります。
話者ごとにIDは割り当てられます。話者の名前が分かる場合はその人の名前を入れて[話者の名前]としてください。
この会議で決まった決定事項がある場合はそれもまとめて下さい。決定事項は誰が、いつまでに何をしなければいかないかをまとめて下さい。

以下は議事録を文字起こしした文章です。この文章を元に議事録を作成してください。
"""

@app.route("/generate-minutes", methods=["POST"])
def generate_minutes():
    """議事録を生成する"""

    # ファイル保存ディレクトリ作成
    os.makedirs(exist_ok=True, name="tmp")

    # アップロードされたファイル保存
    file = request.files.get("file")
    file_name = "uploaded_" + file.filename
    file_path = os.path.join("tmp", file_name)
    file.save(file_path)

    mp3_path = os.path.join("tmp", "example.mp3")
    convert_mp4_to_mp3(file_path, mp3_path)

    # 会議を文字起こし
    meeting_text = whisper.speak_to_text(mp3_path)
    print(meeting_text)

    # 議事録を生成
    minutes = gemma.talk_llm(minutes=meeting_text, prompt=prompt)
    print(minutes)

    return {"result": True, "minutes": minutes}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
