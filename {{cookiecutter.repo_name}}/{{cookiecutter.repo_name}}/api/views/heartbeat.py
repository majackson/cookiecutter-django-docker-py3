from django.http import HttpResponse


def heartbeat_ok(request):
    """
    Just a simple view that returns a 200 response.
    Intended to be use for testing & monitoring of the service.
    """
    return HttpResponse()


def heartbeat_error(request):
    """
    Just a simple view that raises an exception.
    Intended to be use for testing & monitoring of the service.
    """
    raise Exception("This error intentionally raised.")
