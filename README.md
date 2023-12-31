# CV Auto Upload
Upload up-to-date CVs to popular job boards.

## TODO
- Add automatic CV deletion functionality - delete CV with same name.
- Add support for multiple CVs.
- Add unit tests.
- Expand support to AllJobs, Drushim.IL.
- More as I come up with it...

## Requirements
- Currently supports Google Chrome only.
- [Chromedriver](https://googlechromelabs.github.io/chrome-for-testing/): Currently version 120.0.6099.109
- Python 3.11.7

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
- Create .env file in repo folder
- Current structure of .env file is as follows:
```
AJ_Email = ''
AJ_Password = ''
LI_Username = ''
LI_Password = ''
CV_Path = ''
```
AJ = Alljobs credentials. LI = LinkedIn credentials. CV_Path = Path to current up-to-date CV.
If uploaded to GitHub, remember to include .env in .gitignore.
