from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cheat(request):
    """
    Cheat code for testing through get requests
    cookies: cookie_name && cookie_value required to work
    """
    response = ""
    if request.GET.get("cookie_name") != None and request.GET.get("cookie_value"):
        response += f"Added a cookie {request.GET.get('cookie_name')}:{request.GET.get('cookie_value')} <br>"
        request.session[request.GET.get("cookie_name")] = request.GET.get("cookie_value")

    if (show_cookie_value := request.GET.get("show_cookie_value")) != None:
        response += f"Value of the cookie {show_cookie_value}: {request.session[show_cookie_value]}<br>"

    if response == "":
        response = "Didn't found anything to do"
    return HttpResponse(response)
