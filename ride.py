import yaml
import os
stream = file('pkg.yaml', 'r')
yamlDesc = yaml.load(stream)

workspace_path = yamlDesc['workspace_location']+'/src'
os.system('cd '+workspace_path+' && catkin_create_pkg '+yamlDesc['package_name']+ ' '+yamlDesc['dependencies'])

for node in yamlDesc['nodes']:
    nodeScript = open(workspace_path+'/'+yamlDesc['package_name']+'/src/'+node['name']+'.py', 'w+')
    nodeScript.write('#!/usr/bin/env python\n')
    className = node['name'].capitalize()
    classDef = 'class '+className+':\n'
    classDef += '    def __init__(self):\n'
    classDef += '        #initialize node\n        rospy.init_node("'+className+'")\n        self.nodename = rospy.get_name()\n        rospy.loginfo("Started node %s" % self.nodename)\n'
    classDef += '        #params and vars below\n        self.rate = rospy.get_param(\'~rate\','+str(node['rate'])+')\n'

    subsDef = ''
    subsCallbacks = ''
    pubsDef = ''
    imports = 'import rospy\n'
    if 'subs' in node:
        for sub in node['subs']:
            msgPkg = sub['msg_type'].split("/",1)[0]
            msgType = sub['msg_type'].split("/",1)[1]
            subsDef += '        rospy.Subscriber("'+sub['topic']+'", '+msgType+', self.'+sub['topic'].split("/",1)[1]+'Cb)\n'
            imports += 'from '+msgPkg+'.msg import '+msgType+'\n'
            subsCallbacks += '    def '+sub['topic'].split("/",1)[1]+'Cb(self, msg):\n        pass\n'

    if 'pubs' in node:
        for pub in node['pubs']:
            msgPkg = pub['msg_type'].split("/",1)[0]
            msgType = pub['msg_type'].split("/",1)[1]
            imports += 'from '+msgPkg+'.msg import '+msgType+'\n'
            pubsDef += '        self.'+pub['topic'].split("/",1)[1]+'Pub = rospy.Publisher(\''+pub['topic']+'\', '+msgType+', queue_size=10)\n'

    spinDef = '    def spin(self):\n        self.r = rospy.Rate(self.rate)\n        while not rospy.is_shutdown():\n            #do something\n            pass\n            self.r.sleep()\n'

    mainDef = 'if __name__ == \'__main__\':\n    """main"""\n    try:\n        '+node['name']+' = '+className+'()\n        '+node['name']+'.spin()\n    except rospy.ROSInterruptException:\n        pass\n'

    nodeScript.write(imports)
    nodeScript.write(classDef)
    nodeScript.write(subsDef)
    nodeScript.write(pubsDef)
    nodeScript.write(spinDef)
    nodeScript.write(subsCallbacks)
    nodeScript.write(mainDef)
