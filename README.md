
# 🎨 Django Portfolio Project

Welcome to the **Django Portfolio** project! This README file will guide you through setting up and understanding this personal portfolio website. The project is available on [GitHub](https://github.com/MahmoudBayoumi58/django-portfolio) and is deployed on [Vercel](https://django-portfolio-6e60o6x7k-mahmoud-bayoumis-projects.vercel.app/).

---

## 🚀 Project Overview

The **Django Portfolio** project is a personal portfolio website built using the Django framework. It dynamically renders content stored in the database to display various sections, including projects, skills, and contact information. The website is designed with a clean and responsive interface, ensuring a user-friendly experience.

### 🔍 Features

- **Home Page:** Displays your name, job title, and provides navigation links to other sections of the website.
- **About Page:** Showcases detailed information about you, including your skills and certifications.
- **Resume Page:** Presents your professional experience and qualifications through a comprehensive resume.
- **Service Page:** Outlines the services you offer, highlighting how you can provide value to clients or employers.
- **Portfolio Page:** Lists your portfolio projects, showcasing the applications you have developed.
- **Contact Page:** Contains your contact information, allowing potential clients or employers to reach out to you easily.

### 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap, JavaScript
- **Database**: SQLite (Note: For production, consider using PostgreSQL or another robust database system)
- **Deployment**: Vercel (Serverless deployment platform)

### 🗂️ Project Structure

Here’s a brief overview of the project structure:

```plaintext
├── portfolio/
│   ├── templates/
│   │   ├── base/
│   │   │   └── base.html
│   │   ├── portfolio/
│   │   │   ├── home.html
│   │   │   ├── about.html
│   │   │   ├── contact.html
│   │   │   ├── portfolio.html
│   │   │   ├── portfolio-details.html
│   │   │   ├── resume.html
│   │   │   ├── services.html
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── js/
│   │   │   └── scripts.js
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
└── ...
```

### 📦 Setup Instructions

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/MahmoudBayoumi58/django-portfolio.git
   cd django-portfolio
   ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up the Database:**

   Run the following commands to apply migrations and set up the database:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server:**

   Start the server locally to test the application:

   ```bash
   python manage.py runserver
   ```

   The application should be available at `http://127.0.0.1:8000/`.

7. **Deploy to Vercel:**

   The project is configured for deployment on Vercel. Ensure you set up the required environment variables, especially for the database if you're using a cloud database service. For Vercel-specific setup, create a `vercel.json` file and a `build_files.sh` script as needed.

### 📸 Screenshots

Here are some screenshots of the live application:

1. **Home Page:**
   ![Home Page](https://raw.githubusercontent.com/MahmoudBayoumi58/django-portfolio/main/staticfiles/portfolio/img/portfolio-images/home.png)

2. **About Page:**
   ![About Page](https://raw.githubusercontent.com/MahmoudBayoumi58/django-portfolio/main/staticfiles/portfolio/img/portfolio-images/about.png)

3. **Resume Page:**
   ![Resume Page](https://raw.githubusercontent.com/MahmoudBayoumi58/django-portfolio/main/staticfiles/portfolio/img/portfolio-images/resume.png)

4. **Services Page:**
   ![Services Page](https://raw.githubusercontent.com/MahmoudBayoumi58/django-portfolio/main/staticfiles/portfolio/img/portfolio-images/services.png)

5. **Portfolio Page:**
   ![Portfolio Page](https://raw.githubusercontent.com/MahmoudBayoumi58/django-portfolio/main/staticfiles/portfolio/img/portfolio-images/portfolio.png)

6. **Contact Page:**
   ![Contact Page](https://raw.githubusercontent.com/MahmoudBayoumi58/django-portfolio/main/staticfiles/portfolio/img/portfolio-images/contact.png)

### 📊 Dynamic Content

All the pages in this portfolio dynamically render data from the SQLite database. For example:

- **Projects Page**: Fetches projects from the database and displays them in a list format with relevant details.
- **Skills Section**: Automatically updates when new skills are added to the database.
- **Contact Form**: Submits user queries directly into the database.

### 🌐 Considerations for Production

For production deployment, consider the following adjustments:

- **Switch to PostgreSQL**: Replace SQLite with PostgreSQL or another production-ready database.
- **Security Settings**: Ensure that `DEBUG` is set to `False` and that you have properly configured `ALLOWED_HOSTS` and other security settings.
- **Static Files Handling**: Ensure static files are correctly managed, especially when deploying to platforms like Vercel.

### 📬 Contact

For any questions or suggestions regarding this project, feel free to open an issue on the [GitHub repository](https://github.com/MahmoudBayoumi58/django-portfolio) or contact the developer directly.

---

This README provides a comprehensive guide to setting up, running, and understanding the Django Portfolio project. For any further details, please refer to the repository itself.
