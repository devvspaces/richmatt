from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .form import FilterForm, CreateForm
from .models import Product


class Home(TemplateView):
    template_name = 'products/index.html'
    extra_context = {
        'title': 'Our gallery designs',
    }

class ProductsView(ListView):
    template_name = 'products/store.html'
    extra_context = {
        'title': 'Our Store',
    }
    model = Product
    context_object_name = 'products'
    order_by = '-created'
    paginate_by = 5
    form_class = FilterForm

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
        		min_price = form.cleaned_data.get('min_price')
        		max_price = form.cleaned_data.get('max_price')

        		if category:
        			queryset = queryset.filter(category=category)
        		if min_price:
        			queryset = queryset.filter(new_price__gte = min_price)
        		if max_price:
        			queryset = queryset.filter(new_price__lte = max_price)

        		context[self.context_object_name] = queryset
        		context['page_obj'] = ''
        		context['queryset_count'] = queryset.count
        	else:
        		print(form.errors)

        context['form'] = form

        return render(request, self.template_name, context)


class ManageProduct(LoginRequiredMixin, UserPassesTestMixin, ProductsView):
    template_name = 'products/manage_store.html'
    extra_context = {
        'title': 'Our Products',
    }
    paginate_by = 20

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class AddProduct(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    template_name = 'products/add_product.html'
    extra_context = {
        'title': 'Add Product Item',
    }
    model = Product
    context_object_name = 'form'
    form_class = CreateForm

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class UpdateProduct(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'products/add_product.html'
    extra_context = {
        'title': 'Update Product Item',
        'update_page': 'yes'
    }
    model = Product
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


class DeleteProduct(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'products/delete_product.html'
    extra_context = {
        'title': 'Delete Store Product',
    }
    model = Product
    context_object_name = 'item'
    slug_url_kwarg = 'id'
    slug_field = 'id'

    def get_success_url(self):
        messages.success(self.request, 'Product has been successfully deleted')
        return reverse('manage_product')

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False