from django.http import HttpResponse

def method(http_method : str = "GET"):
    """
    Middleware untuk menentukan tipe request
    
    Args:
        http_method : str -> method http [GET, POST, PUT, DELETE, dll]

    Returns:
        view
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if request.method == http_method:
                # Call the view function only if the request method matches
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("Method Not Allowed", status=405)

        return _wrapped_view
    return decorator


