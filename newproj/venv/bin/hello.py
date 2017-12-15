from flask import Flask
from github import Github
import getpass
app = Flask(__name__)

@app.route('/')
def hello_world():
    username = raw_input("Github Username:")
    pw = getpass.getpass()
    g = Github(username,pw)
    for repo in g.get_user().get_repos():
        print repo.name
    return 'Hello World'

if __name__ == '__main__':
   app.run()
