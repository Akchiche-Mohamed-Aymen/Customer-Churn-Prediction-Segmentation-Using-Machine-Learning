import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
from get_recom import createRecommandations
from api import predict_churn
# Page configuration
st.set_page_config(
    page_title="Churn Prediction System",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern UI
st.markdown("""
    <style>
    /* Main background and colors */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Card styling */
    .prediction-card {
        background: white;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        margin: 1rem 0;
    }
    
    /* Header styling */
    .main-header {
        color: white;
        text-align: center;
        padding: 2rem 0;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .sub-header {
        color: white;
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        opacity: 0.9;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Result styling */
    .result-positive {
        background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    .result-negative {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        margin: 2rem 0;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: none;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 7px 20px rgba(0,0,0,0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background: rgba(255, 255, 255, 0.95);
    }
    
    /* Input fields */
    .stNumberInput>div>div>input,
    .stSelectbox>div>div>select {
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        padding: 0.5rem;
    }
    
    /* Section divider */
    .divider {
        height: 2px;
        background: linear-gradient(90deg, transparent, white, transparent);
        margin: 2rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🎯 Customer Churn Prediction System</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Predict customer churn probability using advanced analytics</p>', unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.markdown("### 📝 Customer Information")
    st.markdown("---")
    
    # Personal Information
    st.markdown("#### 👤 Personal Details")
    age = st.number_input("Age", min_value=18, max_value=100, value=35, help="Customer's age")
    sex = st.selectbox("Sex", options=["Male", "Female"], help="Customer's gender")
    
    st.markdown("---")
    
    # Financial Information
    st.markdown("#### 💰 Financial Details")
    credit_score = st.slider("Credit Score", min_value=300, max_value=850, value=650, 
                             help="Customer's credit score (300-850)")
    balance = st.number_input("Account Balance ($)", min_value=0.0, max_value=300000.0, 
                              value=50000.0, step=1000.0, help="Current account balance")
    estimated_salary = st.number_input("Estimated Salary ($)", min_value=0.0, max_value=500000.0, 
                                       value=75000.0, step=5000.0, help="Annual estimated salary")
    
    st.markdown("---")
    
    # Account Information
    st.markdown("#### 🏦 Account Details")
    tenure = st.slider("Tenure (years)", min_value=0, max_value=60, value=3, 
                      help="Years as a customer")
    products_number = st.selectbox("Number of Products", options=list(range(0, 101)),
                                   help="Number of bank products owned")
    credit_card = st.radio("Has Credit Card?", options=["Yes", "No"], horizontal=True)
    active_member = st.radio("Active Member?", options=["Yes", "No"], horizontal=True)
    
    st.markdown("---")
    predict_button = st.button("🔮 Predict Churn", use_container_width=True)

# Main content area
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
        <div class="metric-card">
            <h3>💳 Credit Score</h3>
            <h2>{credit_score}</h2>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
        <div class="metric-card">
            <h3>⏱️ Tenure</h3>
            <h2>{tenure} years</h2>
        </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
        <div class="metric-card">
            <h3>🛍️ Products</h3>
            <h2>{products_number}</h2>
        </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
        <div class="metric-card">
            <h3>💰 Balance</h3>
            <h2>${balance:,.0f}</h2>
        </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Prediction logic
if predict_button:
    data = {
        'age': [age],
        'Female': [int(sex != "Male")],
        'Male': [int(sex == "Male")],
        'credit_score': [credit_score],
        'balance': [balance],
        'estimated_salary': [estimated_salary],
        'tenure': [tenure],
        'products_number': [products_number],
        'credit_card': [int(credit_card == "Yes")],
        'active_member': [int(active_member == "Yes")]
    }
    with st.spinner("🔄 Analyzing customer data..."):
        churn_prediction, churn_probability = predict_churn(data)
        st.markdown("---")
        recommandations = createRecommandations(churn_prediction, churn_probability)
        if churn_prediction == 1:
            st.markdown(f"""
                <div class="result-positive">
                    ⚠️ HIGH CHURN RISK DETECTED<br>
                    <span style="font-size: 3rem;">📉</span><br>
                    Churn Probability: {churn_probability}%
                </div>
            """, unsafe_allow_html=True)
            
            st.error("### 🚨 Recommended Actions:")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                - 📞 **Immediate Contact**: {recommandations['immediate_contact']}
                - 🎁 **Retention Offer**: {recommandations['retention_offer']}
                - 💬 **Feedback Session**: {recommandations['feedback_session']}
                """)
            with col2:
                st.markdown(f"""
                 - 💡 **Personalized Service**: {recommandations['personalized_service']}
                -  📊 **Account Review**: {recommandations['account_review']}
                -  🌟 **Product Upgrade**: {recommandations['product_upgrade']}
                """)
    
        else:
            st.markdown(f"""
                <div class="result-negative">
                    ✅ LOW CHURN RISK<br>
                    <span style="font-size: 3rem;">📈</span><br>
                    Churn Probability: {churn_probability}%
                </div>
            """, unsafe_allow_html=True)
            
            st.success("### 🎉 Customer Retention Status: GOOD")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown(f"""
                - ✨ **Maintain Engagement**: {recommandations['maintain_engagement']}
                - 🎁 **Loyalty Rewards**: {recommandations['loyalty_rewards']}
                - 🌟 **Upsell Opportunities**: {recommandations['upsell_opportunities']}
                """)
            with col2:
                st.markdown(f"""
                 - 💡 **Regular Monitoring**: {recommandations['regular_monitoring']}
                -  📊 **Value Addition**: {recommandations['value_addition']}
                -  🌟 **VIP Treatment**: {recommandations['vip_treatment']}
                """)
        
        # Customer profile summary
        st.markdown("---")
        st.markdown("### 📋 Customer Profile Summary")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
                <div class="prediction-card">
                    <h4>Personal Info</h4>
                    <ul style="text-align: left;">
                        <li>Age: """ + str(age) + """</li>
                        <li>Sex: """ + sex + """</li>
                        <li>Tenure: """ + str(tenure) + """ years</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class="prediction-card">
                    <h4>Financial Info</h4>
                    <ul style="text-align: left;">
                        <li>Credit Score: """ + str(credit_score) + """</li>
                        <li>Balance: $""" + f"{balance:,.0f}" + """</li>
                        <li>Salary: $""" + f"{estimated_salary:,.0f}" + """</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
                <div class="prediction-card">
                    <h4>Account Info</h4>
                    <ul style="text-align: left;">
                        <li>Products: """ + str(products_number) + """</li>
                        <li>Credit Card: """ + credit_card + """</li>
                        <li>Active: """ + active_member + """</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: white; opacity: 0.8; padding: 2rem;">
        <p>🔒 Secure & Confidential | Built with Streamlit | © 2025 Churn Prediction System</p>
    </div>
""", unsafe_allow_html=True)

#python -m streamlit run UI.py