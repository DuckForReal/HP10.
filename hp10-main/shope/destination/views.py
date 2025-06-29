from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Destination
from .forms import DestinationForm
# Create your views here.
def destination_list(request):
    destinations = Destination.objects.all()
    return render(request, 'destination/destination_list.html', {'destinations': destinations})

def destination_detail(request, slug):
    destination = get_object_or_404(Destination, slug=slug)
    return render(request, 'destination/destination_detail.html', {'destination': destination})

def destination_create(request):
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES)
        if form.is_valid():
            destination = form.save()
            messages.success(request, 'Destination created successfully!')
            return redirect('destination:destination_detail', slug=destination.slug)
    else:
        form = DestinationForm()
            
    return render(request, 'destination/destination_form.html',{'form': form, 'title': 'Add New Destination'})
    
def destination_edit(request,slug):
    destination = get_object_or_404(Destination, slug=slug)
    if request.method == 'POST':
        form = DestinationForm(request.POST, request.FILES, instance=destination)
        if form.is_valid():
            destination = form.save()
            messages.success(request, 'Destination updated successfully!')
            return redirect('destination:destination_detail', slug=destination.slug)
    else:
        form = DestinationForm()
    return render(request, 'destination/destination_form.html',{'form': form, 'title': 'Add New Destination'})
    
def destination_delete(request,slug):
    destination = get_object_or_404(Destination, slug=slug)
    if request.method == 'POST':
        destination.delete()
        messages.success(request, 'Destination deleted successfully!')
        return redirect('destination:destination_list')
    return render(request, 'destination/destination_confirm_delete.html',{'destination': destination})