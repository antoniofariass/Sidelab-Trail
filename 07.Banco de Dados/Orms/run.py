from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import AtoresRepository


""" repo = FilmesRepository()

repo.insert('aladdin2', 'fantasia', 1992)
repo.insert('mulan', 'fantasia', 1998)

data = repo.select()
print(data)

repo.delete('mulan')

data = repo.select()
print(data) """

repo = AtoresRepository()
response = repo.select()
print(response)

repo2 = FilmesRepository()
response2 = repo2.select()
filme= response2[0]
print(filme)

