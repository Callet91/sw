FROM tensorflow/tensorflow:latest-gpu-py3-jupyter

WORKDIR /workspaces/my_project

RUN apt update

COPY . .

ENV PYTHONPATH="/workspaces/my_project"

CMD jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --no-browser
