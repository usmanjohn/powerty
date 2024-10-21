from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import MultipleChoiceQuestion, Test, UserAnswer, TestAttempt
from .decorators import member_required, test_access_required



@login_required
def select_test(request):
    latest_attempts = {}
    count_try = 0
    tests = Test.objects.all()
    
    # Get attempts for both members and non-members
    attempts = TestAttempt.objects.filter(user=request.user).order_by('-timestamp')
    count_try = attempts.count()
    
    for attempt in attempts:
        if attempt.test_id not in latest_attempts or attempt.timestamp > latest_attempts[attempt.test_id].timestamp:
            latest_attempts[attempt.test_id] = attempt

    # Add is_accessible flag to tests
    for test in tests:
        test.is_accessible = request.user.userprofile.is_member or test.is_free

    return render(request, 'homeworks/test_list.html', {
        'tests': tests, 
        'count_try': count_try,
        'attempts': latest_attempts.values()
    })

@test_access_required
def start_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    questions = test.questions.all()
    return render(request, 'homeworks/test_start.html', {'questions': questions, 'test': test})


@test_access_required
def question_detail(request, pk):
    question = get_object_or_404(MultipleChoiceQuestion, pk=pk)
    return render(request, 'homeworks/question_detail.html', {'question': question})
     
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
            'pk':question.pk,
            'selected_answer': selected_answer,
            'correct_answer': correct_answer,
            'is_correct': user_answer.is_correct(),
            'explanation': question.explanation,
        })

    return render(request, 'homeworks/test_results.html', {
        'test_attempt': test_attempt,
        'results': results
    })