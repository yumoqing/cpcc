---
name: cpcc-repo
version: 1.0.0
description: cpcc 仓库：73 个文件，主语言JSON 12，Python 2，Shell 2
trigger_conditions:
  - 需要理解、修改或排障 cpcc 的代码
  - 在 cpcc 里定位入口、数据表、对外契约或构建方式
---

# cpcc 仓库技能

> 由仓库实际内容生成的骨架（README/目录/模型定义/契约/构建脚本逐项取证）。新增判断与坑位请直接在下面对应小节补充。

## 定位

**cpcc**

a computing power center manages client

- 远端：`https://github.com/yumoqing/cpcc.git`
- 默认分支：`main`（共 12 个提交）
- 最近提交：2026-11-03 `871b4b0` chore: 忽略 init/logs 等生成物
- 规模：73 个文件；JSON 12，Python 2，Shell 2

## 目录结构

- `wwwroot/` — 前端页面与 `.dspy` 契约（服务端渲染入口）（46 个文件）
- `models/` — 表定义（`models/*.json`，DDL/表结构唯一源）（15 个文件）
- `json/` — CRUD/界面定义（`json/*.json`：tblname+params）（5 个文件）
- `app/` — 应用级初始化 / 菜单与页面装配（1 个文件）
- `conf/` — 配置（`config.json`；密码为 AES 密文）（1 个文件）
- `docs/` — 文档（1 个文件）
- `script/` — 脚本（1 个文件）
- `scripts/` — 脚本（`load_path.py` 权限路径、迁移/初始化）（1 个文件）
- 根文件：`.gitignore`、`README.md`

## 数据表（`models/*.json`，7 张）

- `components`（部件表） — 6 字段
- `cpccluster`（算力集群） — 7 字段
- `cpclist`（算力中心列表） — 10 字段
- `cpcnode`（算力节点） — 11 字段
- `cpcnode_config`（节点配置表） — 4 字段
- `cpcnode_config_detail`（节点配置明细项） — 4 字段
- `cpvalue`（算力值） — 4 字段

> 表结构只改 `models/*.json`，DDL 由它生成；不要手改库。

## CRUD 定义（`json/*.json`，4 个）

- 合规：`components.json`→components、`cpccluster.json`→cpccluster、`cpclist.json`→cpclist、`cpcnode.json`→cpcnode

## 对外契约（`.dspy`，30 个）

- `wwwroot/cpcworker/`：6 个 — add_cpcworker.dspy、delete_cpcworker.dspy、get_availableworker.dspy、get_cpcworker.dspy、new_cpcworker.dspy、update_cpcworker.dspy
- `wwwroot/components/`：4 个 — add_components.dspy、delete_components.dspy、get_components.dspy、update_components.dspy
- `wwwroot/cpccluster/`：4 个 — add_cpccluster.dspy、delete_cpccluster.dspy、get_cpccluster.dspy、update_cpccluster.dspy
- `wwwroot/cpclist/`：4 个 — add_cpclist.dspy、delete_cpclist.dspy、get_cpclist.dspy、update_cpclist.dspy
- `wwwroot/cpcnode/`：4 个 — add_cpcnode.dspy、delete_cpcnode.dspy、get_cpcnode.dspy、update_cpcnode.dspy
- `wwwroot/cpcpod/`：3 个 — get_cpcpod.dspy、get_node_labels.dspy、new_cpcpodyaml.dspy
- `wwwroot/cpcpodyaml/`：3 个 — delete_cpcpodyaml.dspy、get_cpcpodyaml.dspy、update_cpcpodyaml.dspy
- `wwwroot/handy/`：2 个 — get_cpcnodes.dspy、new_cluster.dspy

## 建议阅读顺序

1. `README.md`
2. `docs/`
3. `models/`
4. `wwwroot/`
5. `scripts/load_path.py`

