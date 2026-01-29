from pyexpat.errors import messages
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import MenuForm
from .models import Menu


class MenuCreateView(LoginRequiredMixin, CreateView):

    model= Menu
    form_class = MenuForm
    template_name = 'add_menu.html'
    success_url = reverse_lazy('menu_list')
    login_url = 'login'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Menu item added successfully!")

        return response

    def form_invalid(self, form):
        messages.error(self.request, "There was an error adding the menu item. Please try again.")
        return super().form_invalid(form)




def home(request):
    return render(request, 'home.html')

# def add_menu(request):
#     if request.method == "POST":
#         form = MenuForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('menu_list')
#     else:
#         form = MenuForm()

#     return render(request, 'add_menu.html', {'form': form})


# def menu_list(request):
#     menus = Menu.objects.all()
#     return render(request, 'menu_list.html', {'menus': menus})