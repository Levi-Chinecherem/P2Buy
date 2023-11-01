from django.shortcuts import render, get_object_or_404, redirect
from .models import Feedback
from .forms import FeedbackForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'feedback/feedback_list.html', {'feedbacks': feedbacks})

@login_required
def feedback_create(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback_form.html', {'form': form})

@login_required
def feedback_update(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    if request.method == 'POST':
        form = FeedbackForm(request.POST, instance=feedback)
        if form.is_valid():
            form.save()
            return redirect('feedback_list')
    else:
        form = FeedbackForm(instance=feedback)
    return render(request, 'feedback/feedback_form.html', {'form': form})

@login_required
def feedback_delete(request, feedback_id):
    feedback = get_object_or_404(Feedback, id=feedback_id, user=request.user)
    if request.method == 'POST':
        feedback.delete()
        return redirect('feedback_list')
    return render(request, 'feedback/feedback_confirm_delete.html', {'feedback': feedback})
