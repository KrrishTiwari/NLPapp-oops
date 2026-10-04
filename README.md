# 🧠 NLP Analysis App

A simple **Python-based NLP application** that lets users create an account, log in, and perform different Natural Language Processing tasks through a menu-driven interface.

This project was built while learning **Python, OOP, APIs, and NLP**, and helped me understand how different NLP services can be connected to a Python application.

---

## 📸 Preview

<p align="center">
  <img src="https://placehold.co/900x500?text=NLP+Analysis+App" alt="NLP Analysis App Preview">
</p>

> Replace the image above with a screenshot of your actual application once you have one.

---

## ✨ Features

### 👤 User Registration & Login

* Create a new account using name, email, and password.
* Prevents registration with an already-used email.
* Basic email validation.
* Password input is hidden while typing.
* Login system using the stored credentials.

### 🔎 Named Entity Recognition (NER)

Enter a paragraph and specify what you want to search for.

For example:

```text
John Doe started learning Javascript and Python.
He now works at Google.
```

You can search for:

```text
programming languages
```

The application sends the request to NLPCloud and returns the detected entities.

### 🌍 Language Detection

Enter a paragraph and the application detects its language.

Example:

```text
This is a simple English paragraph.
```

Output:

```text
en
```

### 😊 Sentiment Analysis

Enter a paragraph and the application determines its sentiment.

You can also provide a specific target when required.

Example:

```text
I really enjoyed this movie. The acting was excellent.
```

The application returns the highest-scoring sentiment label.

---

## 🛠️ Technologies Used

* 🐍 **Python**
* 🧱 **Object-Oriented Programming**
* 🌐 **NLPCloud API**
* 🔐 **Environment Variables**
* 📦 **Regular Expressions**
* 🔑 **Getpass**
* 📚 **Python Dictionaries**

---

## 📂 Project Structure

```text
NLP-Analysis-App/
│
├── app.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/NLP-Analysis-App.git
```

Move into the project directory:

```bash
cd NLP-Analysis-App
```

### 2. Install the required packages

```bash
pip install -r requirements.txt
```

If you haven't created `requirements.txt` yet, it should contain:

```text
nlpcloud
```

### 3. Create an NLPCloud API key

Create an account on [NLPCloud](https://nlpcloud.com/) and generate an API key.

**Never put your API key directly inside the Python file.**

---

## 🔐 Setting up the API Key

The application reads the API key from an environment variable:

```python
API_TOKEN = os.getenv("NLPCLOUD_API_KEY")
```

### Windows PowerShell

```powershell
$env:NLPCLOUD_API_KEY="your_api_key_here"
```

Then run:

```powershell
python app.py
```

### Windows Command Prompt

```cmd
set NLPCLOUD_API_KEY=your_api_key_here
python app.py
```

You can also use a `.env` file if you prefer, but **make sure `.env` is included in `.gitignore**.

Example `.env.example`:

```text
NLPCLOUD_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

Run:

```bash
python app.py
```

You'll see:

```text
Hi! How would you like to proceed?

1. Not a Member? Register
2. Already a Member? Login
3. Exit
```

After logging in:

```text
Hi! How would you like to proceed?

1. NER
2. Language Detection
3. Sentiment Analysis
4. Logout
```

---

## 🧩 How It Works

The application is organized around a single `NLPapp` class.

```text
                    NLP Analysis App
                           │
                    ┌──────┴──────┐
                    │             │
               Authentication    NLP Features
                    │             │
              ┌─────┴─────┐   ┌───┼────┬──────────┐
              │           │   │   │    │          │
          Register      Login NER Language  Sentiment
                                Detection  Analysis
```

The application keeps registered users in a Python dictionary while it is running.

For example:

```python
{
    "user@example.com": ["Krrish", "password"]
}
```

The NLP features communicate with NLPCloud through its API.

---

## 🔒 Security

The API key is **not stored directly in the source code**.

Instead, the application reads it from:

```text
NLPCLOUD_API_KEY
```

The real API key should never be committed to GitHub.

A `.gitignore` file should include:

```text
.env
```

---

## 📚 What I Learned

Building this project helped me practice:

* Classes and objects
* Constructors
* Private methods and attributes
* Dictionaries
* Loops and conditional statements
* Functions and helper methods
* Exception handling
* Regular expressions
* API integration
* Environment variables
* User authentication logic
* Working with JSON responses
* Basic NLP concepts

---

## 🔮 Future Improvements

There are several things I'd like to improve in future versions:

* 💾 Store users in a real database instead of an in-memory dictionary
* 🔐 Hash passwords instead of storing them as plain text
* 🖥️ Build a graphical/web interface
* 📊 Display NLP results in a more user-friendly format
* 📝 Add analysis history
* 📈 Add more NLP features
* ☁️ Deploy the application online

---

## 👨‍💻 About the Project

This is a learning project built to practice **Python and Natural Language Processing** while working with real API-based NLP services.

It started as a simple menu-driven Python program and gradually evolved into an application with authentication and multiple NLP features.

---

## ⭐ If you found this project interesting

Feel free to explore the code, suggest improvements, or use the project as a starting point for your own NLP experiments.

**Built with Python 🐍 and a lot of learning along the way.**

