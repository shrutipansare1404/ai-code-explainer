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
 ## Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Code Explanation

![Code Explanation](screenshots/explanation.png)

### Explanation History

![History](screenshots/history.png)


## Run

```bash
pip install -r requirements.txt

streamlit run app.py
```
## Future Improvements

* Add AST-based parsing to extract function names and code structure before sending prompts to the LLM.
* Support code optimization suggestions with a diff view between the original and optimized code.
* Improve time and space complexity detection using static analysis techniques.
* Add syntax highlighting and annotations for important code blocks.

## Challenges Faced

* Integrating the Gemini API securely using environment variables.
* Designing prompts that generate concise and accurate explanations while minimizing hallucinations.
* Managing multiple code submissions and maintaining explanation history within the Streamlit application.

