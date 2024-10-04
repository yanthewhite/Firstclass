
# calculate the cost of the fiber optic cable
# DSC 510
# Week 2
# Programming Assignment Week 2
# Author TOUKA
# 9/8/2024
print('welcome to the fiber optic calculator')
company=input("please enter your company name : ")
feet=input("please enter the number of feet of cable : ")
cost=int(feet)*0.87
print('Receipt for ',company)
print('Number of feet of cable to install :',feet )
print("Total cost: $ {0:<8.2f} ".format(cost))