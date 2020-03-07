### Next-Generation Kinematic Loop Closure (NGK)
To perform a loop closure in Rosetta, firstly prepare a flag file: <br>
  **-in:file:s {name}.pdb <br>
-in:file:fullatom <br>
-loops:loop_file cbCDR3.loops <br>
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
The file name can be {name}.loops 
