from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import mixins, generics

class CustomerList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
 
 
    def get(self, request):
        return self.list(request)
          
    
    def post(self,request):
         return self.create(request)
       
       
class CustomerDetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
     queryset = Customer.objects.all()
     serializer_class = CustomerSerializer
     
     def get(self, request, pk):
         return self.retrieve(request)
     
     def put(self, request, pk):
         return self.update(request)
     
     def delete(self, request, pk):
         return self.destroy(request)
     
       #def get_customer(self,pk):
      #try:
            #return Customer.objects.get(pk=pk)
        #except Customer.DoesNotExist:
            #raise Http404
        
     #def get(self, request, pk):
        #customer = self.get_customer(pk)
        #serializer = CustomerSerializer(customer)
        #return Response(serializer.data)
    
     #def put(self, request, pk):
        #customer = self.get_customer(pk)
        #serializer = CustomerSerializer(customer, data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
     #def delete(self, request, pk):
        #customer = self.get_customer(pk)
        #customer.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT) 
        
        
        

#@api_view(['GET','POST'])
#def customers_List(request):
    #if request.method == 'GET':
        #customers = Customer.objects.all()
        #serializer = CustomerSerializer(customers, many=True)
        #return Response(serializer.data)
    
    #if request.method == 'POST':
         
        #serializer = CustomerSerializer(data=request.data)
        #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data, status=status.HTTP_201_CREATED)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#@api_view(['GET','POST','DELETE'])   
#def customer_details(request, pk):
    #try:
        #customer = Customer.objects.get(pk=pk)
    #except Customer.DoesNotExist:
        #return Response(status=status.HTTP_404_NOT_FOUND)
    
    #if request.method == 'GET':
        #serializer = CustomerSerializer(customer)
        #return Response(serializer.data)
    #if request.method == 'PUT':
        #serializer = CustomerSerializer(customer, data=request.data)
      #if serializer.is_valid():
            #serializer.save()
            #return Response(serializer.data)
        #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #if request.method == 'DELETE':
         #customer.delete()
         #return Response(status=status.HTTP_204_NO_CONTENT)
        
