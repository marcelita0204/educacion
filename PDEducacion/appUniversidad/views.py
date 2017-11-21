from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from rest_framework import viewsets
from django.views import View
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from appUniversidad.models import (
    ProgramaCurricular,
    Facultad,
    ContenidoPrograma,
    Materia,
    Hora,
    Sede,
    Horario
)

class HomePage(LoginRequiredMixin, TemplateView):
    template_name = "appUniversidad/home.html"

class ProgramaCurricularDetailView(LoginRequiredMixin, DetailView):
    model = ProgramaCurricular

class ProgramaCurricularList(LoginRequiredMixin, ListView):
    model = ProgramaCurricular
    context_object_name = 'programascurriculares'
    template_name = 'appUniversidad/indexprogramacurricular.html'

class ProgramaCurricularCreate(LoginRequiredMixin, CreateView):
    model = ProgramaCurricular
    fields = ['nombre']
    template_name = 'appUniversidad/crear-programacurricular.html'
    success_url = reverse_lazy('programascurricularesList')

class ProgramaCurricularUpdate(LoginRequiredMixin, UpdateView):
    model = ProgramaCurricular
    template_name = 'appUniversidad/crear-programacurricular.html'
    success_url = reverse_lazy('programascurricularesList')
    fields = ['nombre']

class ProgramaCurricularDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        programascurriculares = get_object_or_404(ProgramaCurricular, pk=self.kwargs['pk'])
        programascurriculares.delete()
        return redirect('programascurricularesList')

class FacultadDetailView(LoginRequiredMixin, DetailView):
    model = Facultad

class FacultadList(LoginRequiredMixin, ListView):
    model = Facultad
    context_object_name = 'facultades'
    template_name = 'appUniversidad/indexfacultad.html'

class FacultadCreate(LoginRequiredMixin, CreateView):
    model = Facultad
    fields = ['nombre']
    template_name = 'appUniversidad/crear-facultad.html'
    success_url = reverse_lazy('facultadesList')

class FacultadUpdate(LoginRequiredMixin, UpdateView):
    model = Facultad
    template_name = 'appUniversidad/crear-facultad.html'
    success_url = reverse_lazy('facultadesList')
    fields = ['nombre']

class FacultadDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        facultades = get_object_or_404(Facultad, pk=self.kwargs['pk'])
        facultades.delete()
        return redirect('facultadesList')

class ContenidoProgramaDetailView(LoginRequiredMixin, DetailView):
    model = ContenidoPrograma

class ContenidoProgramaList(LoginRequiredMixin, ListView):
    model = ContenidoPrograma
    context_object_name = 'contenidosprogramas'
    template_name = 'appUniversidad/indexcontenidoprograma.html'

class ContenidoProgramaCreate(LoginRequiredMixin, CreateView):
    model = ContenidoPrograma
    fields = ['nombre','tiempo','programacurricular','facultad']
    template_name = 'appUniversidad/crear-contenidoprograma.html'
    success_url = reverse_lazy('contenidosprogramasList')

    def get_context_data(self, **kwargs):
        context = super(ContenidoProgramaCreate, self).get_context_data(**kwargs)
        context['programacurricular'] = ProgramaCurricular.objects.all()
        context['facultad'] = Facultad.objects.all()
        return context

class ContenidoProgramaUpdate(LoginRequiredMixin, UpdateView):
    model = ContenidoPrograma
    template_name = 'appUniversidad/crear-contenidoprograma.html'
    success_url = reverse_lazy('contenidosprogramasList')
    fields = ['nombre','tiempo','programacurricular','facultad']

    def get_context_data(self, **kwargs):
        context = super(ContenidoProgramaUpdate, self).get_context_data(**kwargs)
        context['programacurricular'] = ProgramaCurricular.objects.all()
        context['facultad'] = Facultad.objects.all()
        return context

class ContenidoProgramaDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        contenidosprogramas = get_object_or_404(ContenidoPrograma, pk=self.kwargs['pk'])
        contenidosprogramas.delete()
        return redirect('contenidosprogramasList')

class MateriaDetailView(LoginRequiredMixin, DetailView):
    model = Materia

class MateriaList(LoginRequiredMixin, ListView):
    model = Materia
    context_object_name = 'materias'
    template_name = 'appUniversidad/indexmateria.html'

class MateriaCreate(LoginRequiredMixin, CreateView):
    model = Materia
    fields = ['nombre','contenidoprograma']
    template_name = 'appUniversidad/crear-materia.html'
    success_url = reverse_lazy('materiasList')

    def get_context_data(self, **kwargs):
        context = super(MateriaCreate, self).get_context_data(**kwargs)
        context['contenidoprograma'] = ContenidoPrograma.objects.all()
        return context

class MateriaUpdate(LoginRequiredMixin, UpdateView):
    model = Materia
    template_name = 'appUniversidad/crear-materia.html'
    success_url = reverse_lazy('materiasList')
    fields = ['nombre','contenidoprograma']

    def get_context_data(self, **kwargs):
        context = super(MateriaUpdate, self).get_context_data(**kwargs)
        context['contenidoprograma'] = ContenidoPrograma.objects.all()
        return context

class MateriaDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        materias = get_object_or_404(Materia, pk=self.kwargs['pk'])
        materias.delete()
        return redirect('materiasList')

class HoraDetailView(LoginRequiredMixin, DetailView):
    model = Hora

class HoraList(LoginRequiredMixin, ListView):
    model = Hora
    context_object_name = 'horas'
    template_name = 'appUniversidad/indexhora.html'

class HoraCreate(LoginRequiredMixin, CreateView):
    model = Hora
    fields = ['inicio','fin']
    template_name = 'appUniversidad/crear-hora.html'
    success_url = reverse_lazy('horasList')

class HoraUpdate(LoginRequiredMixin, UpdateView):
    model = Hora
    template_name = 'appUniversidad/crear-hora.html'
    success_url = reverse_lazy('horasList')
    fields = ['inicio','fin']

class HoraDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        horas = get_object_or_404(Hora, pk=self.kwargs['pk'])
        horas.delete()
        return redirect('horasList')

class SedeDetailView(LoginRequiredMixin, DetailView):
    model = Sede

class SedeList(LoginRequiredMixin, ListView):
    model = Sede
    context_object_name = 'sedes'
    template_name = 'appUniversidad/indexsede.html'

class SedeCreate(LoginRequiredMixin, CreateView):
    model = Sede
    fields = ['nombre']
    template_name = 'appUniversidad/crear-sede.html'
    success_url = reverse_lazy('sedesList')

class SedeUpdate(LoginRequiredMixin, UpdateView):
    model = Sede
    template_name = 'appUniversidad/crear-sede.html'
    success_url = reverse_lazy('sedesList')
    fields = ['nombre']

class SedeDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        sedes = get_object_or_404(Sede, pk=self.kwargs['pk'])
        sedes.delete()
        return redirect('sedesList')

class HorarioDetailView(LoginRequiredMixin, DetailView):
    model = Horario

class HorarioList(LoginRequiredMixin, ListView):
    model = Horario
    context_object_name = 'horarios'
    template_name = 'appUniversidad/indexhorario.html'

class HorarioCreate(LoginRequiredMixin, CreateView):
    model = Horario
    fields = ['materia','sede','hora']
    template_name = 'appUniversidad/crear-horario.html'
    success_url = reverse_lazy('horariosList')

    def get_context_data(self, **kwargs):
        context = super(HorarioCreate, self).get_context_data(**kwargs)
        context['materia'] = Materia.objects.all()
        context['sede'] = Sede.objects.all()
        context['hora'] = Hora.objects.all()
        return context


class HorarioUpdate(LoginRequiredMixin, UpdateView):
    model = Horario
    template_name = 'appUniversidad/crear-horario.html'
    success_url = reverse_lazy('horariosList')
    fields = ['materia','sede','hora']

    def get_context_data(self, **kwargs):
        context = super(HorarioUpdate, self).get_context_data(**kwargs)
        context['materia'] = Materia.objects.all()
        context['sede'] = Sede.objects.all()
        context['hora'] = Hora.objects.all()
        return context

class HorarioDelete(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        horarios = get_object_or_404(Horario, pk=self.kwargs['pk'])
        horarios.delete()
        return redirect('horariosList')
