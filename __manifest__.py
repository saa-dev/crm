{
    'name': 'Custom CRM',
    'version': '1.0',
    'category': 'CRM',
    'summary': 'Customizations for CRM module',
    'depends': ['crm'],
    'data': [
        'views/crm_lead_views.xml',
        'views/crm_quick_create_views.xml', 
    ],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
}