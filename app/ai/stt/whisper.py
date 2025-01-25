from faster_whisper import WhisperModel

model_size = "large-v3"


def speak_to_text(input_file: str) -> str:
    model = WhisperModel(model_size, device="cpu", cpu_threads=12)

    segments, info = model.transcribe(
        input_file,
        beam_size=5,
        without_timestamps=True,
        language="ja",
        vad_filter=True,
    )

    gijiroku = ""

    for segment in segments:
        gijiroku = gijiroku + "\n" + segment.text

    return gijiroku
