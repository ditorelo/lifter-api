from rest_framework import viewsets

from api.models import Lift
from api.serializers import LiftSerializer


class LiftViewSet(viewsets.ModelViewSet):
    """
    # ViewSet from lifters
    """

    def get_queryset(self):
        return Lift.objects.filter(athlete=self.kwargs["athlete_pk"])

    def get_serializer_class(self):
        return LiftSerializer
