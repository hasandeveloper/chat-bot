# Chatbot Local Setup (No Poetry)

## Install Miniconda

Download: https://www.anaconda.com/download

```bash
bash ~/Downloads/Miniconda3-*.sh
source ~/miniconda3/bin/activate
```

---

## Create Environment

```bash
conda create -n chat-bot python=3.10
conda activate chat-bot
```

---

## Install Dependencies

```bash
pip install --upgrade pip

pip install \
fastapi uvicorn \
pydantic requests python-dotenv \
openai \
chromadb \
langchain \
langchain-openai \
langchain-community \
langchain-chroma \
jupyterlab notebook ipykernel
```

---

## Fix M1 protobuf issue

```bash
pip install "protobuf<=3.20.3"
```

---

## Register Jupyter

```bash
python -m ipykernel install --user --name=chat-bot --display-name "Python (chat-bot)"
```

---

## Run FastAPI

```bash
uvicorn main:app --reload
```

---

## Run Jupyter (optional)

```bash
jupyter notebook
```
