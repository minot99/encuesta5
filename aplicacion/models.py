from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager    

class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')
        
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        
        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=150, unique=True, default='default_username')
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = UserManager()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    def has_module_perms(self, app_label):
        """
        Determine whether the user has permission to view the app_label module.

        Simplest possible answer: Yes, always.
        """
        return True

    def has_perm(self, perm, obj=None):
        """
        Determine whether the user has the given permission.

        Simplest possible answer: Yes, always.
        """
        return True

class Docente(models.Model):
    ACCESO_RECURSOS_CHOICES = [
        ('si', 'Sí'),
        ('no', 'No'),
    ]
    nombre = models.CharField(max_length=100, verbose_name="Nombre del docente", null=True)
    apellido = models.CharField(max_length=100, verbose_name="Apellido del docente", null=True)
    cedula = models.CharField(max_length=15, unique=True, verbose_name="Cédula del docente")
    telefono_oficina = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono de oficina del docente")
    telefono_personal = models.CharField(max_length=20, verbose_name="Teléfono personal del docente", null=True)
    correo_institucional = models.EmailField(verbose_name="Correo institucional del docente", null=True)
    porcentaje_planes_completados = models.CharField(max_length=6, null=True, choices=[
        ('0-24', '0 - 24%'),
        ('25-49', '25 - 49%'),
        ('50-74', '50 - 74%'),
        ('75-100', '75 - 100%')
    ], verbose_name="Porcentaje de planes completados")

    RANGO_ESTUDIANTES_CHOICES = [
        ('1-10', '1-10'),
        ('11-20', '11-20'),
        ('21-30', '21-30'),
        ('31+', '31+'),
    ]

    FRECUENCIA_HABLA_INGLES_CHOICES = [
        ('nunca', 'Nunca o Casi Nunca'),
        ('algunas_veces', 'Algunas veces'),
        ('muchas_veces', 'Muchas veces'),
        ('siempre', 'Siempre o Casi Siempre'),
    ]

    PORCENTAJE_TIEMPO_INGLES_CHOICES = [
        ('0-24', '0 - 24%'),
        ('25-49', '25 - 49%'),
        ('50-74', '50 - 74%'),
        ('75-100', '75 - 100%'),
    ]

    rango_estudiantes = models.CharField(max_length=5, null=True, choices=RANGO_ESTUDIANTES_CHOICES, verbose_name="Rango promedio de estudiantes por aula")
    frecuencia_habla_ingles = models.CharField(max_length=15, choices=FRECUENCIA_HABLA_INGLES_CHOICES, null=True, verbose_name="Frecuencia con la que habla inglés con sus estudiantes")
    porcentaje_tiempo_ingles = models.CharField(max_length=6, null=True, choices=PORCENTAJE_TIEMPO_INGLES_CHOICES, verbose_name="Porcentaje de tiempo de uso del inglés durante la clase")
    incentiva_hablar_ingles = models.CharField(max_length=15, null=True, choices=FRECUENCIA_HABLA_INGLES_CHOICES, verbose_name="Incentiva a sus estudiantes a hablar inglés")
    porcentaje_promueve_ingles = models.CharField(max_length=6, null=True, choices=PORCENTAJE_TIEMPO_INGLES_CHOICES, verbose_name="Porcentaje de tiempo que promueve el uso del inglés entre estudiantes")
    tiempo_dialogo_ingles = models.CharField(max_length=15, null=True, choices=FRECUENCIA_HABLA_INGLES_CHOICES, verbose_name="Frecuencia de diálogo en inglés con cada estudiante")
    tiempo_promedio_ingles = models.CharField(max_length=15, null=True, choices=FRECUENCIA_HABLA_INGLES_CHOICES, verbose_name="Tiempo promedio de uso del inglés durante la clase")

    senalizaciones_centro_ingles = models.CharField(max_length=2, null=True, choices=ACCESO_RECURSOS_CHOICES, default='no', verbose_name="Cooperación en PPB")
    cantidad_senalizaciones_centro = models.CharField(max_length=10, null=True, choices=[
        ('no_hay', 'No hay'),
        ('1-2', 'Hay 1 - 2'),
        ('3-4', 'Hay 3 - 4'),
        ('5_mas', 'Hay 5 o más')
    ], verbose_name="Cantidad de Señalizaciones en Inglés en su Centro Educativo")
    tipo_senaletica = models.JSONField(verbose_name="Tipo de señalizaciones en inglés ¿Dónde están desplegadas?", null=True)
    evidence = models.FileField(upload_to='evidencias/', null=True, verbose_name="Subir foto o video")
    senaletica_aula = models.CharField(max_length=2, null=True, choices=ACCESO_RECURSOS_CHOICES, default='no', verbose_name="Cooperación en PPB")
    cantidad_senalizaciones_aula = models.CharField(max_length=10, null=True, choices=[
        ('no_hay', 'No hay'),
        ('1-2', 'Hay 1 - 2'),
        ('3-4', 'Hay 3 - 4'),
        ('5_mas', 'Hay 5 o más')
    ], verbose_name="Cantidad de Señalizaciones en Inglés dentro del aula de clases")
    #porcentaje_tiempo = models.IntegerField(blank=True, null=True, verbose_name="¿Qué porcentaje del tiempo?")

    FRECUENCIA_CHOICES = [
        ('nunca', 'Nunca'),
        ('a_veces', 'A veces'),
        ('varias_veces', 'Varias veces'),
        ('siempre', 'Siempre o casi siempre'),
    ]

    evidence_file = models.FileField(upload_to='evidencias/', null=True, blank=True, verbose_name="Evidencia")
    musica = models.CharField(max_length=20, choices=[
        ('nunca-casi-nunca', 'Nunca o casi nunca'),
        ('a-veces', 'A veces'),
        ('varias-veces', 'Varias Veces'),
        ('siempre-casi-siempre', 'Siempre o casi siempre')
    ], default='nunca-casi-nunca', verbose_name="Música")
    teatro = models.CharField(max_length=20, choices=[
        ('nunca-casi-nunca', 'Nunca o casi nunca'),
        ('a-veces', 'A veces'),
        ('varias-veces', 'Varias Veces'),
        ('siempre-casi-siempre', 'Siempre o casi siempre')
    ], default='nunca-casi-nunca', verbose_name="Teatro")
    coreografia = models.CharField(max_length=20, choices=[
        ('nunca-casi-nunca', 'Nunca o casi nunca'),
        ('a-veces', 'A veces'),
        ('varias-veces', 'Varias Veces'),
        ('siempre-casi-siempre', 'Siempre o casi siempre')
    ], default='nunca-casi-nunca', verbose_name="Coreografía")

    frecuencia_interaccion_directivos = models.CharField(max_length=12, null=True, choices=FRECUENCIA_CHOICES, verbose_name="Frecuencia de interacción con directivos/administrativos en inglés")
    frecuencia_interaccion_docente = models.CharField(max_length=12, null=True, choices=FRECUENCIA_CHOICES, verbose_name="Frecuencia de interacción con otros docentes en inglés")
    frecuencia_interaccion_padres = models.CharField(max_length=12, null=True, choices=FRECUENCIA_CHOICES, verbose_name="Frecuencia de interacción con padres de familia en inglés")
    interactua_estudiantes = models.CharField(max_length=20, null=True, choices=FRECUENCIA_CHOICES, verbose_name="Interacción con estudiantes en inglés fuera de clase")
    actividades_ingles_fuera_clase = models.JSONField(verbose_name="Actividades en inglés fuera del aula", null=True)

    ANOS_EXPERIENCIA_CHOICES = [
        ('0', '0 (está en su primer año)'),
        ('1-3', '1-3'),
        ('4-6', '4-6'),
        ('7_mas', '7 o más'),
    ]

    SECTOR_EXPERIENCIA_CHOICES = [
        ('Oficial', 'Oficial'),
        ('Particular', 'Particular'),
        ('Ambos', 'Ambos'),
    ]

    NIVEL_INGLES_CHOICES = [
        ('A0', 'A0: Principiante'),
        ('A1-A2', 'A1 - A2: Básico'),
        ('A2-B1', 'A2 - B1: Pre-intermedio'),
        ('B1', 'B1: Intermedio'),
        ('B2', 'B2: Intermedio-Alto'),
        ('C1-C2', 'C1 - C2: Avanzado'),
    ]

    anos_experiencia = models.CharField(max_length=5, choices=ANOS_EXPERIENCIA_CHOICES, null=True, verbose_name="Años de experiencia en impartir clases")
    sector_experiencia = models.CharField(max_length=10, choices=SECTOR_EXPERIENCIA_CHOICES, verbose_name="Sector de experiencia", null=True)
    niveles_impartidos = models.JSONField(verbose_name="Niveles en los que ha impartido clases", null=True)
    nivel_actual = models.JSONField(verbose_name="Nivel actual en el que imparte clases", null=True)
    titulo_ensenanza = models.CharField(max_length=2, choices=ACCESO_RECURSOS_CHOICES, default='no', null=True, verbose_name="Cooperación en PPB")
    nivel_titulo = models.CharField(max_length=12, blank=True, verbose_name="Nivel del título", null=True)
    
    titulos_formales = models.JSONField(verbose_name="Títulos formales relacionados a la enseñanza del idioma inglés", null=True)
    licenciatura_ano = models.IntegerField(null=True, blank=True)
    postgrado_ano = models.IntegerField(null=True, blank=True)
    maestria_ano = models.IntegerField(null=True, blank=True)
    doctorado_ano = models.IntegerField(null=True, blank=True)
    
    cursos_educacion_continua = models.JSONField(verbose_name="Cursos de educación continua", null=True)
    certificacion_ingles = models.CharField(max_length=2, choices=ACCESO_RECURSOS_CHOICES, default='no', verbose_name="Cooperación en PPB", null=True)
    nivel_ingles_docente = models.CharField(max_length=6, choices=NIVEL_INGLES_CHOICES, blank=True, null=True, verbose_name="Nivel de inglés del docente")
    nivel_ingles_docente_no_certificado = models.CharField(max_length=6, choices=NIVEL_INGLES_CHOICES, blank=True, null=True, verbose_name="Nivel de inglés del docente (no certificado)")
    renovar_certificacion = models.CharField(max_length=2, choices=ACCESO_RECURSOS_CHOICES, default='no', null=True, verbose_name="¿Estaría dispuesto a tomar o renovar su certificación en inglés?")


    trimestre = models.CharField(max_length=20, default='')  # Ajusta según necesidad
    mes = models.CharField(max_length=20, default='')  # Ajusta según necesidad
    semana = models.CharField(max_length=20, default='')

    FRECUENCIA_RECURSOS_CHOICES = [
        ('nunca', 'Nunca o Casi Nunca'),
        ('algunas_veces', 'Algunas veces'),
        ('muchas_veces', 'Muchas veces'),
        ('siempre', 'Siempre o Casi Siempre'),
    ]

    

    ACUERDO_CHOICES = [
        ('muy_en_desacuerdo', 'Muy en desacuerdo'),
        ('desacuerdo', 'Desacuerdo'),
        ('de_acuerdo', 'De acuerdo'),
        ('muy_de_acuerdo', 'Muy de acuerdo'),
    ]

    frecuencia_uso_recursos = models.CharField(max_length=15, null=True, choices=FRECUENCIA_RECURSOS_CHOICES, verbose_name="Frecuencia de uso de recursos en la clase de inglés")
    acceso_recursos = models.CharField(max_length=2, choices=ACCESO_RECURSOS_CHOICES, verbose_name="Acceso a recursos para clases", null=True)
    importancia_formacion_bilingue = models.CharField(max_length=17, null=True, choices=ACUERDO_CHOICES, verbose_name="Interés de padres en formación bilingüe")
    valoracion_formacion_bilingue = models.CharField(max_length=17, null=True, choices=ACUERDO_CHOICES, verbose_name="Valoración de la formación bilingüe")
    prioridad_ppb = models.CharField(max_length=17, choices=ACUERDO_CHOICES, null=True, verbose_name="Prioridad del PPB")
    participacion_padres = models.CharField(max_length=17, choices=ACUERDO_CHOICES, null=True, verbose_name="Participación de padres en enseñanza")
    cooperacion_ppb = models.CharField(max_length=2, null=True, choices=ACCESO_RECURSOS_CHOICES, default='no', verbose_name="Cooperación en PPB")
    encargado_ppb = models.CharField(max_length=100, blank=True, null=True, verbose_name="Encargado de PPB")

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Coordinador(models.Model):
    # Formulario 1
    docentes_por_asignatura = models.PositiveIntegerField()
    participa_activamente_ppb = models.BooleanField()
    estudiantes_por_nivel_ppb = models.PositiveIntegerField()
    docentes_capacitados_ppb = models.PositiveIntegerField()
    docentes_aprobados_ppb = models.PositiveIntegerField()
    docentes_capacitacion_exterior = models.PositiveIntegerField()

    # Formulario 2
    codigos_plan_estudio = models.CharField(max_length=255)
    planes_estudio = models.CharField(max_length=255)
    asignaturas_ingles_en_plan = models.BooleanField()
    asignaturas_ingles_dictadas = models.BooleanField()
    planes_clase_contraste = models.TextField()
    horas_ingles = models.PositiveIntegerField()
    horas_teoricas = models.PositiveIntegerField()
    horas_practicas = models.PositiveIntegerField()

    # Formulario 3
    actividades_propio_centro = models.BooleanField()
    actividades_meduca_centro = models.BooleanField()
    actividades_externas_centro = models.BooleanField()
    detalle_actividades_anual = models.TextField()
    cantidad_estudiantes_actividades_externas = models.JSONField(default=dict)  # This can store grade-wise participation.

    # Formulario 4
    after_school_existencia = models.BooleanField()
    after_school_descripcion = models.TextField()
    after_school_participacion = models.JSONField(default=dict)  # Grade-wise participation.

    # Formulario 5
    tipo_senalizaciones_ingles = models.JSONField(default=list)
    senalizaciones_aula_ingles = models.BooleanField()
    cantidad_senalizaciones_aula = models.PositiveIntegerField()

    # Formulario 6
    interactua_directivos_ingles = models.PositiveIntegerField()
    interactua_docentes_ingles = models.PositiveIntegerField()
    interactua_padres_ingles = models.PositiveIntegerField()
    interactua_estudiantes_ingles = models.BooleanField()
    porcentaje_interaccion_estudiantes = models.PositiveIntegerField()
    actividades_ingles_fuera_aula = models.JSONField(default=list)
    frecuencia_actividades_ingles = models.CharField(max_length=20)

    def __str__(self):
        return f"Coordinador ID: {self.id}"

class Director(models.Model):
    nombre = models.CharField(max_length=100, default='N/A')
    apellido = models.CharField(max_length=100, default='N/A')
    cedula = models.CharField(max_length=20, default='N/A')
    telefono_oficina = models.CharField(max_length=20, default='N/A')
    telefono_personal = models.CharField(max_length=20, default='N/A')
    correo_institucional = models.EmailField(default='N/A@example.com')
    correo_personal1 = models.EmailField(default='N/A@example.com')
    correo_personal2 = models.EmailField(default='N/A@example.com')
    codigo_siace = models.CharField(max_length=100, default='N/A')
    nombre_centro_educativo = models.CharField(max_length=100, default='N/A')
    region_educativa = models.CharField(max_length=100, default='N/A')
    provincia = models.CharField(max_length=100, default='N/A')
    direccion = models.CharField(max_length=255, default='N/A')
    nivel_escolar = models.CharField(max_length=50, default='N/A')
    matricula_total = models.IntegerField(default=0)
    grado1 = models.IntegerField(default=0)
    femenino1 = models.IntegerField(default=0)
    masculino1 = models.IntegerField(default=0)
    grado2 = models.IntegerField(default=0)
    femenino2 = models.IntegerField(default=0)
    masculino2 = models.IntegerField(default=0)
    grado3 = models.IntegerField(default=0)
    femenino3 = models.IntegerField(default=0)
    masculino3 = models.IntegerField(default=0)
    grado4 = models.IntegerField(default=0)
    femenino4 = models.IntegerField(default=0)
    masculino4 = models.IntegerField(default=0)
    total_docentes = models.CharField(max_length=50, default='N/A')
    docentes1 = models.CharField(max_length=50, default='N/A')
    docentes2 = models.CharField(max_length=50, default='N/A')
    docentes3 = models.CharField(max_length=50, default='N/A')
    docentes4 = models.CharField(max_length=50, default='N/A')
    estudiantes_salon = models.CharField(max_length=50, default='N/A')
    docentes_asignatura = models.CharField(max_length=50, default='N/A')
    participa_ppb = models.BooleanField(default=False)
    estudiantes_nivel_ppb = models.CharField(max_length=20, default='N/A')
    docentes_capacitados_ppb = models.CharField(max_length=20, default='N/A')
    docentes_aprobados_ppb = models.CharField(max_length=20, default='N/A')
    docentes_capacitacion_exterior = models.CharField(max_length=20, default='N/A')
    codigos_plan_estudio = models.BooleanField(default=False)
    planes_estudio = models.BooleanField(default=False)
    asignaturas_ingles_plan_estudios = models.BooleanField(default=False)
    asignaturas_ingles_dictadas = models.BooleanField(default=False)
    planes_clase = models.CharField(max_length=20, default='N/A')
    horas_ingles = models.CharField(max_length=20, default='N/A')
    horas_teoricas = models.CharField(max_length=20, default='N/A')
    horas_practicas = models.CharField(max_length=20, default='N/A')
    actividades_propio_centro = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')
    cantidad_estudiantes_actividades_externas_1 = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')
    actividades_meduca_centro = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')
    cantidad_estudiantes_actividades_especiales_1 = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')
    actividades_externas_centro = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')
    cantidad_estudiantes_actividades_centro_1 = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')
    detalle_actividades_anual = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')
    after_school_existencia = models.CharField(max_length=2, choices=(
        ("no", "No"),
        ("si", "Sí"),
    ), default='Nunca o Casi Nunca')
    after_school_descripcion = models.CharField(max_length=2, choices=(
        ("no", "No"),
        ("si", "Sí"),
    ), default='Nunca o Casi Nunca')
    after_school_participacion_1 = models.CharField(max_length=50, choices=(
        ("Nunca o Casi Nunca", "Nunca o Casi Nunca"),
        ("Algunas veces", "Algunas veces"),
        ("Muchas veces", "Muchas veces"),
        ("Siempre o Casi Siempre", "Siempre o Casi Siempre"),
    ), default='Nunca o Casi Nunca')    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class CoordinadorTecnologia(models.Model):
    # Multimedia resources
    tiene_multimedia = models.BooleanField(default=False)
    materiales_multimedia = models.JSONField(default=list)
    cantidad_cd = models.IntegerField(default=0)
    cantidad_dvd = models.IntegerField(default=0)
    cantidad_mp4 = models.IntegerField(default=0)
    cantidad_streaming = models.IntegerField(default=0)
    cantidad_otros_multimedia = models.IntegerField(default=0)

    # English learning software details
    software_existencia = models.BooleanField(default=False)
    software_cantidad = models.IntegerField(default=0)
    software_listado = models.TextField(blank=True, null=True)
    software_licencia = models.BooleanField(default=False)
    software_internet_requerido = models.BooleanField(default=False)
    software_usuarios = models.IntegerField(default=0)

    # IT infrastructure
    existencia_laboratorios = models.BooleanField(default=False)
    cantidad_laboratorios = models.IntegerField(default=0)
    computadoras_por_laboratorio = models.IntegerField(default=0)
    marca_equipos = models.CharField(max_length=255, blank=True, null=True)
    ano_fabricacion = models.IntegerField(blank=True, null=True)
    computadoras_bocinas = models.BooleanField(default=False)
    computadoras_auriculares = models.BooleanField(default=False)
    computadoras_microfonos = models.BooleanField(default=False)
    computadoras_internet = models.BooleanField(default=False)

    # Internet and Wi-Fi infrastructure
    internet_existencia = models.BooleanField(default=False)
    tipo_enlace_internet = models.CharField(max_length=100, blank=True, null=True)
    ancho_banda = models.IntegerField(default=0)
    wifi_solucion_existencia = models.BooleanField(default=False)
    wifi_alcance = models.JSONField(default=list)
    wifi_cobertura_porcentaje = models.IntegerField(default=0)
    acceso_wifi_administrativos = models.BooleanField(default=False)
    acceso_wifi_docentes = models.BooleanField(default=False)
    acceso_wifi_estudiantes = models.BooleanField(default=False)
    percepcion_velocidad_internet = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"CoordinadorTecnologia ID: {self.id}"

class OtrosDocentes(models.Model):
    habla_ingles_otras_asignaturas = models.BooleanField(default=False)
    porcentaje_tiempo_ingles_otras = models.IntegerField()
    incentiva_hablar_ingles_otras = models.BooleanField(default=False)

    def __str__(self):
        return f"Docente: {self.id}"

class CoordinadorLengua(models.Model):
    # Formulario 1 - Recursos Multimedia
    presentaciones = models.IntegerField(default=0)
    simulaciones = models.IntegerField(default=0)
    juegos = models.IntegerField(default=0)
    objetos_aprendizaje = models.IntegerField(default=0)
    entornos_virtuales = models.IntegerField(default=0)
    cantidad_cd = models.IntegerField(default=0)
    cantidad_dvd = models.IntegerField(default=0)
    cantidad_mp4 = models.IntegerField(default=0)
    cantidad_streaming = models.IntegerField(default=0)
    cantidad_otros = models.IntegerField(default=0)

    # Formulario 2 - Materiales Fungibles
    fungibles_existencia = models.BooleanField(default=False)
    materiales_tipo_ubicacion = models.TextField(blank=True)
    materiales_inventario = models.TextField(blank=True)
    materiales_reposicion = models.CharField(max_length=255, blank=True)
    medios_compra = models.TextField(blank=True)

    def __str__(self):
        return f"Coordinador de Lengua: {self.id}"
    
class ESTER(models.Model):
    cantidad_cursos = models.IntegerField(default=0, help_text="Cantidad de cursos disponibles en ESTER")
    cantidad_ova = models.IntegerField(default=0, help_text="Cantidad de Objetos Virtuales de Aprendizaje (OVA) disponibles")
    cantidad_libros_ingles = models.IntegerField(default=0, help_text="Cantidad de libros en inglés disponibles")
    cantidad_audiolibros = models.IntegerField(default=0, help_text="Cantidad de audiolibros disponibles")
    cantidad_otros_recursos = models.IntegerField(default=0, help_text="Cantidad de otros recursos disponibles")

    acceso_ester_numero_2023_2024 = models.IntegerField(default=0, help_text="Número total de accesos de directores y docentes al Ecosistema ESTER durante 2023 y 2024")
    acceso_ester_porcentaje_2023_2024 = models.IntegerField(default=0, help_text="Porcentaje de acceso de directores y docentes al Ecosistema ESTER durante 2023 y 2024", validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return f"ESTER Recursos ID: {self.id}"