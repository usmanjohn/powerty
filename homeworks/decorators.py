from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps

def member_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return redirect('login')  # Replace 'login' with your login URL name

        # Ensure the user has a UserProfile
        try:
            if request.user.userprofile.is_member:
                return view_func(request, *args, **kwargs)
        except AttributeError:
            pass  # UserProfile does not exist

        # Option 1: Raise Permission Denied
        raise PermissionDenied

        # Option 2: Redirect to a different page
        # return redirect('not_member')  # Replace 'not_member' with your desired URL name

    return _wrapped_view