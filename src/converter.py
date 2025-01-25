from pydub import AudioSegment
import os

def convert_mp4_to_mp3(input_file, output_file):
    """
    MP4ファイルをMP3に変換する関数

    Parameters:
        input_file (str): 入力MP4ファイルのパス
        output_file (str): 出力MP3ファイルのパス
    """

    target_sr = 16000

    try:
        # MP4を読み込む
        audio = AudioSegment.from_file(input_file, format="mp4")
        audio = audio.set_frame_rate(target_sr)
        # MP3として書き出す
        audio.export(output_file, format="wav")
        print(f"変換が完了しました: {output_file}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    # 入力MP4ファイルのパスを指定
    input_path = "in/example.mp4"
    # 出力MP3ファイルのパスを指定
    output_path = "out/example.wav"

    # ファイルが存在するか確認
    if os.path.exists(input_path):
        convert_mp4_to_mp3(input_path, output_path)
    else:
        print(f"入力ファイルが見つかりません: {input_path}")
