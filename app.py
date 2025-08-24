from flask import Flask, render_template, request
import random

app = Flask(__name__)

# This is the character set for the password generator
A = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@$%^&*()-_+='

@app.route('/')
def home():
    """Renders the homepage with the password input form."""
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_passwords():
    """Generates passwords based on user input and renders the results."""
    try:
        # Get the password length and number of passwords from the form
        length = int(request.form['length'])
        num = int(request.form['num'])

        # Create a list to store the generated passwords
        passwords = []
        for _ in range(num):
            password = ''.join(random.choice(A) for _ in range(length))
            passwords.append(password)
        
        # Render the result template with the generated passwords
        return render_template('result.html', passwords=passwords)

    except (ValueError, KeyError):
        # Handle cases where input is not a valid number or is missing
        error_message = "Please enter valid numeric values for both fields."
        return render_template('index.html', error=error_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
