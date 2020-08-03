from django.contrib import admin
from pages.models import Gym, CurrentPeople, Review, ReviewComment

admin.site.register(Gym),
admin.site.register(CurrentPeople),
admin.site.register(Review),
admin.site.register(ReviewComment),
