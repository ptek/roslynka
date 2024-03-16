# Roslinka

A toy project for monitoring the humidity levels of the plants. The project is
based on a raspberry pi, with Adafruit STEMMA Soil Sensor connected to it.

Currently the Raspberry pi is running the latest dietpi image, with python3 and poetry installed. The project is using the Adafruit CircuitPython library to read the sensor data.

# Setup and Dependencies

Following system-wide packages must be installed on the Raspberry Pi (on dietpi OS):

```shell
apt-get install --no-install-recommends -y \
  build-essential \
  rpi.gpio-common \
  i2c-tools \
  libgpiod-dev \
  python3 \
  python3-rpi.gpio \
  python3-libgpiod

pip install uv
```
