Gephi Facebook Graph
====================

Creates a graph of your Facebook friends and exports it to a Gephi readable XML file.
<<<<<<< HEAD
Connects to Facebook using the oauth service provided by foauth (https://foauth.org/).
You'll need to make a foauth account in order to use it.

Usage
-----

Simply run fb_graph.py and enter the email address and password that you use to connect
to services using a foauth account. The graph will be output in a file called output.gexf which
can be loaded into the <a href="https://gephi.org/">Gephi</a> graph visualisation program.
=======
Facebook command line OAuth implementation (in fb_auth.py) based on code published here: http://goo.gl/MrlfR

Configuration
-------------
There is currently no server avalible to interface requests to the Facebook Graph API from this script.
Instead, you must register and create a new app with Facebook. Once your new app is registered, you must place your application
ID and secret in a file called <b>.fb_app_config</b> like so:

```
Your_App_ID
Your_App_Secret
```

You must also configure your application's website (redirect) URL to be ```http://127.0.0.1:8080```

Plans to possibly convert the application to use <a href="https://foauth.org/">foauth</a> instead are in the works!
>>>>>>> 7e6e41c9020060edc6699d38e1f5cbdc98229d34
