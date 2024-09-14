#toggle button to be made for show all projects
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import streamlit as st
from portfolio import Portfolio
import streamlit.components.v1 as html
from streamlit_pdf_viewer import pdf_viewer

# # Inject viewport meta tag
# st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0">', unsafe_allow_html=True)

# Initialize Portfolio and load projects
portfolio = Portfolio("app/resource/my_portfolio.xlsx")
portfolio.load_portfolio()

# Streamlit Web UI
def main():
    # Inject custom CSS for styling
    custom_css = """
    <style>
        body {
            background-color: #f5f5f5;
        }
        input[type="text"] {
            color: #FF4B4B;
            background-color: #grey;
            border-radius: 5px;
            padding: 12px;
            border: 2px solid #FF4B4B;
            width: 100%;
            box-sizing: border-box;
            transition: all 0.2s ease-out;
            outline: none;
        }
        input[type="text"]:hover {
            background-color: #FFE4E4;
            padding: 15px;
            font-size: 24px;
        }
        input[type="text"]:focus {
            background-color: #FFE4E4;
            border: 2px solid #FF4B4B;
            padding: 12px;
            caret-color: #FF4B4B;
        }
        .subheader {
            color: #c0c0c0;
            font-size: 24px;
            font-weight: bold;
        }
        label {
            font-size: 24px;
            font-weight: bold;
            color: #c0c0c0;
            margin-bottom: 0px;
        }
        .description {
            color: #a9a9a9;
            font-size: 18px;
        }
        .link-container a {
            text-decoration: none;
            color: black;
            transition: transform 0.2s ease, color 0.2s ease;
        }
        .link-container a:hover {
            color: #FF4B4B;
            transform: scale(1.1);
        }
        .header{
            margin-top: -20px;
            margin-bottom: -20px
        }
    </style>
    """
    
    st.markdown(custom_css, unsafe_allow_html=True)

    # Title and description
    st.markdown("""<h1 style='font-size: 81px; color:#FF4B4B; margin-top:-36px'><span style=' font-size: 64px;'>Hi, I'm</span><br><span style=''>Shashank Soni!</span></h1>""", unsafe_allow_html=True)
    st.markdown("<p style=' font-size: 1.5em; font-weight: bold; margin-top:-22px'> I solve problems with code. Occasionally, I create them 🤷‍♂️</p>", unsafe_allow_html=True)
    st.markdown("<p class='description'>Full-stack developer with a passion for AI/ML and LLMs, skilled in building intelligent, scalable web applications with seamless user experiences and a touch of UI/UX expertise.</p>", unsafe_allow_html=True)
    st.write("---")
    

    st.header("Projects")

    # Search bar for filtering projects by TechStack with placeholder
    search_query = st.text_input(label=" ", placeholder="Search my Projects by Tech Stack (e.g., Java, Python)")




    # Show all projects button
    if st.button("Show All Projects"):
        results = portfolio.get_all_projects()  # Use get_all_projects to fetch all projects
        if results:
            st.write("Showing all projects:")
            for project in results:
                project_name = project.get('project_name', 'Unknown')
                project_url = project.get('url', '#')
                st.markdown(f"**{project_name}** - [View Project]({project_url})")
        else:
            st.write("No projects found.")

    # Filter projects based on search query
    if search_query:
        results = portfolio.query_links([search_query])
        st.write(f"Showing results for: {search_query}")
        
        if results:
            for project in results:
                project_name = project.get('project_name', 'Unknown')
                project_url = project.get('url', '#')
                st.markdown(f"**{project_name}** - [View Project]({project_url})")
        else:
            st.write("No projects found with that tech stack.")

    #Personal Interests
    st.write("----")
    st.header("Personal Interests")
    st.markdown("""
        <p class = 'description' >
        I'm passionate about <strong style='font-size: 1.4em; color: #FF4B4B;'>Calisthenics</strong>, focusing on bodyweight exercises to stay fit. 
        I enjoy playing <strong style='font-size: 1.4em; color: #FF4B4B;'>Badminton</strong> and competing in this fast-paced sport. 
        In my free time, I indulge in <strong style='font-size: 1.4em; color: #FF4B4B;'>Photography</strong>, capturing moments and scenes that inspire me. <strong style='font-size: 1.4em; color: #FF4B4B;'>Music</strong> is a constant companion while I work, and I might just be listening to it right now.
        Additionally, I also have a deep appreciation for <strong style='font-size: 1.4em; color: #FF4B4B;'>Art</strong>. </p>
    """, unsafe_allow_html=True)

    st.write("----")    
    # Contact Info & resume download
    
    col1, col2 = st.columns(2)

    with col1:
        st.header("Contact Me")

        st.write("""
        <style>
            .contact-info {
                transition: color 0.2s ease, transform 0.2s ease;
            }
            .contact-info:hover {
                color: #FF4B4B;
                transform: scale(1.1);
            }
        </style>
        <div class="link-container" style="display: flex; align-items: center; margin-bottom: 10px;">
            <span style="font-size: 16px; margin-right: 5px;">📞</span>
            <span>Phone: <a href="tel:+916205468356" class="contact-info">+91 6205 468 356</a></span>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
            <div class="link-container" style="display: flex; align-items: center; margin-bottom: 10px;">
                <span style="font-size: 16px; margin-right: 5px;">📧</span>
                <span>Email: <a href="mailto:shashank.err404@gmail.com" class="contact-info">shashank.err404@gmail.com</a></span>
            </div>
            """, unsafe_allow_html=True)


        st.write("""
        <div class="link-container" style="display: flex; align-items: center; margin-bottom: 10px;">
            <img src="https://img.icons8.com/?size=100&id=LoL4bFzqmAa0&format=png&color=000000" style="width: 20px; height: 20px; margin-right: 5px;" />
            <a href="https://github.com/shashank651156">GitHub</a>
        </div>
        """, unsafe_allow_html=True)

        st.write("""
            <div class="link-container" style="display: flex; align-items: center; margin-bottom: 10px;">
                <img src="https://img.icons8.com/?size=100&id=xuvGCOXi8Wyg&format=png&color=000000" style="width: 20px; height: 20px; margin-right: 5px;" />
                <a href="https://www.linkedin.com/in/shashank-soni-b85a451b3/">LinkedIn</a>
            </div>
        """, unsafe_allow_html=True)

        st.write("""
            <div class="link-container" style="display: flex; align-items: center; margin-bottom: 10px;">
                <img src="https://img.icons8.com/?size=100&id=Xy10Jcu1L2Su&format=png&color=000000" style="width: 20px; height: 20px; margin-right: 5px;" />
                <a href="https://www.instagram.com/shashank___soni___/">Instagram</a>
            </div>
                
                """, unsafe_allow_html=True)

    # with col2:
    #     st.header("Resume")
        
    #     # Create a button for downloading the file
    #     with open("app/resource/Shashank_Soni_Resume.pdf", "rb") as file:
    #         st.download_button(
    #             label="Download Resume",
    #             data=file,
    #             file_name="Shashank_Soni_Resume.pdf",
    #             mime="application/pdf"
    #         )
    visible = False

    with col2:
        st.header("Resume")

        # Create a button for downloading the file
        with open("app/resource/Shashank_Soni_Resume.pdf", "rb") as file:
            st.download_button(
                label="Download Resume",
                data=file,
                file_name="Shashank_Soni_Resume.pdf",
                mime="application/pdf",
                key="download_button"
            )
            # st.snow()

        
        # Create a button to view the PDF
        view_button = st.button("View Resume")

        if view_button:

            visible= not visible
    st.write("----") 



    with st.container():
        if visible:
            pdf_url = "app/resource/Shashank_Soni_Resume.pdf"  # The path to your PDF file
            pdf_viewer(pdf_url, width=700, height=1111)

     
if __name__ == '__main__':
    main()

