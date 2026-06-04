#!/usr/bin/env python3
"""
cpcc 模块 RBAC 权限管理脚本

使用方法:
    cd ~/repos/sage
    ./py3/bin/python ~/repos/cpcc/scripts/load_path.py
"""

import subprocess
import os
import sys


def find_sage_root():
    candidates = [
        os.path.expanduser("~/repos/sage"),
        os.path.expanduser("~/sage"),
        os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),
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
# 权限路径定义
# ============================================================

# any — 无需登录
PATHS_ANY = [
    f"/{MOD}/menu.ui",
]

# logined — 所有已登录用户
PATHS_LOGINED = [
    # 模块入口
    f"/{MOD}",
    f"/{MOD}/index.ui",

    # 老式布局文件（兼容）
    f"/{MOD}/top.ui",
    f"/{MOD}/center.ui",
    f"/{MOD}/bottom.ui",
    f"/{MOD}/app_panel.ui",

    # components/
    f"/{MOD}/components/index.ui",
    f"/{MOD}/components/get_components.dspy",
    f"/{MOD}/components/add_components.dspy",
    f"/{MOD}/components/update_components.dspy",
    f"/{MOD}/components/delete_components.dspy",

    # cpccluster/
    f"/{MOD}/cpccluster/index.ui",
    f"/{MOD}/cpccluster/get_cpccluster.dspy",
    f"/{MOD}/cpccluster/add_cpccluster.dspy",
    f"/{MOD}/cpccluster/update_cpccluster.dspy",
    f"/{MOD}/cpccluster/delete_cpccluster.dspy",

    # cpclist/
    f"/{MOD}/cpclist/index.ui",
    f"/{MOD}/cpclist/get_cpclist.dspy",
    f"/{MOD}/cpclist/add_cpclist.dspy",
    f"/{MOD}/cpclist/update_cpclist.dspy",
    f"/{MOD}/cpclist/delete_cpclist.dspy",

    # cpcnode/
    f"/{MOD}/cpcnode/index.ui",
    f"/{MOD}/cpcnode/get_cpcnode.dspy",
    f"/{MOD}/cpcnode/add_cpcnode.dspy",
    f"/{MOD}/cpcnode/update_cpcnode.dspy",
    f"/{MOD}/cpcnode/delete_cpcnode.dspy",

    # cpcpod/
    f"/{MOD}/cpcpod/index.ui",
    f"/{MOD}/cpcpod/get_cpcpod.dspy",
    f"/{MOD}/cpcpod/get_node_labels.dspy",
    f"/{MOD}/cpcpod/new_cpcpodyaml.dspy",
    f"/{MOD}/cpcpod/new_podyaml.ui",

    # cpcpodyaml/
    f"/{MOD}/cpcpodyaml/index.ui",
    f"/{MOD}/cpcpodyaml/get_cpcpodyaml.dspy",
    f"/{MOD}/cpcpodyaml/update_cpcpodyaml.dspy",
    f"/{MOD}/cpcpodyaml/delete_cpcpodyaml.dspy",

    # cpcworker/
    f"/{MOD}/cpcworker/index.ui",
    f"/{MOD}/cpcworker/get_cpcworker.dspy",
    f"/{MOD}/cpcworker/add_cpcworker.dspy",
    f"/{MOD}/cpcworker/update_cpcworker.dspy",
    f"/{MOD}/cpcworker/delete_cpcworker.dspy",
    f"/{MOD}/cpcworker/get_availableworker.dspy",
    f"/{MOD}/cpcworker/new_cpcworker.dspy",
    f"/{MOD}/cpcworker/new_worker.ui",

    # handy/
    f"/{MOD}/handy/get_cpcnodes.dspy",
    f"/{MOD}/handy/new_cluster.dspy",
    f"/{MOD}/handy/new_cluster.ui",
]

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
