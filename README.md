# FileHostingWebServer
Files Hosting webserver using ngrok


<h1 > Description </h1>
Basic webpage made for hosting files and accessing them from any part of the globe, with the help on ngrok, could be also used for sharing files with friends on the fly!
using python-flask, html/js , gunicorn, and ngrok. easy to use just follow the instructions!

<h1 color="green">installation</h1>
First make sure that you have:
<ul>
  <li>ngrok</li>
  <li>flask</li>
  <li>gunicorn</li>
</ul>




to install them first:
<h2>NGROK INSTALLATION: </h2>
make sure you're in the /Downloads directory
<pre> " wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz "</pre>
<pre> "tar zxvf /path/to/ngrok.tgz"</pre>
<pre> "./ngrok authtoken [your_auth_token]"</pre>
<br>
<b> TO GET YOUR TOKEN GO TO NGROK.COM AND REGISTER...</b>
<div>
<a href="https://www.youtube.com/watch?v=LYmhwKVNjk4&ab_channel=TECHDHEE">Here is a youtube guide</a>
</div>

<h2>FLASK INSTALLATION: </h2>
<pre>" pip install Flask "</pre>

<h2>GUNICORN INSTALLATION: </h2>
<pre>" pip install gunicorn "</pre>

<h1>After that you've installed everything we'll start with the server</h1>
<li> put "app.py" and "/templates/" and "/uploads/" and "/instance/" in var/www/html/ </li>
your /var/www/html/ should look like this 
<img src="screenshot1.PNG">
<li>open a terminal in the same directory</li>
<pre>" sudo python app.py "</pre>
<li>then open a new terminal in the same directory and run </li>
<pre>" python3 -m gunicorn -w 4 -b 127.0.0.1:8080 app:app "</pre>
<li>once again open a new terminal wherever you like and run</li>
<pre>"ngrok http 5000"</pre>
<br>
it should look something like this <img src="screenshot2.PNG">

NGROK will give you a url you can share it with friends from anywhere to share files!
all the uploads will be saved in /var/www/html/uploads/
you might need to run 
<pre>"sudo chmod -R 755 /var/www/html"</pre> </li>
if you get a premission error
<br>
<br>
once you've done all the steps you should have something like this 
<img src="screenshot3.PNG">
<br>
<p>It is suggested to work more on the front end (css, js) and have a good design. however, this works!</p>

For any help join my discord server 
<a href="https://discord.gg/587R6vqK8w">JOIN SERVER!</a>
