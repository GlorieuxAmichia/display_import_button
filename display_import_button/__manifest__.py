# -*- coding: utf-8 -*-
{
	'name': "Display Import Button",
	'sequence': 0,
	'summary': """Display Import Button""",
	'description': """
		This module is used to manage the display of the "import" button on your
		list, form, kanban view, according to your needs.
	""",
	'author': "SLife (AKA AMICHIA FREJUS ARNAUD)",
	'category': 'web',
	'version': '1.0',
	'depends': ['web'],
	'data': [
		'views/import_template.xml',
	],
	'images': [
		'static/src/img/main_1.png',
		'static/src/img/main_screenshot.png'
	],
	'qweb': ['static/src/xml/template.xml'],
	'installable': True,
	'auto_install': False,
}
