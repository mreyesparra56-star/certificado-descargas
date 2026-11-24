# Issues de Certificados para un Evento

El líder del equipo crea estos issues en GitHub (**Issues → New issue**), copiando el título y la descripción, y le asigna cada uno a un integrante (**Assignees**). Las etiquetas (**Labels**) ya vienen en GitHub.

Van del más fácil al más difícil. Equipo de 2: issues 1 a 4 · equipo de 3: 1 a 6 · equipo de 4: 1 a 6, más uno que propongan ustedes.

---

## 1. `docs: mejorar el README`
**Label:** `documentation`

Completar el README para que alguien que no conoce el proyecto lo entienda: qué problema resuelve, cómo se usa, una captura de un certificado y quiénes lo hicieron.

**Listo cuando:**
- [ ] El README explica qué hace y cómo se usa
- [ ] Tiene una captura de un certificado
- [ ] Tiene los nombres del equipo

---

## 2. `feat: cambiar el evento por uno nuestro`
**Label:** `good first issue`

El equipo escoge su evento: un torneo de videojuegos, un campeonato de microfútbol, una feria de emprendimiento, el que quieran. Cambiar el nombre del evento en la plantilla y los datos de `participantes.csv` (se puede editar en Excel o en VS Code). Mínimo 15 participantes.

**Listo cuando:**
- [ ] La plantilla tiene el nombre de nuestro evento
- [ ] El CSV tiene nuestros participantes, con roles y equipos
- [ ] Generé los certificados y se ven bien
- [ ] Actualicé el README con este cambio

---

## 3. `feat: diseñar nuestra plantilla`
**Label:** `enhancement`

Darle al certificado la identidad del evento: colores, tipografía, un logo o un emoji, el texto. Todo se cambia en `plantilla.html`, sin tocar el código Python.

**Pista:** las fuentes de Google Fonts se pueden usar con una línea `<link>` en el `<head>`.

**Listo cuando:**
- [ ] El certificado tiene un diseño propio del evento
- [ ] Se sigue viendo bien al imprimir (Ctrl + P)
- [ ] Actualicé el README con este cambio

---

## 4. `feat: color distinto según el rol`
**Label:** `enhancement`

Que el certificado cambie de color según el rol: oro para el primer lugar, plata para el segundo, bronce para el tercero y otro color para mentores y jurados. Los participantes quedan con el color normal.

**Pista:** agreguen en la plantilla un campo nuevo, por ejemplo `{{color}}`, y que el script decida qué color poner según el rol.

**Listo cuando:**
- [ ] Los primeros, segundos y terceros lugares tienen su color
- [ ] Mentores y jurados tienen otro color
- [ ] Actualicé el README con este cambio

---

## 5. `feat: código de verificación`
**Label:** `enhancement`

Los certificados reales traen un código para comprobar que no son falsos. Darle a cada certificado un código único, por ejemplo `HCK-2026-0007`, que aparezca en el certificado. Además, guardar en `verificacion.csv` el código, el nombre y el rol de cada persona.

**Listo cuando:**
- [ ] Cada certificado muestra su código, y no hay dos iguales
- [ ] Se crea `verificacion.csv` con código, nombre y rol
- [ ] Actualicé el README con este cambio

---

## 6. `fix: nombres con caracteres que rompen el archivo`
**Label:** `bug`

**Este es un error real del script:** el nombre de la persona se usa como nombre del archivo, y hay caracteres que no se pueden usar en un nombre de archivo, como `/`, `:` o `?`. Pruébalo: agrega al final de `participantes.csv` esta línea y ejecuta el script:
```
Kevin Ospina / K-Dev,Participante,Byte Club,App de turnos para barberías
```
El script se detiene con un error y no termina los certificados. Hay que limpiar el nombre del archivo, sin cambiar el nombre que sale en el certificado.

**Listo cuando:**
- [ ] Con la línea de Kevin, el script termina sin errores
- [ ] El certificado de Kevin muestra su nombre completo
- [ ] Explico en el PR cómo lo probé
- [ ] Actualicé el README con este cambio

---

## 7. (Equipos de 4) Su propia mejora
**Label:** `enhancement`

Propongan una mejora o una forma de aplicar los certificados a algo real: su proyecto formativo, un evento del SENA, su trabajo. Escriban el issue ustedes mismos, con su lista de **Listo cuando**, que incluya actualizar el README.
