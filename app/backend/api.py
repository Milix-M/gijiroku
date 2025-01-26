import os
from flask import Flask, request
from lib.ai.llm import gemma
from lib.ai.stt import whisper

app = Flask(__name__, instance_relative_config=True)


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

    # 会議を文字起こし
    meeting_text = whisper.speak_to_text(file_path)
    print(meeting_text)

    # 議事録を生成
    minutes = gemma.talk_llm(meeting_text)
    print(minutes)

    return {"result": True, "minutes": minutes}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
