from flask import Flask, redirect, url_for, request,render_template, session
from github import Github
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
          return render_template('new.html', user = name)

@app.route('/data.tsv',methods = ['POST', 'GET'])
def fun():
    user = session["username"]
    pw = session["password"]
    g = Github(user,pw)
    fdata = """letter	frequency\n"""
    d = {}
    for repo in g.get_user().get_repos():
        numberOfCommits = 0
        print repo.name
        for commit in repo.get_commits():
            numberOfCommits += 1
        #fdata = fdata +  repr(numberOfCommits) + '\<br/\>'
        fdata = fdata + repo.name + "	" + repr(numberOfCommits) + "\n"
    return fdata


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      pw = request.form['pw']
      session["username"] = user
      session["password"] = pw
      g = Github(user,pw)
      fdata = ""
      d = {}
      for repo in g.get_user().get_repos():
          numberOfCommits = 0
          fdata = repo.name
          print repo.name
          for commit in repo.get_commits():
              numberOfCommits += 1
          #fdata = fdata +  repr(numberOfCommits) + '\<br/\>'
          d[fdata] = numberOfCommits

      return render_template('new.html', user = d)
      #return redirect(url_for('success',name = user, password = pw))
   else:
      return render_template('login.html')
if __name__ == '__main__':
    app.secret_key = 'djhvoiyewvohraubvhfa'
    app.run(debug = True)
