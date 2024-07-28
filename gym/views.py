from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .forms import MemberForm
from django.utils import timezone
from datetime import timedelta

def dashboard(request):
    members = Member.objects.all()
    due_members = [member for member in members if member.is_due()]
    context = {
        'members': members,
        'due_members': due_members,
    }
    return render(request, 'gym/dashboard.html', context)

def member_list(request):
    members = Member.objects.all()
    return render(request, 'gym/member_list.html', {'members': members})

def member_create(request):
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm()
    return render(request, 'gym/member_form.html', {'form': form})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('member_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'gym/member_form.html', {'form': form})

def member_delete(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == 'POST':
        member.delete()
        return redirect('member_list')
    return render(request, 'gym/member_confirm_delete.html', {'member': member})

def report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        members = Member.objects.filter(fee_date__range=[start_date, end_date])
        total_revenue = sum(member.fee_amount for member in members)
        context = {
            'total_revenue': total_revenue,
            'start_date': start_date,
            'end_date': end_date,
        }
        return render(request, 'gym/report.html', context)
    return render(request, 'gym/report.html')
