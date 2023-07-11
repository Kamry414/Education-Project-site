from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer


@csrf_exempt
def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        name = request.POST.get('name')

        if not email or not password or not name:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        try:
            user = CustomUser.objects.create_user(username=email, password=password, name=name)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)

        return JsonResponse({'id': user.id, 'email': user.email, 'name': user.name}, status=201)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def sign_in(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')

        if not username or not password:
            return JsonResponse({'error': 'Missing required fields'}, status=400)

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return JsonResponse({'id': user.id, 'username': user.email, 'name': user.name}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


@csrf_exempt
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'message': 'Successfully signed out'}, status=200)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)



class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ChangePasswordView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    partial_update = True


class UpdateAvatarView(generics.UpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    partial_update = True
    lookup_field = 'id'
