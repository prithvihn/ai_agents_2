# ai_agents
# ai_agents_2

A minimal AI agents starter repository demonstrating example usage of generative AI models in Python using different providers (Azure OpenAI + Google AI). This project is a fork of `gokul-1998/ai_agents` and contains example scripts for building AI-powered workflows and experiments.:contentReference[oaicite:2]{index=2}

---

## 🧠 Overview

This repo showcases simple examples of interacting with large language models using:

- **Azure AI Inference client** — demo for Chat Completions using `gpt-4o-mini` (via Azure + GitHub AI endpoint) – see `app.py`.:contentReference[oaicite:3]{index=3}  
- **Google Generative AI integration via LangChain** — demo for a Chat model (Gemini) using `langchain_google_genai` – see `main.py`.:contentReference[oaicite:4]{index=4}

> ⚠️ These examples are intended as **starting points** for experimentation and learning about agent-based workflows and API integration.

---

## 🚀 Features

- 🔹 Example script showcasing an LLM call to Azure/GitHub AI endpoint (**app.py**)  
- 🔹 Example script showing a basic generative model call via **LangChain/Google AI** (**main.py**)  
- 🔹 Environment setup via `.env` for API credentials  
- 🔹 Python dependency templates in `requirements.txt`

---

## 📁 Repo Structure
├── .gitignore
├── README.md
├── app.py # Azure + GitHub AI completion example
├── main.py # LangChain Google Generative AI example
├── main2.py # (Optional stub for expansion)
├── email_sender.py # (Optional utility file)
├── requirements.txt
├── requirements-windows.text


---

## 🛠️ Prerequisites

Before running the examples, ensure you have:

✔ Python **3.8+** installed  
✔ An API key for the respective AI provider(s)  
✔ A `.env` file with environment variables set

Example `.env`:

```bash
GITHUB_TOKEN=your_github_token_here
GOOGLE_API_KEY=your_google_api_key_here
# Add other keys as needed

📦 Installation

Clone the repo:

git clone https://github.com/prithvihn/ai_agents_2.git
cd ai_agents_2

Install the dependencies:

pip install -r requirements.txt

Create and populate your .env file in the project root.

▶️ Usage
Run the Azure/GitHub AI example
python app.py

This script initializes a client and runs a simple question through an AI model to print the response.

Run the LangChain Google AI example
python main.py
