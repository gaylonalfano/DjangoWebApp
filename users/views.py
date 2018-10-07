from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm  -- Can remove after replacing with UserRegisterForm
from django.contrib import messages
# After creating a new form with a new email field, import the form:
# After creating the UserUpdateForm and ProfileUpdateForm, import:
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
# To restrict users from viewing profile page without being logged in
from django.contrib.auth.decorators import login_required

# Let's create a register view to handle the logic for the register route
def register(request):
    # Create a form that is going to be passed to the template that we will create from this view
    # with {'form': form} we're simply creating a blank form and rendering it out to the template
    # There are different types of http requests (get, post, etc.)
    # Adding conditional to handle POST or GET requests
    if request.method == "POST":  # was the request a POST request?
        #form = UserCreationForm(request.POST)  # create a new form that has the data that's within request.POST
        form = UserRegisterForm(request.POST)  # replaced w/ new form
        if form.is_valid():  # is it valid? UserCreationForm does all this
            form.save()  # saves the user data 
            username = form.cleaned_data.get('username')
            #messages.success(request, f"Account created for {username}!")  # before login page was created
            messages.success(request, f"Your account has been created! You are now able to log in.")  # after login page created
            # Now redirect user to home page after success
            #return redirect("blog-home")  # name of urlpattern for blog home page
            return redirect('login')  # after login page created
    else:
        #form = UserCreationForm()  # creates a new instance of the form
        form = UserRegisterForm()  # replaced w/ new form
    return render(request, 'users/register.html', {'form': form})  


# Let's create a user profile view that references the user profile template
# Later, after we created the UserUpdateForma and ProfileUpdateForm, let's create
# instances of these:
@login_required
def profile(request):
    u_form = UserUpdateForm()  # instantiate as empty for now
    p_form = ProfileUpdateForm()
    # Let's pass these forms to our profile template by creating context dict
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    # Now, let's pass this context into our template so we can access these forms
    return render(request, 'users/profile.html', context)