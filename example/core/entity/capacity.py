from dataclasses import dataclass


@dataclass
class Capacity:
    adsl: bool
    fibre: bool

    @property
    def has_adsl_capacity(self) -> bool:
        return self.adsl

    @property
    def has_fibre_capacity(self) -> bool:
        return self.fibre
