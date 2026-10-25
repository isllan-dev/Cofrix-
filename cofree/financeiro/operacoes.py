from decimal import Decimal


def calcular_valor_guardado(saldo):
    return saldo * Decimal("0.50")


def calcular_valor_livre(saldo):
    return saldo * Decimal("0.30")


def calcular_valor_investimento(saldo):
    return saldo * Decimal("0.20")