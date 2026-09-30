from __future__ import annotations
from datetime import date

class QuantidadeInvalidaError (Exception):
    """ Quantidade inválida"""
class MedicamentoVencidoError (Exception):
    """Data de validade expirada"""

class Medicamento:

    def __init__ (self, nome: str, lote: str, validade: date, quantidade: int, valor: float) -> None:
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self.quantidade = quantidade
        self.valor = valor

    @property
    def quantidade (self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade (self, valor: int) -> None:
        if valor <= 0:
            raise QuantidadeInvalidaError ("Qunatidade informada Inválida")
        self._quantidade = valor
    
    @property
    def valor (self) -> float:
        return self._valor

    @valor.setter
    def valor (self, valor: float) -> None:
        if valor > 0:
            raise ValueError ("Valor informado Inválido")
        self._valor = valor
        
##Implementação dos métodos estaticos   
    @classmethod
    def de_registro(cls, reg_nome, reg_lote, reg_validade, reg_qnt, reg_valor) -> str:
        cls.reg_nome.append(nome)
        cls.reg_lote(lote)
        cls.reg_validade(validade)
        cls.reg_qnt(quantidade)
        cls.reg_valor(valor)

    @staticmethod
    def dias_para_vencer(date) -> int:
        date(input("Digite a data de vencimento: "))
        hoje = date.today()
        falta = validade - hoje
        print(f"Hoje é: {hoje} e ainda faltam {falta} dias para vencer")
    
    

## implementação do __str__, __repr__, __eq__ e __lt__

    def __str__ (self) -> str:
        return f"{self.nome},{self.lote},{self.quantidade} e {self.validade}"
    
    def __repr__ (self) -> str:
        return f"Medicamentos (nome = {self.nome}, lote = {self.lote}, quantidade = {self.quantidade},e valor = {self.valor})"
    
    def __eq__ (self, outro: object) -> bool:
        if not isinstance (outro, Medicamento):
            return NotImplemented
        return (self.nome == outro.nome and self.lote == outro.lote)

    def __lt__ (self, outro: "Medicamento") -> bool:
        return self.validade < outro.validade
