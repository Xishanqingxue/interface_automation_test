from django.contrib import admin
from api_test.models import Project
from api_test.models import Host
from api_test.models import ApiGroupLevel
from api_test.models import ApiHead
from api_test.models import ApiInfo
from api_test.models import ApiParameter
from api_test.models import TestCaseGroupLevel
from api_test.models import TestCase
from api_test.models import TestCaseInfo
# Register your models here.


list_of_page = 20
admin.site.site_header = '通用后台管理系统'
admin.site.site_title = '通用后台管理系统'

class ProjectAdmin(admin.ModelAdmin):
    # 项目表
    list_display = ['id', 'name', 'version', 'type', 'desc', 'status', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'type']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class HostAdmin(admin.ModelAdmin):
    # 测试环境地址表
    list_display = ['id', 'project_id', 'name', 'host', 'desc', 'status', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'host']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class ApiGroupLevelAdmin(admin.ModelAdmin):
    # 接口一级分组表
    list_display = ['id', 'project_id', 'name', 'founder', 'update_time', 'create_time']
    search_fields = ['name']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class ApiHeadAdmin(admin.ModelAdmin):
    # 请求头表
    list_display = ['id', 'name', 'value', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'value']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class ApiInfoAdmin(admin.ModelAdmin):
    # 接口信息表
    list_display = ['id', 'project_id', 'api_group_level_id', 'name', 'http_type', 'request_type', 'api_address',
                    'head_id', 'request_parameter_type', 'status', 'desc', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'http_type', 'request_type', 'api_address', 'request_parameter_type']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class ApiParameterAdmin(admin.ModelAdmin):
    # 接口入参表
    list_display = ['id', 'api_id', 'name', 'type', 'value', 'required', 'restrict', 'description', 'founder',
                    'update_time', 'create_time']
    search_fields = ['name', 'value']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class TestCaseGroupLevelAdmin(admin.ModelAdmin):
    # 用例一级分组表
    list_display = ['id', 'project_id', 'name', 'founder', 'update_time', 'create_time']
    search_fields = ['name']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class TestCaseAdmin(admin.ModelAdmin):
    # 用例表
    list_display = ['id', 'project_id', 'case_group_level_id', 'name', 'desc', 'founder', 'update_time', 'create_time']
    search_fields = ['name']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


class TestCaseInfoAdmin(admin.ModelAdmin):
    # 用例详情表
    list_display = ['id', 'case_id', 'name', 'api_id', 'seq', 'founder', 'update_time', 'create_time']
    search_fields = ['name']
    list_per_page = list_of_page
    ordering = ['id']
    list_display_links = ['name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(ApiGroupLevel, ApiGroupLevelAdmin)
admin.site.register(ApiHead, ApiHeadAdmin)
admin.site.register(ApiInfo, ApiInfoAdmin)
admin.site.register(ApiParameter, ApiParameterAdmin)
admin.site.register(TestCaseGroupLevel, TestCaseGroupLevelAdmin)
admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestCaseInfo)
