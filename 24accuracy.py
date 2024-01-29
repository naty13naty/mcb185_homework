# a program that returns the accuracy and F1 score by Naty Tsegai

def accuracy_f1(tp, tn, fp, fn):
	accuracy = (tp + tn)/ (tp + tn + fp +fn)
	precision = tp / (tp + fp)
	recall = tp / (tp + fn)
	f1_score = 2 * (precision * recall) / (precision + recall)
	assert(tp + tn + fp + fn > 0)
	assert(precision + recall > 0)
	assert(tp + fp > 0)
	return accuracy, f1_score
	
#testing the program	
print(accuracy_f1(5, 32, 66, 89))
print(accuracy_f1(9, 13, 53, 24))