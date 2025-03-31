import streamlit as st

from streamlit_option_menu import option_menu
# import os
# from dotenv import load_dotenv
# load_dotenv()

# import home, trending, account, your_post, about
import account, about, analyze, database, summarize, home, format
st.set_page_config(
        page_title="PaperFlow",
        page_icon='🕮'
)

class PaperFlow:
    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })
        
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title='Paper Flow',
                options=['Home','Account','Format','Analyze','Summarize','About'],
                icons=['house','person-circle','trophy-fill','chat-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#353942"},
        "nav-link-selected": {"background-color": "#02ab21"},}
            )
            
        if app == "Home":
            home.app()
        if app == "Account":
            account.app()    
        if app == "Format":
            format.app()        
        if app == 'Analyze':
            analyze.app()
        if app == 'Summarize':
            summarize.app()   
        if app == 'About':
            about.app()   
            
    run()
    