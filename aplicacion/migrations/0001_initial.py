# Generated by Django 4.2.3 on 2024-04-28 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('username', models.CharField(default='default_username', max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Coordinador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docentes_por_asignatura', models.PositiveIntegerField()),
                ('participa_activamente_ppb', models.BooleanField()),
                ('estudiantes_por_nivel_ppb', models.PositiveIntegerField()),
                ('docentes_capacitados_ppb', models.PositiveIntegerField()),
                ('docentes_aprobados_ppb', models.PositiveIntegerField()),
                ('docentes_capacitacion_exterior', models.PositiveIntegerField()),
                ('codigos_plan_estudio', models.CharField(max_length=255)),
                ('planes_estudio', models.CharField(max_length=255)),
                ('asignaturas_ingles_en_plan', models.BooleanField()),
                ('asignaturas_ingles_dictadas', models.BooleanField()),
                ('planes_clase_contraste', models.TextField()),
                ('horas_ingles', models.PositiveIntegerField()),
                ('horas_teoricas', models.PositiveIntegerField()),
                ('horas_practicas', models.PositiveIntegerField()),
                ('actividades_propio_centro', models.BooleanField()),
                ('actividades_meduca_centro', models.BooleanField()),
                ('actividades_externas_centro', models.BooleanField()),
                ('detalle_actividades_anual', models.TextField()),
                ('cantidad_estudiantes_actividades_externas', models.JSONField(default=dict)),
                ('after_school_existencia', models.BooleanField()),
                ('after_school_descripcion', models.TextField()),
                ('after_school_participacion', models.JSONField(default=dict)),
                ('tipo_senalizaciones_ingles', models.JSONField(default=list)),
                ('senalizaciones_aula_ingles', models.BooleanField()),
                ('cantidad_senalizaciones_aula', models.PositiveIntegerField()),
                ('interactua_directivos_ingles', models.PositiveIntegerField()),
                ('interactua_docentes_ingles', models.PositiveIntegerField()),
                ('interactua_padres_ingles', models.PositiveIntegerField()),
                ('interactua_estudiantes_ingles', models.BooleanField()),
                ('porcentaje_interaccion_estudiantes', models.PositiveIntegerField()),
                ('actividades_ingles_fuera_aula', models.JSONField(default=list)),
                ('frecuencia_actividades_ingles', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='CoordinadorLengua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('presentaciones', models.IntegerField(default=0)),
                ('simulaciones', models.IntegerField(default=0)),
                ('juegos', models.IntegerField(default=0)),
                ('objetos_aprendizaje', models.IntegerField(default=0)),
                ('entornos_virtuales', models.IntegerField(default=0)),
                ('cantidad_cd', models.IntegerField(default=0)),
                ('cantidad_dvd', models.IntegerField(default=0)),
                ('cantidad_mp4', models.IntegerField(default=0)),
                ('cantidad_streaming', models.IntegerField(default=0)),
                ('cantidad_otros', models.IntegerField(default=0)),
                ('fungibles_existencia', models.BooleanField(default=False)),
                ('materiales_tipo_ubicacion', models.TextField(blank=True)),
                ('materiales_inventario', models.TextField(blank=True)),
                ('materiales_reposicion', models.CharField(blank=True, max_length=255)),
                ('medios_compra', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CoordinadorTecnologia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiene_multimedia', models.BooleanField(default=False)),
                ('materiales_multimedia', models.JSONField(default=list)),
                ('cantidad_cd', models.IntegerField(default=0)),
                ('cantidad_dvd', models.IntegerField(default=0)),
                ('cantidad_mp4', models.IntegerField(default=0)),
                ('cantidad_streaming', models.IntegerField(default=0)),
                ('cantidad_otros_multimedia', models.IntegerField(default=0)),
                ('software_existencia', models.BooleanField(default=False)),
                ('software_cantidad', models.IntegerField(default=0)),
                ('software_listado', models.TextField(blank=True, null=True)),
                ('software_licencia', models.BooleanField(default=False)),
                ('software_internet_requerido', models.BooleanField(default=False)),
                ('software_usuarios', models.IntegerField(default=0)),
                ('existencia_laboratorios', models.BooleanField(default=False)),
                ('cantidad_laboratorios', models.IntegerField(default=0)),
                ('computadoras_por_laboratorio', models.IntegerField(default=0)),
                ('marca_equipos', models.CharField(blank=True, max_length=255, null=True)),
                ('ano_fabricacion', models.IntegerField(blank=True, null=True)),
                ('computadoras_bocinas', models.BooleanField(default=False)),
                ('computadoras_auriculares', models.BooleanField(default=False)),
                ('computadoras_microfonos', models.BooleanField(default=False)),
                ('computadoras_internet', models.BooleanField(default=False)),
                ('internet_existencia', models.BooleanField(default=False)),
                ('tipo_enlace_internet', models.CharField(blank=True, max_length=100, null=True)),
                ('ancho_banda', models.IntegerField(default=0)),
                ('wifi_solucion_existencia', models.BooleanField(default=False)),
                ('wifi_alcance', models.JSONField(default=list)),
                ('wifi_cobertura_porcentaje', models.IntegerField(default=0)),
                ('acceso_wifi_administrativos', models.BooleanField(default=False)),
                ('acceso_wifi_docentes', models.BooleanField(default=False)),
                ('acceso_wifi_estudiantes', models.BooleanField(default=False)),
                ('percepcion_velocidad_internet', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='N/A', max_length=100)),
                ('apellido', models.CharField(default='N/A', max_length=100)),
                ('cedula', models.CharField(default='N/A', max_length=20)),
                ('telefono_oficina', models.CharField(default='N/A', max_length=20)),
                ('telefono_personal', models.CharField(default='N/A', max_length=20)),
                ('correo_institucional', models.EmailField(default='N/A@example.com', max_length=254)),
                ('correo_personal1', models.EmailField(default='N/A@example.com', max_length=254)),
                ('correo_personal2', models.EmailField(default='N/A@example.com', max_length=254)),
                ('codigo_siace', models.CharField(default='N/A', max_length=100)),
                ('nombre_centro_educativo', models.CharField(default='N/A', max_length=100)),
                ('region_educativa', models.CharField(default='N/A', max_length=100)),
                ('provincia', models.CharField(default='N/A', max_length=100)),
                ('direccion', models.CharField(default='N/A', max_length=255)),
                ('nivel_escolar', models.CharField(default='N/A', max_length=50)),
                ('matricula_total', models.IntegerField(default=0)),
                ('grado1', models.IntegerField(default=0)),
                ('femenino1', models.IntegerField(default=0)),
                ('masculino1', models.IntegerField(default=0)),
                ('grado2', models.IntegerField(default=0)),
                ('femenino2', models.IntegerField(default=0)),
                ('masculino2', models.IntegerField(default=0)),
                ('grado3', models.IntegerField(default=0)),
                ('femenino3', models.IntegerField(default=0)),
                ('masculino3', models.IntegerField(default=0)),
                ('grado4', models.IntegerField(default=0)),
                ('femenino4', models.IntegerField(default=0)),
                ('masculino4', models.IntegerField(default=0)),
                ('total_docentes', models.CharField(default='N/A', max_length=50)),
                ('docentes1', models.CharField(default='N/A', max_length=50)),
                ('docentes2', models.CharField(default='N/A', max_length=50)),
                ('docentes3', models.CharField(default='N/A', max_length=50)),
                ('docentes4', models.CharField(default='N/A', max_length=50)),
                ('estudiantes_salon', models.CharField(default='N/A', max_length=50)),
                ('docentes_asignatura', models.CharField(default='N/A', max_length=50)),
                ('participa_ppb', models.BooleanField(default=False)),
                ('estudiantes_nivel_ppb', models.CharField(default='N/A', max_length=20)),
                ('docentes_capacitados_ppb', models.CharField(default='N/A', max_length=20)),
                ('docentes_aprobados_ppb', models.CharField(default='N/A', max_length=20)),
                ('docentes_capacitacion_exterior', models.CharField(default='N/A', max_length=20)),
                ('codigos_plan_estudio', models.BooleanField(default=False)),
                ('planes_estudio', models.BooleanField(default=False)),
                ('asignaturas_ingles_plan_estudios', models.BooleanField(default=False)),
                ('asignaturas_ingles_dictadas', models.BooleanField(default=False)),
                ('planes_clase', models.CharField(default='N/A', max_length=20)),
                ('horas_ingles', models.CharField(default='N/A', max_length=20)),
                ('horas_teoricas', models.CharField(default='N/A', max_length=20)),
                ('horas_practicas', models.CharField(default='N/A', max_length=20)),
                ('actividades_propio_centro', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
                ('cantidad_estudiantes_actividades_externas_1', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
                ('actividades_meduca_centro', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
                ('cantidad_estudiantes_actividades_especiales_1', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
                ('actividades_externas_centro', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
                ('cantidad_estudiantes_actividades_centro_1', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
                ('detalle_actividades_anual', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
                ('after_school_existencia', models.CharField(choices=[('no', 'No'), ('si', 'Sí')], default='Nunca o Casi Nunca', max_length=2)),
                ('after_school_descripcion', models.CharField(choices=[('no', 'No'), ('si', 'Sí')], default='Nunca o Casi Nunca', max_length=2)),
                ('after_school_participacion_1', models.CharField(choices=[('Nunca o Casi Nunca', 'Nunca o Casi Nunca'), ('Algunas veces', 'Algunas veces'), ('Muchas veces', 'Muchas veces'), ('Siempre o Casi Siempre', 'Siempre o Casi Siempre')], default='Nunca o Casi Nunca', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre del docente')),
                ('apellido', models.CharField(max_length=100, null=True, verbose_name='Apellido del docente')),
                ('cedula', models.CharField(max_length=15, unique=True, verbose_name='Cédula del docente')),
                ('telefono_oficina', models.CharField(blank=True, max_length=20, null=True, verbose_name='Teléfono de oficina del docente')),
                ('telefono_personal', models.CharField(max_length=20, null=True, verbose_name='Teléfono personal del docente')),
                ('correo_institucional', models.EmailField(max_length=254, null=True, verbose_name='Correo institucional del docente')),
                ('porcentaje_planes_completados', models.CharField(choices=[('0-24', '0 - 24%'), ('25-49', '25 - 49%'), ('50-74', '50 - 74%'), ('75-100', '75 - 100%')], max_length=6, null=True, verbose_name='Porcentaje de planes completados')),
                ('rango_estudiantes', models.CharField(choices=[('1-10', '1-10'), ('11-20', '11-20'), ('21-30', '21-30'), ('31+', '31+')], max_length=5, null=True, verbose_name='Rango promedio de estudiantes por aula')),
                ('frecuencia_habla_ingles', models.CharField(choices=[('nunca', 'Nunca o Casi Nunca'), ('algunas_veces', 'Algunas veces'), ('muchas_veces', 'Muchas veces'), ('siempre', 'Siempre o Casi Siempre')], max_length=15, null=True, verbose_name='Frecuencia con la que habla inglés con sus estudiantes')),
                ('porcentaje_tiempo_ingles', models.CharField(choices=[('0-24', '0 - 24%'), ('25-49', '25 - 49%'), ('50-74', '50 - 74%'), ('75-100', '75 - 100%')], max_length=6, null=True, verbose_name='Porcentaje de tiempo de uso del inglés durante la clase')),
                ('incentiva_hablar_ingles', models.CharField(choices=[('nunca', 'Nunca o Casi Nunca'), ('algunas_veces', 'Algunas veces'), ('muchas_veces', 'Muchas veces'), ('siempre', 'Siempre o Casi Siempre')], max_length=15, null=True, verbose_name='Incentiva a sus estudiantes a hablar inglés')),
                ('porcentaje_promueve_ingles', models.CharField(choices=[('0-24', '0 - 24%'), ('25-49', '25 - 49%'), ('50-74', '50 - 74%'), ('75-100', '75 - 100%')], max_length=6, null=True, verbose_name='Porcentaje de tiempo que promueve el uso del inglés entre estudiantes')),
                ('tiempo_dialogo_ingles', models.CharField(choices=[('nunca', 'Nunca o Casi Nunca'), ('algunas_veces', 'Algunas veces'), ('muchas_veces', 'Muchas veces'), ('siempre', 'Siempre o Casi Siempre')], max_length=15, null=True, verbose_name='Frecuencia de diálogo en inglés con cada estudiante')),
                ('tiempo_promedio_ingles', models.CharField(choices=[('nunca', 'Nunca o Casi Nunca'), ('algunas_veces', 'Algunas veces'), ('muchas_veces', 'Muchas veces'), ('siempre', 'Siempre o Casi Siempre')], max_length=15, null=True, verbose_name='Tiempo promedio de uso del inglés durante la clase')),
                ('senalizaciones_centro_ingles', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=2, null=True, verbose_name='Cooperación en PPB')),
                ('cantidad_senalizaciones_centro', models.CharField(choices=[('no_hay', 'No hay'), ('1-2', 'Hay 1 - 2'), ('3-4', 'Hay 3 - 4'), ('5_mas', 'Hay 5 o más')], max_length=10, null=True, verbose_name='Cantidad de Señalizaciones en Inglés en su Centro Educativo')),
                ('tipo_senaletica', models.JSONField(null=True, verbose_name='Tipo de señalizaciones en inglés ¿Dónde están desplegadas?')),
                ('evidence', models.FileField(null=True, upload_to='evidencias/', verbose_name='Subir foto o video')),
                ('senaletica_aula', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=2, null=True, verbose_name='Cooperación en PPB')),
                ('cantidad_senalizaciones_aula', models.CharField(choices=[('no_hay', 'No hay'), ('1-2', 'Hay 1 - 2'), ('3-4', 'Hay 3 - 4'), ('5_mas', 'Hay 5 o más')], max_length=10, null=True, verbose_name='Cantidad de Señalizaciones en Inglés dentro del aula de clases')),
                ('evidence_file', models.FileField(blank=True, null=True, upload_to='evidencias/', verbose_name='Evidencia')),
                ('musica', models.CharField(choices=[('nunca-casi-nunca', 'Nunca o casi nunca'), ('a-veces', 'A veces'), ('varias-veces', 'Varias Veces'), ('siempre-casi-siempre', 'Siempre o casi siempre')], default='nunca-casi-nunca', max_length=20, verbose_name='Música')),
                ('teatro', models.CharField(choices=[('nunca-casi-nunca', 'Nunca o casi nunca'), ('a-veces', 'A veces'), ('varias-veces', 'Varias Veces'), ('siempre-casi-siempre', 'Siempre o casi siempre')], default='nunca-casi-nunca', max_length=20, verbose_name='Teatro')),
                ('coreografia', models.CharField(choices=[('nunca-casi-nunca', 'Nunca o casi nunca'), ('a-veces', 'A veces'), ('varias-veces', 'Varias Veces'), ('siempre-casi-siempre', 'Siempre o casi siempre')], default='nunca-casi-nunca', max_length=20, verbose_name='Coreografía')),
                ('frecuencia_interaccion_directivos', models.CharField(choices=[('nunca', 'Nunca'), ('a_veces', 'A veces'), ('varias_veces', 'Varias veces'), ('siempre', 'Siempre o casi siempre')], max_length=12, null=True, verbose_name='Frecuencia de interacción con directivos/administrativos en inglés')),
                ('frecuencia_interaccion_docente', models.CharField(choices=[('nunca', 'Nunca'), ('a_veces', 'A veces'), ('varias_veces', 'Varias veces'), ('siempre', 'Siempre o casi siempre')], max_length=12, null=True, verbose_name='Frecuencia de interacción con otros docentes en inglés')),
                ('frecuencia_interaccion_padres', models.CharField(choices=[('nunca', 'Nunca'), ('a_veces', 'A veces'), ('varias_veces', 'Varias veces'), ('siempre', 'Siempre o casi siempre')], max_length=12, null=True, verbose_name='Frecuencia de interacción con padres de familia en inglés')),
                ('interactua_estudiantes', models.CharField(choices=[('nunca', 'Nunca'), ('a_veces', 'A veces'), ('varias_veces', 'Varias veces'), ('siempre', 'Siempre o casi siempre')], max_length=20, null=True, verbose_name='Interacción con estudiantes en inglés fuera de clase')),
                ('actividades_ingles_fuera_clase', models.JSONField(null=True, verbose_name='Actividades en inglés fuera del aula')),
                ('anos_experiencia', models.CharField(choices=[('0', '0 (está en su primer año)'), ('1-3', '1-3'), ('4-6', '4-6'), ('7_mas', '7 o más')], max_length=5, null=True, verbose_name='Años de experiencia en impartir clases')),
                ('sector_experiencia', models.CharField(choices=[('Oficial', 'Oficial'), ('Particular', 'Particular'), ('Ambos', 'Ambos')], max_length=10, null=True, verbose_name='Sector de experiencia')),
                ('niveles_impartidos', models.JSONField(null=True, verbose_name='Niveles en los que ha impartido clases')),
                ('nivel_actual', models.JSONField(null=True, verbose_name='Nivel actual en el que imparte clases')),
                ('titulo_ensenanza', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=2, null=True, verbose_name='Cooperación en PPB')),
                ('nivel_titulo', models.CharField(blank=True, max_length=12, null=True, verbose_name='Nivel del título')),
                ('titulos_formales', models.JSONField(null=True, verbose_name='Títulos formales relacionados a la enseñanza del idioma inglés')),
                ('licenciatura_ano', models.IntegerField(blank=True, null=True)),
                ('postgrado_ano', models.IntegerField(blank=True, null=True)),
                ('maestria_ano', models.IntegerField(blank=True, null=True)),
                ('doctorado_ano', models.IntegerField(blank=True, null=True)),
                ('cursos_educacion_continua', models.JSONField(null=True, verbose_name='Cursos de educación continua')),
                ('certificacion_ingles', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=2, null=True, verbose_name='Cooperación en PPB')),
                ('nivel_ingles_docente', models.CharField(blank=True, choices=[('A0', 'A0: Principiante'), ('A1-A2', 'A1 - A2: Básico'), ('A2-B1', 'A2 - B1: Pre-intermedio'), ('B1', 'B1: Intermedio'), ('B2', 'B2: Intermedio-Alto'), ('C1-C2', 'C1 - C2: Avanzado')], max_length=6, null=True, verbose_name='Nivel de inglés del docente')),
                ('nivel_ingles_docente_no_certificado', models.CharField(blank=True, choices=[('A0', 'A0: Principiante'), ('A1-A2', 'A1 - A2: Básico'), ('A2-B1', 'A2 - B1: Pre-intermedio'), ('B1', 'B1: Intermedio'), ('B2', 'B2: Intermedio-Alto'), ('C1-C2', 'C1 - C2: Avanzado')], max_length=6, null=True, verbose_name='Nivel de inglés del docente (no certificado)')),
                ('renovar_certificacion', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=2, null=True, verbose_name='¿Estaría dispuesto a tomar o renovar su certificación en inglés?')),
                ('trimestre', models.CharField(default='', max_length=20)),
                ('mes', models.CharField(default='', max_length=20)),
                ('semana', models.CharField(default='', max_length=20)),
                ('frecuencia_uso_recursos', models.CharField(choices=[('nunca', 'Nunca o Casi Nunca'), ('algunas_veces', 'Algunas veces'), ('muchas_veces', 'Muchas veces'), ('siempre', 'Siempre o Casi Siempre')], max_length=15, null=True, verbose_name='Frecuencia de uso de recursos en la clase de inglés')),
                ('acceso_recursos', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], max_length=2, null=True, verbose_name='Acceso a recursos para clases')),
                ('importancia_formacion_bilingue', models.CharField(choices=[('muy_en_desacuerdo', 'Muy en desacuerdo'), ('desacuerdo', 'Desacuerdo'), ('de_acuerdo', 'De acuerdo'), ('muy_de_acuerdo', 'Muy de acuerdo')], max_length=17, null=True, verbose_name='Interés de padres en formación bilingüe')),
                ('valoracion_formacion_bilingue', models.CharField(choices=[('muy_en_desacuerdo', 'Muy en desacuerdo'), ('desacuerdo', 'Desacuerdo'), ('de_acuerdo', 'De acuerdo'), ('muy_de_acuerdo', 'Muy de acuerdo')], max_length=17, null=True, verbose_name='Valoración de la formación bilingüe')),
                ('prioridad_ppb', models.CharField(choices=[('muy_en_desacuerdo', 'Muy en desacuerdo'), ('desacuerdo', 'Desacuerdo'), ('de_acuerdo', 'De acuerdo'), ('muy_de_acuerdo', 'Muy de acuerdo')], max_length=17, null=True, verbose_name='Prioridad del PPB')),
                ('participacion_padres', models.CharField(choices=[('muy_en_desacuerdo', 'Muy en desacuerdo'), ('desacuerdo', 'Desacuerdo'), ('de_acuerdo', 'De acuerdo'), ('muy_de_acuerdo', 'Muy de acuerdo')], max_length=17, null=True, verbose_name='Participación de padres en enseñanza')),
                ('cooperacion_ppb', models.CharField(choices=[('si', 'Sí'), ('no', 'No')], default='no', max_length=2, null=True, verbose_name='Cooperación en PPB')),
                ('encargado_ppb', models.CharField(blank=True, max_length=100, null=True, verbose_name='Encargado de PPB')),
            ],
        ),
        migrations.CreateModel(
            name='ESTER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad_cursos', models.IntegerField(default=0, help_text='Cantidad de cursos disponibles en ESTER')),
                ('cantidad_ova', models.IntegerField(default=0, help_text='Cantidad de Objetos Virtuales de Aprendizaje (OVA) disponibles')),
                ('cantidad_libros_ingles', models.IntegerField(default=0, help_text='Cantidad de libros en inglés disponibles')),
                ('cantidad_audiolibros', models.IntegerField(default=0, help_text='Cantidad de audiolibros disponibles')),
                ('cantidad_otros_recursos', models.IntegerField(default=0, help_text='Cantidad de otros recursos disponibles')),
                ('acceso_ester_numero_2023_2024', models.IntegerField(default=0, help_text='Número total de accesos de directores y docentes al Ecosistema ESTER durante 2023 y 2024')),
                ('acceso_ester_porcentaje_2023_2024', models.IntegerField(default=0, help_text='Porcentaje de acceso de directores y docentes al Ecosistema ESTER durante 2023 y 2024', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
            ],
        ),
        migrations.CreateModel(
            name='OtrosDocentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habla_ingles_otras_asignaturas', models.BooleanField(default=False)),
                ('porcentaje_tiempo_ingles_otras', models.IntegerField()),
                ('incentiva_hablar_ingles_otras', models.BooleanField(default=False)),
            ],
        ),
    ]
