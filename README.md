# Intellectiva: Research Paper Archive

Intellectiva is a research paper archive developed using Django, Bootstrap, and jQuery. The archive allows users to view and download research articles and journals. Users can also log in and log out of the system.

## Screenshots

Here are some screenshots of the Intellectiva research paper archive:

### Main Page

![image](https://user-images.githubusercontent.com/102748742/236437318-9cc0687f-2863-4612-a44f-2c5b11a8aa5c.png)
![image](https://user-images.githubusercontent.com/102748742/236437360-0c6d4e60-1594-4f33-b249-1c8106f85dd4.png)

### Article Detail Page

![image](https://user-images.githubusercontent.com/102748742/236437548-5ecdf1a0-56f2-4ab6-9357-d21d250e909e.png)

### Login / Signup Page

![image](https://user-images.githubusercontent.com/102748742/236437157-60dd9448-bfbd-43b5-b476-7fb65f739401.png)
![image](https://user-images.githubusercontent.com/102748742/236438005-4a7bc6a9-dab1-4d25-9009-67b2fe300801.png)

I hope these screenshots give you a better idea of what Intellectiva looks like and how it works.

## Getting Started

To use Intellectiva, you will need to have Python and Django installed on your system. You can clone the repository from GitHub and run it locally using the following commands:

```
gh repo clone sohamw03/ResearchPaperArchive
cd intellectiva
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

After running the above commands, you can access the Intellectiva archive by visiting [http://localhost:8000](http://localhost:8000) in your web browser.

## Features

### Login/Logout

Users can log in and log out of the system. When a user is logged in, they can view and download articles and journals.

### View Articles and Journals

The archive displays a list of articles and journals on the main page. When a user clicks on an article or journal, they are taken to a detailed page where they can view the title, author, abstract, and a PDF preview of the content.

### Search

Users can search for articles and journals using keywords.

## Technologies Used

Intellectiva was developed using the following technologies:

- Python
- Django
- Bootstrap
- jQuery
- SQLite

## Contributing

If you would like to contribute to Intellectiva, please submit a pull request. All contributions are welcome!
