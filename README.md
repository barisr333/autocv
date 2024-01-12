# autocv
Automatically update CV files in popular job boards.

## TODO
- Fix AllJobs script (currently broken).
- Hebrew CV name support (Python parsing issue from JSON).
- Containerize w/ Docker.

## Requirements
- Currently supports Google Chrome and Microsoft Edge.
- [Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/), Version 120.0.6099.109
- [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH), Version 120.0.2210.91
- Python 3.10+

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
browser=''
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
- Wrapper script available, in scripts folder run:
```shell
bash run.sh
```
