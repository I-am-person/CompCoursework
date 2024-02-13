import math
import streamlit as st
import pandas as pd
import numpy as np
from datetime import date
import data
import time

# def budgetResetButtonCallback():
#     data.budgetCost = []
#     data.budgetName = []
    
    

#Home page
def homePage():
    st.title("Home")
    category = True
    if category:
        data.totalIncome = st.number_input("Monthly Income")
        home_cost = st.number_input("Cost to maintain home")
        transportation_cost = st.number_input("Transportation cost")
        if st.button("done"):
            data.initialBudget = data.totalIncome - home_cost - transportation_cost
            data.budgetLeft = data.initialBudget
            st.session_state.initialBudget = data.initialBudget
            st.session_state.budgetLeft = data.budgetLeft
            #st.session_state.budgetValue = 0
            "Initial Budget:", str(data.initialBudget).split(".")[0]
            if initalBudget <= 0: 
                st.write(":red[You may have keyed in one or more variable wrongly! Please re-key in your values.]")

#Budget page
def budgetPage():
    if 'initialBudget' not in st.session_state:
        st.session_state.initialBudget = data.initialBudget
    if 'budgetLeft' not in st.session_state:
        st.session_state.budgetLeft = data.budgetLeft
    if 'budgetValue' not in st.session_state:
        st.session_state.budgetValue = 0
    # if 'budgetValueArray' not in st.session_state:
    #     st.session_state.budgetValueArray = []
    # if 'budgetNameArray' not in st.session_state:
    #     st.session_state.budgetNameArray = []
    if data.initialBudget == 0:
        st.warning(":red[Please input a valid income]",icon="⚠️")
    else:
        if st.session_state.budgetLeft - st.session_state.budgetValue >= 0:
            st.session_state.budgetLeft -= st.session_state.budgetValue
        if st.session_state.budgetLeft/st.session_state.initialBudget < (data.warning/100):
            st.warning(f"Budget left is less than {data.warning}% of total budget",icon="⚠️")
        st.title("Budget")
        "Initial Budget:", str(data.initialBudget)
        "Budget Left:", str(st.session_state.budgetLeft)
        #"Budget Left:", st.session_state.budgetLeft
        budget_i = True
        if budget_i:
            def budgetButtonCallback():
                #st.write(st.session_state.budgetName)
                #st.write(st.session_state.budgetValue)
                #st.session_state.budgetLeft -= st.session_state.budgetValue
                
                if st.session_state.budgetValue <= 0 or st.session_state.budgetName == "":
                    st.write(":red[Please input a valid value/name]")
                elif st.session_state.budgetLeft - st.session_state.budgetValue <= 0:
                    st.write(":red[Amount spent has exceeded budget!]")
                else:
                    # data.budgetLeft -= budget_value
                    # st.session_state.budgetValueArray.append(st.session_state.budgetValue)
                    # st.session_state.budgetNameArray.append(st.session_state.budgetName)
                    data.budgetCost.append(budget_value)
                    data.budgetName.append(budget_name)
            # with st.form(key='budget_form'):
            with st.form("budget_form"):
                budget_name = st.text_input("",label_visibility="collapsed",placeholder="Expenditure name",key='budgetName')
                budget_value = st.number_input("Expenditure value", key='budgetValue')
                submit = st.form_submit_button('Done', on_click=budgetButtonCallback())
                
            # doneButton = st.button(label="Done", on_click=budgetButtonCallback())
            #st.write(invalid_value)
        
        st.write(pd.DataFrame({
        'Expenditure Name': data.budgetName,
        'Expenditure Cost': data.budgetCost,
        }))
        
#base values before starting
def settingsPage():
    st.title("Settings")
    data.warning = st.number_input("Percentage at which to display the warning at",value = data.warning)
    if st.button("Reset Settings"):
        data.warning = 30
    if st.button("Reset Values"):
        data.value = 0
        data.initialBudget = 0
        data.budgetLeft = 0
        data.totalIncome = 0
        data.totalExpense = []
        data.budgetCost = []
        data.budgetName = []
        data.categories = []
        data.valueArray = []
        data.page_data = 0
        data.budgetValue = 0
        

# = Main code = 
invalid_value = ""
budget_value = 0

# Page selection
st.sidebar.title("Budgeteer")
page = data.page_data
if st.sidebar.button("Home"):
    page = 0
    data.page_data = 0
if st.sidebar.button("Budget"):
    page = 1
    data.page_data = 1
if st.sidebar.button("Settings"):
    page = 2
    data.page_data = 2
# Run pages
if page == 0:
    homePage()
elif page == 1:
    budgetPage()
elif page == 2:
    settingsPage()
