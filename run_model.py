import numpy as np
import yaml
import joblib
import argparse
from model_interface.paralel_MLmodel import get_result_157, init_worker_updated
import model_paths

xsdict = joblib.load(model_paths.__path_xs_pickle__)
fabulist = np.array([ 0. ,  0.1,  0.5,  1. ,  2. ,  4. ,  6. ,  8. , 10. , 12.5, 15. , 17.5, 20. , 25. , 30. , 35. , 40. , 45. , 50. , 55. , 60. , 65. , 70. , 75. , 80. ]) # list of depeltion steps used in xs generation
faaxial = np.array([15.24, 10.16,  5.08, 30.48, 30.48, 30.48, 30.48, 30.48, 30.48, 30.48, 30.48, 30.48, 30.48,  5.08, 10.16, 15.24])
corebulist =  [0.1, 0.4, 0.5, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
total_height = np.sum(faaxial)
idx11 = [0]
idx22 = [1,2,3,4,5,6,7,9,18,27,36,45,54,63]
initbumap = np.zeros((1,81,16))


class input_parser():
    def __init__(inp_file):
        with open(inp_file) as f:
            try:
                input_data = yaml.safe_load(f)
            except yaml.parser.ParserError:
                raise yaml.parser.ParserError("Trouble reading the '.yaml' input file. Please check the integrity of the input, including the consistency of spaces!")
        return input_data

    def construct_quarter_core(incomplete_LP):
        new_LP = [incomplete_LP[0],incomplete_LP[1],incomplete_LP[10],incomplete_LP[19],incomplete_LP[28],incomplete_LP[37],incomplete_LP[46],incomplete_LP[55],incomplete_LP[64]] 
        for assemb in incomplete_LP[1:]:
            new_LP.append(assemb)
        return new_LP


class initialize():
    def Parse_Args():
        input_help_message = 'Input file containing all the information needed to perform the optimization routine.\n'
        input_help_message += ' Input file extension needs to be a .yaml file.'
        parser = argparse.ArgumentParser()
        parser.add_argument('--input',help=input_help_message,
                            required=False,type=str,default=None)
        return parser.parse_args()

parser = initialize.Parse_Args()
input_data = input_parser.__init__(parser.input)
LPs = input_parser.construct_quarter_core(input_data['loading_pattern'])
init_worker_updated()
Fd_all, Fq_all, maxboron, cycle_length = get_result_157(LPs, corebulist, xsdict, fabulist, faaxial, total_height, idx11, idx22, initbumap)

print("Prediction Complete")

with open("core_output.txt", "w") as f:
    f.write("-Core Performance Prediction Complete-\n")
    f.write("\n")
    f.write("Core: \n")
    f.write(f"   {LPs[0]}\n")
    for start in range(9, 81, 9):
        row = LPs[start:start+9]
        f.write(" ".join(f"{str(x):>6}" for x in row) + "\n")
    f.write("\n")
    f.write("\n")
    f.write("Performance Parameters:  \n")
    f.write(f"Max Enthalpy Rise Peaking Factor: {round(float(Fd_all),3)}\n")
    f.write(f"Max Pin Power Peaking Factor: {round(float(Fq_all),3)}\n")
    f.write(f"Max Critical Boron Concentration (ppm): {round(float(maxboron),3)}\n")
    f.write(f"Cycle Length (EFPD): {round(float(cycle_length),3)}\n")
    f.write("\n\n")