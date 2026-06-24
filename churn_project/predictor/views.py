from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST

# Create your views here.


def preprocess(data):

    model_columns = [
        "senior_citizen",
        "partner",
        "dependents",
        "tenure",
        "phone_service",
        "paperless_billing",
        "monthly_charges",
        "total_charges",
        "contract_Month-to-month",
        "contract_One year",
        "contract_Two year",
        "gender_male",
        "payment_method_Credit card (automatic)",
        "payment_method_Electronic check",
        "payment_method_Mailed check",
        "multiple_lines_No phone service",
        "multiple_lines_Yes",
        "internet_service_Fiber optic",
        "internet_service_No",
        "online_security_No internet service",
        "online_security_Yes",
        "online_backup_No internet service",
        "online_backup_Yes",
        "device_protection_No internet service",
        "device_protection_Yes",
        "tech_support_No internet service",
        "tech_support_Yes",
        "streaming_t_v_No internet service",
        "streaming_t_v_Yes",
        "streaming_movies_No internet service",
        "streaming_movies_Yes",
    ]

    processed_data = {}

    for col in model_columns:
        processed_data[col]=0

    # Numeric features

    processed_data["tenure"] = int(data["tenure"])
    processed_data["monthly_charges"] = float(data["monthly_charges"])
    processed_data["total_charges"] = float(data["total_charges"])

    # binary features/columns

    binary_map = {"yes": 1, "no": 0}

    processed_data["phone_service"] = binary_map[data["phone_service"]]
    processed_data["dependents"] = binary_map[data["dependents"]]
    processed_data["partner"] = binary_map[data["partner"]]
    processed_data["senior_citizen"] = binary_map[data["senior_citizen"]]
    processed_data["paperless_billing"] = binary_map[data["paperless_billing"]]

    # Frontend columns that need One-Hot Encoding
    one_hot_features = [
            "multiple_lines",
            "internet_service",
            "online_security",
            "online_backup",
            "device_protection",
            "tech_support",
            "streaming_t_v",
            "streaming_movies",
            "contract",
            "payment_method",
            "gender"
        ]

    for col in one_hot_features:
        value = data[col]

        if value == "yes":
            value = "Yes"

        encoded = col + "_" + value

        if encoded in processed_data:
            processed_data[encoded] = 1
            
    import pandas as pd
    df = pd.DataFrame([processed_data])
    return df

def dashboard(request):
    
    return render(request,"dashboard.html")

@require_POST
def predict(request):

    # first collect the processed data
    form_data=request.POST
    processed_data=preprocess(form_data)
    
    #import ml model
    import joblib
    import os
    from django.conf import settings
    model_path = os.path.join(settings.BASE_DIR, "..", "model", "churn_model.pkl")
    model = joblib.load(model_path)
    #make prediction
    prediction=model.predict(processed_data)[0]
    return render(request,"result.html",{
        "prediction":prediction
    })
    
