from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from functools import wraps
from .models import Practice, PracticeAttempt
from django.shortcuts import get_object_or_404


def practice_access_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        # Get the test object if 'pk' is in kwargs
        test = None
        if 'pk' in kwargs:
            # Handle both Test instances and TestAttempt instances
            if 'practice-results' in request.path:
                test_attempt = get_object_or_404(PracticeAttempt, id=kwargs['pk'])
                test = test_attempt.test
            else:
                test = get_object_or_404(Practice, pk=kwargs['pk'])

        try:
            # Allow access if user is a member or if the test is free
            if request.user.userprofile.is_member or (test and test.is_free):
                return view_func(request, *args, **kwargs)
        except AttributeError:
            pass

        raise PermissionDenied

    return _wrapped_view