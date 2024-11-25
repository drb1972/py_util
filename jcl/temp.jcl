//PROD001X JOB (124400000),'BROADCOM',CLASS=A,MSGCLASS=X,  
//      NOTIFY=&SYSUID
//****************************************************     
//DELETEDS EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
    DELETE PROD001.UNTRS
    SET MAXCC = 0                                     
//****************************************************     
//UNTERPDS EXEC PGM=TRSMAIN,PARM=UNPACK                    
//SYSPRINT DD SYSOUT=*                                     
//INFILE   DD DSN=PROD001.TRS,                            
//            DISP=SHR                                     
//OUTFILE  DD DSN=PROD001.UNTRS,
//            DISP=(NEW,CATLG),                            
//            SPACE=(CYL,(10,10))  