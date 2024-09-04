#!/u01/app/oracle/middleware/Jen_wls12c/oracle_common/common/bin/wlst.sh
def wlDeployUndeploy(username, password, adminURL, appName, location, targets):
    try:
        #connect to admin server
        connect(username, password, adminURL)
        #start edit operation
        edit()
        startEdit()

        #stop application
        stopApplication(appName)

        #start undeploying application to "AdminServer" server
        progress = undeploy(appName, timeout=60000)
        progress.printStatus()
        save()
        activate(20000,block="true")
        #start deploying application to ""AdminServer" server
        progress = deploy(appName,location,targets)
        progress.printStatus()
        #print 'Done deploying application' +appname

    except Exception, e:
         print ex.toString()
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.1.125:7001','benefits','/u01/app/oracle/middleware/applications/benefits.war','admin_test')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.1.125:7001','messaging','/u01/app/oracle/middleware/applications/messaging.war','admin_test')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.1.125:7001','contacts','/u01/app/oracle/middleware/applications/contacts.war','admin_test')
wlDeployUndeploy('weblogic','weblogic1','t3://192.168.1.125:7001','timeoff','/u01/app/oracle/middleware/applications/timeoff.war','admin_test')

