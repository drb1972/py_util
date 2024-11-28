//PROD001X JOB (124400000),'DIEGO',CLASS=A,MSGCLASS=X,  
//      NOTIFY=&SYSUID
//****************************************************     
//DELETEDS EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
    DELETE PROD001.TRS
    SET MAXCC = 0                                     
//****************************************************     
//TERSE    EXEC PGM=TRSMAIN,PARM='PACK'
//SYSPRINT DD SYSOUT=*
//INFILE   DD DISP=SHR,DSN=PROD001.LIB.REXX
//OUTFILE  DD DSN=PROD001.TRS,
//            DCB=(RECFM=FB,BLKSIZE=6144,LRECL=1024),
//            UNIT=SYSDA,SPACE=(CYL,(750,200),RLSE),
//            DISP=(NEW,CATLG,DELETE)