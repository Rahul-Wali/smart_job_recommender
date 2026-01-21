from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Job
from accounts.models import UserProfile
from ml_engine.recommender import JobRecommender


def home_view(request):
    """
    Landing page view.
    """
    jobs_count = Job.objects.filter(is_active=True).count()
    context = {
        'jobs_count': jobs_count,
    }
    return render(request, 'jobs/home.html', context)


@login_required
def dashboard_view(request):
    """
    User dashboard showing profile summary and quick actions.
    """
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        # Create profile if doesn't exist
        profile = UserProfile.objects.create(user=request.user, skills='')
        messages.warning(request, 'Please update your profile with your skills to get job recommendations.')
    
    # Get recent jobs
    recent_jobs = Job.objects.filter(is_active=True)[:6]
    
    context = {
        'profile': profile,
        'recent_jobs': recent_jobs,
        'total_jobs': Job.objects.filter(is_active=True).count(),
    }
    return render(request, 'jobs/dashboard.html', context)


@login_required
def job_list_view(request):
    """
    Display all active jobs with pagination.
    """
    jobs = Job.objects.filter(is_active=True).order_by('-created_at')
    
    # Pagination
    paginator = Paginator(jobs, 10)  # Show 10 jobs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'total_jobs': jobs.count(),
    }
    return render(request, 'jobs/job_list.html', context)


@login_required
def job_detail_view(request, job_id):
    """
    Display detailed information about a specific job.
    """
    job = get_object_or_404(Job, id=job_id, is_active=True)
    
    context = {
        'job': job,
    }
    return render(request, 'jobs/job_detail.html', context)


@login_required
def recommend_jobs_view(request):
    """
    Generate and display job recommendations based on user skills using ML.
    """
    try:
        profile = request.user.profile
    except UserProfile.DoesNotExist:
        messages.error(request, 'Please update your profile with skills first.')
        return redirect('accounts:profile')
    
    # Check if user has skills
    if not profile.skills or not profile.skills.strip():
        messages.warning(request, 'Please add your skills in your profile to get recommendations.')
        return redirect('accounts:profile')
    
    # Get all active jobs
    all_jobs = Job.objects.filter(is_active=True)
    
    if not all_jobs.exists():
        messages.info(request, 'No jobs available at the moment. Please check back later.')
        return redirect('jobs:dashboard')
    
    # Initialize recommender and get recommendations
    recommender = JobRecommender()
    recommendations = recommender.get_recommendations(profile.skills, all_jobs)
    
    # Filter recommendations with score > 0
    filtered_recommendations = [rec for rec in recommendations if rec['similarity_score'] > 0]
    
    if not filtered_recommendations:
        messages.info(request, 'No matching jobs found for your skills. Try updating your skills or browse all jobs.')
        context = {
            'recommendations': [],
            'user_skills': profile.get_skills_list(),
            'no_matches': True,
        }
    else:
        context = {
            'recommendations': filtered_recommendations,
            'user_skills': profile.get_skills_list(),
            'no_matches': False,
        }
    
    return render(request, 'jobs/recommendations.html', context)
