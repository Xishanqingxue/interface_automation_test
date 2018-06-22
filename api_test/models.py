from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Project(models.Model):
    """
    项目表
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='项目名称')
    version = models.CharField(max_length=50, verbose_name='版本')
    type = models.CharField(max_length=50, verbose_name='类型', choices=(('Web', 'Web'),('App', 'App')))
    desc = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    status = models.BooleanField(default=True, verbose_name='状态')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')


    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '项目'
        verbose_name_plural = '项目'

class Host(models.Model):
    """
    host域名表
    """
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    name = models.CharField(max_length=50, verbose_name='名称')
    host = models.CharField(max_length=1024, verbose_name='Host地址')
    desc = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    status = models.BooleanField(default=True, verbose_name='状态')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'HOST'
        verbose_name_plural = 'HOST管理'


class ApiGroupLevel(models.Model):
    """
    接口一级分组
    """
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    name = models.CharField(max_length=50, verbose_name='接口一级分组名称')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '接口分组'
        verbose_name_plural = '接口分组'


class ApiHead(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, verbose_name="名称")
    value = models.CharField(max_length=1024, blank=True, null=True, verbose_name='内容')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '请求头'
        verbose_name_plural = '请求头管理'


class ApiInfo(models.Model):
    """
    接口信息
    """
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, related_name='api_project', on_delete=models.CASCADE, verbose_name='所属项目')
    api_group_level_id = models.ForeignKey(ApiGroupLevel, blank=True, null=True,related_name='First',on_delete=models.SET_NULL, verbose_name='所属一级分组')
    name = models.CharField(max_length=50, verbose_name='接口名称')
    http_type = models.CharField(max_length=50, default='HTTP', verbose_name='http/https', choices=(('HTTP', 'HTTP'),('HTTPS', 'HTTPS')))
    request_type = models.CharField(max_length=50, verbose_name='请求方式', choices=(('POST', 'POST'),('GET', 'GET'),('PUT', 'PUT'),('DELETE', 'DELETE')))
    api_address = models.CharField(max_length=1024, verbose_name='接口地址')
    head_id = models.ForeignKey(ApiHead, related_name='api_head', on_delete=models.CASCADE, verbose_name='请求头')
    request_parameter_type = models.CharField(max_length=50, verbose_name='请求参数格式', choices=(('form-data', '表单(form-data)'),('raw', '源数据(raw)')))
    status = models.BooleanField(default=True, verbose_name='状态')
    desc = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '接口'
        verbose_name_plural = '接口管理'


class ApiParameter(models.Model):
    """
    接口入参
    """
    id = models.AutoField(primary_key=True)
    api_id = models.ForeignKey(ApiInfo, on_delete=models.CASCADE, verbose_name="所属接口", related_name='requestParameter')
    name = models.CharField(max_length=1024, verbose_name="参数名")
    type = models.CharField(default="String", max_length=1024, verbose_name='参数类型',choices=(('Int', 'Int'), ('String', 'String')))
    value = models.CharField(max_length=1024, blank=True, null=True, verbose_name='参数值')
    required = models.BooleanField(default=True, verbose_name="是否必填")
    restrict = models.CharField(max_length=1024, blank=True, null=True, verbose_name="输入限制")
    description = models.CharField(max_length=1024, blank=True, null=True, verbose_name="描述")
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '请求参数'
        verbose_name_plural = '请求参数管理'


class TestCaseGroupLevel(models.Model):
    """
    自动化用例一级分组
    """
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='项目')
    name = models.CharField(max_length=50, verbose_name='用例一级分组')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用例分组'
        verbose_name_plural = '用例分组管理'


class TestCase(models.Model):
    """
    自动化测试用例
    """
    id = models.AutoField(primary_key=True)
    project_id = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='所属项目')
    case_group_level_id = models.ForeignKey(TestCaseGroupLevel, blank=True, null=True,on_delete=models.SET_NULL, verbose_name='所属用例一级分组')
    name = models.CharField(max_length=50, verbose_name='用例名称')
    desc = models.CharField(max_length=1024, blank=True, null=True, verbose_name='描述')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '自动化测试用例'
        verbose_name_plural = '自动化测试用例'
#
#
class TestCaseInfo(models.Model):
    """
    用例执行接口
    """
    id = models.AutoField(primary_key=True)
    case_id = models.ForeignKey(TestCase, on_delete=models.CASCADE,verbose_name='用例', related_name="case_name")
    name = models.CharField(max_length=50, verbose_name='操作步骤名称')
    api_id =  models.ForeignKey(ApiInfo, on_delete=models.CASCADE,verbose_name='接口名称')
    seq = models.CharField(max_length=50, verbose_name='执行顺序')
    founder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, max_length=1024, verbose_name='创建人')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最近修改时间')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '用例接口'
        verbose_name_plural = '用例接口管理'
