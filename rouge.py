from pyrouge import Rouge155
r = Rouge155()
 
r.system_dir = 'data/system_summaries'
r.model_dir = 'data/model_summaries'
r.system_filename_pattern = 'summary.(\d+).txt'
r.model_filename_pattern = 'summary.[A-Z].#ID#.txt'
 
output = r.convert_and_evaluate()
print(output)
output_dict = r.output_to_dict(output)

