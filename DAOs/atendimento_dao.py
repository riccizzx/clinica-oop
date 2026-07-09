from DAOs.dao import DAO
from model.atendimento import Atendimento

class AtendimentoDAO(DAO):
    def __init__(self):
        super().__init__('atendimentos.pkl')

    def add(self, atendimento: Atendimento, id_atendimento: int):
        if (atendimento is not None) and isinstance(atendimento, Atendimento):
            super().add(id_atendimento, atendimento)

    def update(self, atendimento: Atendimento, id_atendimento: int):
        if (atendimento is not None) and isinstance(atendimento, Atendimento):
            super().update(id_atendimento, atendimento)

    def get(self, key: int):
        return super().get(key)

    def remove(self, key: int):
        return super().remove(key)
        
    def get_all(self):
        return super().get_all()
