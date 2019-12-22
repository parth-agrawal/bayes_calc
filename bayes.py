print("Enter prior probability, probability that the hypothesis is true")
hyp_t = float(input(">"))
print("Enter likelihood of experiment, given hypothesis true")
like_hyp_t = float(input(">"))
print("Enter likelihood of experiment, given hypothesis false")
like_hyp_f = float(input(">"))

# compare the weightage of the two
hyp_f = 1-hyp_t

bayes = round((hyp_t * like_hyp_t)/(hyp_t * like_hyp_t + hyp_f * like_hyp_f), 4) * 100

print("The Bayesian probability that the hypothesis is true is:", bayes, "%")

