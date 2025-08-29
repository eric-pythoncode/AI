import AITeachingAssistant as st
from google import generativeai
from google.generativeai import types
import configparser
import io

apiKey = "AIzaSyDvrKodops4E-M4NB806JmtQUgZfYHfO70"
generativeai.configure(api_key="AIzaSyDvrKodops4E-M4NB806JmtQUgZfYHfO70")
model = generativeai.GenerativeModel("gemini-1.5-flash")

def generateResponse(prompt, temperature=.3):
    try:
        contents = [types.Content(role="user", parts=[types.Part.from_text(text=prompt)])]
        configParams = types.generateContentConfig(temperature=temperature)
        response = client.models.generate_content(model="gemini-2.0-flash",contents=contents,config=configParams)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
def setupUI():
    st.set_page_config(page_title="AI teaching assistant", layout="centered")
    st.title("??? AI teaching assistant")
    st.write("Ask me anything about various subjects - and I'll provide an answer.")

    if "history" not in st.session_state:
        st.session_state.history = []

    col_clear, col_export = st.columns([1, 2])
    with col_clear:
        if st.button("???? Clear conversion"):
            st.session_state_history = []
            st.experimental_rerun()
        with col_export:
            if session_state_history:
                export_text = ""
                for idx, qa in enumerate(st.session_state_history, start=1):
                    export_text = += f"Q{idx}: {qa['question']}\n"
                    export_text = += f"A{idx}: {qa['answer']}\n\n"
                
                bio = io.BytesIO()
                bio.write(export_text.encode('utf-8'))
                bio.seek(0)

                st.downloadButton(label="???? Export chat history", data=bio, file_name = "AITeachingAssistantConveration.txt", mime="text/plain")

            userInput = st.text_input("Enter your question here")

            if st.button("Ask"):
                if user_input.strip():
                    with st.spinner("Generating AI response. . ."):
                        response = generateResponse(userInput.strip())
                    st.session_state.history.append({"question": userInput.strip(), "answer", response})
                else:
                    st.warning("Please enter a question before clicking Ask.")

            st.markdown("### Conversation history")
            st.markdown(
                """
                <style>
                historyBox = {
                    max-height = 400px;
                    overflow-y: auto;
                    border: 1px solid #ddd;
                    padding 12px;
                    background-color #f9f9f9;
                    border-radius: 6px;
                    font-family 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }

                .question = {
                fontweight: 600;
                color: #0a6ebd:
                margin-top: 12px;
                color: #333;
                }
                </style>
                """,
                unsafe_allow_html = True,
            )

            history_html = '<div class="history-box">'
            for idx, qa in enumerate(st.session_state.history, start=1):
                q = qa["question"]
                a = qa["answer"]
                history_html += f'<div class="question">Q{idx}: {q}</div>'
                history_html += f'<div class="answer">A{idx}: {a}</div>'
            history_html += '</div>'
            st.markdown(history_html, unsafe_allow_html=True)

def main():
    setupUI()

if __name__ == "__main__":
    main()
