# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",
    'summary': """Sencilla Lista de tareas""",
    'description': """
        Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos
    """,
    'author': "Sergi García",
    'website': "https://apuntesfpinformatica.es",

    # Indicamos que es una aplicación
    'application': True,

    # Vamos a utilizar la categoría Productivity
    'category': 'Productivity',
    'version': '0.1',

    # Indicamos lista de módulos necesarios para que este funcione correctamente
    'depends': ['base'],

    # Esto siempre se carga
    'data': [
        # Este primero indica la política de acceso del módulo
        'security/ir.model.access.csv',
        # Cargamos las vistas y las plantillas
        'views/views.xml',
    ]
}