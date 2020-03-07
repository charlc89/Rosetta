### Next-Generation Kinematic Loop Closure (NGK)
To perform a loop closure in Rosetta, firstly prepare a flag file: <br>
  **-in:file:s {name}.pdb
-in:file:fullatom
-loops:loop_file cbCDR3.loops
-nstruct 500**

**-loops:fast
-loops:max_kic_build_attempts 250
-loops:remodel perturb_kic
-loops:refine refine_kic**

**-ex1
-ex2
-use_input_sc**

**-out:file:fullatom
-out:file:scorefile {name}.fasc** <br>
The file name can be {name}.loops 
