from django.shortcuts import render

# Create your views here.
from django.contib import messages
from django.contib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views import generic
from groups.models import Group,GroupMember

class CreateGroup(LoginRequiredMixin,generic.CreateView):
    fields=('name','description')
    model = Group

class SingleGroup(generic.DetailView):
    model = Group

class ListGroups(generic.ListView):
    model = Group

class JoinGroup(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        group = get_object_or_404(Group,slig=self.kwargs.get('slug'))

        try:
            GroupMember.objects.create(user=self.request,group=group)
        except IntegrityError:
            messages.warning(self.request,'Warning already a Member!')
        else:
            messages.success(self.request,'You are now a member')

        return super().get(request,*args,**kwargs)


class LeaveGroup(LoginRequiredMixin,generic.RedirectView):
     def get_redirect_url(self,*args,**kwargs):
        return reverse('groups:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        try:
            membership = models.GroupMember.objects.filter(user=self.request.user,group__slug=self.kwargs.get('slug')).get()
        except models.GroupMember.DoesNotExist:
            messages.warning(self.request,'Sorry you are not a part of this group!')

        else:
            membership.delete()
            messages.success(self.request,'Yor have left the group!')
                
        return super().get(request,*args,**kwargs)
