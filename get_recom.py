from schemas import ChurnOne , ChurnZero
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from keys import key

#==================================================
def getRecommandations(churn, churn_probability):
    responseClass = ChurnOne if churn == 1 else ChurnZero
    chat =  ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=1.0,  # Gemini 3.0+ defaults to 1.0
    max_tokens=100,
    timeout=None,
    api_key= key,
    max_retries=2
)
    
    parser = JsonOutputParser(pydantic_object=responseClass)
    prompt_template = PromptTemplate(
    template="{user_prompt}\n\n{format_instructions}",
    input_variables=["user_prompt"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    formatted_prompt = prompt_template.format(user_prompt= f'Churn: {churn}, Churn Probability: {churn_probability}%')
    messages = [
     SystemMessage(content=f"""
You are a customer retention and growth expert AI.

Your task is to generate clear, actionable, and realistic business
recommendations based on a machine learning churn prediction.

Rules:
- NEVER predict churn yourself.
- ONLY use the provided churn value (0 or 1).
- If churn = 1, focus on retention, risk mitigation, and re-engagement.
- If churn = 0, focus on loyalty, upselling, and long-term value growth.
- Recommendations must be specific, short (At most 15 words for each recommendation), practical, and measurable.
- Avoid generic advice.
- Output must have schema of the responseClass : {responseClass.model_json_schema()}

Context:
- Churn: {churn}
- Churn Probability: {churn_probability}%
"""),
     HumanMessage(content=formatted_prompt)
    ]
    response = chat.invoke(messages)
    return parser.parse(response.content)

def createRecommandations(churn, churn_probability):
    try:
        return getRecommandations(churn, churn_probability)
    except:
        recommandation = {}
        if churn == 1:
            recommandation['immediate_contact'] = "Contact the customer within 24 hours to address concerns."
            recommandation['retention_offer'] =  "Provide a personalized retention offer or discount."
            recommandation['feedback_session'] =  "Schedule a feedback call to understand dissatisfaction."
            recommandation['account_review']="Review recent account activity to identify issues."
            recommandation['personalized_service']="Assign a dedicated account manager if applicable."
            recommandation['product_upgrade'] = "Offer a trial of premium features to increase value."
        else:
            recommandation['maintain_engagement'] ="Maintain regular communication with the customer."
            recommandation['loyalty_rewards'] ="Reward loyalty with points, discounts, or perks."
            recommandation['upsell_opportunities'] ="Introduce relevant additional products or services."
            recommandation['regular_monitoring'] ="Continue monitoring engagement and usage patterns."
            recommandation['value_addition'] ="Share useful tips, insights, or educational content."
            recommandation['vip_treatment'] ="Acknowledge and appreciate the customer’s loyalty."
        return recommandation
