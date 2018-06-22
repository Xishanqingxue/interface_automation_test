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

class ProjectAdmin(admin.ModelAdmin):
    # 项目表
    list_display = ['id', 'name', 'version', 'type', 'desc', 'status', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'type']


class HostAdmin(admin.ModelAdmin):
    # 测试环境地址表
    list_display = ['id', 'project_id', 'name', 'host', 'desc', 'status', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'host']


class ApiGroupLevelAdmin(admin.ModelAdmin):
    # 接口一级分组表
    list_display = ['id', 'project_id', 'name', 'founder', 'update_time', 'create_time']
    search_fields = ['name']


class ApiHeadAdmin(admin.ModelAdmin):
    # 请求头表
    list_display = ['id', 'name', 'value', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'value']


class ApiInfoAdmin(admin.ModelAdmin):
    # 接口信息表
    list_display = ['id', 'project_id', 'api_group_level_id', 'name', 'http_type', 'request_type', 'api_address',
                    'head_id', 'request_parameter_type', 'status', 'desc', 'founder', 'update_time', 'create_time']
    search_fields = ['name', 'http_type', 'request_type', 'api_address', 'request_parameter_type']


class ApiParameterAdmin(admin.ModelAdmin):
    # 接口入参表
    list_display = ['id', 'api_id', 'name', 'type', 'value', 'required', 'restrict', 'description', 'founder',
                    'update_time', 'create_time']
    search_fields = ['name', 'value']


class TestCaseGroupLevelAdmin(admin.ModelAdmin):
    # 用例一级分组表
    list_display = ['id', 'project_id', 'name', 'founder', 'update_time', 'create_time']
    search_fields = ['name']


class TestCaseAdmin(admin.ModelAdmin):
    # 用例表
    list_display = ['id', 'project_id', 'case_group_level_id', 'name', 'desc', 'founder', 'update_time', 'create_time']
    search_fields = ['name']


class TestCaseInfoAdmin(admin.ModelAdmin):
    # 用例详情表
    list_display = ['id', 'case_id', 'name', 'api_id', 'seq', 'founder', 'update_time', 'create_time']
    search_fields = ['name']


admin.site.register(Project, ProjectAdmin)
admin.site.register(Host, HostAdmin)
admin.site.register(ApiGroupLevel, ApiGroupLevelAdmin)
admin.site.register(ApiHead, ApiHeadAdmin)
admin.site.register(ApiInfo, ApiInfoAdmin)
admin.site.register(ApiParameter, ApiParameterAdmin)
admin.site.register(TestCaseGroupLevel, TestCaseGroupLevelAdmin)
admin.site.register(TestCase, TestCaseAdmin)
admin.site.register(TestCaseInfo)
