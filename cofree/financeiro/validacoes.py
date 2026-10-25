import math
from decimal import Decimal,InvalidOperation


def validar_saldo_inicial(valor_informado):
    try:
        valor_informado = valor_informado.strip()
        valor_informado = valor_informado.replace(",", ".")
        valor_informado = Decimal(valor_informado)

    except InvalidOperation:
        return None

    if valor_informado < 0:
        return None

    if not math.isfinite (valor_informado):
        return None

    return valor_informado


