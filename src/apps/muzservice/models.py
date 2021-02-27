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

class Album(TimestampedModel, ActivityMarkModel):
    name = models.CharField(verbose_name="Имя альбома", 
                            max_length=64, blank=False, null=False)
    album_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            editable=False)
    album_group = models.CharField(verbose_name="Группа, создавшая альбом",
                            max_length=64, blank=False, null=False)
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


# class IMG(models.Model):
#     photo = models.ForeignKey(to='Photo', on_delete=models.CASCADE,
#                               null=True, related_name='images')
#     img_type = models.CharField(max_length=1, choices=IMG_TYPES,
#                                 default='W')
#     size = models.CharField(max_length=1, choices=SIZE_TYPES,
#                             default='M')
#     uuid = models.UUIDField(primary_key=True, default=uuid.uuid4,
#                             editable=False)

#     def get_absolute_path(self) -> str:
#         return os.path.join(self.photo.get_absolute_path(), self.get_name_file())

#     def get_url(self) -> str:
#         dir_name_path = os.path.join(MEDIA_URL, PHOTO_TO_UPLOAD)
#         dir_name_path = os.path.join(dir_name_path, str(self.photo.uuid))
#         return "%s/%s" % (dir_name_path, self.get_name_file())

#     def get_name_file(self) -> str:
#         return TEMPLATE_IMG_NAME.format(photo_uuid=str(self.photo.uuid),
#                                         size=self.get_size_display().lower(),
#                                         type=self.get_img_type_display().lower())

#     class Meta:
#         verbose_name = "IMG"
#         verbose_name_plural = "IMGs"

#     def __str__(self):
#         return "Photo(%s) %s - %s" % (self.photo, self.get_size_display(), self.get_img_type_display())

#     def __repr__(self):
#         return "%s %s %s" % (self.get_img_type_display(),
#                              self.get_size_display(),
#                              self.uuid)

#     def get_absolute_url(self):
#         return reverse("IMG_detail", kwargs={"pk": self.pk})


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
