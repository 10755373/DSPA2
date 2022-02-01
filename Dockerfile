FROM python:3.7

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install Flask && \
    pip install torch && \
    pip install albumentations && \
    pip install opencv-python && \
    pip install datetime && \
    pip install geocoder && \
    pip install numpy && \
    pip install IPython && \
    pip install pillow && \
    pip install python-math && \
    pip install exif && \
    pip install torchvision && \
    pip install matplotlib && \
    pip install pandas && \
    pip install sklearn && \
    pip install data_loader && \
    pip install pyrebase && \
    pip install flask_cors

WORKDIR /app
COPY . /app

ENV PORT 5000
ENV HOST 0.0.0.0
ENV FLASK_APP=app.py

ENTRYPOINT [ "python" ]

CMD ["./app.py", "-m" , "flask", "run", "-p", "$PORT", "--host", "$HOST"]
