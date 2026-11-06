# Translator Website

A modern, responsive, single-page business card website for a certified German translator. The project is built with Django and features a distinctive dark design, animated backgrounds (Lava Lamp, floating dust particles, and deep sea waves), interactive UI elements, and dynamic content management.

## Tech Stack

- **Backend:** Python 3, Django 5.x
- **Frontend:** HTML5, CSS3, Bootstrap 5
- **Animations:** AOS (Animate On Scroll), custom JavaScript animations, and CSS Keyframes
- **Database:** SQLite
- **Design:** Dark theme with dynamic, multi-layered animated backgrounds

## Features

- Fully responsive design (desktop, tablet, and mobile).

- **Three Distinct Animated Sections:**
  - **Hero:** Dynamic Lava Lamp background with randomly generated, morphing shapes.
  - **Offer:** Floating dust particles and glowing sparks rising upwards.
  - **Location:** Deep sea-inspired, Aurora-like glowing waves in the background.

- **Interactive UI Elements:**
  - Custom scroll-based zoom animations for the Hero and Offer cards.
  - Glowing icon effects on card hover.
  - Smooth scrolling between website sections.
  - Custom scrollbar styling.
  - Interactive hover effects and modern UI elements.

- **Google Maps Integration:**
  - Google Maps embedded in the Location section.
  - Dark-mode styled map.
  - Interactive hover lift effect.

- Contact information dynamically retrieved from the database.
- Django Admin panel for easy content management.
- Custom HTML templates built with Django Template Language.
- Organized CSS architecture with separate stylesheets for animations, layout, responsiveness, and individual website components.

## Project Structure

```text
TRANSLATOR_WEBSITE/
│
├── config/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── core/
│   ├── migrations/
│   │
│   ├── static/
│   │   └── css/
│   │       ├── animations.css
│   │       ├── base.css
│   │       ├── lava-lamp.css
│   │       ├── layout.css
│   │       ├── offer-cards.css
│   │       ├── responsive.css
│   │       └── style.css
│   │
│   ├── templates/
│   │   └── core/
│   │       ├── base.html
│   │       ├── index.html
│   │       └── page.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── context_processors.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── media/
│
├── .gitignore
├── manage.py
├── README.md
└── requirements.txt
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/TRANSLATOR_WEBSITE.git
cd TRANSLATOR_WEBSITE
```

### 2. Create and activate a virtual environment

**Windows:**

```bat
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply database migrations

```bash
python manage.py migrate
```

### 5. Create an administrator account

```bash
python manage.py createsuperuser
```

Follow the instructions in the terminal to create your administrator credentials.

### 6. Start the development server

```bash
python manage.py runserver
```

### 7. Open the website

Visit the following address in your browser:

```text
http://127.0.0.1:8000/
```

## Django Administration

The project includes a Django Admin panel for managing website content and database records.

To access the administration panel, visit:

```text
http://127.0.0.1:8000/admin/
```

Log in using your superuser credentials.

## Requirements

The project requires:

- Python 3
- Django 5.x
- Pillow
- A modern web browser

All Python dependencies are listed in `requirements.txt`.

To generate or update the dependency list, run:

```bash
pip freeze > requirements.txt
```

## GitHub Deployment

### 1. Initialize Git

Run the following commands from the project root directory:

```bash
git init
git add .
git commit -m "Initial commit: Modern translator website with animated backgrounds"
git branch -M main
```

### 2. Create a GitHub repository

1. Visit [GitHub](https://github.com/).
2. Create a new repository named `TRANSLATOR_WEBSITE`.
3. Do not initialize it with a README, `.gitignore`, or license if these files already exist locally.

### 3. Connect and push the repository

Replace `YOUR_USERNAME` with your actual GitHub username:

```bash
git remote add origin https://github.com/YOUR_USERNAME/TRANSLATOR_WEBSITE.git
git push -u origin main
```

## License

This project is intended for educational and portfolio purposes.