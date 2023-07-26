# Academic Publication Database - LensAcademia

LensAcademia is a Django-based academic publication database that allows you to manage and organize information about authors, research papers, keywords, and research groups. It provides a RESTful API to interact with the data, making it easy to integrate with other applications.

## Features

* Create, read, update, and delete research papers, authors, and keywords.
* Search for research papers by name, author, or keyword.
* Expose an API for accessing the data.

## Requirements

* Python 3.8+
* Django 4.2+
* Django Rest Framework 3.12+
* django-cors-headers

## Installation and Setup

To run the lensAcademia Backend API locally, follow these steps:

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd tick-it-backend
    ```

2. Create and activate a virtual environment:

    ```bash
    pipenv shell
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Apply database migrations:

    ```bash
    python manage.py migrate
    ```

5. Create a superuser (admin) to access the Django admin interface:

    ```bash
    python manage.py createsuperuser
    ```

6. Run the development server:

    ```bash
    python manage.py runserver
    ```

## Api End points

The lensAcademia API provides the following endpoints:

## Authors:

    List all authors: /api/authors/
    Get details for a specific author: /api/authors/<author_id>/

Keywords:

    List all keywords: /api/keywords/
    Get details for a specific keyword: /api/keywords/<keyword_id>/

Research Papers:

    List all research papers: /api/researchpapers/
    Get details for a specific research paper: /api/researchpapers/<research_paper_id>/

Research Groups (TG):

    List all research groups: /api/tgs/
    Get details for a specific research group: /api/tgs/<tg_id>

## Django Admin Interface

You can access the Django admin interface at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/). Use your superuser credentials to log in and manage venues and events through the admin panel.

## Contributing

Contributions to the lensAcademia Backend API are welcome! If you find a bug, have a feature request, or want to improve the code, feel free to open an issue or submit a pull request.