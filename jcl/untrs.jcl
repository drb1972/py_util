//<userid>X JOB (124400000),'DIEGO',CLASS=A,MSGCLASS=X,  
//      NOTIFY=&SYSUID
//****************************************************     
//DELETEDS EXEC PGM=IDCAMS
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
    DELETE <outfile>
    SET MAXCC = 0                                     
//****************************************************     
//UNTERPDS EXEC PGM=TRSMAIN,PARM=UNPACK                    
//SYSPRINT DD SYSOUT=*                                     
//INFILE   DD DSN=<infile>,                            
//            DISP=SHR                                     
//OUTFILE  DD DSN=<outfile>,
//            DISP=(NEW,CATLG),                            
//            <space>  