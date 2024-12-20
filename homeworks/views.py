from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import MultipleChoiceQuestion, Test, UserAnswer, TestAttempt
from .decorators import member_required, test_access_required
from itertools import groupby
from operator import attrgetter


from django.db.models import Case, When, Value, IntegerField

def select_test(request):
    # Define the custom order for test types
    type_order = {
        'math': 1,
        'geometry': 2,
        'mixed': 3,
        'other': 4
    }
    
    # Create a Case/When for custom type ordering
    type_order_case = Case(
        *[When(type=key, then=Value(value)) for key, value in type_order.items()],
        output_field=IntegerField(),
    )
    
    # Get all tests with custom ordering
    tests = Test.objects.annotate(
        type_order=type_order_case
    ).order_by(
        'type_order',  # First order by type (math -> geometry -> mixed -> other)
        'order',       # Then by the order field
        'date'        # Finally by date (newest first)
    )
    
    attempts = []
    count_try = 0
    
    if request.user.is_authenticated:
        attempts = TestAttempt.objects.filter(user=request.user).order_by('-timestamp')
        count_try = attempts.count()
        
        # Get latest attempts for each test
        latest_attempts = {}
        for attempt in attempts:
            if attempt.test_id not in latest_attempts or \
               attempt.timestamp > latest_attempts[attempt.test_id].timestamp:
                latest_attempts[attempt.test_id] = attempt
        attempts = latest_attempts.values()

    # Add is_accessible flag to tests
    for test in tests:
        test.is_accessible = request.user.is_authenticated and \
            (request.user.userprofile.is_member or test.is_free)

    # Group tests by type for template rendering
    grouped_tests = {}
    for test in tests:
        if test.type not in grouped_tests:
            grouped_tests[test.type] = []
        grouped_tests[test.type].append(test)

    return render(request, 'homeworks/test_list.html', {
        'tests': tests,
        'grouped_tests': grouped_tests,
        'count_try': count_try, 
        'attempts': attempts
    })
    
@test_access_required
def start_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()
    return render(request, 'homeworks/test_start.html', {'questions': questions, 'test': test})



     
@test_access_required
def submit_test(request, pk):
    test = get_object_or_404(Test, id=pk)
    questions = test.questions.all()
    
    if request.method == 'POST':
        correct_answers = 0
        total_questions = questions.count()
        
        # Create a new test attempt
        test_attempt = TestAttempt.objects.create(user=request.user, test=test)
        
        for question in questions:
            selected_choice = int(request.POST.get(f'question_{question.id}'))
            user_answer = UserAnswer.objects.create(
                user=request.user,
                question=question,
                selected_choice=selected_choice,
                test_instance=test,
                test_attempt=test_attempt
            )
            if user_answer.is_correct():
                correct_answers += 1
        
        score = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
        test_attempt.score = score
        test_attempt.save()

        return redirect('test-results', pk=test_attempt.id)
    
    return render(request, 'homeworks/test_start.html', {'test': test, 'questions': questions})

@test_access_required
def test_results(request, pk):
    test_attempt = get_object_or_404(TestAttempt, id=pk, user=request.user)
    user_answers = UserAnswer.objects.filter(test_attempt=test_attempt)

    results = []
    for user_answer in user_answers:
        question = user_answer.question
        correct_answer = getattr(question, f'choice{question.correct_answer}')
        selected_answer = getattr(question, f'choice{user_answer.selected_choice}')
        results.append({
            'question': question.question_text,
            'questionpk':question.pk,
            'selected_answer': selected_answer,
            'correct_answer': correct_answer,
            'is_correct': user_answer.is_correct(),
            'explanation': question.explanation,
        })

    return render(request, 'homeworks/test_results.html', {
        'test_attempt': test_attempt,
        'results': results
    })

@login_required
def question_detail(request, pk):
    question = get_object_or_404(MultipleChoiceQuestion, pk=pk)
    return render(request, 'homeworks/question_detail.html', {'question': question})