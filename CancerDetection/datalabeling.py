import pandas as pd

if __name__ == '__main__':
	# # load up each data set and try to label it
	# # bladder
	# bladder = pd.read_csv("data/DNA/imputed_bladder.txt", sep = '\t', header = None)
	# bladder = bladder.transpose()
	# bladder["Cancer"]= 0
	# bladder.set_value(list(range(102,124)), "Cancer", -1)
	# bladder.set_value(list(range(0,6)), "Cancer", 1)
	# bladder.set_value(list(range(7,102)), "Cancer", 1)
	# bladder.set_value(list(range(124,126)), "Cancer", 1)



	# # colon
	# colon = pd.read_csv("data/DNA/imputed_colon.txt", sep = ' ', header = None)
	# colon = colon.transpose()
	# print(colon.shape)
	# colon["Cancer"] = 0
	# colon.set_value(list(range(40,63)), "Cancer", -1)
	# colon.set_value(list(range(0,40)), "Cancer", 1)
	# print(colon)

	# leuk
	# leuk = pd.read_csv("data/DNA/imputed_leuk.txt", sep = '\t', header = None)
	# leuk = leuk.transpose()
	# leuk['Cancer'] = 0
	# leuk.set_value(list(range(48,73)), "Cancer", -1)
	# leuk.set_value(list(range(0,48)), "Cancer", 1)
	# print('leuk',leuk)

	# # liver
	# liver = pd.read_csv("data/DNA/imputed_liver.txt", sep = '\t', header = None)
	# liver = liver.transpose()
	# liver["Cancer"] = 0
	# liver.set_value(list(range(115,191)), "Cancer", -1)
	# liver.set_value(list(range(8,112)), "Cancer", 1)
	# liver.set_value(4, "Cancer", 1)
	# print(liver["Cancer"])


	# prostate
	# prostate = pd.read_csv("data/DNA/imputed_prostate.csv", header = None)
	# print(prostate)
	# print(prostate.shape)
	# prostate = prostate.rename(index=str, columns={0: "Cancer"})
	# print(prostate)

	# # write them all out

	# bladder.to_csv('data/DNA/labeled_baddler.csv')
	# leuk.to_csv('data/DNA/labeled_leuk.csv')
	# liver.to_csv('data/DNA/labeled_liver.csv')
	# prostate.to_csv('data/DNA/labeled_prostate.csv')
