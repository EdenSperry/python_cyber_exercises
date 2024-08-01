from flask import Flask, request
import html

app = Flask(__name__)

# Vulnerable page (before fixing XSS)


@app.route('/vulnerable')
def vulnerable():
    user_input = request.args.get('input', '')
    return f"<h1>User Input:</h1> {user_input}"  # This is vulnerable to XSS

# Secure page (after fixing XSS)


@app.route('/secure')
def secure():
    user_input = request.args.get('input', '')
    sanitized_input = html.escape(user_input)  # Sanitize user input
    return f"<h1>User Input:</h1> {sanitized_input}"


if __name__ == '__main__':
    app.run(debug=True)


# Access the Vulnerable Page: Open a web browser and visit:
# http: // 127.0.0.1: 5000/vulnerable?input = <script > alert('XSS') < /script >

# Access the Secure Page: Visit:
# http: // 127.0.0.1: 5000/secure?input = <script > alert('XSS') < /script >
