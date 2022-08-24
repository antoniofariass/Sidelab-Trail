#Na associação uma classe nao depende da outro, logo caso exclua, as outras classes continuaram

from classes import Escritor
from classes import Caneta
from classes import MaquinaDeEscrever

escritor = Escritor('Joãozinho')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta #associando escritor e caneta, no atributo ferramenta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina #associando escritor e maquina, no atributo ferramenta
escritor.ferramenta.escrever()