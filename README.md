## Renamer-Bot
<p align="center" > <img alt="GitHub top language" src="https://img.shields.io/github/languages/top/Wolfy024/Renamer-Bot?style=plastic">
 <a> <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr-raw/Wolfy024/Renamer-Bot?color=blue&label=Open%20PRs"> <img alt="GitHub closed pull requests" src="https://img.shields.io/github/issues-pr-closed-raw/Wolfy024/Renamer-Bot?color=blue&label=Closed%20PRs"> </a> </p>

<p align="center" > <img alt="GitHub forks" src="https://img.shields.io/github/forks/Wolfy024/Renamer-Bot?logoColor=blue&style=social"> </p>

## Basic Overview

This is aimed to be a private renamer bot for you and your admin community.Only works in PM, Group support be added later. It will respond in group but will crash.Only one person can use the bot at a time for now(This has been done to preserve the batch renaming feature).Multiple user support soon.

## Added Features

- [x] Batch Renaming
- [x] Cancellation Feature
- [x] Downloading / Uploading Progress
- [x] Batch Renaming
- [x] Auto forwarding to Channel


## Commands

| Commands    | Description | 
| :---        |    :---     |
| /start      | Confirm if the bot is alive. |
| /help       | Basic overview |
| /setthumb   | Set thumbnail | 
| /remthumb   | Remove thumbnail | 
| /rename `name to be used without extension`| Renames the replied file |
| /batch `name to be used without extension` | Renames batch of files from the file replied till last with automatic numbering at its end |
| /batch(number) `name to be used without extension` | Renames batch of files from the file specified till the number of messages given |
| #zzz`followed by a number at the end of rename`| For custom numbering. (only works with both /batch commands.)
| /autoforward `channel id with - ` | Forward to given channel (not to  mention bot should be in the given channel) |
| /autoforward(number)  `channel id with - ` | Forward to given channel from the specified file till the number of messages given (not to  mention bot should be in the given channel) |
| /add `user ID`  | Adds user to whitelist (_Everytime you restart the bot, you have to re-add everyone. The code maks use of a local list and not a database._)|



## Deploy To Heroku 
<details>
 <summary> Deploy </summary>
Fill the VARS correctly and turn on the dyno worker.<br>
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Wolfy024/Renamer-Bot)
</details>

## Known Issues
Can't Support multiple users as of now.
