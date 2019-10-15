# news-highlight

news-highlight is an app that fetches data from [News API](https://newsapi.org/) and displays it on a webpage

## author

Timothy Oliver [@ThukuWakogi](https://github.com/ThukuWakogi)

## features

1. Users can view news sources.
2. Users can visit news sources' home page
3. Users can view news articles from a news source
4. Users can be directed to full news article

## behaviour driven development

|behaviour|input|output|
|-|-|-|
|Home page loads.|User clicks on 'visit page' link.|User is directed to news source home page.|
|Home page loads.|User clicks on 'View articles' link.|User is directed to Source page|
|Source page loads|User clicks on 'Read full article' link.|User is directed to link with full article|

## SetUp

To view a demo of the application, click [here](https://thukuwakogi-news-highlight.herokuapp.com/).

The source code for this application can be accessed. For it to run, you will need [Python](https://www.python.org/) and an api key from [News API](https://newsapi.org/)

a copy of the source code can be gotten through:

- downloading the zip from github.
- opening a terminal in the preferred directory then entering `git clone https://github.com/ThukuWakogi/news-highlight.git`
- using a git client such as [Github desktop](https://desktop.github.com/) or [GitKraken](https://www.gitkraken.com/)

### installing

#### windows

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python -m venv virtual`
* Activating the virtual environment may change based on the terminal or shell being used.
* For command prompt, enter `virtual\Scripts\activate` or simply type in activate.
* For powershell, the execution policy should be bypassed for the script to run. This can be done by entering `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then proceeding on with entering .`.\virtual\Scripts\Activate.ps1`
* Install packages. `pip install -r requirements.txt`
* Setting environment variables differs with the terminal or shell being used
* For command prompt, enter your news api key `SET NEWS_API_KEY=<your news api key here>` then start the server `python manage.py server`
* For powershell, enter your news api key `$env:NEWS_API_KEY="<your news api key here>"` then start the server `python manage.py server`

#### unix

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python3.x -m venv --without-pip virtual` replace x with version in host machine, preferably version v3.6 for this project
* Activate the virtual environment `source virtual/bin/activate`
* Download pip into the virtual environment `curl https://bootstrap.pypa.io/get-pip.py | python`
* Install packages. `pip install -r requirements.txt`
* set `NEWS_API_KEY` environment variable `export NEWS_API_KEY=<your news api key here>`
* start the server `python3.x manage.py server`
