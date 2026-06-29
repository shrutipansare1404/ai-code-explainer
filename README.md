# AI-Powered Code Explainer
## Project Summary

This project is an AI-powered code explainer built using Streamlit and Google's Gemini API. Users can paste Python or JavaScript code and receive concise, plain-English explanations. The application maintains a history of previous explanations and attempts to estimate time complexity when applicable.

## Tech Stack

* Python
* Streamlit
* Gemini API

## Features

* Accepts Python and JavaScript code
* Generates plain-English explanations
* Stores explanation history
* Estimates time complexity when possible

## Architecture

User
→ Streamlit UI
→ Gemini API
→ Explanation

## Why Gemini?

Gemini was chosen because it provides fast responses and a free API tier suitable for rapid development.

## Hallucination Handling

To reduce hallucinations:

* The prompt instructs the model not to guess.
* The model explicitly mentions uncertainty.
* Explanations are restricted to the provided code only.

## Run

```bash
pip install -r requirements.txt

streamlit run app.py
```
