from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps
from .models import Test, TestAttempt
from django.shortcuts import get_object_or_404
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

def test_access_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        # Get the test object if 'pk' is in kwargs
        test = None
        if 'pk' in kwargs:
            # Handle both Test instances and TestAttempt instances
            if 'test-results' in request.path:
                test_attempt = get_object_or_404(TestAttempt, id=kwargs['pk'])
                test = test_attempt.test
            else:
                test = get_object_or_404(Test, pk=kwargs['pk'])

        try:
            # Allow access if user is a member or if the test is free
            if request.user.userprofile.is_member or (test and test.is_free):
                return view_func(request, *args, **kwargs)
        except AttributeError:
            pass

        raise PermissionDenied

    return _wrapped_view
from .models import MultipleChoiceQuestion

