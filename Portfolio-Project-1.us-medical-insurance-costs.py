#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs

# # Comprehensive Insurance Dataset Analysis Project
# 
# ### Introduction
# 
# This Jupyter Notebook embarks on a comprehensive analysis of the "insurance.csv" dataset, with a primary focus on comparing insurance costs between smokers and non-smokers. The dataset encompasses seven columns:
# 
# Age: Integer representing the age of the insured.
# Sex: String indicating the gender of the insured (male/female).
# BMI: Float representing the Body Mass Index of the insured.
# Children: Integer indicating the number of children/dependents covered by the insurance.
# Smoker: Boolean value specifying whether the insured is a smoker (yes/no).
# Region: String denoting the region of the insured.
# Charges: Float representing the insurance charges.
# 
# ### Project Scope and Goals
# 
# Average Age Calculation: Determine the average age of the patients in the dataset.
# 
# Gender Distribution: Return the count of males and females present in the dataset.
# 
# Geographical Analysis: Identify the geographical distribution of patients based on their regions.
# 
# Average Yearly Medical Charges: Calculate and return the average yearly medical charges incurred by the patients.
# 
# Insurance Cost Comparison:
# 
# Calculate the average insurance charges for male smokers.
# Calculate the average insurance charges for male non-smokers.
# Calculate the average insurance charges for female smokers.
# Calculate the average insurance charges for female non-smokers.
# Compare insurance costs between male smokers and male non-smokers.
# Compare insurance costs between female smokers and female non-smokers.
# 
# ### Implementation Details
# 
# To perform these inspections,define a class named PatientsInfo, containing five methods:
# 
# analyze_ages(): Calculates the average age of the patients.
# analyze_sexes(): Returns the count of males and females in the dataset.
# unique_regions(): Identifies the unique geographical regions represented in the dataset.
# average_charges(): Calculates and returns the average yearly medical charges incurred by the patients.
# insurance_cost_comparison(): Compares insurance costs between male smokers, male non-smokers, female smokers, and female non-smokers.
# 
# This comprehensive analysis aims to provide detailed insights into various facets of the dataset. By focusing on demographic distribution, regional representation, and tailored comparisons of insurance costs based on gender and smoking habits, the analysis offers a comprehensive exploration of the dataset. The PatientsInfo class facilitates the execution of these operations, enhancing the overall understanding of the dataset.

# ### 1. Data Loading:
# 
# Use the csv library to read the "insurance.csv" file.
# Create a list of dictionaries, where each dictionary represents a row in the dataset.

# In[6]:


import csv

data_list = []
with open('insurance.csv','r') as insurance_csv:
    file_dict = csv.DictReader(insurance_csv)
    for row in file_dict:
        data_list.append(row)


# In[7]:


print(data_list[:5])


# ### 2. Class Creation:
# 
# Define a class named PatientsInfo to encapsulate the analysis methods.
# 
# 2. Class Methods:
# 
# 2.1 analyze_ages():
# Calculate the average age of the patients.
# 
# 2.2 analyze_sexes():
# Return the count of males and females in the dataset.
# 
# 2.3 unique_regions():
# Identify the unique geographical regions represented in the dataset.
# 
# 2.4 average_charges():
# Calculate and return the average yearly medical charges incurred by the patients.
# 
# 2.5 insurance_cost_comparison():
# 
# Calculate the average insurance charges for male smokers.
# Calculate the average insurance charges for male non-smokers.
# Compare insurance costs between male smokers and male non-smokers.
# 
# Calculate the average insurance charges for female smokers.
# Calculate the average insurance charges for female non-smokers.
# Compare insurance costs between female smokers and female non-smokers.

# In[190]:


class PatientsInfo:
    def __init__(self, data_list):
        self.data_list = data_list
    
    def analyze_ages(self):
        avg_age = 0
        for i in range(len(self.data_list)):
            avg_age += int(self.data_list[i]['age'])
        return avg_age / len(data_list)
    
    def analyze_sexes(self):
        males = 0
        females = 0
        for i in range(len(self.data_list)):
            if self.data_list[i]['sex'] == 'male':
                males += 1
            elif self.data_list[i]['sex'] == 'female':
                females += 1
        return ('Number of Male Patients is: '+str(males)+'. Number of Female Patients is: '+str(females))
    
    def unique_regions(self):
        regions = []
        for i in range(len(self.data_list)):
            if self.data_list[i]['region'] not in regions:
                regions.append(self.data_list[i]['region'])
        return regions
    
    def average_charges(self):
        avg_charge = 0
        for i in range(len(data_list)):
            avg_charge += float(self.data_list[i]['charges'])
        return ('The average charge for all patients is: $'+str(round(avg_charge/len(data_list),2)))
    
    def insurance_cost_comparison(self):
        male_smokers_avg_charge = 0
        male_non_smokers_avg_charge = 0
        female_smokers_avg_charge = 0
        female_non_smokers_avg_charge = 0
        
        male_smokers_count = 0
        male_non_smokers_count = 0
        female_smokers_count = 0
        female_non_smokers_count = 0
        
        for i in range(len(self.data_list)):
            if self.data_list[i]['sex'] == 'male' and self.data_list[i]['smoker'] == 'yes':
                male_smokers_avg_charge += float(self.data_list[i]['charges'])
                male_smokers_count += 1
            elif self.data_list[i]['sex'] == 'male' and self.data_list[i]['smoker'] == 'no':
                male_non_smokers_avg_charge += float(self.data_list[i]['charges'])
                male_non_smokers_count += 1
            elif self.data_list[i]['sex'] == 'female' and self.data_list[i]['smoker'] == 'yes':
                female_smokers_avg_charge += float(self.data_list[i]['charges'])
                female_smokers_count +=1
            elif self.data_list[i]['sex'] == 'female' and self.data_list[i]['smoker'] == 'no':
                female_non_smokers_avg_charge += float(self.data_list[i]['charges'])
                female_non_smokers_count += 1
        
        # Calculate average insurance cost for a single individual
        avg_cost_single_male_smoker = round(male_smokers_avg_charge / max(1, male_smokers_count), 2)
        avg_cost_single_male_non_smoker = round(male_non_smokers_avg_charge / max(1, male_non_smokers_count), 2)
        avg_cost_single_female_smoker = round(female_smokers_avg_charge / max(1, female_smokers_count), 2)
        avg_cost_single_female_non_smoker = round(female_non_smokers_avg_charge / max(1, female_non_smokers_count), 2)
        
        print("Male Smokers count: ",male_smokers_count)
        print("Male non Smokers count: ",male_non_smokers_count)
        print("Female Smokers count: ",female_smokers_count)
        print("female non Smokers count: ",female_non_smokers_count)
        
        print("\nThe average insurance cost for a single male smoker is: $", avg_cost_single_male_smoker)
        print("The average insurance cost for a single male non-smoker is: $", avg_cost_single_male_non_smoker)
        print("The average insurance cost for a single female smoker is: $", avg_cost_single_female_smoker)
        print("The average insurance cost for a single female non-smoker is: $", avg_cost_single_female_non_smoker)
        print("\nThe difference in insurance cost between a male smoker and non smoker is: $",round(avg_cost_single_male_smoker - avg_cost_single_male_non_smoker, 2))
        print("The difference in insurance cost between a female smoker and non smoker is: $",round(avg_cost_single_female_smoker - avg_cost_single_female_non_smoker, 2))


# In[191]:


patient_info = PatientsInfo(data_list)


# In[192]:


print(patient_info.analyze_ages())


# In[193]:


print(patient_info.analyze_sexes())


# In[194]:


print(patient_info.unique_regions())


# In[195]:


print(patient_info.average_charges())


# In[196]:


patient_info.insurance_cost_comparison()


# From the analysis, several observations and conclusions can be drawn:
# 
# Gender Disparity:
# 
# The dataset has a higher count of non-smoking individuals compared to smokers for both males and females.
# The average insurance cost for a single male smoker is significantly higher than that of a male non-smoker.
# Similarly, the average insurance cost for a single female smoker is considerably higher than that of a female non-smoker.
# Insurance Cost Disparities:
# 
# The difference in insurance costs between male smokers and non-smokers is substantial, indicating that being a smoker has a significant impact on insurance charges for males.
# The same pattern is observed for females, where smokers incur considerably higher insurance costs compared to non-smokers.
# Cost of Smoking:
# 
# Both male and female smokers, on average, face a higher financial burden for insurance compared to their non-smoking counterparts.
# The cost difference between smokers and non-smokers is notable, highlighting the financial implications of smoking on insurance charges.
# Consideration for Individuals:
# 
# The average insurance cost for a single male smoker is much higher than that of a single male non-smoker.
# The same pattern is observed for females, emphasizing the impact of smoking on individual insurance costs.
# Policy Implications:
# 
# These findings suggest that insurance policies may consider higher premiums for individuals who smoke, especially given the substantial difference in average insurance costs between smokers and non-smokers.
# Potential Further Investigation:
# 
# Additional exploration and statistical analysis could be conducted to understand other factors influencing insurance costs, such as BMI, number of children, or regional variations.
# Overall, the analysis underscores the financial consequences of smoking on health insurance costs, supporting the notion that smokers generally face higher insurance premiums compared to non-smokers.
