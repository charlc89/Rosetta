import os
def LoopModel():
    print("Total no. of model:",end='')
    Terminator=int(input())
    for p in range(1, Terminator+1):
        with open("flag_CDR","w") as FlagFile:
            FlagFile.write(f"""-in:file:s LaG{p}_Un.pdb
-in:file:fullatom
-loops:loop_file cbCDR3.loops

-nstruct 500

-loops:fast
-loops:max_kic_build_attempts 250
-loops:remodel perturb_kic
-loops:refine refine_kic

-ex1
-ex2
-use_input_sc

-out:file:fullatom
-out:file:scorefile loopspace_{p}.fasc""")
#loop model instruction integrates into each loop, getting model(should we do that?)
        os.system("/Users/charles/Documents/Rosetta/main/source/bin/loopmodel.default.macosclangrelease @flag_CDR")
        TotalScore=[]
        BodyName=[]
        with open(f"loopspace_{p}.fasc","r") as FlagScore:               #open with directry if needed(absolute loc)
                  #"cbCDR3" changed into 'loopspace_"var" '                                                    #name the file "loopspace"1"" where "1" is the variable to be increased with loop
            for line in FlagScore:                                      #target each line of data
               if "SEQUENCE:" not in line:                              #exclude first and second line
                   if "total_score" not in line:
                       ScoreList=line.strip().split()                   #make the line string into list, with data in sequence
                       TotalScore.append(float(ScoreList[1]))           #the first data is total score, the one we need to sort
                       BodyName.append(ScoreList[len(ScoreList)-1])     #the name of structure should be recoreded accordingly
        lowest=TotalScore[0]                                            #find minimial value
        for i in TotalScore:    
            if i<=lowest:       
                lowest=i
        Tar=TotalScore.index(lowest)                                    #find the index for the lowest total score
        with open("Data_record.txt","a") as f:                          #set an file to record data
            f.write(f" LaG{p}: Unrelaxed {lowest};{BodyName[Tar]}   ")  #record the information at file
            
        #print(f"Lowest total score is from {BodyName[Tar]} with the score being {lowest}")
 
        f=open(f"flag_relax","w+")                          #create a file within the folder as the script                                    
        f.write(f"""-s {BodyName[Tar]}.pdb
-out:suffix _relaxed
-nstruct 1
-relax:default_repeats 5""")
        PDB=str(BodyName[Tar])+".pdb"
        print(PDB)
        Count=p
        os.system("/Users/charles/Documents/Rosetta/main/source/bin/relax.default.macosclangrelease -s {} -out:suffix _relaxed{} -nstruct 10 -relax:default_repeats 5".format(PDB, Count))
        RelEng=[]                                                       #same as above, create list for containing total score and structure name
        RelNam=[]       
        with open(f"score_relaxed{p}.sc","r") as RelSoc:                    #open with directry if needed(absolute loc) 
            for lin in RelSoc:
               if "SEQUENCE:" not in lin:                               #same logic as above
                   if "total_score" not in lin:     
                       Relist=lin.strip().split()
                       RelEng.append(float(Relist[1]))
                       RelNam.append(Relist[len(Relist)-1])
            Relow=RelEng[0]
            for j in RelEng:                                            #same logic for minimal value factor
                if j<=Relow:
                    Relow=j
            Ind=RelEng.index(Relow)
        with open("Data_record.txt","a") as f:                          #same file location for data recording
            f.write(f"Relaxed {Relow};{RelNam[Ind]} \n")
    

LoopModel()
