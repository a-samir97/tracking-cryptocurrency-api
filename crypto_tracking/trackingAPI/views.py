from rest_framework.generics import ListAPIView

from .models import Cryptocurrency
from .serializers import CryptocurrencySerializer

class CryptocurrencyListViewAPI(ListAPIView):
    queryset = Cryptocurrency.objects.all()
    serializer_class = CryptocurrencySerializer
