import pytest
from tienda import calcular_precio, calcular_iva

def test_integracion_precio_con_iva_try():
    """Prueba de integración para flujo exitoso"""
    precio_base = 200
    descuento = 10
    precio_con_desc = calcular_precio(precio_base, descuento) # 180
    total_con_iva = calcular_iva(precio_con_desc)
    
    assert total_con_iva == pytest.approx(208.8)

def test_integracion_descuento_invalido_exception():
    """Prueba de integración validando excepción esperada con pytest.raises"""
    precio_base = 100
    descuento_invalido = 150 
    
    with pytest.raises(ValueError, match="El descuento debe estar entre 0 y 100"):
        calcular_precio(precio_base, descuento_invalido)