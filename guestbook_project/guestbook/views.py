from .models import GuestbookEntry
from django.shortcuts import render, redirect
from .forms import GuestbookEntryForm
from django.shortcuts import get_object_or_404

def guestbook_home(request):
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'home.html', {'entries': entries})


def add_guestbook_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook_home')
    else:
        form = GuestbookEntryForm()
    return render(request, 'add_entry.html', {'form': form})

def edit_guestbook_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('guestbook_home')
    else:
        form = GuestbookEntryForm(instance=entry)
    return render(request, 'edit_entry.html', {'form': form, 'entry': entry})

def delete_guestbook_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        input_email = request.POST.get('email')
        if input_email == entry.author_email:
            entry.delete()
            return redirect('guestbook_home')
        else:
            error_message = "Неправильный email."
            return render(request, 'delete_entry.html', {'entry': entry, 'error_message': error_message})
    return render(request, ''
                           'delete_entry.html', {'entry': entry})


