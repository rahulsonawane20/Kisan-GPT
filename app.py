import streamlit as st
from PIL import Image
import base64

# Load the background image
def set_background(image_file):
    with open(image_file, "rb") as file:
        encoded_string = base64.b64encode(file.read()).decode()
    background_style = f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpg;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .back-arrow {{
            position: absolute;
            top: -47px;
            left: -280px;
            z-index: 1000;
            border-radius: 50%; /* Round shape */
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2); /* Shadow effect */
        }}
        .back-arrow img {{
            width: 45px; /* Width of the back arrow icon */
            height: 45px; /* Height of the back arrow icon */
        }}
        </style>
    """
    st.markdown(background_style, unsafe_allow_html=True)

# Apply CSS to increase the font size of sidebar options
st.markdown(
    """
    <style>
    /* Increase font size for sidebar options */
    .css-1y4p8pu {
        font-size: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Set the background image (adjust the path to your image)
set_background("Background_Image.jpg")

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()
back_arrow_image_path = 'AL4.png'

# Encode the icon images
encoded_back_arrow = encode_image_to_base64(back_arrow_image_path)
st.markdown(f'''
<div class="back-arrow">
<a href="http://localhost:8501">
<img src="data:image/png;base64,{encoded_back_arrow}" alt="Back Arrow">
</a>
</div>
''', unsafe_allow_html=True)

# Example Streamlit app content
st.markdown(
    """
    <style>
    
    [data-testid="stSidebar"] {
        background-color: rgba(0.2, 0.2, 0.2, 0.1);  /* Fully transparent */
    }
 
   
    [data-testid="stSidebar"] .css-1d391kg {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Apply CSS to add spacing between radio buttons
st.markdown(
    """
    <style>
    div[role="radiogroup"] > label {
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Sidebar content
st.sidebar.title("Explore")
option = st.sidebar.radio("Select", ["Market Insights", "Financial Insights", "Trade Analysis"])

if option == "Market Insights":
    st.title("Market Insights")
    st.write("Discover comprehensive insights into market trends, key statistics, and more to guide informed business strategies.")
    power_bi_report_url = "https://app.powerbi.com/reportEmbed?reportId=d523da4d-e181-4868-a313-4eae11895b71&autoAuth=true&ctid=76a2ae5a-9f00-4f6b-95ed-5d33d77c4d61"
    st.markdown(f'<iframe width="920" height="600" src="{power_bi_report_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

elif option == "Financial Insights":
    st.title("Financial Insights")
    st.write("Access in-depth insights into financial data, comprehensive reports, and key aspects to support strategic decision-making.")
    power_bi_report_url = "https://app.powerbi.com/reportEmbed?reportId=4a30b2ba-f812-4742-b2a2-b3b19d3d20bf&autoAuth=true&ctid=76a2ae5a-9f00-4f6b-95ed-5d33d77c4d61"
    st.markdown(f'<iframe width="920" height="600" src="{power_bi_report_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)

elif option == "Trade Analysis":
    st.title("Trade Analysis")
    st.write("Explore comprehensive analysis of agricultural trade data, trends, and patterns to drive informed decision-making and strategic insights.")
    power_bi_report_url = "https://app.powerbi.com/reportEmbed?reportId=d8cf5204-88aa-4835-b08b-6bcf7cdb099f&autoAuth=true&ctid=76a2ae5a-9f00-4f6b-95ed-5d33d77c4d61"
    st.markdown(f'<iframe width="920" height="600" src="{power_bi_report_url}" frameborder="0" allowFullScreen="true"></iframe>', unsafe_allow_html=True)
