
-- ./cpcnode_config.xlsx





drop table if exists cpcnode_config;
CREATE TABLE cpcnode_config
(

  `id` VARCHAR(32)   comment 'id',
  `nodeid` VARCHAR(32)   comment '节点名称',
  `name` VARCHAR(255)   comment '名称',
  `description` VARCHAR(3000)   comment '描述'


,primary key(id)


)
engine=innodb 
default charset=utf8 
comment '节点配置表'
;


-- ./cpccluster.xlsx





drop table if exists cpccluster;
CREATE TABLE cpccluster
(

  `id` VARCHAR(32)   comment 'id',
  `name` VARCHAR(255)   comment '名称',
  `cpcid` VARCHAR(32) NOT NULL  comment '算力中心id',
  `clustertype` VARCHAR(1)   comment '集群类型',
  `controllerid` VARCHAR(32)   comment '控制节点id',
  `enable_date` date   comment '启用日期',
  `export_date` date   comment '停用日期'


,primary key(id)


)
engine=innodb 
default charset=utf8 
comment '算力集群'
;


-- ./cpcnode.xlsx





drop table if exists cpcnode;
CREATE TABLE cpcnode
(

  `id` VARCHAR(32)   comment 'id',
  `name` VARCHAR(255)   comment '名称',
  `ip` VARCHAR(90)   comment '内网ip',
  `sshport` int   comment 'ssh端口号',
  `adminuser` VARCHAR(99)   comment '管理账号',
  `adminpwd` VARCHAR(99)   comment '管理密码',
  `cpcid` VARCHAR(32) NOT NULL  comment '算力中心id',
  `node_status` VARCHAR(1)   comment '节点状态',
  `clusterid` int   comment '所属集群',
  `enable_date` date   comment '启用日期',
  `export_date` date   comment '停用日期'


,primary key(id)


)
engine=innodb 
default charset=utf8 
comment '算力节点'
;


-- ./cpvalue.xlsx





drop table if exists cpvalue;
CREATE TABLE cpvalue
(

  `id` VARCHAR(32)   comment 'id',
  `comid` VARCHAR(255)   comment '部件id',
  `cpval` double(18,3)   comment '算力值',
  `cpunit` VARCHAR(1)   comment '算力单位'


,primary key(id)


)
engine=innodb 
default charset=utf8 
comment '算力值'
;


-- ./cpclist.xlsx





drop table if exists cpclist;
CREATE TABLE cpclist
(

  `id` VARCHAR(32)   comment 'id',
  `name` VARCHAR(255)   comment '名称',
  `orgid` VARCHAR(32)   comment '属主机构id',
  `pcapi_url` VARCHAR(500)   comment 'pcapi网址',
  `api_user` VARCHAR(100)   comment '接口用户',
  `api_pwd` VARCHAR(100)   comment '接口密码',
  `enable_date` date   comment '启用日期',
  `expire_date` date   comment '停用日期',
  `contactname` VARCHAR(100)   comment '联系人',
  `contactphone` VARCHAR(100)   comment '联系电话'


,primary key(id)


)
engine=innodb 
default charset=utf8 
comment '算力中心列表'
;


-- ./components.xlsx





drop table if exists components;
CREATE TABLE components
(

  `id` VARCHAR(32)   comment 'id',
  `name` VARCHAR(255)   comment '名称',
  `ccatelogid` VARCHAR(255)   comment '部件分类',
  `cmodel` VARCHAR(255)   comment '型号',
  `unitname` VARCHAR(32)   comment '计量名',
  `unitvalue` int   comment '计量值'


,primary key(id)


)
engine=innodb 
default charset=utf8 
comment '部件表'
;


-- ./cpcnode_config_detail.xlsx





drop table if exists cpcnode_config_detail;
CREATE TABLE cpcnode_config_detail
(

  `id` VARCHAR(32)   comment 'id',
  `nodeconfigid` VARCHAR(32)   comment '节点配置id',
  `comid` VARCHAR(32)   comment '部件id',
  `comcnt` int   comment '部件数量'


,primary key(id)


)
engine=innodb 
default charset=utf8 
comment '节点配置明细项'
;


