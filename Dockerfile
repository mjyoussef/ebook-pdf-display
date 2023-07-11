FROM python:3.11-slim-bookworm

COPY . .

RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y curl \
            libegl1 \
            libopengl0 \
            xz-utils

RUN curl -s https://download.calibre-ebook.com/linux-installer.sh | sh /dev/stdin

CMD [ "python", "./main.py" ]