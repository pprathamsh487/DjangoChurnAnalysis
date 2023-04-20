from django.shortcuts import render
from django.http import HttpResponse
from joblib import load
# Create your views here.
from pathlib import Path
THIS_FOLDER = Path(__file__).parent.resolve()
my_file = THIS_FOLDER / "savedModels/model.joblib"
model = load(my_file)

def getDetails(request):
    if request.method == "POST":
        predictor = [int(request.POST['creditScore']), 
                    int(request.POST['Age']),

                    
                    int(request.POST['Tenure']),
                    int(request.POST['Balance']),
                    int(request.POST['NumOfProducts']),
                    int(request.POST['HasCrCard']),
                    int(request.POST['IsActiveMember']),
                    int(request.POST['EstimatedSalary']),
                    int(request.POST['GeographyGermany']),
                    int(request.POST['GeographySpain']),
                    int(request.POST['GenderMale'])]
        print("Predictor : ", predictor)
        y_pred = model.predict([predictor])
        print("y_pred value",y_pred)
        if y_pred < 0.5:
            y_pred = "Customer will leave"
        else :
            y_pred = "Customer will stay"

        print("result :",y_pred)
        return render(request, "index.html", {'result':y_pred})
    return render(request, "index.html")
    
