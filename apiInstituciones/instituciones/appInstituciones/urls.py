from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from appInstituciones import views

# urlpatterns = [
#     url(r'^snippets/$', views.snippet_list),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
	#Te presenta en modo de vista el get y post
    url(r'^Universidad/$', views.UniversidadList.as_view()),
    #te presenta solo uno con sus metyodos de un CRUD
    url(r'^Universidad/(?P<pk>[0-9]+)/$', views.UniversidadDetail.as_view()),
	#Te presenta en modo de vista el get y post
    url(r'^Hospital/$', views.HospitalList.as_view()),
    #te presenta solo uno con sus metyodos de un CRUD
    url(r'^Hospital/(?P<pk>[0-9]+)/$', views.HospitalDetail.as_view()),
	#Te presenta en modo de vista el get y post
    url(r'^Terminal/$', views.TerminalList.as_view()),
    #te presenta solo uno con sus metyodos de un CRUD
    url(r'^Terminal/(?P<pk>[0-9]+)/$', views.TerminalDetail.as_view()),
	#Te presenta en modo de vista el get y post
    url(r'^Aeropuerto/$', views.AeropuertoList.as_view()),
    #te presenta solo uno con sus metyodos de un CRUD
    url(r'^Aeropuerto/(?P<pk>[0-9]+)/$', views.AeropuertoDetail.as_view()),
	#Te presenta en modo de vista el get y post
    url(r'^Empresas/$', views.EmpresasList.as_view()),
    #te presenta solo uno con sus metyodos de un CRUD
    url(r'^Empresas/(?P<pk>[0-9]+)/$', views.EmpresasDetail.as_view()),
]
#solo se pone para que no me de problemas en el formato ... json , xml ....
urlpatterns = format_suffix_patterns(urlpatterns)