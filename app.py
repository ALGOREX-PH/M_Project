import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key
import warnings
from streamlit_option_menu import option_menu
from streamlit_extras.mention import mention
warnings.filterwarnings("ignore")

genai.configure(api_key=google_gemini_api_key)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 32768,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
)

st.set_page_config(page_title="Lex Project by Algorex Technologies", page_icon="", layout="wide")

with st.sidebar :
    st.image('images/Logo.png')
    with st.container() :
        l, m, r = st.columns((1, 3, 1))
        with l : st.empty()
        with m : st.empty()
        with r : st.empty()

    options = option_menu(
        "Dashboard", 
        ["Home", "About Us", "Model"],
        icons = ['book', 'globe', 'tools'],
        menu_icon = "book", 
        default_index = 0,
        styles = {
            "icon" : {"color" : "#dec960", "font-size" : "20px"},
            "nav-link" : {"font-size" : "17px", "text-align" : "left", "margin" : "5px", "--hover-color" : "#262730"},
            "nav-link-selected" : {"background-color" : "#262730"}          
        })



# Options : Home
if options == "Home" :

   st.title('The Lex Project by Algorex Technologies')
   st.subheader("Overview")
   st.write("The Lex Project is an innovative AI application designed to revolutionize the digital landscape of law firm websites. Our mission is to help legal practices enhance their online presence by delivering in-depth UX and UI reviews, coupled with actionable recommendations for improvement.")
   st.write("## Key Features")
   st.write("### 1. Automated UX/UI Analysis :")
   st.write("The Lex Project utilizes advanced machine learning algorithms to automatically evaluate the user experience and interface of law firm websites. This includes assessing navigation, layout, visual appeal, and overall usability.")
   st.write("### 2. Actionable Insights :")
   st.write("Our AI-driven analysis provides clear, actionable insights that law firms can implement to improve their website's performance. This includes suggestions for design enhancements, content restructuring, and navigation improvements.")
   st.write("### 3. Performance Metrics :")
   st.write("The Lex Project offers detailed performance metrics, including page load times, mobile responsiveness, and user engagement statistics. These metrics help law firms understand their website's strengths and areas for improvement.")
   st.write("### 4. Customizable Reports :")
   st.write("Users can generate customizable reports that highlight key findings and recommendations. These reports are designed to be easily understood by both technical and non-technical stakeholders, ensuring that all team members can contribute to the improvement process.")
   st.write("### 5. Benchmarking :")
   st.write("The Lex Project includes benchmarking features that allow law firms to compare their website's performance against industry standards and competitors. This provides valuable context and helps set realistic improvement goals.")
   st.write("## Benefits")
   st.write("Enhanced Client Experience: By optimizing their website's UX and UI, law firms can provide a more engaging and user-friendly experience for their clients, leading to higher satisfaction and retention rates.")
   st.write("Increased Conversion Rates: A well-designed website can lead to increased conversion rates, as potential clients are more likely to contact a law firm if they have a positive online experience.")
   st.write("Competitive Advantage: Law firms that leverage the Lex Project can gain a competitive edge by staying ahead of industry trends and ensuring their website meets the highest standards of usability and design.")
   st.write("Data-Driven Decisions: With access to detailed analytics and insights, law firms can make data-driven decisions to continually improve their online presence and client engagement.")
   st.write("## How It Works")
   st.write("1. Website Analysis: The user inputs the URL of the law firm website into the Lex Project platform.")
   st.write("2. AI Evaluation: Our AI models analyze the website, evaluating various aspects of UX and UI.")
   st.write("3. Report Generation: The Lex Project generates a comprehensive report detailing the findings and providing actionable recommendations.")
   st.write("4. Implementation: Law firms can use the insights and recommendations to make targeted improvements to their website.")
   st.write("5. Continuous Improvement: By regularly using the Lex Project, law firms can continuously monitor and enhance their website's performance.")
   st.write("The Lex Project is your partner in creating a compelling and effective online presence for your law firm. With our AI-driven insights and recommendations, you can ensure your website not only looks great but also delivers an exceptional user experience.")

elif options == "About Us" :
     st.title('The Lex Project by Algorex Technologies')
     st.subheader("About Us")
     st.write("# Algorex PH")
     st.image('images/Meer.jpg')
     st.write("## Pinoy AI Engineer and Competitive Programmer")
     st.text("Connect with me via Linkedin : https://www.linkedin.com/in/algorexph/")
     st.text("Kaggle Account : https://www.kaggle.com/daniellebagaforomeer")
     st.write("# Kristine Shyra Carpio")
     st.image('images/Shyra.jpeg')
     st.write("## Operations Manager at Homely Spaces")
     st.text("Connect with me via Linkedin : https://www.linkedin.com/in/kristine-shyra-carpio-618a18214/")
     st.write("\n")


elif options == "Model" :
     st.title('The M Project by Algorex Technologies')
     st.subheader("I want to share about ...")
     col1, col2, col3 = st.columns([1, 2, 1])

     with col2:
          topic_ideas = st.text_input("Topic", placeholder="My Latest Project, Shower Thoughts, My Latest Achievement, etc.")
          submit_button = st.button("Generate LinkedIn Post")

     if submit_button:
        with st.spinner("Generating Post"):
             prompt = """
             You are an AI assistant specialized in crafting engaging, detailed, and professional LinkedIn posts. You will take the user's input from the textbox "I want to share about ......" and create an insightful and motivational LinkedIn post based on the importance of Motherhood, Tech for Good, Women Empowerment, Motivation, Inspiration, and Diversity. Each post should be friendly, outgoing, and tailored to connect with a professional audience on LinkedIn. Follow this structure:

             Friendly Greeting and Introduction:

             Start with a friendly greeting and a brief introduction related to the topic provided by the user.
             Detailed Exploration:

             Dive into the chosen topic with personal insights, reflections, and relevant experiences.
             Highlight any relevant projects, achievements, or initiatives, especially those related to Motherhood, Tech for Good, Women Empowerment, Motivation, Inspiration, and Diversity.
             Key Takeaways:

             Summarize the main points or provide actionable advice related to the topic.
             Closing Statement:

             Encourage the audience to share their thoughts, experiences, or simply say hello.
             Hashtags:

             Include relevant hashtags to enhance visibility.
             Input and Output Example:
             User Input:
             "I want to share about the intersection of motherhood and women empowerment."

             Example Output:

             🌟 The Powerful Intersection of Motherhood and Women Empowerment 🌟

             Hello LinkedIn Family! 👋

             I’m Chinelo, and today I want to discuss a topic close to my heart: the powerful intersection of motherhood and women empowerment. Balancing a tech career and motherhood has taught me invaluable lessons in resilience, creativity, and strength.

             Motherhood and Women Empowerment
             👩‍👧‍👦 Embracing Motherhood: Being a mother is a journey filled with challenges and rewards. It has shaped me into a more empathetic and driven professional. The skills we develop as mothers – multitasking, problem-solving, and nurturing – are incredibly valuable in the workplace.

             💪 Empowering Women: Empowering women in all aspects of life, including motherhood, is essential. By supporting each other, sharing our stories, and advocating for flexible work environments, we can create a more inclusive and empowering culture for all women.

             Tech for Good
             💻 Leveraging Tech: Technology has the power to create positive change. From developing tools that support working mothers to using AI for social good, tech can be a force for empowerment and progress.

             Key Takeaways
             Celebrate Dual Roles: Embrace and celebrate the dual role of being a mother and a professional. Both roles enrich each other and contribute to a more fulfilling life.
             Support Systems: Build and rely on support systems, both at home and in the workplace. Encouragement and understanding from peers and leaders make a significant difference.
             Advocate for Flexibility: Advocate for flexible work policies that support work-life balance. Flexibility is key to empowering more women to thrive in their careers while being present for their families.
             Looking Ahead
             The future is bright when we harness the power of motherhood and women empowerment. Let’s continue to inspire, motivate, and support each other in our journeys. Together, we can create a world where every woman can succeed, both at home and in the workplace.

             I’d love to connect with fellow mothers, tech enthusiasts, and advocates for women empowerment. Share your thoughts, experiences, or even just a hello in the comments below. Let’s build a brighter future together!

             #Motherhood #WomenEmpowerment #TechForGood #Motivation #Inspiration #Diversity #Community

             Use this structure and these guidelines to generate similar posts based on the user's input.

             """ + "I want you to generate an engaging, detailed, and professional LinkedIn post about " + topic_ideas
             chat_session = model.start_chat()
             
             response = chat_session.send_message(prompt)
    
        st.success("Linkedin Post generated successfully!")
        st.subheader(topic_ideas)
        st.write(response.text)