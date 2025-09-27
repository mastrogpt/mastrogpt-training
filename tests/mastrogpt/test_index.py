import sys
sys.path.append("packages/mastrogpt/index")
import index as m

def test_legacy():
    __file__ = "packages/mastrogpt/index/index.py"    
    actions = m.invoke("actions")
    indexes = m.get_indexes(actions)
    services = m.get_services(indexes)
    #print(services)
    m.legacy(services)

