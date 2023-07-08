from django.db import transaction
from ..models import AdsLocation


class AdsProcessor:
    """
    This processor is used to perform some common operations on ads
    """

    @classmethod
    def set_visits_to_zero():
        """
        It is used to set no. of visits per day to zero
        for unexpired Ads.
        """
        with transaction.atomic():
            ads = AdsLocation.objects.with_expiration_data() \
                                    .filter(date_expired=False) \
                                    .update(visits=0)