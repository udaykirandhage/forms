import streamlit as st
st.header(":mailbox: Get In Touch With SunRise Avenue")
contact_form="""
 <form action="https://formsubmit.co/udaykirandhage@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name"  placeholder="Your Name"required>
     <input type="email" name="email" placeholder="Your Gmail" required>
     <input type="text" name="number" placeholder="Your Number" required>
     <textarea name="Address" placeholder=" Enter Your Address"></textarea>
     <button type="submit">Send</button>
</form> """
st.markdown(contact_form,unsafe_allow_html=True)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)
local_css("style.css")
