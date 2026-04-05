````markdown
# Chatbot Local Setup

## Download and Install Miniconda

1. Download Mini conda:  
   https://www.anaconda.com/download/success?reg=skipped  

2. Install:
   ```bash
   bash ~/Downloads/Miniconda3-py310_23.7.2-MacOSX-arm64.sh
````

3. Source it:

   ```bash
   source ~/miniconda3/bin/activate
   ```

---

## Create Virtual Environment

1. Create environment:

   ```bash
   conda create -n chat-bot python=3.10
   ```

2. Activate environment:

   ```bash
   conda activate chat-bot
   ```

3. Install required packages:

   ```bash
   pip install openai ipykernel jupyterlab notebook chromadb langchain-chroma
   ```

4. Register Jupyter kernel:

   ```bash
   python -m ipykernel install --user --name=chat-bot --display-name "Python (chat-bot)"
   ```

5. Clone repo and navigate into the terminal:

   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

---

## Backend API Run

1. Install dependencies:

   ```bash
   poetry install --no-root
   ```

2. Run FastAPI server:

   ```bash
   poetry run uvicorn main:app --reload
   ```

**Note:** Use the port that shows in terminal.

---

## Jupyter Run (Optional for Learning and Testing)

1. Start Jupyter:

   ```bash
   jupyter notebook
   ```

**Note:** Navigate to Jupyter directory to run and test flexibly.

```
```
