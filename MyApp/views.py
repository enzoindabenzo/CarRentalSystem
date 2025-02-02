from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Driver, Car, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def login_view(request):
    if request.method == 'POST':
        # Get username and password from the form
        username = request.POST.get('loginusername')
        password = request.POST.get('loginpassword')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Log the user in
            login(request, user)
            messages.success(request, "You have been successfully logged in!")

            try:
                # Check if the user has a related Driver profile
                driver = Driver.objects.get(user=user)
                print(f"Driver profile found for {driver.name}")  # Debug statement
                return redirect('driver_dashboard')  # Redirect to the Driver dashboard
            except Driver.DoesNotExist:
                print("No driver profile found for this user")  # Debug statement
                return redirect('home')  # Non-driver users can go to the homepage
        else:
            # Invalid credentials
            messages.error(request, "Invalid username or password.")
            return redirect('user_login')  # Use the correct login page path
    else:
        # Render the login template for GET requests
        return render(request, 'user_login.html')


@login_required
def driver_dashboard(request):
    try:
        driver = Driver.objects.get(user=request.user)
        tasks = driver.task_set.all()  # Fetch tasks related to the driver

        # Calculate earnings dynamically (example: $50 per completed task)
        earnings = sum(2000 for task in tasks if task.status == 'Completed')

        return render(request, 'driver_dashboard.html', {
            'driver': driver,  # Pass driver to template
            'tasks': tasks,
            'earnings': earnings
        })
    except Driver.DoesNotExist:
        # If no driver profile exists for the user, show an error page
        messages.error(request, 'Driver profile not found.')
        return redirect('home')  # Redirect back to home if no driver found


def calculate_earnings(driver):
    # Calculate earnings based on tasks or completed orders
    completed_tasks = Task.objects.filter(driver=driver, status='Completed')
    return len(completed_tasks) * 2000  # Example: Assume each completed task earns $50


@login_required
def update_task_status(request, task_id):
    task = get_object_or_404(Task, id=task_id)

    if task.driver.user == request.user:
        task.status = 'Completed'
        task.save()
        messages.success(request, "Task marked as completed.")
    else:
        messages.error(request, "You are not authorized to update this task.")

    return render(request, 'driver_dashboard.html')


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html ')


def register(request):
    if request.method == "POST":
        name = request.POST['name']
        username = request.POST['username']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if User.objects.filter(username=username).first():
            messages.error(request, "Username already taken")
            return redirect('register')
        if User.objects.filter(email=email).first():
            messages.error(request, "Email already taken")
            return redirect('register')

        if password != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Create user
        myuser = User.objects.create_user(username=username, email=email, password=password)
        myuser.first_name = name
        myuser.save()

        # Create driver profile for this user
        driver = Driver(user=myuser, name=name, phone=number, status="Active", availability=True)
        driver.save()

        messages.success(request, "Your account has been successfully created!")
        return redirect('signin')

    return render(request, 'register.html')


def signin(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or dashboard depending on the user
        else:
            messages.error(request, "Invalid credentials")
            return redirect('signin')

    return render(request, 'user_login.html')  # Change template if necessary


def signout(request):
    logout(request)
    # messages.success(request,"Successfully logged out!")
    return redirect('home')


# return HttpResponse('signout')

def vehicles(request):
    cars = Car.objects.all()
    # print(cars)
    params = {'car': cars}
    return render(request, 'vehicles.html ', params)


def bill(request):
    cars = Car.objects.all()
    params = {'cars': cars}
    return render(request, 'bill.html', params)


def order(request):
    if request.method == "POST":
        billname = request.POST.get('billname', '')
        billemail = request.POST.get('billemail', '')
        billphone = request.POST.get('billphone', '')
        billaddress = request.POST.get('billaddress', '')
        billcity = request.POST.get('billcity', '')
        cars13 = request.POST['cars13']
        dayss = request.POST.get('dayss', '')
        date = request.POST.get('date', '')
        fl = request.POST.get('fl', '')
        tl = request.POST.get('tl', '')
        # print(request.POST['cars11'])

        orders = Order(name=billname, email=billemail, phone=billphone, address=billaddress, city=billcity, cars=cars11,
                       days_for_rent=dayss, date=date, loc_from=fl, loc_to=tl)
        orders.save()
        return redirect('home')
    else:
        print("error")
        return render(request, 'bill.html')


def contact(request):
    if request.method == "POST":
        contactname = request.POST.get('contactname', '')
        contactemail = request.POST.get('contactemail', '')
        contactnumber = request.POST.get('contactnumber', '')
        contactmsg = request.POST.get('contactmsg', '')

        contact = Contact(name=contactname, email=contactemail, phone_number=contactnumber, message=contactmsg)
        contact.save()
    return render(request, 'contact.html ')
