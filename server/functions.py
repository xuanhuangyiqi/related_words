from django.http import HttpResponse


def jsonResponse():
    response = HttpResponse()
    response['Content-Type'] = 'application/json'
    return response
