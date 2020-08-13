from django.contrib import admin
from pages.models import Gym, CurrentPeople, Review, ReviewComment
from pages.models import ReviewRec, CommentRec

admin.site.register(Gym),
admin.site.register(CurrentPeople),
admin.site.register(Review),
admin.site.register(ReviewComment),
admin.site.register(ReviewRec),
admin.site.register(CommentRec),