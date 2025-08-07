# Event Logger

[](https://www.python.org/downloads/)
[](https://www.djangoproject.com/)
[](https://www.mysql.com/)

A robust and efficient web application for logging and tracking daily laboratory experiments. Built with Python and the Django framework, this project demonstrates a clean backend architecture, database management with MySQL, and a dynamic user interface rendered with server-side logic.

## 🚀 Demo

Here is a look at the user interface of the **Event Logger**:

<img width="1475" height="842" alt="image" src="https://github.com/user-attachments/assets/993ed546-784f-4303-86de-acca92a1cb97" />


## ✨ Features

  * **Log Management**: Create, view, and delete daily logs.
  * **Entry Tracking**: Add detailed, timestamped entries to each daily log.
  * **Dynamic UI**: The interface is dynamically updated using JavaScript and jQuery to provide a smooth user experience without page reloads.
  * **Data Export**: Export log data to a CSV file for reporting and analysis.
  * **Efficient Data Handling**: Asynchronous requests (AJAX) are used to fetch and display log entries, ensuring the application is fast and responsive.
  * **Organized View**: A dual-panel layout allows for easy navigation between daily logs and their corresponding entries.

## 🛠️ Technologies Used

### Backend

  * **Python**: Core programming language.
  * **Django**: High-level Python web framework for rapid development and clean, pragmatic design.
  * **MySQL**: Robust, open-source relational database for data storage.

### Frontend

  * **HTML5**
  * **CSS3**
  * **JavaScript**
  * **jQuery**: For simplified DOM manipulation.
  * **Bootstrap**: For responsive UI components.

## 📂 Project Structure

The project follows a standard Django project structure:

```
Event_Logger/
├── EventLogger_Project/      # The Django project folder
│   ├── Event_Logger/         # The main project configuration
│   │   ├── __init__.py
│   │   ├── settings.py       # Project settings
│   │   ├── urls.py           # Project-level URL routing
│   │   └── wsgi.py
│   ├── event_app/            # The Django app for logging events
│   │   ├── migrations/
│   │   ├── static/           # CSS, JavaScript files
│   │   ├── templates/        # HTML templates
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py         # Database models (Log, Entry)
│   │   ├── tests.py
│   │   ├── urls.py           # App-level URL routing
│   │   └── views.py          # Application logic and request handling
│   └── manage.py             # Django's command-line utility
└── README.md
```

## 👤 Contact

Asaf Dov - [GitHub Profile](https://www.google.com/search?q=https://github.com/AsafDov)

Project Link: [https://github.com/AsafDov/Event\_Logger](https://www.google.com/search?q=https://github.com/AsafDov/Event_Logger)
