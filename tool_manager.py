import importlib
import pkgutil
import tools

def load_tools():
    registry = {}
    for loader, name, _ in pkgutil.iter_modules(tools.__path__):
        module = importlib.import_module(f"tools.{name}")
        if hasattr(module, "run"):
            registry[name] = {
                "run": module.run,
                "name": getattr(module, "TOOL_NAME", name),
                "desc": getattr(module, "TOOL_DESC", "Kein Beschreibungstext")
            }
    return registry