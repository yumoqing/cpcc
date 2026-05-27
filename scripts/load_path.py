#!/usr/bin/env python3
"""
cpcc 模块 RBAC 权限管理脚本

使用方法:
    cd ~/repos/sage
    ./py3/bin/python ~/cpcc/scripts/load_path.py

每次代码变更如有新 path 出现，需同步更新此脚本。
"""

import subprocess
import os
import sys

def find_sage_root():
    candidates = [
        os.path.expanduser("~/repos/sage"),
        os.path.expanduser("~/sage"),
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))),
    ]
    for c in candidates:
        if os.path.isdir(os.path.join(c, "py3")) and os.path.isdir(os.path.join(c, "wwwroot")):
            return c
    return None

SAGE_ROOT = find_sage_root()
if not SAGE_ROOT:
    print("ERROR: Cannot find Sage root directory")
    sys.exit(1)

PYTHON = os.path.join(SAGE_ROOT, "py3", "bin", "python")
SET_PERM_SCRIPT = os.path.join(SAGE_ROOT, "set_role_perm.py")

MOD = "cpcc"

# ============================================================
# 权限路径定义 — 每次新增页面或API时同步更新
# ============================================================

# any — 无需登录（菜单、登录页等）
PATHS_ANY = [
    f"/cpcc/menu.ui",]

# logined — 需要认证的页面和 API
PATHS_LOGINED = [
    f"/cpcc",
    f"/cpcc/app_panel.ui",
    f"/cpcc/bottom.ui",
    f"/cpcc/center.ui",
    f"/cpcc/components",
    f"/cpcc/components/add_components.dspy",
    f"/cpcc/components/delete_components.dspy",
    f"/cpcc/components/get_components.dspy",
    f"/cpcc/components/index.ui",
    f"/cpcc/components/update_components.dspy",
    f"/cpcc/cpccluster",
    f"/cpcc/cpccluster/add_cpccluster.dspy",
    f"/cpcc/cpccluster/delete_cpccluster.dspy",
    f"/cpcc/cpccluster/get_cpccluster.dspy",
    f"/cpcc/cpccluster/index.ui",
    f"/cpcc/cpccluster/update_cpccluster.dspy",
    f"/cpcc/cpclist",
    f"/cpcc/cpclist/add_cpclist.dspy",
    f"/cpcc/cpclist/delete_cpclist.dspy",
    f"/cpcc/cpclist/get_cpclist.dspy",
    f"/cpcc/cpclist/index.ui",
    f"/cpcc/cpclist/update_cpclist.dspy",
    f"/cpcc/cpcnode",
    f"/cpcc/cpcnode/add_cpcnode.dspy",
    f"/cpcc/cpcnode/delete_cpcnode.dspy",
    f"/cpcc/cpcnode/get_cpcnode.dspy",
    f"/cpcc/cpcnode/index.ui",
    f"/cpcc/cpcnode/update_cpcnode.dspy",
    f"/cpcc/cpcpod",
    f"/cpcc/cpcpod/get_cpcpod.dspy",
    f"/cpcc/cpcpod/get_node_labels.dspy",
    f"/cpcc/cpcpod/index.ui",
    f"/cpcc/cpcpod/new_cpcpodyaml.dspy",
    f"/cpcc/cpcpod/new_podyaml.ui",
    f"/cpcc/cpcpodyaml",
    f"/cpcc/cpcpodyaml/delete_cpcpodyaml.dspy",
    f"/cpcc/cpcpodyaml/get_cpcpodyaml.dspy",
    f"/cpcc/cpcpodyaml/index.ui",
    f"/cpcc/cpcpodyaml/update_cpcpodyaml.dspy",
    f"/cpcc/cpcworker",
    f"/cpcc/cpcworker/add_cpcworker.dspy",
    f"/cpcc/cpcworker/delete_cpcworker.dspy",
    f"/cpcc/cpcworker/get_availableworker.dspy",
    f"/cpcc/cpcworker/get_cpcworker.dspy",
    f"/cpcc/cpcworker/index.ui",
    f"/cpcc/cpcworker/new_cpcworker.dspy",
    f"/cpcc/cpcworker/new_worker.ui",
    f"/cpcc/cpcworker/update_cpcworker.dspy",
    f"/cpcc/handy",
    f"/cpcc/handy/get_cpcnodes.dspy",
    f"/cpcc/handy/new_cluster.dspy",
    f"/cpcc/handy/new_cluster.ui",
    f"/cpcc/index.ui",
    f"/cpcc/top.ui",]

# ============================================================
# 执行注册
# ============================================================

def run_set_perm(role, path):
    cmd = [PYTHON, SET_PERM_SCRIPT, role, path]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

def register_role_paths(role, paths):
    count = 0
    for p in paths:
        if run_set_perm(role, p):
            count += 1
    print(f"  {role}: {count}/{len(paths)} paths registered")
    return count

def main():
    print(f"Sage root: {SAGE_ROOT}")
    total = 0
    total += register_role_paths("any", PATHS_ANY)
    total += register_role_paths("logined", PATHS_LOGINED)
    print(f"\nDone. Total {total} permission entries registered.")
    print("NOTE: Restart Sage after permission changes to reload RBAC cache.")

if __name__ == "__main__":
    main()
