from flask import Flask, redirect, request, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return "Strona glowna"

@app.route('/mypage/me')
def about():
    return render_template('about.html')

def save_message(message):
    print(message)

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form['message']

        save_message(message)
    return render_template('contact.html')

@app.route('/submit_message', methods=['POST'])
def submit_message():
    if request.method == 'POST':
        message = request.form['message']
        print('Wiadomosc:', message)
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)