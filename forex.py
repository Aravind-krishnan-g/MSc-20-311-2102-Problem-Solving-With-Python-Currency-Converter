#!/usr/bin/env python
# coding: utf-8

# # ONLINE CURRENCY CONVERTER

# In[ ]:


# pip install forex-python streamlit


# ## IMPORTING LIBRARIES

# Documentations for these libraries: [forex_python](https://forex-python.readthedocs.io/en/latest/index.html) and [streamlit](https://docs.streamlit.io/en/stable/index.html)

# In[11]:


from forex_python.converter import CurrencyRates # module to convert currency
import streamlit as st # web app framework library


# ## MAIN CODE

# In[12]:


class converter:
    
    def __init__(self):
        # the below dictionary contains collection of supported currencies in forex_python
        # dictionary keys represent common currency names
        # while values are their corresponding 3 letter code
        self.dict_of_currencies = {'Euro Member Countries':'EUR', 'Indonesia Rupiah'    :'IDR', 'Bulgaria Lev'       :'BGN',
                              'Israel Shekel'        :'ILS', 'United Kingdom Pound':'GBP', 'Denmark Krone'      :'DKK',
                              'Canada Dollar'        :'CAD', 'Japan Yen'           :'JPY', 'Hungary Forint'     :'HUF',
                              'Romania New Leu'      :'RON', 'Malaysia Ringgit'    :'MYR', 'Sweden Krona'       :'SEK',
                              'Singapore Dollar'     :'SGD', 'Hong Kong Dollar'    :'HKD', 'Australia Dollar'   :'AUD',
                              'Switzerland Franc'    :'CHF', 'South Korea Won'     :'KRW', 'China Yuan Renminbi':'CNY',
                              'Turkey Lira'          :'TRY', 'Croatia Kuna'        :'HRK', 'New Zealand Dollar' :'NZD',
                              'Thailand Baht'        :'THB', 'United States Dollar':'USD', 'Norway Krone'       :'NOK',
                              'Russia Ruble'         :'RUB', 'India Rupee'         :'INR', 'Mexico Peso'        :'MXN',
                              'Czech Republic Koruna':'CZK', 'Brazil Real'         :'BRL', 'Poland Zloty'       :'PLN',
                              'Philippines Peso'     :'PHP', 'South Africa Rand'   :'ZAR' }
        
        self.c = CurrencyRates() # creating an object of the module

    # function 'display' will contain the web framework using streamlit
    def display(self): 
        
        st.title('Online currency converter')   # setting title of the app      
        exp= st.beta_expander("About") # 'About' section contains details about the project
        exp.write("This web application was developed using [forex-python](https://forex-python.readthedocs.io/en/latest/index.html) and [streamlit](https://docs.streamlit.io/en/stable/index.html) web application framework.")
        exp.write(" This project was done as a part of Msc-Problem solving with python course.") 
        exp.write("You can check out the work at [github](https://github.com/Aravind-krishnan-g/MSc-20-311-2102-Problem-Solving-With-Python-Currency-Converter)")
        
        option=st.selectbox('Select an option',['Get forex rate','Convert currency']) # user can select either of 2 options
        option1 = st.selectbox('Select a currency',list(self.dict_of_currencies.keys())) # selecting 1st currency
        try:
            if(option == 'Convert currency'):
                amount=st.number_input("Enter amount to convert") # area to enter amount to convert
            else:
                amount=1.0   
        except:
            st.error("Error occured. Please ensure that you entered a number!")
        option2 = st.selectbox('Select another currency',list(self.dict_of_currencies.keys())) # selecting second currency
        c1=self.dict_of_currencies[option1] # converting currency to 3 letter code
        c2=self.dict_of_currencies[option2] # converting currency to 3 letter code
        
        if c1 and c2 : # checking whether both currency options are entered
            if(st.button("Show")): # button to show result
                with st.spinner('Calculating.....'):
                    output=self.c.convert(c1,c2,amount) # calculating conversion
                st.write("Selected conversion : ",option1," to ",option2)
                st.write(amount," ",option1," = ",output," ",option2) # displaying result
                        
    


# ## DRIVER CODE

# In[13]:



class_object = converter() # creating class object
class_object.display() # calling web application

