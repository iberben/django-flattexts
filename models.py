from django.core.cache import cache
from django.db import models
from django.db.models.query import QuerySet

class FlatTextManager(models.Manager):
    def get_query_set(self):
        return FlatTextQuerySet(self.model)

    def empty_cache(self, id, slug):
        'Invalidate the cache for given id & slug'
        cache.set('flattext__%s' % slug, None, 5)
        cache.set('flattext__id__%s' % id, None, 5)

class FlatTextQuerySet(QuerySet):
    def get(self, *args, **kwargs):
        """
        Checks the cache to see if there's a cached entry for this pk. If not,
fetches using super then stores the result in cache.
        """
        key = ''
        if len(kwargs) == 1:
            k = kwargs.keys()[0]
            if k in ('slug', 'slug__exact'):
                key = 'flattext__%s' % kwargs.values()[0]
            elif k in ('pk', 'pk__exact', 'id', 'id__exact'):
                key = 'flattext__id__%s' % kwargs.values()[0]

            obj = cache.get(key)

        if obj is None:
            try:
                obj = super(FlatTextQuerySet, self).get(*args, **kwargs)
            finally:
                if obj is None:
                    # if it doesn't exists, create an empty object
                    obj = FlatText()
                if key:
                    cache.set(key, obj, 0)
        return obj


class FlatText(models.Model):
    slug = models.SlugField()
    content = models.TextField()

    objects = FlatTextManager()

    def __unicode__(self):
        """A string representation of a FlatText"""
        return self.slug

    def save(self, *args, **kwargs):
        super(FlatText, self).save(*args, **kwargs)
        self.objects.empty_cache(self.id, self.slug)

    def delete(self):
        slug = self.slug
        id = self.id
        super(FlatText, self).delete()
        self.objects.empty_cache(id, slug)
