import os
import sys


in_path = sys.argv[1] #input file

out_path = sys.argv[2] #output file

scores_path = sys.argv[3] #scores file

ngbs = sys.argv[4] #number of neighbours in reliefF

topn = sys.argv[5] #number of SNPs to be selected

os.system('java -jar mdr_3.0.2.jar -filter=RELIEFF -parallel -relieff_neighbors={neighbours} -select_N={topn} {input_file} {output_file} > {scores_file}'.format(neighbours = ngbs, topn = topn, input_file = in_path, output_file = out_path, scores_file = scores_path))
		