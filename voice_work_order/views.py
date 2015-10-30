from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse,reverse_lazy
from django.http import HttpResponse
from forms import *

class IndexView(FormView):
    template_name = 'voice_work_order/index.html'
    form_class = SessionForm

    def get_success_url(self,**kwargs): 
        return reverse('workorder:session', kwargs={'session_id':self.session_id}) 

    def form_valid(self,form,**kwargs):
        customer = Customer(name=form.cleaned_data['customer'])
        plane = Plane(model=form.cleaned_data['model'])
        customer.save()
        plane.save()
        session = Session(customer=customer,plane=plane)
        session.save()
        self.session_id = session.pk
        return super(IndexView, self).form_valid(form,**kwargs)
    def get_context_data(self,**kwargs):
        context = super(IndexView,self).get_context_data(**kwargs)
        context['sessions'] = Session.objects.all()
        return context

def session(request,session_id):
    context = {}
    context['session_id'] = session_id
    return render(request,'voice_work_order/session.html',context)

def workorder(request,session_id,ordertype):
    dic = {'it':'IT related',
           'mech':'Mechanical',
           'cos':'Cosmetic'
     }
    form = WorkOrderForm(initial={'ordertype': dic[ordertype]})
    context = {}
    context['form'] = form
    context['session_id'] = session_id
    return render(request,'voice_work_order/workorder.html',context)

