### Next-Generation Kinematic Loop Closure (NGK)
###### 1. Create a flag file: <br>
  **-in:file:s {name}.pdb <br>
-in:file:fullatom <br>
-loops:loop_file {name}.loops <br>
-nstruct 500** <br>

**-loops:fast <br>
-loops:max_kic_build_attempts 250<br>
-loops:remodel perturb_kic<br>
-loops:refine refine_kic**<br>

**-ex1<br>
-ex2<br>
-use_input_sc**<br>

**-out:file:fullatom<br>
-out:file:scorefile {name}.fasc** <br>
To have a producitve run, nstruct should be set as 500 and the attempts should be 250
###### 2. Create a loop file
**LOOP 115 118 0 0 1** <br>
The loop file should be named as {name}.loop
###### 3. Run the code 
` /Users/charles/Documents/Rosetta/main/source/bin/loopmodel.default.macosclangrelease @flag_NGK `
### Select the lowest scoring model 
### Structure refinement (Relax)
###### 1. Create a flag file: <br>
**-s {name}.pdb <br>
-out:suffix _{name} <br>
-nstruct 10 <br>
-relax:default_repeats 5** <br>
The nstruct should be 5-15
###### 2. Run the code 
` /Users/charles/Documents/Rosetta/main/source/bin/relax.default.macosclangrelease @flag_relax `
### Select the lowest scoring model 
