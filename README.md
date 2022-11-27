<h1 align="center">Discord TOURNAMENT</h1>
<p align=center>
    <a target="_blank" href="https://www.python.org/downloads/" title="Python Version"><img src="https://img.shields.io/badge/python-%33.8-purple.svg"></a>
</p> 

<p align="center"><b>Python script which find winners by reactions on message in discord</b></p>

<p align="center">  
        <img src="https://i.ibb.co/3hrtXFY/screen1.png" alt=""/>
</p>

## About

Python script to choose a certain number of winners by reactions on discord message

## Configuring

**Rename *.env.dev* to *.env***

**Open *.env* configuration file with text editor and set the following variables:**
```ini
DISCORD_TOKEN=Mj3COTc3swA5MzA0MDA2NjU3.G3gnQv
CHANNEL_ID=780950361702924308
MESSAGE_ID=1044038040605179905
REACTION_ID=55242:1044037047771475998
```
### How to get DISCORD_TOKEN
Press F12 or Ctrl+Shift+I in your browser.
Open Console

paste this into the Console (while being logged in) and before the loading animation has finished, paste it again.
```javascript
window.location.reload();
copy(document.body.appendChild(document.createElement `iframe`).contentWindow.window.localStorage.token);
```
The token should be in your Clipboard. If it's just "null" or "undefined" do the same thing again. Don't wait too long inbetween the two times

### How to get CHANNEL_ID and MESSAGE_ID
<p>Copy message link</p>
<img src="https://i.ibb.co/80G2Nt0/mess.png">

```
https://discord.com/channels/721887895157211181/780950361702924308/1044038040605179905

CHANNEL_ID=780950361702924308 (second number)
MESSAGE_ID=1044038040605179905 (third number)
```

### How to get REACTION_ID
Press F12 or Ctrl+Shift+I in your browser.

Press Ctrl+Shift+C, point to reaction and click on it

<img src="https://i.ibb.co/Mcfw277/Screenshot-2.png">

<img src="https://i.ibb.co/N7bCSWq/Screenshot-3.png">

get values in *alt* and *data-id* and join with ':'
```
REACTION_ID=1259tickgreen:840273469731766313
```
## Running
### Using Python
```shell
# install requirements
$ python3 -m pip install -r requirements.txt
# run script
$ python3 main.py
```