**Servicio de Usuarios y Ubicaciones**

### **Descripción**
Este microservicio se encarga de gestionar el registro de usuarios y su asociación con ubicaciones geográficas específicas. Utiliza tecnología de geofencing para validar que los usuarios se encuentren dentro de sectores predefinidos, garantizando una relación precisa entre usuarios y ubicaciones. Este servicio es una pieza clave para sistemas de notificaciones y alertas personalizadas basadas en la localización.

### **Responsable**
**Nombre:** Jaime Mendoza y Alyce Maldonado  
**Rol:** Desarrolladores principales del microservicio de usuarios y ubicaciones.

### **Objetivo**
El objetivo de este microservicio es permitir que los usuarios se registren y asocien sus datos personales con una ubicación validada, asegurando la gestión efectiva de notificaciones y alertas personalizadas en base a su ubicación geográfica.

### **Funcionalidad**
1. **Registro de Usuarios:**  
   - Los usuarios pueden registrarse proporcionando su información personal y seleccionando su ubicación en un mapa interactivo.  
2. **Validación de Ubicación mediante Geofencing:**  
   - Se utiliza geofencing para validar que la ubicación seleccionada pertenece a un sector definido dentro del sistema.  
3. **Gestión de Notificaciones:**  
   - Las ubicaciones validadas permiten enviar notificaciones relevantes basadas en la geolocalización del usuario.  
4. **Reportes de Cortes:**  
   - Los usuarios registrados pueden reportar cortes de servicios (agua, luz, etc.) especificando el tipo de corte y el sector afectado.  

### **Clases y Métodos**
#### **Usuario**
- **reportarCorte(tipo: String, sector: Sector): void**  
  Permite al usuario reportar cortes de servicios indicando el tipo y el sector afectado.  

- **recibirNotificacion(mensaje: String): void**  
  Recibe notificaciones relevantes relacionadas con su sector.

#### **Ubicacion**
- **geolocalizacion(tipo: String, sector: Sector): void**  
  Valida que la ubicación proporcionada pertenece a un sector predefinido.  

#### **Sector**
- Representa un área geográfica predefinida utilizada para validar usuarios y gestionar notificaciones.

### **Flujo del Servicio**
1. El usuario se registra proporcionando datos personales.  
2. Selecciona su ubicación mediante un mapa interactivo.  
3. El sistema valida la ubicación utilizando geofencing para asegurarse de que pertenece a un sector definido.  
4. La información del usuario se almacena en una base de datos para:  
   - Gestionar la recepción de notificaciones.  
   - Validar reportes de cortes en base a su ubicación.