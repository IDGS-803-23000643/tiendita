import pytest
from tienda import calcular_precio, calcular_iva

def test_integracion_precio_con_iva_try():
    """Prueba de integración usando try/except para flujo exitoso"""
    try:
        precio_base = 200
        descuento = 10
        precio_con_desc = calcular_precio(precio_base, descuento) # 180
        total_con_iva = calcular_iva(precio_con_desc)
        
        assert total_con_iva == 208.8
    except Exception as e:
        pytest.fail(f"La prueba de integración falló inesperadamente: {e}")

def test_integracion_descuento_invalido_exception():
    """Prueba de integración atrapando una excepción esperada"""
    try:
        precio_base = 100
        descuento_invalido = 150 
        
        calcular_precio(precio_base, descuento_invalido)
        pytest.fail("Se esperaba un ValueError pero la función no lanzó error.")
    
    except ValueError as ex:
        assert "El descuento debe estar entre 0 y 100" in str(ex)
    except Exception as e:
        pytest.fail(f"Se lanzó una excepción no prevista: {e}")