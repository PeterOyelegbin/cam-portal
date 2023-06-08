from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .models import LoanApplication, UserModel
from .forms import ApplicationForm, ApplicationUpdateForm, ReviewForm


# Create your views here.
@login_required(login_url='http://127.0.0.1:8000/accounts/login') 
def applicationList(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    applicants = LoanApplication.objects.filter(applicant_name__icontains=q).order_by('-date_applied')
    return render(request, 'home.html', {'applicants': applicants})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def applicationForm(request):
    formset = ApplicationForm(request.POST or None)
    if formset.is_valid():
        sender = request.user
        recipient = get_object_or_404(UserModel, id=formset.data['recipient'])
        # send the token to the user email
        send_mail(
            subject='LAPS: Loan Application',
            message= f"Dear {recipient.first_name} {recipient.last_name},\n\n{formset.data['applicant_name']} with account number: {formset.data['applicant_account']} has applied for a loan, please click the link below to review the application.\nhttps://laps.vercel.app. \n\nRegards,\n{sender.first_name} {sender.last_name}\n{sender.email}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient.email]
        )
        formset.save()
        messages.success(request, 'Application submitted successfully')
        return redirect('home')
    else:       
        return render(request, 'application_form.html', {'formset': formset})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def applicationDetails(request, pk):
    applicant = get_object_or_404(LoanApplication, id=pk)
    return render(request, 'application_details.html', {'applicant': applicant})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def applicationUpdate(request, pk):
    object = get_object_or_404(LoanApplication, id=pk)
    formset = ApplicationUpdateForm(request.POST or None, instance=object)
    if formset.is_valid():
        formset.save()
        messages.success(request, 'Application successfully updated')
        return redirect('/application/details/'+pk)
    else:
        return render(request, 'application_update.html', {'formset': formset})


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def applicationDelete(request, pk):
    object = get_object_or_404(LoanApplication, id=pk)
    object.delete()
    return redirect('home')


@login_required(login_url='http://127.0.0.1:8000/accounts/login')
def applicationReview(request, pk):
    object = get_object_or_404(LoanApplication, id=pk)
    formset = ReviewForm(request.POST or None)
    if formset.is_valid():
        print(formset.data['official'])
        print(formset.data['applicant'])
        reviewer = get_object_or_404(UserModel, id=formset.data['official'])
        applicant = get_object_or_404(LoanApplication, id=formset.data['applicant'])
        recipient = get_object_or_404(UserModel, id=formset.data['recipient'])
        # notify the recipient by mail
        send_mail(
            subject='LAPS: Loan Review Request',
            message= f"Dear {recipient.first_name} {recipient.last_name},\n\nThis is to inform you that {reviewer.first_name} {reviewer.last_name} has reviewed {applicant.applicant_name}'s loan application with account number: {applicant.applicant_account}, please click the link below to view my review and make yours as well.\nhttps://laps.vercel.app/application/details/{formset.data['applicant']}. \n\nRegards,\n{reviewer.first_name} {reviewer.last_name}\n{reviewer.email}",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[recipient.email]
        )
        formset.save()
        messages.success(request, 'Review submitted successfully')
        return redirect('home')
    else:
        return render(request, 'review_form.html', {'formset': formset, 'data': object})
