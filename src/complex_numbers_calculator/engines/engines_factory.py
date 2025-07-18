from .octonion_engine import OctonionEngine
from .base_engine import BaseEngine

engines = {
    'octonion': OctonionEngine,
}

def get_engine(engine_name: str) -> BaseEngine:
    """
    Factory function to get the engine.
    
    :return: An instance of Engine.
    """
    try:
        return engines[engine_name.lower()]()
    except KeyError as e:
        raise ValueError(f"Engine '{engine_name}' is not supported.") from e
