from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from map.models import Snippet


class StaticViewSitemap(Sitemap):
    changefreq = 'always'

    def items(self):
        return ['index', 'about', 'contact', 'support']

    def location(self, item):
        return reverse(item)


class SnippetSitmap(Sitemap):
    def items(self):
        return Snippet.objects.all()
