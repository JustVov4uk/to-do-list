# To-Do List

A simple Django-based To-Do List application with tasks and tags.

## Features

* Create, update, and delete tasks
* Mark tasks as done/undone
* Assign multiple tags to tasks (many-to-many relationship)
* Paginated task list
* Sort tasks: incomplete first, then complete; newest tasks on top
* Export/import data using Django fixtures (JSON)

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd to-do-list
```

2. Create a virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. (Optional) Load initial data:

```bash
python manage.py loaddata fixtures/all_data.json
```

6. Run the development server:

```bash
python manage.py runserver
```

Open your browser at `http://127.0.0.1:8000`.

## Usage

* Go to the main page to see all tasks.
* Use the sidebar to navigate between tasks and tags.
* Pagination is enabled for long lists.
* Tasks are sorted automatically: incomplete tasks first, newest first.

## Project Structure

```
to-do-list/
├── config/            # Django app
├── fixtures/          # JSON fixtures for tasks and tags
├── manage.py
└── README.md
```

## License

This project is open-source.
