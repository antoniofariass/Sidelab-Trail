from unittest import mock 
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.filmes import Filmes


session = UnifiedAlchemyMagicMock(
    data=[
    (
        [mock.call.query(Filmes),
        mock.call.filter(Filmes.genero == "MMM")
        ],
        [Filmes(titulo="Ola",genero="MMM",ano=12)]
    )
]
)

def test_select():
    response = session.query(Filmes).filter(Filmes.genero == "MMM").all()
    print()
    print(response)