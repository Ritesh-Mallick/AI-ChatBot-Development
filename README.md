# AI ChatBot

This project implements a simple chatbot using Natural Language Processing (NLP) techniques. The chatbot reads a text corpus, preprocesses the text, and generates responses to user input based on the similarity of the input to the sentences in the corpus.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

### Prerequisites

Make sure you have the following libraries installed:

- numpy
- nltk
- scikit-learn

You can install them using pip:

```bash
pip install numpy nltk scikit-learn
```

### Download NLTK Data
The code requires some NLTK data packages. You can download them using the following commands:
```
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
```
### Download the Code
Clone this repository to your local machine:
```
git clone https://github.com/your-username/chatbot.git
cd chatbot
```
## Usage
- Prepare Your Text Corpus: Ensure you have a text file named chatbot.txt in the project directory. This file should contain the text corpus the chatbot will use to generate responses.

- Run the Chatbot: Execute the script to start the chatbot:
```
python chatbot.py
```
- Interact with the Chatbot: Start typing your text after the greeting to talk to the chatbot. To exit, type Bye.
## Features
- Text Preprocessing: The chatbot preprocesses the input text by converting it to lowercase, removing punctuation, and lemmatizing the tokens.
- Greeting Recognition: The chatbot can recognize and respond to common greetings.
- Response Generation: The chatbot generates responses based on the similarity of user input to sentences in

### Code Overview
- Imports and Initial Setup: The code imports necessary libraries and reads the text corpus.
- Text Preprocessing: Functions are defined to normalize text by removing punctuation and lemmatizing tokens.
- Greeting Functions: The code includes predefined inputs and responses for greetings.
- Response Function: The chatbot generates responses based on user input using TF-IDF and cosine similarity.
- Chat Flow: The main loop handles user interaction with the chatbot.

### Contributing
- Contributions are welcome! Please feel free to submit a Pull Request.

### License
- This project is licensed under the MIT License. See the LICENSE file for details.
