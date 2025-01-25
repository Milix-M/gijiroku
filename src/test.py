from faster_whisper import WhisperModel

model_size = "large-v3"

model = WhisperModel(model_size, device="cpu", cpu_threads=14)

segments, info = model.transcribe("out/example.wav", beam_size=5, without_timestamps=True, language="ja", vad_filter=True)

print("Detected language '%s' with probability %f" %
      (info.language, info.language_probability))

for segment in segments:
    print(segment.text)
