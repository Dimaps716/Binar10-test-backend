# Binar10-test-backend

_The site has a postgres database, I had a problem with my computer that did not allow me to use the MYSQL database but it is all the pertinent configuration to use the MYSQL database_

_These will allow you to get a copy of the working project on your local machine for development and testing ._

See Implementation to learn how to implement the project.


### Prerequisites  ๐


```
Docker
ubuntu terminal
```

### Instalaciรณn ๐ง

in the terminal located in the folder where you have this project, you can look at the folders and files that the project has with the ls command,
then run the following.
```
git clone https://github.com/Dimaps716/Binar10-test-backend.git
```
move to developer branch.

This will install the dependencies and requirements of the project.

```
docker-compose build
```
run migrations

```
docker-compose run web python manage.py makemigrations

docker-compose run web python manage.py migrate

```
for now the database is empty
```
docker-compose ps
```
create a user
```
docker-compose run web python manage
.py createsuperuser
```

here you can see the images and their status
```
docker-compose up
```
this will activate the servers

```
http://localhost:8000/admin
```
enter a couple of categories and a couple of products and you're done
## Built with ๐ ๏ธ


* [Docker] (https://docs.docker.com/compose/reference/run/)
* [Django] (https://www.djangoproject.com/)
* [python] (https://www.python.org/)


## Authors โ๏ธ


* ** Dimanso perez ** - * Initial Work * - [Dimaps716] (https://github.com/Dimaps716)


## License ๐

This project is under the License (Your License) - see the  (LICENSE.md) file for details

## Expressions of Gratitude ๐

* Tell others about this project ๐ข
* Invite a beer ๐บ or a coffee โ to someone on the team.
* Give thanks publicly ๐ค.




---
โจ๏ธ with โค๏ธ by [Dimaps716] (https://github.com/Dimaps716) ๐
