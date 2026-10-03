total_chores=5
original_count=total_chores
print(f"You have {original_count} chores to complete today!.\n")

complete_count=0
count_num=1

while count_num<=total_chores:
     if count_num==1:
          next_chore="Make your bed"
     elif count_num==2:
            next_chore="Do the dishes"
     elif count_num==3:
            next_chore="Make breakfast"
        
     answer=input(f"Have you finished: {next_chore}?(yes/no):")

     if answer=="yes":
            complete_count+=1
            count_num+=1
            print("Great chore complete!")
     else:
           print("Ok,Finish and check again.")
     print(f"Remaining chores:{total_chores-complete_count}")
     print()

