//<userid>X JOB (124400000),'DIEGO',CLASS=A,MSGCLASS=X,  
//      NOTIFY=&SYSUID
//****************************************************     
//DELETEDS EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
    DELETE <outfile>
    SET MAXCC = 0                                     
//****************************************************     
//TERSE    EXEC PGM=TRSMAIN,PARM='PACK'
//SYSPRINT DD SYSOUT=*
//INFILE   DD DISP=SHR,DSN=<infile>
//OUTFILE  DD DSN=<outfile>,
//            DCB=(RECFM=FB,BLKSIZE=6144,LRECL=1024),
//            UNIT=SYSDA,SPACE=(CYL,(750,200),RLSE),
//            DISP=(NEW,CATLG,DELETE)