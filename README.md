# githubAPI
For work using the github API

The githubAPI file in the main directory can be run by a python interpreter on the command line and will ask for 
a username and password from the developer. It will then display information about the logged in deveoper.

The D3graph folder requires the use of flask to run python in a web browser. You can download flask and run the login.py 
file on the command line. If you then go to http://localhost:5000/login you will come to a login page where you can 
enter you github credentials. This will then display the repos and commits of that developer and will a graph of that
data, this may take a few seconds to display while the script retrieves data from the githubAPI.
