                                                                                                                                                                                                                                                                                                                                                                                    
# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login, authenticate, logout

User = get_user_model()

def login_view(request):
    if request.method == "POST":
        identifiant = request.POST.get('identifiant')
        password = request.POST.get('password1')

        # Authentifiez l'utilisateur
        user = authenticate(request, username=identifiant, password=password)

        # Vérifiez si l'authentification a réussi
        if user is not None:
            # Connectez l'utilisateur
            login(request, user)
            return redirect('home')  # Redirigez l'utilisateur vers la page d'accueil après la connexion
        else:
            error_message = "Identifiant ou mot de passe incorrect."
            return render(request, 'accounts/login.html', {'error_message': error_message})

    return render(request, "accounts/login.html")

def signup(request):
    if request.method == "POST":
        identifiant = request.POST.get('identifiant')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Vérifiez si l'identifiant est vide
        if not identifiant:
            error_message = "L'identifiant ne peut pas être vide."
            return render(request, 'accounts/signup.html', {'error_message': error_message})

        # Vérifiez si les mots de passe correspondent
        if password1 != password2:
            error_message = "Les mots de passe ne correspondent pas."
            return render(request, 'accounts/signup.html', {'error_message': error_message})
        
        # Vérifiez si un utilisateur avec le même identifiant existe déjà
        if User.objects.filter(username=identifiant).exists():
            error_message = "Cet identifiant est déjà utilisé. Veuillez en choisir un autre."
            return render(request, 'accounts/signup.html', {'error_message': error_message})

        # Créez l'utilisateur
        user = User.objects.create_user(identifiant, password=password1)

        # Connectez automatiquement l'utilisateur après l'inscription
        login(request, user)

        # Redirigez l'utilisateur vers la page d'accueil
        return redirect('index')

    return render(request, "accounts/signup.html")

def logout_user(request):
    logout(request)
    return redirect('home')