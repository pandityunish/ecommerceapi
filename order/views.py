from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser, MultiPartParser
from .serializers import OrderSerializer

class CreateOrderView(View):
    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        # Parse the JSON data from the request body
        data = JSONParser().parse(request)
        
        # Create a new order object from the serialized data
        serializer = OrderSerializer(data=data, context={'request': request})
        if serializer.is_valid():
            order = serializer.save()
            
            # Return a JSON response with the serialized order data
            return JsonResponse({'success': True, 'data': serializer.data})
        else:
            # Return a JSON response with the validation errors
            return JsonResponse({'success': False, 'errors': serializer.errors})

    def get(self, request):
        # Return a JSON response with an error message
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
