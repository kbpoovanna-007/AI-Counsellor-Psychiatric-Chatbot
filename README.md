# AI Psychatric Counselor Application

This repository contains a web-based counseling application that uses LLaMA 3.2 and Langchain for providing automated counseling services.

## Repository Structure

- about.html
- counselor_app.py
- image.jpg
- dex.html
- requirement.txt
- trynow.html

## Prerequisites

Before running the application, ensure you have the following installed:
- Python 3.8 or higher
- Git
- Ollama

## Installation Guide

### 1. Install Ollama

Visit the official Ollama download page based on your operating system:
- Windows: https://ollama.com/download/windows
- Linux: `curl -fsSL https://ollama.com/install.sh | sh`
- MacOS: `brew install ollama`

### 2. Choose and Install Your LLM Model

1. Visit https://ollama.com/search to explore available models
2. Choose a model that best fits your needs. Consider factors like:
   - Model size and performance requirements
   - Specific capabilities needed for counseling
   - Hardware requirements
   - License restrictions

### 3. Pull your chosen model (example using llama2):
```
ollama pull llama3.2
```



## 4. Set Up Python Environment

### Clone the repository:
```
git clone <repository-url>
cd <repository-name>
```

### Create and activate a virtual environment:

#### For Windows:
```
python -m venv venv
.\venv\Scripts\activate
```


#### For Linux/MacOS:
```
python3 -m venv venv
source venv/bin/activate
```

## Install required packages:
```
pip install -r requirement.txt
```

### Install additional required packages:
```
pip install langchain streamlit
```



## Running the Application

### Start the Ollama server (in a new terminal):
```
ollama serve
```

### Enter Virtual Environment
```
.venv\Scripts\activate.bat
```

### Run the streamlit app
```
stramlit run counselor_app.py
```


In a different terminal, make sure your virtual environment is activated, then run the Streamlit application:
streamlit run counselor_app.py

## Usage

The main application interface is accessible through the Streamlit server
Navigate through different pages using the HTML files:

1. index.html: Main landing page
2. about.html: Information about the service
3. trynow.html: Quick access to counseling services



## Troubleshooting

If you encounter any issues with Ollama:

- Ensure the Ollama server is running (ollama serve)
- Check if your chosen model is properly installed (ollama list)
- For Windows-specific issues, refer to the Windows installation guide on Ollama's website


## For virtual environment issues:

- Make sure you're in the correct directory
- Verify that the virtual environment is activated (you should see (venv) in your terminal)


## For package installation issues:

- Try updating pip: pip install --upgrade pip
- Install packages one by one if batch installation fails



## Additional Notes

- Ensure you have sufficient disk space for the LLM model (size varies by model choice)
- The application requires an active internet connection for initial setup
- Keep all HTML files in the same directory for proper navigation
- Different models may have different performance characteristics and hardware requirements
