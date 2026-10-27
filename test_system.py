import pytest
from tienda import calcular_precio, calcular_iva

def test_sistema_flujo_compra_exitoso():
    """Prueba de sistema (Simula el flujo completo de una compra)"""
    try:
        subtotal = 500
        descuento = 20
        
        precio_rebajado = calcular_precio(subtotal, descuento)
        total_final = calcular_iva(precio_rebajado)
        
        assert precio_rebajado == 400.0
        assert total_final == 464.0
        print("Flujo de sistema ejecutado correctamente en el bloque try.")
        
    except Exception as e:
        pytest.fail(f"El sistema falló en el flujo normal: {e}")

def test_sistema_flujo_compra_con_error():
    """Prueba de sistema manejando excepciones ante entradas incorrectas"""
    try:
        calcular_precio(-50, 10)
    except ValueError:
        assert True 
    except Exception as e:
        pytest.fail(f"Ocurrió un error inesperado de sistema: {e}")