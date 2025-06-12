from django.conf import settings
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Post

# Список статей с фильтрацией опубликованных
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        # фильтрация только опубликованных статей
        return super().get_queryset().filter(is_published=True)

# Детальный просмотр статьи с увеличением счетчика просмотров
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        # увеличиваем счетчик просмотров при каждом просмотре
        obj.views_counter += 1
        if obj.views_counter == 30 and not obj.notified:
            send_mail(
                subject='Congratulations! The post has reached 30 views',
                message=f'Your post "{obj.title}" has reached 30 views!',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
            obj.notified = True
        obj.save(update_fields=['views_counter', 'notified'])
        return obj

# Создание новой статьи
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('blog:post_list')

# Обновление статьи с перенаправлением на страницу просмотра после успешного редактирования
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content', 'preview_image', 'is_published']
    template_name = 'blog/post_form.html'

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.object.pk})


# Удаление статьи (опционально)
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
