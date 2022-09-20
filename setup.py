from setuptools import setup

setup(
    name="wifi-speed",
    description="A tool to change the speed of WI-FI",
    version="0.0.1",
    url="https://github.com/abdulrahman1s/wifi-speed",
    packages=["wifi_speed", "wifi_speed.util", "wifi_speed.routers"],
    install_requires = ["questionary==1.10.0", "pyquery==1.4.3"],
    scripts = ["bin/wifi-speed"],
)