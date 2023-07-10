FROM python:3.11-slim-bookworm

COPY . .

# Install prerequisites
RUN pip install -r requirements.txt

RUN apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y --no-install-recommends \
                  ca-certificates \
                  xvfb \
                  libegl1 \
                  libopengl0 \
                  libxkbcommon-x11-0 \
                  libxcomposite-dev \
                  # QTWebEngine deps
                  libxdamage-dev libxrandr-dev libxtst6 \
                  curl \
                  gnupg2 \
                  xz-utils \
                  && rm -rf /var/lib/apt/lists/*

RUN curl -s https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

CMD [ "python", "./main.py" ]