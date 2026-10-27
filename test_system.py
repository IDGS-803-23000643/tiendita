import pytest
from tienda import calcular_precio, calcular_iva

def test_sistema_flujo_compra_exitoso():
    """Prueba de sistema (Simula el flujo completo de una compra)"""
    subtotal = 500
    descuento = 20
    
    precio_rebajado = calcular_precio(subtotal, descuento)
    total_final = calcular_iva(precio_rebajado)
    
    assert precio_rebajado == 400.0
    assert total_final == pytest.approx(464.0)

def test_sistema_flujo_compra_con_error():
    """Prueba de sistema manejando excepciones ante entradas incorrectas"""
    with pytest.raises(ValueError):
        calcular_precio(-50, 10)