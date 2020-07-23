# Cookie cheat

Django application that can be used to modifiy the value of cookies on a browser with get messages.

## Warning:

The code here can modify the cookies and they'll still seem totally normal for the browser.
**Make sure that you never use this app in production**

The `.gitignore` is set up so that you can add the app in a project folder and it won't be seen by git
(unless you use -f) but make sure to clean `yourproject/urls.py` before committing.

## Installation:

- Put the cheat folder in the project root
- in `yourproject/urls.py` add
  ```py
  from django.urls import include

  urlpatterns = [
  ...
  path('cheat/', include('cheat.urls')),
  ...
  ]
  ```
- It's now possible to alter cookies

## Usage:

Go to `yoururl/cheat?` and add arguments. Several can be used at the same time

### Add a cookie:
Will create a new cookie with the name `cookie_name` and the value `cookie_value`. Both arguments must be present to add the cookie.

Example: `yoururl/cheat?cookie_name=new_cookie&cookie_value=new_value`
will create a cookie named `new_cookie` with a value of `new_value`

### View cookie value
Will display the value of the cookie `show_cookie_value`

Example: `yoururl/cheat?show_cookie_value=new_cookie`
will display `new_value` if you've done the example above
