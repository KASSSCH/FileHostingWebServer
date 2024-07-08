# FileHostingWebServer
Files Hosting webserver using ngrok


<h1> Description </h1>
Basic webpage made for hosting files and accessing them from any part of the globe, with the help on ngrok. Could be hosted to tor network for a safer environment, could be also used for sharing files with friends on the fly!
using python-flask, html/js , gunicorn, and ngrok. easy to use just follow the instructions!

<h1>installation</h1>
First make sure that you have:
<ul>
  <li>ngrok</li>
  <li>flask</li>
  <li>gunicorn</li>
</ul>




to install them first:
<h2>NGROK INSTALLATION: </h2>
make sure you're in the /Downloads directory
<li> " wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz "</li>
<li> "tar zxvf /path/to/ngrok.tgz"</li>
<li> "./ngrok authtoken [your_auth_token]"</li>
<b> TO GET YOUR TOKEN GO TO NGROK.COM AND REGISTER...</b>
<div>
<a href="https://www.youtube.com/watch?v=LYmhwKVNjk4&ab_channel=TECHDHEE">Here is a youtube guide</a>
</div>

<h2>FLASK INSTALLATION: </h2>
<li>" pip install Flask "</li>

<h2>GUNICORN INSTALLATION: </h2>
<li>" pip install gunicorn "</li>
<h1>After that you've installed everythin we'll start with the server</h1>
<li> put "app.py" and "/templates/index.html" and "/uploads/" in var/www/html/ </li>
<li>open a terminal then type the command "cd /var/www/html"</li>
<li>run " sudo python app.py "</li>
<li>then open a new terminal in the same directory and run " python3 -m gunicorn -w 4 -b 127.0.0.1:8080 app:app "</li>
<li>last step run 'sudo ngrok http server in a new terminal that can be in any directory"</li>
NGROK will give you a url you can share it with friends from anywhere to share files!

For any help join my discord server 
<a href="https://discord.gg/587R6vqK8w">JOIN SERVER!</a>
