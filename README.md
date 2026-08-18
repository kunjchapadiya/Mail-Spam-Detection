# 📬 Email Spam Detection System

An end-to-end Machine Learning web application that classifies emails as **Spam** or **Ham (Legitimate)** using Natural Language Processing (NLP). 

The project features a lightweight, single-layer architecture powered completely by **Streamlit**. The interface directly handles user input, processes text data, and executes predictions using a saved Multinomial Naive Bayes model. All project dependencies are managed using **uv** for ultra-fast setup.

---

## 🏗️ Architecture Overview

```text
[ User Email Input ] ➡️ [ Streamlit App (Port 8501) ] ➡️ [ Loaded .pkl Model ] ➡️ [ Instant UI Result ]
```

- **Framework**: Streamlit (Pure Python Web UI)
- **Machine Learning**: Scikit-Learn (Multinomial Naive Bayes + CountVectorizer)
- **Environment Management**: uv (Blazing fast alternative to pip)

---

## ⚡ Features

- **Real-time Inference**: Instant email text classification.
- **No Complex Setup**: Single-script deployment without needing an external API or database.
- **Interactive UI**: Clean interface built entirely in Python (no HTML/CSS required).

---

## 🚀 Getting Started

### Prerequisites

Ensure you have Python 3.10+ installed. Install **uv** on your system if you haven't already:

```bash
# x86/ARM macOS and Linux
curl -LsSf https://astral.sh | sh

# Windows (PowerShell)
powershell -c "irm https://astral.sh | iex"
```

### 1. Clone & Setup Project

Clone the repository and set up a clean virtual environment using `uv`:

```bash
git clone https://github.com/kunjchapdiya/Mail-Spam-Detection.git

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
```

### 2. Generate the Model Artifact (`.pkl`)

Run your training script to vectorize your dataset, train the Multinomial NB model, and save the binary bundle:

```bash
uv run --with scikit-learn --with joblib python train.py
```
*This step generates `multinomial_model.pkl` in your root directory.*

### 3. Run the Streamlit Application

Launch the web application locally by running:

```bash
uv run --with streamlit --with scikit-learn --with joblib streamlit run app.py
```
- Your web browser will automatically open the application interface at: `http://localhost:8501`

---

## 📁 Repository Structure

```text
├── app.py                      # Streamlit application main web interface
├── dataset.xlsx                # dataset a which is used for train a model
├── multinomial_model.pkl       # Saved serialized bundle (Auto-generated)
├── mail.ipynb                  # write a full code foir train the model
└── README.md                   # Project documentation
```

---

## 📦 Cloud Deployment Note

To share this app publicly, you can deploy it for free on **Streamlit Community Cloud**. First, use `uv` to output a standard requirements file for the platform:

```bash
uv pip freeze > requirements.txt
```
Push your files (`app.py`, `multinomial_model.pkl`, and `requirements.txt`) to a GitHub repository, log into [share.streamlit.io](https://streamlit.io), and link your repository to go live!
