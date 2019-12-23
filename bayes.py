def trimmed_input():
    input_str = input(">")
    output = ""
    for x in input_str:
        if(x.isnumeric() or x == "."):
            output += str(x)
        else:
            return output
            


print("Enter prior probability, probability that the hypothesis is true")

hyp_t = float(trimmed_input())/100


print("Enter likelihood of experiment, given hypothesis true")
like_hyp_t = float(trimmed_input())/100
print("Enter likelihood of experiment, given hypothesis false")
like_hyp_f = float(trimmed_input())/100

# compare the weightage of the two
hyp_f = 1-hyp_t

joint_true = hyp_t * like_hyp_t
joint_false = hyp_f * like_hyp_f

bayes = round((joint_true)/(joint_true + joint_false), 5) * 100

print("The Bayesian probability that the hypothesis is true is:", bayes, "%")


like_ratio = joint_true/joint_false
print("The ratio between the joint probabilities is: ", like_ratio)


