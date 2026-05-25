import pdfplumber

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Home Page
def home(request):

    return render(request, 'index.html')


# Register Page
def register(request):

    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        user.save()

        return redirect('login')

    return render(request, 'register.html')


# Login Page
def login_page(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

    return render(request, 'login.html')


# Dashboard
def dashboard(request):

    return render(request, 'dashboard.html')


# Upload Resume + ATS Analyzer
def upload_resume(request):

    extracted_text = ""

    matched_skills = []
    missing_skills = []

    score = 0
    feedback = ""

    uploaded_resume_name = ""
    job_description_text = ""

    if request.method == 'POST':

        uploaded_file = request.FILES['resume']

        uploaded_resume_name = uploaded_file.name

        job_description_text = request.POST['job_description']

        job_description = job_description_text.lower()

        # Save uploaded file
        with open(uploaded_file.name, 'wb+') as destination:

            for chunk in uploaded_file.chunks():

                destination.write(chunk)

        # Extract text from PDF
        with pdfplumber.open(uploaded_file.name) as pdf:

            for page in pdf.pages:

                text = page.extract_text()

                if text:

                    extracted_text += text.lower()

        # Technical Skills List
        technical_skills = [

            "python",
            "django",
            "flask",
            "fastapi",

            "html",
            "css",
            "javascript",
            "react",
            "bootstrap",

            "sql",
            "mysql",
            "postgresql",
            "mongodb",

            "machine learning",
            "deep learning",
            "data science",
            "data analysis",

            "tensorflow",
            "pytorch",
            "opencv",
            "computer vision",

            "numpy",
            "pandas",
            "matplotlib",
            "seaborn",

            "git",
            "github",

            "rest api",
            "aws",
            "docker",

            "power bi",
            "excel"
        ]

        # Compare Skills
        for skill in technical_skills:

            if skill in job_description:

                if skill in extracted_text:

                    matched_skills.append(skill)

                else:

                    missing_skills.append(skill)

        # Calculate ATS Score
        total_skills = len(matched_skills) + len(missing_skills)

        if total_skills > 0:

            score = int(
                (len(matched_skills) / total_skills) * 100
            )

        # Feedback System
        if score >= 80:

            feedback = "Excellent Resume Match! Your resume is highly optimized for this job."

        elif score >= 60:

            feedback = "Good Resume Match! Add a few missing skills to improve ATS score."

        elif score >= 40:

            feedback = "Average Resume Match! Your resume needs improvement for this role."

        else:

            feedback = "Low ATS Score! Add more relevant technical skills to your resume."

    return render(request, 'upload_resume.html', {

        'score': score,

        'matched_skills': matched_skills,

        'missing_skills': missing_skills,

        'uploaded_resume_name': uploaded_resume_name,

        'job_description_text': job_description_text,

        'feedback': feedback
    })


# Logout
def logout_page(request):

    logout(request)

    return redirect('login')