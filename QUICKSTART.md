# 🚀 Quick Start Guide

## AI-Powered Smart Job Recommendation Platform

This guide will help you get the application running in **under 5 minutes**.

---

## ⚡ Fast Setup (5 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 3: Load Sample Data (Optional but Recommended)
```bash
python manage.py shell
```

Then paste this code:
```python
from jobs.models import Job

Job.objects.create(
    title="Senior Python Developer",
    company="Tech Innovations Inc",
    location="Remote",
    salary_range="$100k - $150k",
    required_skills="Python, Django, REST API, PostgreSQL, Docker, Git",
    description="We are looking for an experienced Python developer to join our team."
)

Job.objects.create(
    title="Machine Learning Engineer",
    company="AI Solutions Corp",
    location="San Francisco, CA",
    salary_range="$120k - $180k",
    required_skills="Python, Machine Learning, TensorFlow, Scikit-learn, Data Science",
    description="Join our ML team to build cutting-edge AI solutions."
)

Job.objects.create(
    title="Full Stack Developer",
    company="Web Innovations LLC",
    location="New York, NY",
    salary_range="$90k - $130k",
    required_skills="JavaScript, React, Node.js, Python, Django, MongoDB",
    description="Full stack role working on modern web applications."
)

print(f"Created {Job.objects.count()} jobs!")
exit()
```

### Step 4: Create Admin User (Optional)
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

### Step 5: Run the Server
```bash
python manage.py runserver
```

**🎉 Done! Visit: http://127.0.0.1:8000/**

---

## 📱 Using the Application

### For Regular Users:

1. **Register** → Go to http://127.0.0.1:8000/accounts/register/
   - Fill in your details
   - **Important:** Add your skills (comma-separated)
   - Example: `Python, Django, Machine Learning, Data Science`

2. **Login** → Use your credentials

3. **Get Recommendations** → Click "Get Job Recommendations"
   - AI will analyze your skills
   - See match scores and confidence levels

4. **Browse Jobs** → View all available positions

5. **Update Profile** → Add more skills anytime

### For Admins:

1. **Access Admin Panel** → http://127.0.0.1:8000/admin/
2. **Manage Jobs** → Add, edit, delete job postings
3. **View Users** → See registered users and their profiles

---

## 🧪 Testing the ML Engine

Try these skill combinations to see different recommendations:

| Skills | Expected Top Matches |
|--------|---------------------|
| `Python, Django, REST API` | Senior Python Developer |
| `Python, Machine Learning, TensorFlow` | Machine Learning Engineer |
| `JavaScript, React, Node.js` | Full Stack Developer |
| `Docker, Kubernetes, AWS` | DevOps Engineer |

---

## 🔍 Verification Checklist

✅ All dependencies installed  
✅ Database migrations completed  
✅ Sample jobs created  
✅ Server running without errors  
✅ Home page loads (http://127.0.0.1:8000/)  
✅ Registration works  
✅ Login works  
✅ Recommendations generate correctly  

---

## 🐛 Troubleshooting

### Issue: "No module named django"
**Solution:** Run `pip install -r requirements.txt`

### Issue: "Table doesn't exist"
**Solution:** Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### Issue: "No jobs available"
**Solution:** Load sample data (see Step 3 above)

### Issue: Port already in use
**Solution:** Use a different port:
```bash
python manage.py runserver 8080
```

---

## 📚 Key URLs

| Page | URL |
|------|-----|
| Home | http://127.0.0.1:8000/ |
| Register | http://127.0.0.1:8000/accounts/register/ |
| Login | http://127.0.0.1:8000/accounts/login/ |
| Dashboard | http://127.0.0.1:8000/dashboard/ |
| Jobs List | http://127.0.0.1:8000/jobs/ |
| Recommendations | http://127.0.0.1:8000/recommendations/ |
| Profile | http://127.0.0.1:8000/accounts/profile/ |
| Admin | http://127.0.0.1:8000/admin/ |

---

## 🎓 Understanding the ML Algorithm

The recommendation system works in 4 steps:

1. **Input**: Your skills → `"Python, Django, Machine Learning"`
2. **Vectorization**: Convert to numbers using TF-IDF
3. **Comparison**: Calculate similarity with each job's requirements
4. **Output**: Ranked list with match percentages

**Example:**
- Your skills: `Python, Django, REST API`
- Job requires: `Python, Django, PostgreSQL, Docker`
- **Match**: 66% (2 out of 3 of your skills match main requirements)

---

## 💡 Pro Tips

1. **Add More Skills** → Better recommendations
2. **Use Specific Terms** → "Machine Learning" vs just "ML"
3. **Include Technologies** → Languages, frameworks, tools
4. **Update Regularly** → Keep skills current

---

## 🚀 Next Steps

- [ ] Customize the design in `static/css/style.css`
- [ ] Add more sample jobs via Admin panel
- [ ] Modify ML algorithm in `ml_engine/recommender.py`
- [ ] Deploy to production (see README.md)

---

## 📞 Need Help?

- Check `README.md` for detailed documentation
- Review code comments for explanations
- All models are documented with docstrings

---

**Built with ❤️ using Django & Machine Learning**

*Perfect for Junior Python Developer portfolios and interview discussions!*
