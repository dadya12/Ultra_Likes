from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, View
from webapp.forms import CommentForm
from webapp.models import Article, Comment
from django.http import JsonResponse


class CreateCommentView(LoginRequiredMixin, CreateView):
    template_name = "comments/create_comment.html"
    form_class = CommentForm

    def form_valid(self, form):
        article = get_object_or_404(Article, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.article = article
        comment.author = self.request.user
        comment.save()
        return redirect(article.get_absolute_url())


class UpdateCommentView(UpdateView):
    template_name = "comments/update_comment.html"
    form_class = CommentForm
    model = Comment

    def get_success_url(self):
        return reverse("webapp:article_detail", kwargs={"pk": self.object.article.pk})


class LikeCommentView(LoginRequiredMixin, View):
    def get(self, request, pk):
        comment = get_object_or_404(Comment, pk=pk)
        liked = request.user in comment.users_likes.all()
        if liked:
            comment.users_likes.remove(request.user)
        else:
            comment.users_likes.add(request.user)
        return JsonResponse({'total_likes': comment.users_likes.count(), 'liked': not liked})


class DeleteCommentView(DeleteView):
    queryset = Comment.objects.all()

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect("webapp:article_detail", pk=self.object.article.pk)
