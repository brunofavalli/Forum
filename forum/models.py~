from django.db import models
from appForum.settings import MEDIA_URL
from django.contrib.auth.models import User

class Forum(models.Model):
    title   = models.CharField('Título', max_length=60)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse2("forum", dpk=self.pk)

    def num_posts(self):
        return sum([t.num_posts() for t in self.threads.all()])

    def last_post(self):
        """Procura o post mais recente."""
        threads = self.threads.all()
        last    = None
        for thread in threads:
            lastp = thread.last_post()
            if lastp and (not last or lastp.created > last.created):
                last = lastp
        return last

class Thread(models.Model):
    title   = models.CharField('Título', max_length=60)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    forum   = models.ForeignKey(Forum, related_name="threads")

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return ("%s - %s" % (self.creator, self.title))

    def get_absolute_url(self) : return reverse2("thread", dpk=self.pk)
    def last_post(self)        : return self.posts.all().last()
    def num_posts(self)        : return self.posts.count()
    def num_replies(self)      : return self.posts.count() - 1


class Post(models.Model):
    title   = models.CharField('Título', max_length=60)
    created = models.DateTimeField('Criado em', auto_now_add=True)
    creator = models.ForeignKey(User, blank=True, null=True)
    thread  = models.ForeignKey(Thread, related_name="posts")
    body    = models.TextField('Conteúdo', max_length=10000)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return "%s - %s - %s" % (self.creator, self.thread, self.title)

    def short(self):
        created = self.created.strftime("%b %d, %I:%M %p")
        return ("%s - %s\n%s" % (self.creator, self.title, created))

    def profile_data(self):
        p = self.creator.profile
        return p.posts, p.avatar


class UserProfile(models.Model):
    avatar = models.ImageField("Imagem perfil", upload_to="images/users", blank=True, null=True)
    posts  = models.IntegerField(default=0)
    user   = models.OneToOneField(User, related_name="profile")

    def __str__(self):
        return self.user.username

    def increment_posts(self):
        self.posts += 1
        self.save()

    def avatar_image(self):
        return (MEDIA_URL + self.avatar.name) if self.avatar else None
