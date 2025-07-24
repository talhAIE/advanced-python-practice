# capture the pic on web cam and convert it into greyscale
import streamlit as st
from PIL import Image


# with st.expander("Start Camera"):
#     camera_img=st.camera_input("Camera")

# if camera_img:
#     img=Image.open(camera_img)
#     gray_img=img.convert('L')
#     st.image(gray_img)

# upload and convert



uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    user_img = Image.open(uploaded_file)
    st.image(user_img.convert('L'))
else:
    st.warning("Please upload an image file.")
