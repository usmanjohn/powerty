from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Max
from .models import PracitceQuestions, Practice, UserPrAnswer, PracticeAttempt

@login_required
def pr_question_detail(request, pk):
    question = get_object_or_404(PracitceQuestions, pk=pk)
    return render(request, 'practice/pr_question_detail.html', {'question': question})
@login_required
def select_practice(request):
    latest_attempts = {}
    count_try = 0
    tests = Practice.objects.all()
    if request.user.userprofile.is_member:
        attempts = PracticeAttempt.objects.filter(user=request.user).order_by('-timestamp')
        count_try = attempts.count 
        for attempt in attempts:
            if attempt.test_id not in latest_attempts or attempt.timestamp > latest_attempts[attempt.test_id].timestamp:
                latest_attempts[attempt.test_id] = attempt

    return render(request, 'practice/practice_list.html', {'tests': tests, 'count_try':count_try,'attempts': latest_attempts.values()})

@login_required
def start_practice(request, pk):
    test = get_object_or_404(Practice, pk=pk)
    questions = test.practice_questions.all()
    progress_percentage = 100
    return render(request, 'practice/practice_start.html', {'questions': questions, 'test': test, 'progress_percentage':progress_percentage})

@login_required
def submit_practice(request, pk):
    test = get_object_or_404(Practice, id=pk)
    questions = test.practice_questions.all()
    
    if request.method == 'POST':
        correct_answers = 0
        total_questions = questions.count()
        
        # Create a new test attempt
        test_attempt = PracticeAttempt.objects.create(user=request.user, test=test)
        
        for question in questions:
            selected_choice = int(request.POST.get(f'question_{question.id}'))
            user_answer = UserPrAnswer.objects.create(
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

        return redirect('practice-results', pk=test_attempt.id)
    
    return render(request, 'practice/practice_start.html', {'test': test, 'questions': questions})

@login_required
def practice_results(request, pk):
    test_attempt = get_object_or_404(PracticeAttempt, id=pk, user=request.user)
    user_answers = UserPrAnswer.objects.filter(test_attempt=test_attempt)


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

    return render(request, 'practice/practice_results.html', {
        'test_attempt': test_attempt,
        'results': results
    })