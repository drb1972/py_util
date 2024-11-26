import sys
import argparse
import os
import zw

try:
   parser = argparse.ArgumentParser(description='Unterse file and open in VSCode')
   parser.add_argument('-f','--file', help='Provide trs file (full or relative path)', required=True)
   parser.add_argument('-t','--type', help='pds or seq', required=True)
   args = parser.parse_args()
except Exception as exc:
   print(sys.exc_info())
   print(exc)

os.system('cls')

# PDS or SEQ
type=args.type.upper()
# check if file exists
local_file=args.file
if not os.path.isfile(local_file):
   print(local_file + "doesn't exist")
   exit(8)

# find userid to set HLQ
hlq=zw.find_userid().upper()
print('userid: '+hlq)

remote_file_tersed=hlq + '.TRS'
remote_file_untersed=hlq + '.UNTRS'

# Check if hlq.TRS file exists
if zw.check_zos_file(remote_file_tersed):
   zw.del_zos_file(remote_file_tersed)

# Create trs file
zw.cre_trs_file(remote_file_tersed)

# Upload local trs to remote (binary)
zw.upload_zos_file(remote_file_tersed,local_file,'-b')

# Create unterse jcl with model
with open('jcl\\untrs.jcl', 'r') as f:
      lines = f.readlines()
with open('jcl\\temp.jcl','wt') as o:
   for i in lines:
      i=i.replace('<userid>',hlq)
      i=i.replace('<outfile>',remote_file_untersed)
      i=i.replace('<infile>',remote_file_tersed)
      if   type=='SEQ': i=i.replace('<space>','SPACE=(CYL,(10,10))')
      elif type=='PDS': i=i.replace('<space>','SPACE=(CYL,(10,10,10))')
      o.write(i)

rc,jobid=zw.submit_local_jcl('jcl\\temp.jcl','-d out -e txt')

print(rc)
print(jobid)

if rc!='CC 0000':
   sysprint='.\\out\\'+jobid+'\\UNTERPDS\\SYSPRINT.txt'
   os.system('code '+sysprint)
else:
   local_untersed='.\\out\\untersed.txt'
   zw.download_zos_file(remote_file_untersed,local_untersed)
   os.system('code '+local_untersed)

exit()