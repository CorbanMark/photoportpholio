from django.shortcuts import render, get_object_or_404
from .models import Project, ServiceRate, PhotographerProfile


def _featured_project():
    return Project.objects.filter(is_featured=True).first()


def _projects_without_featured(queryset):
    featured = _featured_project()
    if featured:
        return queryset.exclude(pk=featured.pk)
    return queryset


def home(request):
    featured_project = _featured_project()
    recent_projects = _projects_without_featured(
        Project.objects.all().order_by('-date_created')
    )[:6]
    profile = PhotographerProfile.objects.first()

    context = {
        'featured': featured_project,
        'projects': recent_projects,
        'profile': profile,
    }
    return render(request, 'index.html', context)


def rates_view(request):
    rates = ServiceRate.objects.all()
    return render(request, 'rates.html', {'rates': rates})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})


def latest_projects(request):
    projects = _projects_without_featured(
        Project.objects.all().order_by('-date_created')
    )

    return render(request, 'category.html', {
        'category_name': 'LATEST WORK',
        'projects': projects,
    })


def fashion_projects(request):
    projects = _projects_without_featured(
        Project.objects.filter(category__iexact='fashion').order_by('-date_created')
    )

    return render(request, 'category.html', {
        'category_name': 'FASHION',
        'projects': projects,
    })
