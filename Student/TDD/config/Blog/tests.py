from django.test import SimpleTestCase, TestCase 

from .models import Article


class BlogAppTest(SimpleTestCase)
    
    def test_django(self):
        self.assertTrue(True)

class BlogDataTest(SimpleTestCase)
    
    def test_blog(self):
        self.assertEqual(len(Blog.objects.all()), 0)
        Article.objects.create(title='Title 1')
        Article.objects.create(title='Title 2')
        self.assertEqual(len(Blog.objects.all()), 1)

         a = Article.objects.get(pk=2)
        self.assertEqual(a.title,'Title 2')

        a.title = "New Title"
        a.save()
        self.assertEqual(a.title,'New Title 2')


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title 
    def get_absolute_url(self):
        return reverse_lazy("article_list")
    
class ArticleViewsTest(TestCase):
    def test_article_list_view(self):
        self.assertEqual(reverse("article_list"), "/article/")

    def test_article_add_view(self):
        a = dict(title='T 1', body='None')
        b = dict(title='T 2', body='None')
        response = self.client.post(reverse("article_add"), a)
        response = self.client.post(reverse("article_add"), b)
        self.assertEqual(len(Article.objects.all()), 2)
    