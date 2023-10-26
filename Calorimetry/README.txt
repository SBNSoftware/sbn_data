- run1_data_dedx_uncertainty.txt
  - First row and column are headers
  - Row: dE/dX (MeV/cm) bins
  - Column: Track phi in degrees (arccos(abs(trk.dir.x))*180/PI)
  - Data: dE/dX relative uncertainty for each (dE/dX, phi) bin; i.e., uncertaintiy in %
- MakeRootFile.py
  - Converts "run1_data_dedx_uncertainty.txt" to a root object (TGraph2D)
- template_dEdXUncertainty.root
  - Output of MakeRootFile.py

