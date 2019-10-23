from django.test import TestCase
from django.utils import timezone

from .models import Blog, Entry, Author, Comment

# Create your tests here.

class BlogTests(TestCase):
    def test_all_tests(self):
        # delete all the data from all the models
        Comment.objects.all().delete()
        Entry.objects.all().delete()
        Author.objects.all().delete()
        Blog.objects.all().delete()
        # populate with some data
        now = timezone.now()
        b = Blog(name = "Lissun ruokablogi", tagline="Parasta ruokaa 2018")
        b.save()
        author_lissu = Author(name="Lissu Sörsseli",email="lissu@kokki.com")
        author_lissu.save()
        author_jaana = Author(name="Jaana Jämäpuoli",email="jaana@kyokki.com")
        author_jaana.save()
        author_kalle = Author(name="Kalle Kädetön", email="enosaa@muutakaan.com")
        author_kalle.save()
        entry_kakku = Entry(blog=b, headline="Maailman helpoin kakku",
        body_text="tarvitset vain jauhoa, sokeria ja munaa")
        entry_kakku.save() # must save before you can ManyToManyFields
        entry_kakku.authors.add(author_lissu) # ManyToManyFields are added
        entry_kakku.authors.add(author_jaana)
        comment = Comment(entry=entry_kakku, text="Todella hyvä")
        comment.save()
        comment = Comment(entry=entry_kakku, text="Ihan paras")
        comment.save()
        entry_pulla = Entry(blog=b, headline="Nopeat pullat", 
        body_text="Pistä kaupan valmiit jäiset pullaan uuniin ja +200 C, 10 min")
        entry_pulla.save()
        entry_pulla.authors.add(author_lissu)
        comment = Comment(entry=entry_pulla, text="Supernopea!")
        comment.save()
        b2 = Blog(name="Kallen sotkut", tagline="Äijien safkaa")
        b2.save()
        entry_pizza = Entry(blog=b2, headline="Äijäpizza",
        body_text="ÄLÄ säästele missään raaka-aineissa")
        entry_pizza.save()
        entry_pizza.authors.add(author_kalle)
        comment = Comment(entry=entry_pizza, text="ei tätä pysty syömään")
        comment.save()
        comment = Comment(entry=entry_pizza, text="Kerrankin kunnon mättöä!")
        comment.save()
        # let's do some queries
        # I know these should be asserts, but I am too lazy :)
        print("How many authors kakku entry has")
        kakku = Entry.objects.get(headline__contains="kakku") # get finds single
        print(kakku.authors.count())
        print("All blog entries made by Lissu by publishing date order")
        entries = Entry.objects.filter(authors__name="Lissu Sörsseli").order_by('pub_date')
        print(entries)
        print("All blog entries made by Lissu by reverse publishing date order")
        entries = Entry.objects.filter(authors__name="Lissu Sörsseli").order_by('-pub_date')
        print(entries)
        print("All comments:")
        comments = Comment.objects.all()
        print(comments)
        print("Comments to Lissu's blog entries")
        comments = Comment.objects.filter(entry__authors__name="Lissu Sörsseli")
        print(comments)
        
