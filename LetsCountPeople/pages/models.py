from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class Gym(models.Model):
  name = models.CharField(max_length=40)
  address = models.CharField(max_length=100)
  latitude = models.FloatField(null=True, blank=True)
  longitude = models.FloatField(null=True, blank=True)

  def __str__(self):
    if self.latitude and self.longitude:  # 위도, 경도 값이 모두 있을 때
      return '헬스장 이름: %s, 주소: %s, 위도: %f, 경도: %f' % (self.name, self.address, self.latitude, self.longitude)
    else:  # 위도, 경도 값이 하나라도 없을 때
      return '헬스장 이름: %s, 주소: %s' % (self.name, self.address)


class CurrentPeople(models.Model):
  gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
  num_people = models.IntegerField(default=0, null=False, blank=False)
  updated_at = models.DateTimeField(auto_now=True)  # 생성 혹은 변경시 자동으로 시간 업데이트

  def __str__(self):
    # 'self.gym.name' 가능할까?? --> 가능!
    return '헬스장: %s, 현재 사람 수: %d, 최근 업데이트: %s' % (self.gym.name, self.num_people, self.updated_at)

  @receiver(post_save, sender=Gym)
  def create_gym_currentpeople(sender, instance, created, **kwargs):
    if created:
      CurrentPeople.objects.create(gym=instance)


class Review(models.Model):
  gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
  author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
  title = models.CharField(max_length=40)
  content = models.TextField()
  hits = models.IntegerField(default=0)
  rec_users = models.ManyToManyField(User, blank=True, related_name='rec_feeds', through='ReviewRec')
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(null=True)

  def __str__(self):
    return '헬스장: %s, 작성자: %s, 제목: %s, 조회수: %d, 작성: %s, 최근 수정: %s, 고유 번호: %d' % (self.gym.name, self.author, self.title, self.hits, self.created_at, self.updated_at, self.id)


class ReviewComment(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)
  content = models.CharField(max_length=40)
  created_at = models.DateTimeField(default=timezone.now)
  updated_at = models.DateTimeField(null=True)

  def __str__(self):
    return '작성자: %s, 내용: %s, id: %d' % (self.author.username, self.content, self.id)


class ReviewRec(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return '%s recommend %s' % (self.user.username, self.review.title)

