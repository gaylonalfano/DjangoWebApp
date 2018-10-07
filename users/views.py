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
    # Adding logic if the request.method is a POST route
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)  # Fill in form fields with current user info
        # Model forms just need an instance of that specific model object (Profile needs user.profile)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # Checking whether submitted data is valid:
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"Your account has been updated!")
            # You want to add a redirect instead of letting it drop to render() due to POST, GET, REDIRECT PATTERN
            return redirect('profile')  # Causes browser to send another GET request so we don't get weird message
       
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

     # Let's pass these forms to our profile template by creating context dict
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    # Now, let's pass this context into our template so we can access these forms
    return render(request, 'users/profile.html', context)