import ROOT
import array

# Create a ROOT TFile to hold the histogram
output_file = ROOT.TFile("template_dEdXUncertainty.root", "RECREATE")

lines = open("run1_data_dedx_uncertainty.txt").readlines()
## Phi bin
header_row = lines[0]
phi_values = []
for w in header_row.split():
  phi_values.append( float(w) )
NPhi = len(phi_values)

graph_dEdXRelUnc_dEdX_vs_phi = ROOT.TGraph2D()

graph_entry_counter = 0
for i_line, line in enumerate(lines):
  if i_line==0:
    continue
  words = line.split()
  this_dEdX = float(line.split()[0])
  for i_col in range(1, NPhi+1):
    this_phi = phi_values[i_col-1]
    this_value = float(words[i_col])

    graph_dEdXRelUnc_dEdX_vs_phi.SetPoint(graph_entry_counter, this_dEdX, this_phi, this_value*0.01)
    graph_entry_counter += 1

# Write the TGraph2D to the output file
output_file.cd()
graph_dEdXRelUnc_dEdX_vs_phi.SetName("dEdXRelUncertainty_dEdX_vs_phi")
graph_dEdXRelUnc_dEdX_vs_phi.Write()
output_file.Close()

