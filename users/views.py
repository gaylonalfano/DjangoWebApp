from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Let's create a register view to handle the logic for the register route
def register(request):
    # Create a form that is going to be passed to the template that we will create from this view
    # with {'form': form} we're simply creating a blank form and rendering it out to the template
    # There are different types of http requests (get, post, etc.)
    # Adding conditional to handle POST or GET requests
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}!")
            # Now redirect user to home page after success
            return redirect("blog-home")  # name of urlpattern for blog home page
    else:
        form = UserCreationForm()
    form = UserCreationForm()  # creates a new instance of the form
    return render(request, 'users/register.html', {'form': form})