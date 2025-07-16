from appPublic.registerfunction import RegisterFunction
from ahserver.webapp import webapp
from ahserver.serverenv import ServerEnv
from appbase.init import load_appbase
from rbac.check_perm import load_rbac

def UiError(title="出错", message="出错啦", timeout=5):
    return {
        "widgettype":"Error",
        "options":{
            "author":"tr",
            "timeout":timeout,
            "cwidth":15,
            "cheight":10,
            "title":title,
            "message":message
        }
    }

def UiMessage(title="消息", message="后台消息", timeout=5):
    return {
        "widgettype":"Message",
        "options":{
            "author":"tr",
            "timeout":timeout,
            "cwidth":15,
            "cheight":10,
            "title":title,
            "message":message
        }
    }

def get_module_dbname(mname):
	return 'cpcc'

rf = RegisterFunction()
rf.register('get_module_dbname', get_module_dbname)

def init():
	g = ServerEnv()
	g.get_module_dbname = get_module_dbname
	load_appbase()
	load_rbac()
	g.UiError = UiError
	g.UiMessage = UiMessage
	
	# k8sAPI远程指令(目前放到.dspy文件中)
	# 看样子cpcc.py文件中没有使用到数据库函数
	# g.cluster_kubeconfig = cluster_kubeconfig

	g.result_dict = {
		"status": False,
		"info": "failed",
		"data":	None
		}

if __name__ == '__main__':
	webapp(init)

# sword/111111