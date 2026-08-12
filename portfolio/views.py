from django.shortcuts import render, get_object_or_404
from .models import Project, ServiceRate, PhotographerProfile

def home(request):
    featured_project = Project.objects.filter(is_featured=True).first()
    recent_projects = Project.objects.all().order_by('-date_created')[:6]
    profile = PhotographerProfile.objects.first() # Fetches your profile settings
    
    context = {
        'featured': featured_project,
        'projects': recent_projects,
        'profile': profile,
    }
    return render(request, 'index.html', context)

# Rate Card / Services Page (Linked to JOIN+)
def rates_view(request):
    rates = ServiceRate.objects.all()
    return render(request, 'rates.html', {'rates': rates})

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'project_detail.html', {'project': project})

def latest_projects(request):
    # Sort by '-date_created' instead of '-created_at'
    projects = Project.objects.all().order_by('-date_created')
    
    return render(request, 'category.html', {
        'category_name': 'LATEST WORK',
        'projects': projects,
    })

def fashion_projects(request):
    # Filter by fashion and order by latest date
    projects = Project.objects.filter(category__iexact='fashion').order_by('-date_created')
    
    return render(request, 'category.html', {
        'category_name': 'FASHION',
        'projects': projects,
    })