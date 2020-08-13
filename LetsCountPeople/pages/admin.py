from django.contrib import admin
from pages.models import Gym, CurrentPeople, Review, ReviewComment, ReviewRec

admin.site.register(Gym),
admin.site.register(CurrentPeople),
admin.site.register(Review),
admin.site.register(ReviewComment),
admin.site.register(ReviewRec),