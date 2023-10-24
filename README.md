# 慧建驻自动化测试

## 慧建驻版本
2.0.0

## 框架
网易Airtest+poco+Unitest
airtest：https://airtest.netease.com/


##文件结构

```
├─ demo                                 调试
├─ wisbuild                             测试脚本
|   ├─  image                           上传的图片和无法定位的控件id使用图片
|   ├─  page_object                     页面定位脚本
|        ├─addressbook                  通用脚本
|              ├─organization           组织架构页面
|   ├─  login                           登录脚本
|        ├─login_Page                   登录
|              ├─login                  登录页面
|              ├─start_APP              启动APP
|   ├─  log                             个人中心脚本
|        ├─user_info                    用户信息
|              ├─my_Page                我的页面
|              ├─more_user_info         更多个人设置页面
|              ├─user_info              个人中心页面
|              ├─user_setting_Page      更多设置页面
|   ├─  statistics                      统计页面
|        ├─certification_Page           认证页面
|               ├─certification_Page    待认证页面
|        ├─stats_Page                   统计页面
|               ├─nproj_Page.py         认证通过未加入项目统计页面
|               ├─worker_stats_Page     工人统计页面
|   ├─  work                            工作页面
|        ├─project_detail               项目详情
|               ├─proj_Info_Page        项目列表查询
|        ├─project_list                 项目列表
|               ├─proj_filter_Page      筛选控件
|               ├─proj_list_Page        项目列表页面
|        ├─recruitment_list             招工管理（作废）  
|        ├─work_list                    工作列表
|               ├─work_page             工作菜单
|   ├─test_case                         测试用例存放
|   ├─tool                              工具类脚本
|        ├─Camera                       拍照
|        ├─Generate_log                 测试报告
|        ├─Mobile_Phone                 随机手机号
|        ├─permission                   拍照权限
|        ├─phone_devices                连接手机
|        ├─upload_pic                   头像裁剪
|        ├─work_type                    工种选择      
```