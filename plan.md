# Project Roadmap: Job Alert App

## 🔹 Core Pieces to Learn
1. **Web Framework (app skeleton)**
   - Purpose: expose APIs, manage users, structure project
   - Options: Django (all-in-one), FastAPI (modern, lightweight)

2. **Database (store data)**
   - Purpose: store websites, users, jobs found
   - Options: PostgreSQL (market standard), SQLite (easy start)

3. **Scraping / Data Fetching**
   - Purpose: get jobs from websites
   - Tools: Requests + BeautifulSoup
   - Alternative: use APIs if websites provide them

4. **Background Tasks (automation)**
   - Purpose: check websites automatically
   - Tools: Celery, APScheduler, or cron jobs

5. **Notifications**
   - Purpose: send alerts (email) when new jobs appear
   - Start: Django email backend or Python `smtplib`
   - Later: external services (SendGrid, Mailgun)

6. **Authentication (optional for multi-user)**
   - Django: built-in user system
   - FastAPI: JWT tokens

7. **Deployment**
   - Purpose: make app available online
   - Options: Heroku, Railway, Render

---

## 🔹 Big Picture Flow
1. User registers a company website to follow  
2. Website URL saved in the database  
3. Background task checks site regularly  
4. New job found → save in DB → send email notification  
5. API / frontend lets user view their tracked jobs  

---

## 🔹 Learning Approach
- Learn one piece at a time → connect later
- Example path:
  1. Scraping in a standalone script  
  2. Save scraped results in a database  
  3. Build an API with Django/FastAPI  
  4. Add automation (background tasks)  
  5. Send email notifications  
  6. Add authentication (if needed)  
  7. Deploy  

---