from .models import GuestbookEntry
from django.shortcuts import render, redirect
from .forms import GuestbookEntryForm
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
