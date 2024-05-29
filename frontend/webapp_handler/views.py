from django.shortcuts import render, redirect, get_object_or_404
from .forms import TextEntryForm
from .models import TextEntry
from .services import process_text_list
from src.app import App

app = App(True, pickle_filepath="graph.gpickle")
app.initialize_state()

def text_entry_view(request):
    if request.method == 'POST':
        form = TextEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('text_entry_success')
    else:
        form = TextEntryForm()
    return render(request, 'webapp_handler/text_entry.html', {'form': form})

def text_entry_success_view(request):
    entries = TextEntry.objects.all()
    geojson = None  # Initially, no processing done
    if request.method == 'POST':
        # Check if the processing button is clicked
        if 'process_text' in request.POST:
            # Process all texts
            texts = [entry.text for entry in entries]
            geojson = process_text_list(texts, app)
    return render(request, 'webapp_handler/text_entry_success.html', {
        'entries': entries,
        'geojson': geojson
    })

def delete_text_entry_view(request, entry_id):
    entry = get_object_or_404(TextEntry, id=entry_id)
    entry.delete()
    return redirect('text_entry_success')

def process_text_entries_view(request):
    pass