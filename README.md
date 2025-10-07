# FastMCP-Functions

Un servidor MCP (Model Context Protocol) implementado como Azure Functions para proporcionar herramientas personalizadas a sistemas de IA.

## 📋 Descripción

Este proyecto implementa un servidor MCP utilizando Azure Functions que permite a los sistemas de IA acceder a herramientas personalizadas a través de triggers genéricos. El servidor está configurado para manejar llamadas MCP mediante webhooks y runtime.

## 🛠️ Tecnologías

- **Azure Functions** - Plataforma serverless de Microsoft Azure
- **Python 3.12** - Lenguaje de programación principal
- **MCP (Model Context Protocol)** - Protocolo para la comunicación con sistemas de IA
- **JSON** - Formato de intercambio de datos

## 📁 Estructura del Proyecto

```
FastMCP-Functions/
├── function_app.py          # Función principal con triggers MCP
├── host.json               # Configuración del host de Azure Functions
├── local.settings.json     # Configuración local para desarrollo
├── requirements.txt        # Dependencias de Python
└── README.md              # Este archivo
```

## 🚀 Configuración y Deployment

### Prerrequisitos

- Python 3.12 o superior
- Azure Functions Core Tools
- Una cuenta de Azure
- Visual Studio Code (recomendado)

### Instalación Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/SebastianGodoy-CG/FastMCP-Functions.git
   cd FastMCP-Functions
   ```

2. **Crear un entorno virtual:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # En Windows
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar variables de entorno:**
   - Edita `local.settings.json` según tus necesidades
   - Para producción, configura las variables en Azure Portal

### Ejecutar Localmente

```bash
func host start
```

O usando la tarea de VS Code: `func: host start`

### Deployment a Azure

1. **Crear una Function App en Azure:**
   ```bash
   az functionapp create --resource-group <resource-group> --consumption-plan-location <location> --runtime python --runtime-version 3.12 --functions-version 4 --name <app-name> --storage-account <storage-account>
   ```

2. **Deployar el código:**
   ```bash
   func azure functionapp publish <app-name>
   ```

## 🔧 Configuración

### host.json

El archivo `host.json` contiene la configuración del servidor MCP:

```json
{
  "version": "2.0",
  "extensions": {
    "mcp": {
      "instructions": "Servidor MCP para ...",
      "serverName": "name_mcp",
      "serverVersion": "2.0.0",
      "messageOptions": {
        "useAbsoluteUriForEndpoint": false
      }
    }
  }
}
```

### local.settings.json

Configuración local para desarrollo:

```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "python"
  }
}
```

## 📝 Uso

### Estructura de Tools

El proyecto incluye una clase `ToolProperty` para definir las propiedades de las herramientas MCP:

```python
class ToolProperty:
    def __init__(self, property_name: str, property_type: str, description: str):
        self.propertyName = property_name
        self.propertyType = property_type
        self.description = description
```

### Ejemplo de Tool

```python
tool_properties_name = [
    ToolProperty("checkIn", "string", "Fecha de entrada en formato 'YYYY-MM-DD'."),
    ToolProperty("checkOut", "string", "Fecha de salida en formato 'YYYY-MM-DD'."),
]

@app.generic_trigger(
    arg_name="context",
    type="mcpToolTrigger",
    toolName="name_aca",
    description="Descripcion completa del tool",
    toolProperties=tool_properties_name_json,
)
def name_function(context) -> str:
    return json.dumps({"message": "MCP template funcionando"})
```

### Personalización

Para agregar nuevas herramientas:

1. Define las propiedades usando `ToolProperty`
2. Convierte las propiedades a JSON
3. Crea una nueva función con el decorador `@app.generic_trigger`
4. Implementa la lógica de tu herramienta

## 🔍 Testing

Para probar las funciones localmente:

1. Inicia el servidor local: `func host start`
2. La función estará disponible en: `http://localhost:7071/runtime/webhook/mpc?code=<system>`
3. Realiza peticiones HTTP para probar el comportamiento

## 📚 Recursos Adicionales

- [Documentación de Azure Functions](https://docs.microsoft.com/en-us/azure/azure-functions/)
- [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)
- [Azure Functions Python Developer Guide](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)

## 🤝 Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Sebastian Godoy** - [@SebastianGodoy-CG](https://github.com/SebastianGodoy-CG)

---

⭐ ¡No olvides dar una estrella al proyecto si te fue útil!