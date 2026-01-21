# 🎯 AI-Powered Smart Job Recommendation Platform

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.2-green)](https://www.djangoproject.com/)
[![Machine Learning](https://img.shields.io/badge/ML-Scikit--learn-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A production-ready web application that uses **Machine Learning** to match job seekers with relevant opportunities based on their skills. Built with Django, this platform leverages **TF-IDF vectorization** and **Cosine Similarity** to provide intelligent, personalized job recommendations.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Usage](#-usage)
- [Machine Learning Algorithm](#-machine-learning-algorithm)
- [Project Structure](#-project-structure)
- [Screenshots](#-screenshots)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

### User Features
- 🔐 **User Authentication**: Secure registration, login, and logout
- 👤 **Profile Management**: Add and update skills, bio, and personal information
- 🎯 **Smart Job Recommendations**: AI-powered job matching based on user skills
- 📊 **Match Scoring**: View relevance scores and confidence levels for each recommendation
- 🔍 **Job Browsing**: Browse and search all available job listings
- 📱 **Responsive Design**: Mobile-friendly, modern UI with smooth animations

### Admin Features
- 🛠️ **Django Admin Panel**: Full CRUD operations for job management
- 📈 **User Management**: View and manage user profiles
- 🎨 **Bulk Actions**: Activate/deactivate multiple jobs at once

### ML Features
- 🤖 **TF-IDF Vectorization**: Convert skills into numerical features
- 📐 **Cosine Similarity**: Calculate job-skill similarity scores
- 🏆 **Ranked Results**: Jobs sorted by match percentage
- 🎓 **Confidence Levels**: Categorized match quality (Excellent, Good, Fair, Low)

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.8+, Django 4.2 |
| **Frontend** | HTML5, CSS3 (Modern Responsive Design) |
| **Database** | SQLite (Django ORM) |
| **Machine Learning** | Scikit-learn (TF-IDF, Cosine Similarity) |
| **Authentication** | Django Authentication System |
| **Architecture** | MVC (Django Apps) |

---

## 🏗️ Architecture

```
smart_job_recommender/
│
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
│
├── smart_job_recommender/             # Main project configuration
│   ├── __init__.py
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Main URL configuration
│   ├── wsgi.py                        # WSGI configuration
│   └── asgi.py                        # ASGI configuration
│
├── accounts/                          # User authentication app
│   ├── models.py                      # UserProfile model
│   ├── views.py                       # Auth views (login, register, profile)
│   ├── forms.py                       # User forms
│   ├── urls.py                        # Account URLs
│   ├── admin.py                       # Admin configuration
│   └── templates/accounts/            # Account templates
│       ├── login.html
│       ├── register.html
│       └── profile.html
│
├── jobs/                              # Job management app
│   ├── models.py                      # Job model
│   ├── views.py                       # Job views
│   ├── urls.py                        # Job URLs
│   ├── admin.py                       # Job admin
│   └── templates/jobs/                # Job templates
│       ├── home.html
│       ├── dashboard.html
│       ├── job_list.html
│       ├── job_detail.html
│       └── recommendations.html
│
├── ml_engine/                         # Machine Learning engine
│   ├── __init__.py
│   └── recommender.py                 # ML recommendation logic
│
├── templates/                         # Global templates
│   └── base.html                      # Base template
│
└── static/                            # Static files
    └── css/
        └── style.css                  # Main stylesheet
```

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/smart-job-recommender.git
cd smart-job-recommender
```

### Step 2: Create Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 5: Create Superuser (Admin)
```bash
python manage.py createsuperuser
```
Follow the prompts to create an admin account.

### Step 6: Load Sample Data (Optional)
```bash
python manage.py shell
```
Then in the Python shell:
```python
from jobs.models import Job

# Create sample jobs
Job.objects.create(
    title="Senior Python Developer",
    company="Tech Corp",
    location="Remote",
    salary_range="$100k - $150k",
    required_skills="Python, Django, REST API, PostgreSQL, Docker",
    description="We are looking for an experienced Python developer to join our team."
)

Job.objects.create(
    title="Machine Learning Engineer",
    company="AI Solutions Inc",
    location="San Francisco, CA",
    salary_range="$120k - $180k",
    required_skills="Python, Machine Learning, TensorFlow, Scikit-learn, Data Science",
    description="Join our ML team to build cutting-edge AI solutions."
)

Job.objects.create(
    title="Full Stack Developer",
    company="Web Innovations",
    location="New York, NY",
    salary_range="$90k - $130k",
    required_skills="JavaScript, React, Node.js, Python, Django, MongoDB",
    description="Full stack role working on modern web applications."
)

exit()
```

### Step 7: Run Development Server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` in your browser.

---

## 🚀 Usage

### For Job Seekers

1. **Register an Account**
   - Navigate to the registration page
   - Fill in your details including skills (comma-separated)
   - Submit the form

2. **Complete Your Profile**
   - Log in to your account
   - Go to Profile page
   - Add/update your skills and bio

3. **Get Recommendations**
   - Click "Get Job Recommendations" from dashboard
   - View AI-generated matches with similarity scores
   - Browse job details and apply

4. **Browse Jobs**
   - View all available jobs
   - Filter and search for opportunities
   - View detailed job descriptions

### For Administrators

1. **Access Admin Panel**
   - Go to `http://127.0.0.1:8000/admin/`
   - Log in with superuser credentials

2. **Manage Jobs**
   - Add new job postings
   - Edit existing jobs
   - Activate/deactivate jobs
   - Use bulk actions for efficiency

3. **Manage Users**
   - View user profiles
   - Monitor user skills and activity

---

## 🤖 Machine Learning Algorithm

### How It Works

The recommendation system uses a **content-based filtering** approach:

#### 1. Text Preprocessing
```python
# User skills and job requirements are cleaned and normalized
user_skills = "Python, Django, Machine Learning"
job_skills = "Python, Django, REST API"
```

#### 2. TF-IDF Vectorization
```python
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words='english',
    ngram_range=(1, 2)
)
# Converts text to numerical vectors
```

#### 3. Cosine Similarity Calculation
```python
from sklearn.metrics.pairwise import cosine_similarity

# Measures similarity between user vector and job vectors
similarity_score = cosine_similarity(user_vector, job_vector)
# Returns value between 0 (no match) and 1 (perfect match)
```

#### 4. Ranking and Filtering
- Jobs are sorted by similarity score (descending)
- Match percentage calculated: `score * 100`
- Confidence levels assigned:
  - **Excellent Match**: ≥70%
  - **Good Match**: 50-69%
  - **Fair Match**: 30-49%
  - **Low Match**: <30%

### Algorithm Benefits
- ✅ Fast and efficient
- ✅ No training data required
- ✅ Transparent and explainable
- ✅ Scales well with data growth
- ✅ Real-time recommendations

---

## 📁 Project Structure

### Models

**UserProfile** (accounts/models.py)
```python
- user: OneToOneField (User)
- skills: TextField
- bio: TextField
- created_at: DateTimeField
- updated_at: DateTimeField
```

**Job** (jobs/models.py)
```python
- title: CharField
- company: CharField
- location: CharField
- salary_range: CharField
- required_skills: TextField
- description: TextField
- is_active: BooleanField
- created_at: DateTimeField
- updated_at: DateTimeField
```

### Key Files

- **ml_engine/recommender.py**: ML recommendation engine
- **accounts/views.py**: User authentication and profile views
- **jobs/views.py**: Job browsing and recommendation views
- **static/css/style.css**: Complete responsive styling
- **templates/base.html**: Base template with navigation

---

## 📸 Screenshots

### Home Page
*Landing page with feature highlights and call-to-action*

### Dashboard
*Personalized user dashboard with quick stats and actions*

### Job Recommendations
*AI-powered recommendations with match scores*

### Profile Management
*Edit skills and personal information*

### Job Details
*Detailed view of job requirements and description*

---

## 🔌 API Documentation

While this version uses traditional Django views, the architecture is designed to easily add REST API endpoints.

### Potential API Endpoints (Future Enhancement)

```
GET    /api/jobs/                    # List all jobs
GET    /api/jobs/<id>/               # Job detail
POST   /api/recommendations/         # Get recommendations
GET    /api/profile/                 # User profile
PUT    /api/profile/                 # Update profile
```

---

## 🧪 Testing

### Run Tests
```bash
python manage.py test
```

### Manual Testing Checklist
- [ ] User registration with skills
- [ ] User login/logout
- [ ] Profile update functionality
- [ ] Job listing display
- [ ] Job detail view
- [ ] Recommendation generation
- [ ] Admin job management
- [ ] Responsive design on mobile

---

## 🔒 Security Considerations

- ✅ CSRF protection enabled
- ✅ Password hashing (Django default)
- ✅ SQL injection prevention (Django ORM)
- ✅ XSS protection
- ⚠️ Change `SECRET_KEY` for production
- ⚠️ Set `DEBUG = False` in production
- ⚠️ Configure `ALLOWED_HOSTS` properly

---

## 🚀 Deployment

### Heroku Deployment

1. Install Heroku CLI
2. Create `Procfile`:
```
web: gunicorn smart_job_recommender.wsgi
```

3. Update `settings.py`:
```python
import os
import dj_database_url

DEBUG = False
ALLOWED_HOSTS = ['your-app.herokuapp.com']
```

4. Deploy:
```bash
heroku create your-app-name
git push heroku main
heroku run python manage.py migrate
```

### AWS/DigitalOcean Deployment
- Use Gunicorn as WSGI server
- Configure Nginx as reverse proxy
- Set up SSL certificate
- Use PostgreSQL for production database

---

## 📚 Learning Resources

This project demonstrates:
- Django MVT architecture
- User authentication & authorization
- Form handling & validation
- Database relationships (OneToOne, Foreign Keys)
- Template inheritance & context processors
- Static files management
- Machine Learning integration
- Responsive web design
- Clean code practices
- Production-ready structure

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

## 🙏 Acknowledgments

- Django Documentation
- Scikit-learn Documentation
- Python Community
- Open Source Contributors

---

## 📞 Support

For issues, questions, or suggestions:
- 🐛 Report bugs via [GitHub Issues](https://github.com/yourusername/smart-job-recommender/issues)
- 💬 Discussions on [GitHub Discussions](https://github.com/yourusername/smart-job-recommender/discussions)
- 📧 Email: support@example.com

---

## 🗺️ Roadmap

Future enhancements:
- [ ] REST API implementation
- [ ] User dashboard analytics
- [ ] Job application tracking
- [ ] Email notifications
- [ ] Advanced filters (location, salary, etc.)
- [ ] Collaborative filtering ML model
- [ ] Job bookmarking feature
- [ ] Resume upload & parsing
- [ ] Company profiles
- [ ] Interview scheduling

---

**⭐ If you find this project helpful, please consider giving it a star!**

---

*Built with ❤️ using Django and Machine Learning*
