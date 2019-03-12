#!/usr/bin/python

from DB import update_mods, new_task, select_mods 
from Config import ModulesDirectory 
import os, base64

def check_module_loaded(module_name, randomuri, user, force=False):
  try:
    modules_loaded = select_mods(randomuri)
    if force:
      for modname in os.listdir(ModulesDirectory):
        if modname.lower() in module_name.lower():
          module_name = modname
      new_task(("loadmodule %s" % module_name), user, randomuri)
    if modules_loaded:
      new_modules_loaded = "%s %s" % (modules_loaded, module_name)
      if module_name not in modules_loaded:
        for modname in os.listdir(ModulesDirectory):
          if modname.lower() in module_name.lower():
            module_name = modname
        new_task(("loadmodule %s" % module_name), user, randomuri)
        update_mods(new_modules_loaded, randomuri)
    else:
      new_modules_loaded = "%s" % (module_name)
      new_task(("loadmodule %s" % module_name), user, randomuri)
      update_mods(new_modules_loaded, randomuri)
  except Exception as e:
    print ("Error loadmodule: %s" % e)

def run_autoloads(command, randomuri, user):
  if "invoke-eternalblue" in command.lower(): check_module_loaded("Exploit-EternalBlue.ps1", randomuri, user)
  if "invoke-psuacme" in command.lower(): check_module_loaded("Invoke-PsUACme.ps1", randomuri, user)
  if "bloodhound" in command.lower(): check_module_loaded("BloodHound.ps1", randomuri, user)
  if "brute-ad" in command.lower(): check_module_loaded("Brute-AD.ps1", randomuri, user)
  if "brute-locadmin" in command.lower(): check_module_loaded("Brute-LocAdmin.ps1", randomuri, user)
  if "bypass-uac" in command.lower(): check_module_loaded("Bypass-UAC.ps1", randomuri, user)
  if "cred-popper" in command.lower(): check_module_loaded("Cred-Popper.ps1", randomuri, user)
  if "cve-2016-9192" in command.lower(): check_module_loaded("CVE-2016-9192.ps1", randomuri, user)
  if "convertto-shellcode" in command.lower(): check_module_loaded("ConvertTo-Shellcode.ps1", randomuri, user)
  if "decrypt-rdcman" in command.lower(): check_module_loaded("Decrypt-RDCMan.ps1", randomuri, user)
  if "dump-ntds" in command.lower(): check_module_loaded("Dump-NTDS.ps1", randomuri, user)
  if "get-computerinfo" in command.lower(): check_module_loaded("Get-ComputerInfo.ps1", randomuri, user)
  if "get-creditcarddata" in command.lower(): check_module_loaded("Get-CreditCardData.ps1", randomuri, user)
  if "get-gppautologon" in command.lower(): check_module_loaded("Get-GPPAutologon.ps1", randomuri, user)
  if "get-gpppassword" in command.lower(): check_module_loaded("Get-GPPPassword.ps1", randomuri, user)
  if "get-idletime" in command.lower(): check_module_loaded("Get-IdleTime.ps1", randomuri, user)
  if "get-ipconfig" in command.lower(): check_module_loaded("Get-IPConfig.ps1", randomuri, user)
  if "get-keystrokes" in command.lower(): check_module_loaded("Get-Keystrokes.ps1", randomuri, user)
  if "get-hash" in command.lower(): check_module_loaded("Get-Hash.ps1", randomuri, user)
  if "get-locadm" in command.lower(): check_module_loaded("Get-LocAdm.ps1", randomuri, user)
  if "get-mshotfixes" in command.lower(): check_module_loaded("Get-MSHotFixes.ps1", randomuri, user)
  if "get-netstat" in command.lower(): check_module_loaded("Get-Netstat.ps1", randomuri, user)
  if "get-passnotexp" in command.lower(): check_module_loaded("Get-PassNotExp.ps1", randomuri, user)
  if "get-passpol" in command.lower(): check_module_loaded("Get-PassPol.ps1", randomuri, user)
  if "get-recentfiles" in command.lower(): check_module_loaded("Get-RecentFiles.ps1", randomuri, user)
  if "get-serviceperms" in command.lower(): check_module_loaded("Get-ServicePerms.ps1", randomuri, user)
  if "get-userinfo" in command.lower(): check_module_loaded("Get-UserInfo.ps1", randomuri, user)
  if "get-wlanpass" in command.lower(): check_module_loaded("Get-WLANPass.ps1", randomuri, user)
  if "invoke-pbind" in command.lower(): check_module_loaded("Invoke-Pbind.ps1", randomuri, user)
  if "get-domaingroupmember" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "invoke-kerberoast" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "invoke-userhunter" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "invoke-daisychain" in command.lower(): check_module_loaded("invoke-daisychain.ps1", randomuri, user)
  if "invoke-hostenum" in command.lower(): check_module_loaded("HostEnum.ps1", randomuri, user)
  if "inject-shellcode" in command.lower(): check_module_loaded("Inject-Shellcode.ps1", randomuri, user)
  if "inveigh-relay" in command.lower(): check_module_loaded("Inveigh-Relay.ps1", randomuri, user)
  if "inveigh" in command.lower(): check_module_loaded("Inveigh.ps1", randomuri, user)
  if "invoke-arpscan" in command.lower(): check_module_loaded("Invoke-Arpscan.ps1", randomuri, user)
  if "arpscan" in command.lower(): check_module_loaded("Invoke-Arpscan.ps1", randomuri, user)
  if "invoke-dcsync" in command.lower(): check_module_loaded("Invoke-DCSync.ps1", randomuri, user)
  if "invoke-eventvwrbypass" in command.lower(): check_module_loaded("Invoke-EventVwrBypass.ps1", randomuri, user)
  if "invoke-hostscan" in command.lower(): check_module_loaded("Invoke-Hostscan.ps1", randomuri, user)
  if "invoke-ms16-032-proxy" in command.lower(): check_module_loaded("Invoke-MS16-032-Proxy.ps1", randomuri, user)
  if "invoke-ms16-032" in command.lower(): check_module_loaded("Invoke-MS16-032.ps1", randomuri, user)
  if "invoke-mimikatz" in command.lower(): check_module_loaded("Invoke-Mimikatz.ps1", randomuri, user)
  if "invoke-psinject" in command.lower(): check_module_loaded("Invoke-PSInject.ps1", randomuri, user)
  if "invoke-pipekat" in command.lower(): check_module_loaded("Invoke-Pipekat.ps1", randomuri, user)
  if "invoke-portscan" in command.lower(): check_module_loaded("Invoke-Portscan.ps1", randomuri, user)
  if "invoke-powerdump" in command.lower(): check_module_loaded("Invoke-PowerDump.ps1", randomuri, user)
  if "invoke-psexec" in command.lower(): check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
  if "invoke-reflectivepeinjection" in command.lower(): check_module_loaded("Invoke-ReflectivePEInjection.ps1", randomuri, user)
  if "invoke-reversednslookup" in command.lower(): check_module_loaded("Invoke-ReverseDnsLookup.ps1", randomuri, user)
  if "invoke-runas" in command.lower(): check_module_loaded("Invoke-RunAs.ps1", randomuri, user)
  if "invoke-smblogin" in command.lower(): check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
  if "invoke-smbclient" in command.lower(): check_module_loaded("Invoke-SMBClient.ps1", randomuri, user)
  if "invoke-smbexec" in command.lower(): check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
  if "invoke-psexec" in command.lower(): check_module_loaded("Invoke-SMBExec.ps1", randomuri, user)
  if "invoke-shellcode" in command.lower(): check_module_loaded("Invoke-Shellcode.ps1", randomuri, user)
  if "invoke-sniffer" in command.lower(): check_module_loaded("Invoke-Sniffer.ps1", randomuri, user)
  if "invoke-sqlquery" in command.lower(): check_module_loaded("Invoke-SqlQuery.ps1", randomuri, user)
  if "invoke-tater" in command.lower(): check_module_loaded("Invoke-Tater.ps1", randomuri, user)
  if "invoke-thehash" in command.lower(): check_module_loaded("Invoke-TheHash.ps1", randomuri, user)
  if "invoke-tokenmanipulation" in command.lower(): check_module_loaded("Invoke-TokenManipulation.ps1", randomuri, user)
  if "invoke-wmichecker" in command.lower(): check_module_loaded("Invoke-WMIChecker.ps1", randomuri, user)
  if "invoke-wmicommand" in command.lower(): check_module_loaded("Invoke-WMICommand.ps1", randomuri, user)
  if "invoke-wscriptbypassuac" in command.lower(): check_module_loaded("Invoke-WScriptBypassUAC.ps1", randomuri, user)
  if "invoke-winrmsession" in command.lower(): check_module_loaded("Invoke-WinRMSession.ps1", randomuri, user)
  if "out-minidump" in command.lower(): check_module_loaded("Out-Minidump.ps1", randomuri, user)
  if "portscan" in command.lower(): check_module_loaded("PortScanner.ps1", randomuri, user)
  if "powercat" in command.lower(): check_module_loaded("powercat.ps1", randomuri, user)
  if "invoke-allchecks" in command.lower(): check_module_loaded("PowerUp.ps1", randomuri, user)
  if "set-lhstokenprivilege" in command.lower(): check_module_loaded("Set-LHSTokenPrivilege.ps1", randomuri, user)
  if "sharpsocks" in command.lower(): check_module_loaded("SharpSocks.ps1", randomuri, user)
  if "find-allvulns" in command.lower(): check_module_loaded("Sherlock.ps1", randomuri, user)
  if "test-adcredential" in command.lower(): check_module_loaded("Test-ADCredential.ps1", randomuri, user)
  if "new-zipfile" in command.lower(): check_module_loaded("Zippy.ps1", randomuri, user)
  if "get-netuser" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "invoke-aclscanner" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-dfsshare" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-objectacl" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "add-objectacl" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netuser" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-domainuser" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netcomputer" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-domaincomputer" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netuser" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netgroup" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netgroupmember" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netshare" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "invoke-sharefinder" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netdomain" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netdomaincontroller" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netforest" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-netforestdomain" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "invoke-mapdomaintrust" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-wmireglastloggedon" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-wmiregcachedrdpconnection" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "get-wmiregmounteddrive" in command.lower(): check_module_loaded("powerview.ps1", randomuri, user)
  if "invoke-wmievent" in command.lower(): check_module_loaded("Invoke-WMIEvent.ps1", randomuri, user)
  if "remove-wmievent" in command.lower(): check_module_loaded("Invoke-WMIEvent.ps1", randomuri, user)
  if "invoke-wmi" in command.lower(): check_module_loaded("Invoke-WMIExec.ps1", randomuri, user)
  if "get-lapspasswords" in command.lower(): check_module_loaded("Get-LAPSPasswords.ps1", randomuri, user)
  
