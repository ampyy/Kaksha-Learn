from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from .models import *
from .forms import *
from django.conf import settings
from .models import Transaction
from .paytm import generate_checksum, verify_checksum
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return render(request, "home.html")


def courses(request):
    courses = Courses.objects.all()
    return render(request, "courses.html", {'courses': courses})


def cour_desc(request, pk):
    course = get_object_or_404(Courses, pk=pk)
    return render(request, "cour_desc.html", {'course': course})


def contactus(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    return render(request, "contactus.html", {'form':form})


def verification(request):
    form = BoughtForm()
    if request.method == 'POST':
        form = BoughtForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BoughtForm()
    return render(request, "verification.html", {'form': form})


def enrolled(request):
    return render(request, "enrolled.html")


def initiate_payment(request, pk):
    if request.method == "GET":
        course = get_object_or_404(Courses, pk=pk)
        return render(request, 'payments/pay.html', {'course': course})
    try:
        name = request.POST['name']
        number = int(request.POST['number'])
        amount = int(request.POST['amount'])
        course_title = request.POST['course_title']
        paid = request.POST['paid']
    except:
        return render(request, 'payments/pay.html', context={'error': 'Wrong Account Details or amount'})

    transaction = Transaction.objects.create(name=name, number=number, courses=course_title,amount=amount,  paid=paid)
    transaction.save()
    merchant_key = settings.PAYTM_SECRET_KEY

    params = (
        ('MID', settings.PAYTM_MERCHANT_ID),
        ('ORDER_ID', str(transaction.order_id)),
        ('CUST_ID', str(transaction.number)),
        ('TXN_AMOUNT', str(transaction.amount)),
        ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
        ('WEBSITE', settings.PAYTM_WEBSITE),
        # ('EMAIL', request.user.email),
        # ('MOBILE_N0', '9911223388'),
        ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
        ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
        # ('PAYMENT_MODE_ONLY', 'NO'),
    )

    paytm_params = dict(params)
    checksum = generate_checksum(paytm_params, merchant_key)

    transaction.checksum = checksum
    transaction.save()

    paytm_params['CHECKSUMHASH'] = checksum
    print('SENT: ', checksum)

    return render(request, 'payments/redirect.html', context=paytm_params)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        received_data = dict(request.POST)
        paytm_params = {}
        paytm_checksum = received_data['CHECKSUMHASH'][0]
        for key, value in received_data.items():
            if key == 'CHECKSUMHASH':
                paytm_checksum = value[0]
            else:
                paytm_params[key] = str(value[0])
        # Verify checksum
        is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
        if is_valid_checksum:
            received_data['message'] = "Checksum Matched"
            return redirect('verification')
        else:
            received_data['message'] = "Checksum Mismatched"
            return render(request, 'payments/callback.html', context=received_data)
        return HttpResponse(status=200)


def preview(request):
    preview = Preview.objects.all()
    return render(request, "preview.html", {"preview" : preview})


def howweteach(request):
    return render(request, "howweteach.html")