# PandasAI CSV Query App 📊

This Streamlit app allows users to upload a CSV file and query data using PandasAI. It uses PandasAI to process queries and generate text-based responses based on the uploaded dataset.

## Features
- 📂 Upload CSV files
- 🤖 Ask AI queries based on the data
- 🔍 View data preview
- 📊 Generate charts and graphs

---

## Setup Guide

### 1️⃣ Clone the Repository
First, clone this repository to your local machine using the following command:
```sh
 git clone https://github.com/yourusername/yourrepo.git
 cd yourrepo
```

### 2️⃣ Install Dependencies
Ensure you have Python installed (preferably Python 3.8+). Then, install the required dependencies:
```sh
 pip install -r requirements.txt
```

### 3️⃣ Get Your PandasAI API Key
To use PandasAI, you need an API key:
1. Visit [PandasAI](https://app.pandabi.ai) and sign up.
2. Navigate to your account settings and generate an API key.

### 4️⃣ Configure API Key Securely
To keep your API key secure, store it in Streamlit's secrets manager:
1. Inside your project folder, create a directory named `.streamlit`.
2. Inside `.streamlit`, create a file named `secrets.toml`.
3. Open `secrets.toml` and add the following line:
   ```toml
   PANDASAI_API_KEY = "your-api-key-here"
   ```
4. **Important:** Do not share this file or commit it to GitHub. To ensure it's ignored, add it to `.gitignore`.

### 5️⃣ Add `.gitignore`
To prevent sensitive files from being uploaded to GitHub, create a `.gitignore` file and add:
```sh
# Ignore API secrets
.streamlit/secrets.toml
```

### 6️⃣ Run the Application
Start the Streamlit app using the following command:
```sh
 streamlit run app.py
```
This will launch the app in your default web browser.

### 7️⃣ Deploying the App
To deploy this app using Streamlit Cloud:
1. Push your code to GitHub.
2. Go to [Streamlit Cloud](https://share.streamlit.io/), sign in, and create a new app.
3. Connect your GitHub repository.
4. Configure secrets in Streamlit Cloud (add `PANDASAI_API_KEY` under "Secrets").
5. Deploy and share your app!

---

## Contributing
Feel free to fork this repository, make improvements, and submit a pull request.

## License
MIT License

