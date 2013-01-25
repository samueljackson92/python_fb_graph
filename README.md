Gephi Facebook Graph
====================

Creates a graph of your Facebook friends and exports it to a Gephi readable XML file.
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
