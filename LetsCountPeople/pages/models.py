from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Gym(models.Model):
    name = models.CharField(max_length = 40)
    address = models.CharField(max_length = 100)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)

    def __str__(self):
        if self.latitude and self.longitude: # 위도, 경도 값이 모두 있을 때
            return 'name: %s, address: %s, latitude: %f, longitude: %f' % (self.name, self.address, self.latitude, self.longitude)
        else: # 위도, 경도 값이 하나라도 없을 때
            return 'name: %s, address: %s' % (self.name, self.address)


class CurrentPeople(models.Model):
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE)
    num_people = models.IntegerField(default = 0, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now = True) # 생성 혹은 변경시 자동으로 시간 업데이트
    
    def __str__(self):
        return 'gym: %s, num_people: %d, last_update: %s' % (self.gym.name, self.num_people, self.updated_at) # 'self.gym.name' 가능할까??

    @receiver(post_save, sender=Gym)
    def create_gym_currentpeople(sender, instance, created, **kwargs):
        if created:
            CurrentPeople.objects.create(gym=instance)

    @receiver(post_save, sender=Gym)
    def save_gym_currentpeople(sender, instance, **kwargs):
        instance.currentpeople.save()

