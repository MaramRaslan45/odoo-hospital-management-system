{
    'name': 'hms',
    'summary': 'hospital management system',
    'depends': ['base','crm'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/department_views.xml',
        'views/doctor_views.xml',
        'views/patient_history_views.xml',
        'views/crm_inherit_customer_view.xml',
    ]
}