{
    'name': "Library Management",
    'summary': """Manage library catalog""",
    'author': "Khodary",
    'license': "AGPL-3",
    'website': "",
    'category': 'Services/Library',
    'version': '0.1',
    'depends': ['base'],
    'application': True,
    'data': [
        'security/library_security.xml',
        "security/ir.model.access.csv",
        'views/book_view.xml',
        'views/library_menu.xml',
        'views/book_list_template.xml',

    ],
}
