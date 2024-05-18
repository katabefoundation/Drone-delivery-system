from django.shortcuts import render

# Create your views here.
from rest_framework import generics,viewsets, permissions
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Drone
from .serializers import UserSerializer,LoginSerializer,DroneSerializer
from django.contrib.auth import authenticate, login
from django.contrib.sessions.models import Session
from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse,HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response


class AuthCheck(APIView):
    permission_classes = []

    def  get(self, request):
        user = UserSerializer(request.user, context={'request':request})
        if request.user.is_authenticated:
            
            # user = UserSerializer(request.user, context={'request':request})
            return Response({'isAuthenticated':True,"user":user.data})
        
        else:
            return Response({'isAuthenticated':False})


class LoginView(APIView):
    authentication_classes = []
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data
            login(request, user)
            permissions.IsAuthenticated.has_permission(self,request,all)
            return Response({"message": "Login successful.",'user_id':user.id}, status=200)

        return JsonResponse(serializer.errors, status=400)

class logoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,req):
        req.user.auth_token.delete()
        return Response({'message':'Logged out'}, status=200)
        

def expire_session_view(request, session_key):
   
    try:
        session = Session.objects.get(session_key = session_key)
        session.delete()
    except Session.DoesNotExist:
        pass
    return HttpResponseRedirect('/admin/sessions/session')


class User_view(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user =  request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
   


#     def login(self, request):
#         serializer = UserLoginSerializer(data = request.data)

#         if serializer.is_valid:
#             email = serilaizer.validated_data['email']
#             password = serilaizer.validated_data['password']
#             user = authenticate(request, email = email, password = pasword )

#             if user:
#                 login(request, user)
#                 return JsonResponse({'message':'loggin successfuly'}, status = 200)
#             else:
#                 return JsonResponse({'message':'Invalid Credentials'}, status=401)
#         return JsonResponse(serializer.error,status=400)

#     def logout(self,request):
#         logout(request)
#         return JsonResponse({'message': 'Logged out'}, status=201) 
    
    

# @csrf_exempt
# @api_view(['POST'])
# def signup(request):
#     if request.method == 'POST':
#         serializer = UserSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status = 201)
#     return JsonResponse(serializer.error,status = 400)
#     # if request.method == 'POST':
#     #     data = json.loads(request.body)
#     #     first_name = data.get('first_name')
#     #     last_name = data.get('last_name')
#     #     username = data.get('username')
#     #     email = data.get('email')
#     #     password = data.get('password').strip()  # Trim whitespace from password

#     #     if not (first_name and last_name and username and email and password):
#     #         return JsonResponse({'error': 'All fields are required'}, status=400)

#     #     try:
#     #         hashed_password = make_password(force_bytes(password))  # Ensure UTF-8 encoding
#     #         user = User.objects.create_user(
#     #             first_name=first_name,
#     #             last_name=last_name,
#     #             username=username,
#     #             email=email,
#     #             password=hashed_password
#     #         )
#     #         user.save()  # Save user data to the 'drone_db' database

#     #         return JsonResponse({'message': 'User created successfully'})

#     #     except IntegrityError:
#     #         return JsonResponse({'error': 'Username or email already exists'}, status=400)

# @csrf_exempt
# def update_user(request, user_id):
#     if request.method == 'PUT':
#         data = json.loads(request.body)
#         try:
#             user = CustomUser.objects.using('drone_db').get(id=user_id)
#             user.first_name = data.get('first_name', user.first_name)
#             user.last_name = data.get('last_name', user.last_name)
#             user.email = data.get('email', user.email)
#             user.save(using='drone_db')
#             return JsonResponse({'message': 'User updated successfully'})
#         except ObjectDoesNotExist:
#             return JsonResponse({'error': 'User not found'}, status=404)

# @csrf_exempt
# def delete_user(request, user_id):
#     if request.method == 'DELETE':
#         try:
#             user = CustomUser.objects.using('drone_db').get(id=user_id)
#             user.delete()
#             return JsonResponse({'message': 'User deleted successfully'})
#         except ObjectDoesNotExist:
#             return JsonResponse({'error': 'User not found'}, status=404)


# @csrf_exempt
# # @api_view(['POST'])
# def login_view(request):
#     if request.method == 'POST':
#         username = request.data.get('username')
#         password = request.data.get('password')

#         user = None
#         if '@' in username:
#             try:
#                 user = User.objects.get(email = username)
#             except ObjectDoesNotExist:
#                 pass 
#         if not user:
#             user = authenticate(username = username, password = password)
        
#             if user:
#                 token,_ = Token.objects.get_or_create(user = user)

#                 return JsonResponse({'token':token_key}, status = 200)
#         return JsonResponse({'error': 'Invalid credentials'})
#     return JsonResponse({'error':'Method not allowed'},status=403)

    # if request.method == 'POST':
    #     data = json.loads(request.body)
    #     email = data.get('email').strip()  # Trim whitespace from email
    #     password = data.get('password').strip()  # Trim whitespace from password
      
    #     try:
    #         user = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         return JsonResponse({'error': 'User does not exist'}, status=401)

    #     # Ensure password is in bytes format for check_password
    #     # password_bytes = force_bytes(password)
    #     hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    #     if check_password(hashed_password, user.password):
    #         user = authenticate(request, email=email, password = hashed_password)
    #         if user is not None:
    #             login(request, user)
    #             role = 'admin' if user.is_staff else 'normal'
    #             return JsonResponse({'message': 'Login Successfully', 'role': role})
    #         else:
    #             return JsonResponse({'error': 'Invalid Email or Password'}, status=401)
    #     else:
    #         return JsonResponse({'error': 'Invalid Email or Password'+ str(hashed_password)}, status=401)

    # return JsonResponse({'error': 'Method not Allowed'}, status=405)      
# @csrf_exempt
# # @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def user_logout(request):
#     if request.method == 'POST':
#         try:
#             # deleting user's tokens to logout
#             request.user.auth_token.delete()
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status = 500)

# class DroneListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Drone.objects.all()
#     serializer_class = DroneSerializer

# class DroneRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Drone.objects.all()
#     serializer_class = DroneSerializer

@api_view(['POST'])
@permission_classes([IsAdminUser])
def add_drone(request):
    serializer = DroneSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=200)
    return Response(serializer.errors, status =400)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def control_drone(request, drone_id):
    drone = Drone.objects.get(pk=drone_id)
    serializer = DroneSerializer(drone,data=request.data,partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 200)
    return Response(serializer.errors, status = 400)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_user(request):
    serializer = UserSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 200)
    return Response(serializer.errors, status = 400)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def set_permission(request, user_id):
    user = UserSerializer.objects.get(pk=user_id)
    serializer = UserSerializer(data = request.data, partial = True)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = 200)
    return Response(serializer.errors, status = 400)
