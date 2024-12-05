# IoT Dashboard Project

This project is an IoT dashboard that visualizes data from various sensors using MQTT and InfluxDB. It allows users to monitor trends and gauges for different rooms or categories and send commands to sensors.

## Project Structure

```
iot-dashboard
├── src
│   ├── app.py               # Entry point of the application
│   ├── dashboard            # Contains logic for rendering the dashboard
│   │   └── __init__.py
│   ├── mqtt                 # Manages MQTT client
│   │   └── __init__.py
│   ├── influxdb             # Handles InfluxDB interactions
│   │   └── __init__.py
│   └── telegraf            # Telegraf configuration
│       └── telegraf.conf
├── requirements.txt         # Project dependencies
├── README.md                # Project documentation
└── setup.py                 # Packaging configuration
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd iot-dashboard
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the Telegraf settings in `src/telegraf/telegraf.conf` to match your MQTT broker and InfluxDB setup.

4. Run the application:
   ```
   python src/app.py
   ```

## Usage Guidelines

- Access the dashboard through your web browser to view sensor data and control commands.
- The dashboard supports multiple rooms or categories, allowing for organized monitoring.
- Use the MQTT functionality to send commands to your sensors as needed.

## Contributing

Feel free to submit issues or pull requests to improve the project!