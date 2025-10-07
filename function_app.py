import azure.functions as func
import json
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

# Clase para definir propiedades de tools
class ToolProperty:
    def __init__(self, property_name: str, property_type: str, description: str):
        self.propertyName = property_name
        self.propertyType = property_type
        self.description = description

    def to_dict(self):
        return {
            "propertyName": self.propertyName,
            "propertyType": self.propertyType,
            "description": self.description,
        }

# Definición de propiedades del tool usando ToolProperty
tool_properties_name = [
    ToolProperty("checkIn", "string", "Fecha de entrada en formato 'YYYY-MM-DD'."),
    ToolProperty("checkOut", "string", "Fecha de salida en formato 'YYYY-MM-DD'."),
]

tool_properties_name_json = json.dumps([tp.to_dict() for tp in tool_properties_name])

# Trigger generico para ejecutar llamados MCP via runtime/webhook
@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="name_aca",
    description="""
    Descripcion completa del tool
    """,
    toolProperties=tool_properties_name_json,
)
def name_function(context) -> str:
    """
    Descripcion completa de la funcion
    """
    return json.dumps({"message": f"MCP template funcionando"})