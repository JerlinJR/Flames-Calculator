import sys
import maskpass

def die(message):
    sys.exit(message)
    
def genderCheckGirl(name):
        if len(name) > 0 and name[len(name) - 1] == 'a' or name[len(name) - 1] == 'i' or name[len(name) - 1] == 'y':
            return name
        else:
            die("Please Enter Girl Name Properly")
            
def genderCheckBoy(name):
        if len(name) > 0 and name[len(name) - 1] == 'a' or name[len(name) - 1] == 'i': 
            die("Please Enter Boy Name Correctly")
        else:
            return name
            
def remove_match_char(list1, list2):

	for i in range(len(list1)):
		for j in range(len(list2)):

			if list1[i] == list2[j]:
				c = list1[i]

				list1.remove(c)
				list2.remove(c)

				list3 = list1 + ["*"] + list2

				return [list3, True]

	list3 = list1 + ["*"] + list2
	return [list3, False]


# Driver code
if __name__ == "__main__":

	Boy = input("Boy Name : ")

	Boy = genderCheckBoy(Boy.lower())

	Boy.replace(" ", "")

	Boy_list = list(Boy)

	#Girl = input("Girl Name : ")
	Girl = maskpass.askpass(prompt="Girl Name:", mask="❤")
   
	Girl = genderCheckGirl(Girl.lower())
	Girl.replace(" ", "")
	Girl_list = list(Girl)
	proceed = True

	while proceed:

		ret_list = remove_match_char(Boy_list, Girl_list)

		con_list = ret_list[0]

		proceed = ret_list[1]

		star_index = con_list.index("*")

		Boy_list = con_list[: star_index]

		Girl_list = con_list[star_index + 1:]

	count = len(Boy_list) + len(Girl_list)

	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

	while len(result) > 1:

		split_index = (count % len(result) - 1)
  
		if split_index >= 0:

			right = result[split_index + 1:]
			left = result[: split_index]

			result = right + left

		else:
			result = result[: len(result) - 1]

	print("Relationship status :", result[0])
