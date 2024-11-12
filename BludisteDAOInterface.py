from abc import ABC, abstractmethod

class BludisteDAOInterface(ABC):
    @abstractmethod
    def nacti_bludiste(self, cesta_k_souboru):
        pass
