FROM debian:bookworm-20250113-slim

RUN apt-get update && apt-get upgrade -y \
    && apt-get install -y python3 python3-pip git \
    && apt-get -y install pciutils ffmpeg

RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124 --break-system-packages \
    && pip install nvidia-cublas-cu12 nvidia-cudnn-cu12==9.* --break-system-packages \
    && pip install faster-whisper --break-system-packages \
    && pip install -q git+https://github.com/HawkClaws/oyama.git ollama --break-system-packages \
    && pip install -q langchain-community tiktoken pydub --break-system-packages

RUN export LD_LIBRARY_PATH=`python3 -c 'import os; import nvidia.cublas.lib; import nvidia.cudnn.lib; print(os.path.dirname(nvidia.cublas.lib.__file__) + ":" + os.path.dirname(nvidia.cudnn.lib.__file__))'` >> ~/.shrc

RUN pip install Flask --break-system-packages
