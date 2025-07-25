from django.shortcuts import render
from sklearn.linear_model import LinearRegression  # <-- Changed from GaussianNB
from .models import ClientRequest
import numpy as np

def index(request):
    return render(request, 'freelance_app/index.html')

def budget_prediction(request):
    if request.method == 'POST':
        # Get inputs from the form
        project_complexity = float(request.POST['project_complexity'])
        project_duration = float(request.POST['project_duration'])

        # Combine features into a 2D array
        features = np.array([[project_complexity, project_duration]])

        # Training data (should be replaced with real data)
        X_train = np.array([[1, 2], [3, 4], [5, 6], [8, 12], [10, 20]])
        y_train = np.array([100, 300, 500, 1000, 2000])

        # Use Linear Regression instead of Naive Bayes
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict budget
        predicted_budget = model.predict(features)

        # Save to DB
        client_request = ClientRequest(
            name=request.POST.get('name', 'Client Name'),
            project_complexity=project_complexity,
            project_duration=project_duration,
            predicted_budget=round(predicted_budget[0], 2)
        )
        client_request.save()

        # Return prediction result
        return render(request, 'freelance_app/result.html', {'budget': round(predicted_budget[0], 2)})

    return render(request, 'freelance_app/form.html')
