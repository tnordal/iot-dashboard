from setuptools import setup, find_packages

setup(
    name='iot-dashboard',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'Flask',
        'paho-mqtt',
        'influxdb-client',
    ],
    entry_points={
        'console_scripts': [
            'iot-dashboard=app:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A dashboard for IoT projects using MQTT and InfluxDB',
    url='https://github.com/yourusername/iot-dashboard',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)