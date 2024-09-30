### Assignment:
Use gpt-engineer to generate a project for visual studio code for your favorite application.
Use screencast to demonstrate various usecases of this extension: https://code.visualstudio.com/docs/editor/artificial-intelligence#_chat-view 
Writing functions and code
Refactoring code
Writing unit tests
Writing entire app
submit your screencast and code generated in github repo
Showcase the power of combining chatgpt plugin and visual studio code 

### Solution:

## GPT-Engineer: 
GPT Engineer is a tool that uses the power of GPT (Generative Pretrained Transformers)to generate code. GPT-Engineer generates code based on desired preferences. This means that you can guide the tool to generate code in a specific style or format, making it a highly adaptable tool for various coding projects.

```sh
# Install GPT Engineer:
python -m pip install gpt-engineer

# Set Up GPT Engineer:
export OPENAI_API_KEY="your API Key"
```


#### Random Joke Generator App:

1. **app.py**: This is the main entry point of the application. It sets up the Flask app, defines a route to fetch and display the joke, and includes a function to fetch the joke from the API.
2. **index.html**: This is the HTML template that renders the web page. It includes a placeholder for the joke and links to the CSS file for styling.
3. **styles.css**: This file contains the CSS styles to make the web page colorful and visually appealing.
4. **requirements.txt**: This file lists the dependencies required for the project.

INFO:httpx:HTTP Request: POST https://api.openai.com/v1/chat/completions "HTTP/1.1 200 OK"
```sh
#!/bin/bash

# Navigate to the project directory
cd random_joke_app

# Install dependencies
pip install -r requirements.txt

# Run the Flask application
python app.py
```

### URL: http://127.0.0.1:5000/

<img width="1440" alt="Screenshot 2024-09-29 at 11 44 44 PM" src="https://github.com/user-attachments/assets/46f5db75-8d52-4a72-8e8d-8fbb7498770a">
