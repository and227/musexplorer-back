import os
import uuid
import shutil

from django.db import models
from django.urls import reverse
# from settings.settings import (BASE_DIR, MEDIA_URL,
#                                PHOTO_TO_UPLOAD, PHOTOS_ROOT,
#                                TEMPLATE_IMG_NAME)

from .core.models import TimestampedModel, ActivityMarkModel
# from .services.path import delete_dir_with_all_files

IMG_TYPES = (('P', 'png'), ('W', 'webp'))
SIZE_TYPES = (('O', 'Origin'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'))

class Group(TimestampedModel, ActivityMarkModel):
    name = models.CharField(verbose_name="Имя группы", 
                            max_length=64, blank=False, null=False)
    group_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    label = models.CharField(verbose_name="Путь к лейблу группы", 
                            max_length=128, blank=False, null=False)
    group_info = models.CharField(verbose_name="Описание группы", 
                            max_length=512, blank=False, null=False)

    class Meta:
        verbose_name = "Group"
        verbose_name_plural = "Groups"
        db_table = 'groups'

class Album(TimestampedModel, ActivityMarkModel):
    name = models.CharField(verbose_name="Имя альбома", 
                            max_length=64, blank=False, null=False)
    album_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    album_group = models.ForeignKey(to='Group', on_delete=models.CASCADE,
                              null=True, related_name='albums',db_column='album_group')
    genre = models.CharField(verbose_name="Жанр альбома",
                            max_length=64, blank=False, null=False)                           
    cover_url = models.CharField(verbose_name="Путь к обложке альбома",
                            max_length=128, blank=False, null=False)
    # photos = models.ManyToManyField(to='Photo',
    #                                 related_name='albums')
    # categories = models.ManyToManyField(to='Category',
    #                                     related_name='albums')

    class Meta:
        verbose_name = "Album"
        verbose_name_plural = "Albums"
        db_table = 'albums'

    # def get_absolute_url(self):
    #     return reverse("Album_detail", kwargs={"pk": self.pk})

# class Category(TimestampedModel, ActivityMarkModel):
#     name = models.CharField(max_length=64)
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                             editable=False)
#     photos = models.ManyToManyField(to='Photo', related_name='categories')

#     class Meta:
#         verbose_name = "Category"
#         verbose_name_plural = "Categories"

#     def get_absolute_url(self):
#         return reverse("Category_detail", kwargs={"pk": self.pk})


class Track(TimestampedModel, ActivityMarkModel):
    name = models.CharField(verbose_name="Наименование комнозиции", max_length=64)
    track_uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4,
                            editable=False)
    album = models.ForeignKey(to='Album', on_delete=models.CASCADE,
                              null=True, related_name='tracks',db_column='album')
    youtube_link = models.CharField(verbose_name="Ссылка к youtube видео",
                            max_length=255, blank=True, null=True)       

    class Meta:
        verbose_name = "Track"
        verbose_name_plural = "Tracks"
        db_table = 'tracks'

    # def get_absolute_path(self) -> str:
    #     return os.path.join(PHOTOS_ROOT, str(self.uuid))

    def __str__(self):
        return "%s_%s" % (self.name, str(self.track_uuid)[:6])

    def __repr__(self):
        return "%s %s" % (self.name, self.track_uuid)

    # def save(self, *args, **kwargs):
    #     # path = os.path.join(PHOTO_TO_UPLOAD, str(self.uuid))
    #     super(Track, self).save(*args, **kwargs)

    # def delete(self):
    #     # print(">>>", self.get_absolute_path())
    #     # delete_dir_with_all_files(self.get_absolute_path())
    #     # IMG.objects.filter(photo=self).delete()
    #     super(Track, self).delete()
