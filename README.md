# WI-FI Speed Changer
I frequently open my router settings to simply change the wifi speed, </br>
Yes, I am lazy enough to write a  program to automate this task.
> \* [Why I changing the speed too often?](https://www.reddit.com/r/Egypt/comments/x7b8lb/unlimited_internet_in_egypt/)

### Supported Routers
- HG630 v2

\* If you are a Python developer, please consider contributing to support more routers, thanks

### Installation & Usage
```s
$ pip install git+https://github.com/abdulrahman1s/wifi-speed.git
# or python -m pip install git+https://github.com/abdulrahman1s/wifi-speed.git
$ wifi-speed
```

### Notice
The program will attempt to read those environment variables `ROUTER_USERNAME` and `ROUTER_PASSWORD` if detected the prompts will NOT show.
