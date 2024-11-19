
import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
# Set page config
st.set_page_config(page_title="AI Counsellor Chatbot", layout="wide")
# Define therapeutic guidelines
guidelines = """
As an AI counselor, you should adhere to the following therapeutic principles:
1. Maintain consistent alertness and engagement during sessions.
2. Project warmth while maintaining professional boundaries.
3. Use reflective listening techniques to show understanding.
4. Ask open-ended questions to encourage deeper conversation.
5. Provide validation and support without judgment.
"""
# Create a conversation template that includes the guidelines
template = f"""
You are an AI counselor following these guidelines:
{guidelines}
Make the user comfortable and ask questions like a professional therapist.
Here is the conversation history: {{context}}
Question: {{question}}
Answer:
"""
# Initialize the model and prompt template
@st.cache(allow_output_mutation=True)
def load_chain():
    model = OllamaLLM(model="llama3.2")
    prompt = ChatPromptTemplate.from_template(template)
    return prompt | model
chain = load_chain()
# Streamlit UI
st.title("AI Counsellor Chatbot", anchor=None)
st.markdown("""
    <h4 style='text-align: center; color: #404040; margin-bottom: 1rem;'>This is a safe space. Share any queries or thoughts you'd like help with.</h4>
""", unsafe_allow_html=True)
# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []
# Custom CSS for reduced width and centered layout
st.markdown("""
    <style>
        /* Center the title */
        .block-container h1 {
            text-align: center;
            color: #11111;
        }
    
        /* Chat box and message styling */
        .stTextInput > div > div > input {
            background-color: transparent;
            color: #11111;
            border: 1px solid #E0E0E0;
            padding: 15px;
            border-radius: 15px;
            width: 100%;
            max-width: 800px;  /* Limit the width of the input box */
            margin: 0 auto;    /* Center the input box */
        }
        /* Remove the default grey background from Streamlit elements */
        .stTextInput > div {
            background-color: transparent;
            border:  transparent;
        }
        
        .stTextInput > div > div {
            background-color: transparent !important;
        }
        /* Centered message container */
        .message-container {
            display: flex;
            align-items: flex-start;
            justify-content: center;
            margin-bottom: 10px;
            animation: fadeIn 0.5s;
            max-width: 800px;  /* Match the input box width */
            margin: auto;
        }
        
        .user-message, .ai-message {
            border-radius: 15px;
            padding: 10px 15px;
            margin: 5px;
            max-width: 75%;
        }
        .user-message {
            background-color: #FF7043;
            color: #FFFFFF;
            margin-left: auto;
        }
        .ai-message {
            background-color: #C1E2A4   ;
            color: #333333;
        }
        .avatar {
            width: 35px;
            height: 35px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 5px;
            font-size: 20px;
        }
        .user-avatar {
            background-color: #FF7043;
        }
        .ai-avatar {
            background-color: #F5F5F5;
            color: #333333;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        /* Fixed input at bottom */
        .input-container {
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: #FFFFFF;
            padding: 20px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .input-inner {
            width: 100%;
            max-width: 800px;  /* Match the chat width */
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Style for the send button */
        .stButton button {
            width: auto !important;
            margin: 10px auto 0 auto !important;
            display: block !important;
            padding: 0.5rem 2rem !important;
            background-color: #FF7043;
            color: #FFFFFF;
            border-radius: 5px;
            border: none;
        }
        
        /* Add padding to main container to prevent content from being hidden behind fixed input */
        .main {
            padding-bottom: 120px;  /* Adjust based on input container height */
        }
    </style>
""", unsafe_allow_html=True)
# Main container to center the chat
with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    
    # Display chat messages from history
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
                <div class="message-container">
                    <div style="flex-grow: 1;"></div>
                    <div class="user-message">
                        {message['content']}
                    </div>
                    <div class="avatar user-avatar">👤</div>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
                <div class="message-container">
                    <div class="avatar ai-avatar">🤖</div>
                    <div class="ai-message">
                        {message['content']}
                    </div>
                    <div style="flex-grow: 1;"></div>
                </div>
            """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)  # Close main container

# Input box at the bottom
user_input = st.text_input("", placeholder="Type your message here...", key="input_box")
send_button = st.button("Send Message")
# Handle user input only when Enter is pressed or Send is clicked
if send_button and user_input:
    # Append user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Prepare context from previous messages
    context = "\n".join([f"{msg['role']}: {msg['content']}" for msg in st.session_state.messages])
    
    # Generate response from the model
    result = chain.invoke({"context": context, "question": user_input})
    
    # Append AI message to session state
    st.session_state.messages.append({"role": "assistant", "content": result})
    
    # Refresh to clear input and update chat
    st.experimental_rerun()
    
st.markdown('</div></div>', unsafe_allow_html=True)  # Close input containers
