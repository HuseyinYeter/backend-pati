
from rest_framework import mixins,generics
from rest_framework.response import Response

from .serializer import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import authentication_classes, permission_classes, api_view


# Create your views here.

class ReportListView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.CreateModelMixin,):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = ReportSerializer
    queryset = Report.objects.all()


    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)

class ReportDetailView(generics.GenericAPIView,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.RetrieveModelMixin):


    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    serializer_class = ReportSerializer
    queryset = Report.objects.all()
    lookup_field = "id"

    def get(self,request,id):
        if id:
            return self.retrieve(request,id)
        return self.list(request)
    def put(self,request,id):
        return self.update(request,id)

    def delete(self,request,id):
        return self.destroy(request,id)

@api_view(["GET","POST"])
def login(request):
    data = request.data
    auth = authenticate(username=data["username"],password = data["password"])

    if auth:
        token = Token.objects.filter(user=auth).first()

        if not token:
            token = Token.objects.create(user=auth)


        return Response({"success":True,"token":token.key})

    return Response({"success":False,"message":"Username or Password is incorrect!"},status=401)

@api_view(["DELETE"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    Token.objects.filter(user=request.user).delete()
    return Response(True)
