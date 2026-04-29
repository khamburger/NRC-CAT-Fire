## CAT Fire Data


### Thermogravimetric Analysis (TGA)
Data Format: [Time (s), Temperature (K), Mass (mg)]. 

File naming convention: MatlID-AgingConditions_Gas_HeatingRate_TestReplicate.csv

A NETZSCH STA 449 F3 Jupiter was used to simultaneously conduct Thermogravimetric Analysis (TGA) experiments.

* Heating Rate: 10 K/min
* Temperature program
  - Initial Temperature: 30 C
  - Initial Isotherm: None (though stability criteria provides ~20 minutes continuous N2 flow at 30 C)  
  - Maximum Temperature: 700 C
  - Final Isotherm: None
* Sample mass: 5 mg +/- 0.1 mg
* Sample geometry: Whole piece cut from cable insulation or jacket
* Calibration type: At the start of each day of testing, a baseline test was performed using an empty crucible. Temperature calibration was performed at the start of this test series (April 2026) using a set of 6 reference metals with transition temperature between 156.6 C to 961.8 C. The onset temperature of melting was determined by crossing point method comparing measured versus expected temperature rise.
* Crucible
  - Type: Al2O3
  - Volume: 85 uL
  - Diameter: 6.8 mm
  - Mass: Approx. 140 mg
  - Lid: False
  - Note: 
* Carrier Gas
  - Type: Nitrogen
  - Flow rate: 50 ml/min (20 mL/min purge, 30 mL/min protective)
  - Note: Ultra High Purity (UHP) Nitrogen
* Instrument
  - Type: NETZSCH STA 449 F3 Jupiter
  - Furnace Type: Platinum
  - Notes: None

## Elongation at Break (EAB)
Data Format: [Time (s), Displacement (mm),  force (N)]. 

File naming convention: MatlID-AgingConditions_StrainRate_TestReplicate.csv