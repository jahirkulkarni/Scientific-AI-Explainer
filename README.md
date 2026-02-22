# 🔬 Scientific AI Explainer
**Team C - Milestone 3 Project**

This is an AI-powered web application that provides detailed scientific explanations for complex terms using the **GPT-2** model.

## 🚀 Features
- **AI Definitions:** Generates 3-4 line explanations for scientific terms.
- **Glass-morphism UI:** Modern and professional user interface.
- **Flask Backend:** Robust integration between the AI model and web frontend.

## 🛠️ Tech Stack
- **Language:** Python
- **Framework:** Flask
- **AI Model:** GPT-2 (HuggingFace Transformers)
- **Deployment:** Ngrok Tunneling

## 📋 Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd Scientific-AI-Explainer
   ```

2. Create a virtual environment:
   ```
   python -m venv .venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     .venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source .venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

### Running the Application
1. Run the Flask app:
   ```
   python app.py
   ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`

**Note:** The GPT-2 model will be downloaded automatically on the first run, which may take some time depending on your internet connection.