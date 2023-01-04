from infra.repository.filmes_repository import FilmesRepository

repo = FilmesRepository()

repo.insert('aladdin', 'fantasia', 1992)
repo.insert('mulan', 'fantasia', 1998)

data = repo.select()
print(data)

repo.delete('mulan')

data = repo.select()
print(data)