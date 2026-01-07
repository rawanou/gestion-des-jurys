{
    'name': 'Gestion des Jurys',
    'version': '1.0',
    'summary': 'Gestion des jurys et décisions',
    'category': 'Education',
    'author': 'KHOUMRI Rawane',
    'depends': ['base'],
    'data': [
      'security/ir.model.access.csv',
      'views/jury_views.xml',
      'views/jury_decision_views.xml',
    ],
    'installable': True,
    'application': True,
}
