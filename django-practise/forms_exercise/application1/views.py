from django.shortcuts import render
from application1.forms import ContactForm

# Create your views here.
def contact_view(request):
    form = ContactForm()  # default form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Example: just print data for now
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(name, email)
            # Optionally, reset the form after submission
            form = ContactForm()
    
    # ALWAYS return a response
    return render(request, 'contact.html', {'form': form})

