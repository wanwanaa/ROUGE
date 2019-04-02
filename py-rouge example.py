# Py-rouge
import rouge


def prepare_results(p, r, f):
    return '\t{}:\t{}: {:5.2f}\t{}: {:5.2f}\t{}: {:5.2f}'.format(metric, 'P', 100.0 * p, 'R', 100.0 * r, 'F1', 100.0 * f)


for aggregator in ['Avg', 'Best', 'Individual']:
    print('Evaluation with {}'.format(aggregator))
    apply_avg = aggregator == 'Avg'
    apply_best = aggregator == 'Best'

    evaluator = rouge.Rouge(metrics=['rouge-n', 'rouge-l', 'rouge-w'],
                           max_n=4,
                           limit_length=True,
                           length_limit=100,
                           length_limit_type='words',
                           apply_avg=apply_avg,
                           apply_best=apply_best,
                           alpha=0.5, # Default F1_score
                           weight_factor=1.2,
                           stemming=True)

    # all_hypothesis = ['I am a student and come from China.\n I am a student']
    # all_references = ['I am a student from China.\n I am girl']
    all_hypothesis = ['228 1755 2205 494 62 20 1060 36 96 97 23 322 571 20 247 560 341 341\n375 1345 1575 1576 1577 1269 192 181 18 1294 1015 1016 419']
    all_references = ['228 1755 2205 511 512 430 199 494 62 1060 36\n227 1047 844 23 96 1537 229 404 74 192 77 33 34 753 121 20 252 23 184 1363 37']

    scores = evaluator.get_scores(all_hypothesis, all_references)

    # for metric, results in sorted(scores.items(), key=lambda x: x[0]):
    #     if not apply_avg and not apply_best: # value is a type of list as we evaluate each summary vs each reference
    #         for hypothesis_id, results_per_ref in enumerate(results):
    #             nb_references = len(results_per_ref['p'])
    #             for reference_id in range(nb_references):
    #                 print('\tHypothesis #{} & Reference #{}: '.format(hypothesis_id, reference_id))
    #                 print('\t' + prepare_results(results_per_ref['p'][reference_id], results_per_ref['r'][reference_id], results_per_ref['f'][reference_id]))
    #         print()
    #     else:
    #         print(prepare_results(results['p'], results['r'], results['f']))
    print(scores)