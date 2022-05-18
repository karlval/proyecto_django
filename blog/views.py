from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# enlistar todos los posts que existan

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        #LLAMADA A TODOS LOS OBJETOS
        posts = Post.objects.all()
        
        context={
            # 1° va nombre de ref en el html, luego la variable que creamos y tiene la info
            'posts': posts 
        }
        return render(request, 'blog_list.html', context)

class BlogCreateView(View):
    def get(self, request, *args, **kwargs):
        form = PostCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = PostCreateForm(request.POST)
            
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                
                # (title, content) son valores que derivan de Post en models.py
                # y se asigna los valores declarados arriba 
                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                
                return redirect('blog:home')
                
                
        context = {
            
        }
        return render(request, 'blog_create.html', context)
    
    
class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        context = {
            'post' : post
        }        
        return render(request, 'blog_detail.html', context)
    
class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog_update.html'
    
    def get_success_url(self):
        #kwargs es la info del objeto que se esta llamando(self) del modelo Post
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk': pk})        
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog:home')