
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SpecificationFormSet, SetupForm
from .models import Setup


def add_setup(request):

    if request.method == 'GET':

        setup = Setup()
        setup_form = SetupForm()
        specifications_formset = SpecificationFormSet(instance=setup)

    elif request.method == 'POST':

        setup_form = SetupForm(request.POST)

        if setup_form.is_valid():
            setup = setup_form.save()

            specifications_formset = SpecificationFormSet(request.POST, instance=setup)

            if specifications_formset.is_valid():
                specifications_formset.save()

            return HttpResponseRedirect(reverse('home'))

    return render(request, 'add.html', {
        'setup_form': setup_form,
        'specifications_formset': specifications_formset})
