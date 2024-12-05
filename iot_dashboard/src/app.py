from flask import Flask, render_template, request, redirect, url_for
from mqtt import mqtt_client
from influxdb import influxdb_client

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard/<room>')
def dashboard(room):
    data = influxdb_client.get_data(room)
    return render_template('dashboard.html', data=data)

@app.route('/send_command', methods=['POST'])
def send_command():
    command = request.form['command']
    mqtt_client.publish("commands", command)
    influxdb_client.write_command(command)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)