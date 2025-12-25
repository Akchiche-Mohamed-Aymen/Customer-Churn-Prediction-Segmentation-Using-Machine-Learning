from schemas import ChurnOne , ChurnZero
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage , SystemMessage
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from keys import key

#==================================================
def createRecommandations(churn, churn_probability):
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
