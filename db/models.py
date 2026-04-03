from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = "db_genre"

    def __str__(self) -> str:
        return self.name


class Actor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        db_table = "db_actor"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="movies")
    genres = models.ManyToManyField(Genre, related_name="movies")

    class Meta:
        db_table = "db_movie"

    def __str__(self) -> str:
        return self.title


class CinemaHall(models.Model):
    name = models.CharField(max_length=255)
    rows = models.IntegerField()
    seats_in_row = models.IntegerField()

    class Meta:
        db_table = "db_cinemahall"

    @property
    def capacity(self) -> int:
        return self.rows * self.seats_in_row

    def __str__(self) -> str:
        return self.name


class MovieSession(models.Model):
    show_time = models.DateTimeField()
    cinema_hall = models.ForeignKey(
        CinemaHall,
        on_delete=models.CASCADE,
        related_name="movie_sessions"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="movie_sessions"
    )

    class Meta:
        db_table = "db_moviesession"

    def __str__(self) -> str:
        return (
            f"{self.movie.title} "
            f"{self.show_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )
