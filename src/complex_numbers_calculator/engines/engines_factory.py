from .octonion_engine import OctonionEngine
from .complex_number_engine import CompexNumberEngine

engines = {
    'octonion': OctonionEngine,
    'complex_number': CompexNumberEngine
}

def get_engine(engine_name: str) -> CompexNumberEngine:
    """
    Factory function to get the engine.
    
    :return: An instance of Engine.
    """
    try:
        return engines[engine_name.lower()]()
    except KeyError as e:
        raise ValueError(f"Engine '{engine_name}' is not supported.") from e
