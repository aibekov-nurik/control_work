from .models import GuestbookEntry
from django.shortcuts import render, redirect
from .forms import GuestbookEntryForm
from django.shortcuts import get_object_or_404

def guestbook_home(request):
    entries = GuestbookEntry.objects.filter(status='active').order_by('-created_at')
    return render(request, 'guestbook/home.html', {'entries': entries})


def add_guestbook_entry(request):
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('guestbook_home')
    else:
        form = GuestbookEntryForm()
    return render(request, 'guestbook/add_entry.html', {'form': form})

def edit_guestbook_entry(request, pk):
    entry = get_object_or_404(GuestbookEntry, pk=pk)
    if request.method == 'POST':
        form = GuestbookEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('guestbook_home')
    else:
        form = GuestbookEntryForm(instance=entry)
    return render(request, 'guestbook/edit_entry.html', {'form': form, 'entry': entry})

