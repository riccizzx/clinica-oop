
class Procedimento:
    def __init__(self, descricao: str, custo: float):
        self.__descricao = descricao
        self.__custo = custo

    @property
    def descricao(self):
        return self.__descricao

    @property
    def custo(self):
        return self.__custo

    @descricao.setter
    def descricao(self, descricao: str):
        self.__descricao = descricao

    @custo.setter
    def custo(self, custo: float):
        self.__custo = custo

    def calcular_custo(self) -> float:
        """Retorna o custo do procedimento."""
        return self.__custo
