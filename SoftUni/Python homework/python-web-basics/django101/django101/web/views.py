from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views

from django101.web.models import Todo, Category


def permissions_required(required_permissions):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            user = request.user
            if not user.is_authenticated or \
                    not user.has_perms(required_permissions):
                return HttpResponse('No permission')
            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator


# @login_required(login_url='/login-with-fb')
# @login_required
@permissions_required(required_permissions=['web.change_category'])
def index(request):
    if not request.user.is_authenticated:
        redirect('login')

    print(request.user)

    user = authenticate(
        request,
        username='aleksiev',
        password='12345qwe'
    )
    if user.has_perm('web.change_category'):
        cat = Category.objects.get(pk=4)
        cat.name = 'New Name'
        cat.save()

    if user:
        login(request, user)

    context = {
        'title': 'Function-base view',
    }

    return render(request, 'index.html', context)


class IndexView(LoginRequiredMixin, views.View):

    def get(self, request):
        context = {
            'title': 'Class-based view',
        }

        return render(request, 'index.html', context)

    # def post(self, request):
    #     pass
    #
    # def put(self, request):
    #     pass

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return {
            'title': 'Class based with TemplateView',
        }


class TodosListView(views.ListView):
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name',)
    context_object_name = 'todos'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     return context

    def get_queryset(self):
        queryset = super().get_queryset()

        title_filter = self.request.GET.get('filter', None)

        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)
        #  queryset.prefetch_related('category')

        return queryset


class TodosDetailsView(views.DetailView):
    model = Todo
    template_name = 'todos-details.html'
    context_object_name = 'todo'


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')
    fields = '__all__'

# class RedirectToIndexView(views.RedirectView):
#     url = reverse_lazy('index class-based')
#
#     def get_redirect_url(self, *args, **kwargs):
#         if ....:
#             return 'place 1'
#         else:
#             return 'place 2'


# class PetDetails(views.View):
#     model = Pet
#     template_name = 'pet-details.html'