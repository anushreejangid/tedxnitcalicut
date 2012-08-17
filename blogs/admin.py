from django.contrib import admin
from blogs.models import *
from django.core.urlresolvers import reverse

from tinymce.widgets import TinyMCE

'''class TinyMCEFlatPageAdmin(FlatPageAdmin):

	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name in ('body', 'content'):
			return db_field.formfield(widget=TinyMCE(attrs={'cols': 100, 'rows': 30}, mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
			))
		return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)
	class Media:
		js = ('js/tiny_mce/tiny_mce.js',
		'js/tiny_mce/textareas.js',)
'''
class BlogpostAdmin(admin.ModelAdmin):
	list_display = ('title','name','email','body','created')
	search_feilds = ('name','email')
	def formfield_for_dbfield(self, db_field, **kwargs):
        	if db_field.name in ('body', 'content'):
        		return db_field.formfield(widget=TinyMCE(attrs={'cols': 100, 'rows': 30},mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        	return super(BlogpostAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    	class Media:
		js = ('js/tiny_mce/textareas.js',
			'js/tiny_mce/tiny_mce.js')
	


class CommentAdmin(admin.ModelAdmin):
	list_display = ['post','name','created','body']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Blogpost , BlogpostAdmin)
