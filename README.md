# NLP Analysis App

A command-line Python application that combines a simple user login system with three text-analysis tools: named entity recognition, language detection, and sentiment analysis. The analysis is done by the [NLP Cloud](https://nlpcloud.com/) API.

I built this to practice object-oriented Python, input validation, and working with a third-party API.

## Features

- **Accounts:** register with a name, email, and password, then log in. Emails are checked for a valid format, duplicates are rejected, and passwords are hidden while typing.
- **Named Entity Recognition (NER):** enter a paragraph and describe what to look for (for example, "programming languages") and the app returns the matching entities.
- **Language detection:** returns the language code of the text you enter, such as `en`.
- **Sentiment analysis:** returns the highest-scoring sentiment label for a paragraph. You can optionally give a target to score the sentiment toward.

## Requirements

- Python 3.8 or newer
- An NLP Cloud account and API key

## Installation

Clone the repository and move into it:

```bash
git clone https://github.com/KrrishTiwari/NLPapp-oops.git
cd NLPapp-oops
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

The app reads your API key from the `NLPCLOUD_API_KEY` environment variable. The key is never stored in the code, so set the variable before running the app.

**macOS / Linux**

```bash
export NLPCLOUD_API_KEY="your_api_key_here"
```

**Windows (PowerShell)**

```powershell
$env:NLPCLOUD_API_KEY="your_api_key_here"
```

**Windows (Command Prompt)**

```cmd
set NLPCLOUD_API_KEY=your_api_key_here
```

The variable only lasts for the current terminal session, so run the app from the same terminal window.

## Usage

```bash
python app.py
```

You will start at the main menu:

```
Hi! How would you like to proceed?
1. Not a Member? Register
2. Already a Member? Login
3. Exit
```

After logging in, you can choose a feature:

```
Hi! How would you like to proceed?
1. NER
2. Language Detection
3. Sentiment Analysis
4. Logout
```

### Example inputs

**NER**

```
Paragraph: John Doe started learning JavaScript and Python. He now works at Google.
Search for: programming languages
```

**Language detection**

```
Paragraph: This is a simple English paragraph.
Output: en
```

**Sentiment analysis**

```
Paragraph: I really enjoyed this movie. The acting was excellent.
Target: (press Enter to skip)
```

## Project Structure

```
NLPapp-oops/
├── app.py              # Application code
├── requirements.txt    # Python dependencies
├── README.md
└── .gitignore
```

## How It Works

Everything lives in a single `NLPapp` class. Two menu loops handle navigation (one before login, one after), and small helper methods validate input for names, emails, and passwords. The NLP features send requests to NLP Cloud using the `nlpcloud` client. NER and sentiment analysis use the `gpt-oss-120b` model, and language detection uses `python-langdetect`. API errors are caught and printed instead of crashing the program.

## Known Limitations

- Users are stored in a dictionary in memory, so all accounts are lost when the program exits.
- Passwords are stored as plain text. This is fine for a learning project but should never be done in a real application.
- The NER and sentiment features print the model's response mostly as returned, without much formatting.
- There are no automated tests yet.

## Roadmap

- Hash passwords with `bcrypt` or `hashlib`
- Save users to SQLite instead of memory
- Format the analysis output so it is easier to read
- Add unit tests for the input validation and menu logic
- Keep a history of past analyses for each user

## Contributing

This is a personal learning project, but suggestions are welcome. If you spot a bug or have an idea, open an issue.
