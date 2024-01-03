# CV Auto Upload
Upload up-to-date CVs to popular job boards.

## TODO
- Add AllJobs support (currently broken).
- Add Hebrew CV name support (currently Python can't seem to parse the JSON).
- Add wrapper script to run everything.

## Requirements
- Currently supports Google Chrome only.
- [Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/): Currently version 120.0.6099.109
- Python 3.7

## Packages
- Selenium and dotenv packages required.
```shell
pip install selenium
```
```shell
pip install python-dotenv
```
## Usage
- Clone repo.
- Create .env and path_config.json file in repo folder. A .env file specifies environment variables and is used for sensitive login info. The path_config.json file specifies name and system path for each CV file.
- Current structure of .env file is as follows:
```
AJ_EMAIL = ''
AJ_PASSWORD = ''
LI_USERNAME = ''
LI_PASSWORD = ''
DR_EMAIL=''
DR_PASSWORD=''
```
LI = LinkedIn, AJ = AllJobs, DR = Drushim.IL

- path_config.json file structure is as follows:
```json
 [
    {
        "Name": "Example1",
        "Path": "C:\\Users\\myUser\\Ex_CV_1.pdf"
    },

    {
        "Name": "Example2",
        "Path": "C:\\Users\\myUser\\Ex_CV_2.pdf"
    }
]
```
- **IMPORTANT**: 'Name' field must be a **unique** string or substring included in the CV name on LinkedIn/AJ.
- **IMPORTANT**: Don't forget to include .env and .json files in .gitignore.
