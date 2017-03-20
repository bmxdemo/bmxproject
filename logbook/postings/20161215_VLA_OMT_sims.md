## Dec 15, 2016: VLA OMT + transition HFSS modeling

After visiting Michigan, I began to design a transition to couple the OMT to a feed horn. We decided to base the transition on one designed for the VLA at 1-2 GHz. (Here is the paper: 
[05722981.pdf](https://github.com/bmxdemo/bmxproject/files/655665/05722981.pdf)). Because of the dimension mismatch at the back of the transition relative to the OMT, however, I could not get good enough throughput. We probably could have tweaked the transition design to work, but it became clear a simple scaled version of the VLA OMT + VLA transition was both more compact and higher throughput than the existing OMT. We thus decided to go with this design.

The VLA design is quite fancy. There are a series of orthogonal "shorting blocks" instead of a single backshort. These reflect only the TE01 and TE10 modes, respectively, which allows the conductor height above the backshort be identical for each polarization. The TE11 mode propagates through the shorting blocks and is absorbed by some absorber placed at the back. I drew the VLA OMT + transition in HFSS and scaled it up by a factor 1.43. 

Figure 1 shows S21 for the VLA design, including the shorting blocks and absorber. Figure 2 shows the same design but eliminating the blocks and absorber and drawing in a single backshort, splitting the difference between the optimal x and y coax heights. (I also decreased the coax spacing.) The main differences are that there is slightly different coupling for x and y without the shorting blocks, and that there is a narrow null in S21 at 0.83 GHz owing to the TE11 mode propagation without the absorber.

### Figure 1 - VLA OMT + transition with blocks and absorber
![omt_vla_blocks_plus_vla_s21_withabsorber](https://cloud.githubusercontent.com/assets/6098508/21239855/b9cd56d2-c2d6-11e6-92ea-d4045a7e97f6.png)

### Figure 2 - VLA OMT + transition without blocks and absorber
![omt_vla_noblocks_plus_vla_s21](https://cloud.githubusercontent.com/assets/6098508/21239955/2eed8b4e-c2d7-11e6-95a1-c006ca848c6b.png)

Figure 3 shows S21 for modes other than TE01 and TE10 (x and y), which just proves what the paper says, that it is TE11 causing the problem at 0.83 GHz.  (TE11 is trans3 as labeled in the HFSS model, and I checked the mode vector pattern, it is indeed TE11.)

### Figure 3 - higher order modes in the VLA sans blocks design
![omt_transition_final_noblocks_s21](https://cloud.githubusercontent.com/assets/6098508/21240068/abad5790-c2d7-11e6-8f14-a605c3a6b4c7.png)

The design is much easier and cheaper to manufacture without the blocks and absorber, and it is only a very narrow frequency range affected by the higher order mode propagaion. Therefore, we've decided to proceed with the modified VLA design with a single backshort.
