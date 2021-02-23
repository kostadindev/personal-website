
from flask import Flask, render_template, request, redirect
import csv
import smtplib
from email.message import EmailMessage

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name='index.html'):
    return render_template(page_name)


def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        name = data['name']
        email = data['email']
        message = data['message']

        # commented because python anywhere does not support smtp requests
        # gmail = EmailMessage()

        # gmail['from'] = 'Kostadin Devedzhiev'
        # gmail['to'] = 'kostadin@hawaii.edu'
        # gmail['subject'] = f'Website Message from {name}, {email}'

        # gmail.set_content(message)

        # with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        #     smtp.ehlo()
        #     smtp.starttls()
        #     smtp.login('kocetobrat@gmail.com', 'DMjk2tKE')
        #     smtp.send_message(gmail)

        csv_writer = csv.writer(database, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form(page_name='index.html'):
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thank-you.html')
        except:
            return 'did not save to database'
    else:
        return 'error line 44 app.py'


if __name__ == '__main__':
    app.run()
