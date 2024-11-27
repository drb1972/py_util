import sys
import argparse
import os
import zw

try:
   parser = argparse.ArgumentParser(description='Terse file and donwload to ./out folder')
   parser.add_argument('-f','--file', help='Provide file to terse', required=True)
   args = parser.parse_args()
except Exception as exc:
   print(sys.exc_info())
   print(exc)

os.system('cls')

remote_file=args.file.upper()
# check if file name syntax is correct
tf,message=zw.check_zos_file_name(remote_file)
if not tf: 
   print(f'Please check the name of the fle: {remote_file}')
   print(message)
   exit(8)

# check if file to terse exists
if not zw.check_zos_file(remote_file):
   print(f"File {remote_file} doen't exist")
   exit(8)

# find userid to set HLQ
hlq=zw.find_userid().upper()
print('userid: '+hlq)

remote_file_tersed=hlq + '.TRS'

# Create unterse jcl with model
with open('jcl\\trs.jcl', 'r') as f:
      lines = f.readlines()
with open('jcl\\temp.jcl','wt') as o:
   for i in lines:
      i=i.replace('<userid>',hlq)
      i=i.replace('<outfile>',remote_file_tersed)
      i=i.replace('<infile>',remote_file)
      o.write(i)

# submit /jcl/temp.jcl
rc,jobid=zw.submit_local_jcl('jcl\\temp.jcl','-d out -e txt')

print(rc)
print(jobid)

if rc!='CC 0000':
   sysprint='.\\out\\'+jobid+'\\UNTERPDS\\SYSPRINT.txt'
   os.system('code '+sysprint)
else:
   local_file_tersed=f'.\\out\\{remote_file}.trs'
   zw.download_zos_file(remote_file_tersed,local_file_tersed,'-b')
   print(f'The tersed file is in {local_file_tersed}')

exit()