from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

# Create your views here.


def preprocess(data):
    binary_map = {"yes": 1, "no": 0}
    phone_service = binary_map[data["phone_service"]]
    gender = binary_map[data["gender"]]
    partner = binary_map[data["partner"]]
    senior_citizen = binary_map[data["senior_citizen"]]
    paperless_billing = binary_map[data["paperless_billing"]]

    return phone_service, gender, partner, senior_citizen, paperless_billing

def dashboard(request):
    
    return render(request,"dashboard.html")

@require_POST
def collect_data(request):
    form_data=request.POST
    print(form_data)
    return HttpResponse("Data received")


@require_POST
def predict():
    pass

# 'senior_citizen',
# 'partner',
# 'dependents',
# 'tenure',
# 'phone_service',
# 'paperless_billing',
# 'monthly_charges',
# 'total_charges',
# 'contract_Month-to-month',
# 'contract_One year',
# 'contract_Two year',
# 'gender_Male',
# 'payment_method_Credit card (automatic)',
# 'payment_method_Electronic check',
# 'payment_method_Mailed check',
# 'multiple_lines_No phone service',
# 'multiple_lines_Yes',
# 'internet_service_Fiber optic',
# 'internet_service_No',
# 'online_security_No internet service',
# 'online_security_Yes',
# 'online_backup_No internet service',
# 'online_backup_Yes',
# 'device_protection_No internet service',
# 'device_protection_Yes',
# 'tech_support_No internet service',
# 'tech_support_Yes',
# 'streaming_t_v_No internet service',
# 'streaming_t_v_Yes',
# 'streaming_movies_No internet service',
# 'streaming_movies_Yes'
