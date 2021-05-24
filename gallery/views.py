from datetime import datetime
from random import sample

from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, FormView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Gallery
from .forms import FilterForm, CreateForm


class GalleryView(ListView):
    template_name = 'products/gallery.html'
    extra_context = {
        'title': 'Our gallery designs',
    }
    model = Gallery
    context_object_name = 'gallery'
    order_by = '-created'

    @property
    def object_list(self, *args, **kwargs):
        return self.get_queryset().order_by(self.order_by)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        # Send the categories we have
        context['categories'] = [{'name': i[1], 'tag': i[0]} for i in Gallery.CATEGORY]

        return render(request, self.template_name, context)

class ManageGallery(LoginRequiredMixin, UserPassesTestMixin, ListView):
    template_name = 'products/manage_gallery.html'
    extra_context = {
        'title': 'Our gallery designs',
    }
    model = Gallery
    context_object_name = 'gallery'
    order_by = '-created'
    paginate_by = 20
    form_class = FilterForm

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    @property
    def object_list(self, *args, **kwargs):
        return self.get_queryset().order_by(self.order_by)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        form = self.form_class()
        queryset = self.object_list
        context['queryset_count'] = queryset.count

        filter_btn = request.GET.get('submit')
        if filter_btn == 'filter':
            # Needs filtering
            form = self.form_class(request.GET)

            if form.is_valid():
                category = form.cleaned_data.get('category')

                if category:
                    queryset = queryset.filter(category=category)

                context[self.context_object_name] = queryset
                context['page_obj'] = ''
                context['queryset_count'] = queryset.count
            else:
                print(form.errors)

        context['form'] = form

        return render(request, self.template_name, context)


class AddGallery(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'products/add_gallery.html'
    extra_context = {
        'title': 'Add Gallery Item',
    }
    model = Gallery
    context_object_name = 'form'
    form_class = CreateForm

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class UpdateGallery(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'products/add_gallery.html'
    extra_context = {
        'title': 'Update Gallery Item',
        'update_page': 'yes'
    }
    model = Gallery
    context_object_name = 'form'
    form_class = CreateForm
    slug_url_kwarg = 'id'
    slug_field = 'id'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

    @property
    def object(self, *args, **kwargs):
        return get_object_or_404(self.model, id=self.kwargs.get(self.slug_field))

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()

        context['obj'] = self.object

        return render(request, self.template_name, context)

class DeleteGallery(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'products/delete_gallery.html'
    extra_context = {
        'title': 'Delete Gallery Image',
    }
    model = Gallery
    context_object_name = 'item'
    slug_url_kwarg = 'id'
    slug_field = 'id'

    def get_success_url(self):
        messages.success(self.request, 'Image has been successfully deleted')
        return reverse('manage_gallery')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False